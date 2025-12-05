from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text

# from app.routers import example
from app.configs.database import Base, engine, get_db

# Импорт всех моделей для создания таблиц
from app.models import employee, ticket, category, priority, chat_history

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI(title="HelpDesk AI Gateway", version="1.0.0")

# CORS configuration
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
# app.include_router(example.router)

@app.get("/")
def read_root():
    return {"message": "HelpDesk AI Gateway API"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database connection failed: {str(e)}")
