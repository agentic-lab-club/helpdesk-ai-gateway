from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.employee import Employee, EmployeeStatus


def get_and_assign_free_employee(db: Session) -> Employee | None:
    """Получает первого свободного сотрудника и делает его занятым"""
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


def free_employee(db: Session, employee_id: int) -> Employee | None:
    """Освобождает сотрудника по ID"""
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    
    if employee:
        employee.status = EmployeeStatus.FREE
        db.commit()
        db.refresh(employee)
    
    return employee
