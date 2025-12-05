from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.routers import example
# from app.configs.database import Base, engine

# Uncomment to create tables
# Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Template", version="1.0.0")

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
    return {"message": "API Template"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
