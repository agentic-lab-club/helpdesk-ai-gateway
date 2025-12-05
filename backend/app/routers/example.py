# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List

# from app.configs.database import get_db
# from app.schemas.example import ExampleCreate, ExampleRead, ExampleUpdate
# from app.services.example_service import (
#     create_example,
#     get_example,
#     get_examples,
#     update_example,
#     delete_example
# )

# router = APIRouter(prefix="/examples", tags=["examples"])

# @router.post("/", response_model=ExampleRead)
# def create_example_endpoint(example: ExampleCreate, db: Session = Depends(get_db)):
#     return create_example(db=db, example=example)

# @router.get("/{example_id}", response_model=ExampleRead)
# def read_example(example_id: int, db: Session = Depends(get_db)):
#     db_example = get_example(db, example_id=example_id)
#     if db_example is None:
#         raise HTTPException(status_code=404, detail="Example not found")
#     return db_example

# @router.get("/", response_model=List[ExampleRead])
# def read_examples(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     examples = get_examples(db, skip=skip, limit=limit)
#     return examples

# @router.put("/{example_id}", response_model=ExampleRead)
# def update_example_endpoint(example_id: int, example: ExampleUpdate, db: Session = Depends(get_db)):
#     db_example = update_example(db, example_id=example_id, example=example)
#     if db_example is None:
#         raise HTTPException(status_code=404, detail="Example not found")
#     return db_example

# @router.delete("/{example_id}")
# def delete_example_endpoint(example_id: int, db: Session = Depends(get_db)):
#     db_example = delete_example(db, example_id=example_id)
#     if db_example is None:
#         raise HTTPException(status_code=404, detail="Example not found")
#     return {"message": "Example deleted successfully"}
