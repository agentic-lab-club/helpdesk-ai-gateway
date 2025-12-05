from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.configs.database import get_db
from app.schemas.employee import EmployeeRead
from app.services.employee_service import get_and_assign_free_employee, free_employee

router = APIRouter(tags=["employees"])


@router.get("/employee", response_model=EmployeeRead)
def get_free_employee(db: Session = Depends(get_db)):
    """Получить первого свободного сотрудника и сделать его занятым"""
    employee = get_and_assign_free_employee(db)
    if not employee:
        raise HTTPException(status_code=404, detail="No free employees available")
    return employee


@router.post("/employee/{employee_id}", response_model=EmployeeRead)
def free_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    """Освободить сотрудника по ID"""
    employee = free_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee
