from sqlalchemy.orm import Session

from . import models, schemas


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employee_by_email(db: Session, email: str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()


def get_employees(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(offset).limit(limit).all()


def create_employee(db: Session, employee_deatils: schemas.EmployeeCreateSchema):
    db_employee = models.Employee(name=employee_deatils.name, email=employee_deatils.email)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee