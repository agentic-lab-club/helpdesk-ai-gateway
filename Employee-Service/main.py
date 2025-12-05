from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import Base, engine, get_db
from app import models, schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Service", version="1.0.0")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/employees/free/reserve", response_model=schemas.EmployeeRead)
def reserve_free_employee(db: Session = Depends(get_db)):
    employee = crud.pick_and_reserve_free_employee(db)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No free employees available",
        )
    return employee


@app.post("/employees/by-telegram/free", response_model=schemas.EmployeeRead)
def mark_employee_free(
    payload: schemas.EmployeeTelegramId,
    db: Session = Depends(get_db),
):
    """
    n8n шлёт POST с telegram_id, мы по нему находим employee и
    ставим статус FREE.
    """
    employee = crud.mark_employee_free_by_telegram(db, payload.telegram_id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee with this telegram_id not found",
        )
    return employee
