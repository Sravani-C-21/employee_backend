from typing import List
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db import crud, models, schemas
from db.database import SessionLocal, engine
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/employees/", response_model=schemas.EmployeeResponseSchema)
def create_employee(employee: schemas.EmployeeCreateSchema, db: Session = Depends(get_db)):
    try:
        db_employee = crud.create_employee(db=db, employee_deatils=employee)
        json_compatible_item_data = jsonable_encoder(db_employee)
        return JSONResponse(content=json_compatible_item_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e.orig))

@app.get("/employees/{employee_id}", response_model=schemas.EmployeeResponseSchema)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if not db_employee:
        raise HTTPException(status_code=400, detail="Employee does not exist with given id")
    json_compatible_item_data = jsonable_encoder(db_employee)
    return JSONResponse(content=json_compatible_item_data)


@app.get("/employees/", response_model=schemas.EmployeeResponseSchema)
def list_employees(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = crud.get_employees(db, offset=offset, limit=limit)
    json_compatible_item_data = jsonable_encoder(employees)
    return JSONResponse(content=json_compatible_item_data)


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)