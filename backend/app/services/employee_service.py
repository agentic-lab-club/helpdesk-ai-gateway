from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.employee import Employee, EmployeeStatus
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


def create_employee(db: Session, employee: EmployeeCreate) -> Employee:
    """Создать нового сотрудника"""
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_employee(db: Session, employee_id: int) -> Employee | None:
    """Получить сотрудника по ID"""
    return db.query(Employee).filter(Employee.id == employee_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100) -> list[Employee]:
    """Получить список сотрудников"""
    return db.query(Employee).offset(skip).limit(limit).all()


def update_employee(db: Session, employee_id: int, employee_update: EmployeeUpdate) -> Employee | None:
    """Обновить сотрудника"""
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        for key, value in employee_update.dict(exclude_unset=True).items():
            setattr(employee, key, value)
        db.commit()
        db.refresh(employee)
    return employee


def delete_employee(db: Session, employee_id: int) -> Employee | None:
    """Удалить сотрудника"""
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        db.delete(employee)
        db.commit()
    return employee


def assign_free_employee(db: Session) -> Employee | None:
    """Получить первого свободного сотрудника и сделать его занятым"""
    stmt = (
        select(Employee)
        .where(Employee.status == EmployeeStatus.FREE)
        .with_for_update(skip_locked=True)
        .limit(1)
    )
    
    employee = db.scalars(stmt).first()
    
    if employee:
        employee.status = EmployeeStatus.BUSY
        db.commit()
        db.refresh(employee)
    
    return employee


def release_employee(db: Session, employee_id: int) -> Employee | None:
    """Освободить сотрудника по ID"""
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    
    if employee:
        employee.status = EmployeeStatus.FREE
        db.commit()
        db.refresh(employee)
    
    return employee
