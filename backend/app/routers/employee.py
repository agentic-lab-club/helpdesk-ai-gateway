from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.configs.database import get_db
from app.schemas.employee import EmployeeCreate, EmployeeRead, EmployeeUpdate
from app.services.employee_service import (
    create_employee,
    get_employee,
    get_employees,
    update_employee,
    delete_employee,
    assign_free_employee,
    release_employee
)

router = APIRouter(prefix="/employees", tags=["employees"])


@router.post("/", response_model=EmployeeRead)
def create_employee_endpoint(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """Создать нового сотрудника"""
    return create_employee(db, employee)


@router.get("/", response_model=List[EmployeeRead])
def get_employees_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Получить список сотрудников"""
    return get_employees(db, skip, limit)


@router.get("/{employee_id}", response_model=EmployeeRead)
def get_employee_endpoint(employee_id: int, db: Session = Depends(get_db)):
    """Получить сотрудника по ID"""
    employee = get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.put("/{employee_id}", response_model=EmployeeRead)
def update_employee_endpoint(employee_id: int, employee_update: EmployeeUpdate, db: Session = Depends(get_db)):
    """Обновить сотрудника"""
    employee = update_employee(db, employee_id, employee_update)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.delete("/{employee_id}")
def delete_employee_endpoint(employee_id: int, db: Session = Depends(get_db)):
    """Удалить сотрудника"""
    employee = delete_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}


@router.post("/assign", response_model=EmployeeRead)
def assign_free_employee_endpoint(db: Session = Depends(get_db)):
    """Назначить первого свободного сотрудника (сделать занятым)"""
    employee = assign_free_employee(db)
    if not employee:
        raise HTTPException(status_code=404, detail="No free employees available")
    return employee


@router.post("/{employee_id}/release", response_model=EmployeeRead)
def release_employee_endpoint(employee_id: int, db: Session = Depends(get_db)):
    """Освободить сотрудника по ID"""
    employee = release_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee
