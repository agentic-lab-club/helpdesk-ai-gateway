import random
import uuid
from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy import select

from app import models, schemas
from app.models import EmployeeStatus


def create_employee(db: Session, data: schemas.EmployeeCreate) -> models.Employee:
    employee = models.Employee(
        full_name=data.full_name,
        telegram_id=data.telegram_id,
        status=data.status,
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def get_employee(db: Session, employee_id: UUID) -> models.Employee | None:
    stmt = select(models.Employee).where(models.Employee.id == employee_id)
    return db.scalar(stmt)


def get_employee_by_telegram(db: Session, telegram_id: str) -> models.Employee | None:
    stmt = select(models.Employee).where(models.Employee.telegram_id == telegram_id)
    return db.scalar(stmt)


def list_employees(db: Session, skip: int = 0, limit: int = 100):
    stmt = select(models.Employee).offset(skip).limit(limit)
    return db.scalars(stmt).all()


def update_employee(
    db: Session, employee: models.Employee, data: schemas.EmployeeUpdate
) -> models.Employee:
    if data.full_name is not None:
        employee.full_name = data.full_name
    if data.telegram_id is not None:
        employee.telegram_id = data.telegram_id
    if data.status is not None:
        employee.status = data.status

    db.commit()
    db.refresh(employee)
    return employee


def delete_employee(db: Session, employee: models.Employee) -> None:
    db.delete(employee)
    db.commit()


# -------------------------------------------
# ---- ВЫБРАТЬ ПЕРВОГО СВОБОДНОГО (FREE) ----
# -------------------------------------------
def pick_and_reserve_free_employee(db: Session) -> models.Employee | None:
    """
    Находит первого свободного сотрудника (status=FREE),
    блокирует строку, ставит BUSY и возвращает.
    Работает корректно при конкурентных запросах (PostgreSQL).
    """

    stmt = (
        select(models.Employee)
        .where(models.Employee.status == EmployeeStatus.FREE)
        .with_for_update(skip_locked=True)     # пропускает занятые блокировкой
        .limit(1)
    )

    employee = db.scalars(stmt).first()

    if not employee:
        return None

    employee.status = EmployeeStatus.BUSY
    db.commit()
    db.refresh(employee)

    return employee


# ---------------------------------------------------
# ---- ПО telegram_id ПОМЕТИТЬ как FREE (освободить)
# ---------------------------------------------------
def mark_employee_free_by_telegram(db: Session, telegram_id: str) -> models.Employee | None:
    employee = get_employee_by_telegram(db, telegram_id)
    if not employee:
        return None

    employee.status = EmployeeStatus.FREE
    db.commit()
    db.refresh(employee)

    return employee


# ---------------------------------------------------------
# ---- ГЕНЕРАЦИЯ 10–20 РАНДОМНЫХ СОТРУДНИКОВ -------------
# ---------------------------------------------------------
def create_random_employees(
    db: Session,
    min_count: int = 10,
    max_count: int = 20,
) -> list[models.Employee]:
    """
    Создаёт от min_count до max_count сотрудников
    с рандомными именами, telegram_id и статусами.
    """

    count = random.randint(min_count, max_count)
    employees: list[models.Employee] = []

    for i in range(count):
        full_name = f"Employee {i + 1}"
        telegram_id = f"tg_{uuid.uuid4().hex[:10]}"
        status = random.choice([EmployeeStatus.FREE, EmployeeStatus.BUSY])

        employee = models.Employee(
            full_name=full_name,
            telegram_id=telegram_id,
            status=status,
        )

        db.add(employee)
        employees.append(employee)

    db.commit()

    for e in employees:
        db.refresh(e)

    return employees
