from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.employee import *
from app.crud.employee import *

router = APIRouter(prefix="/employees", tags=["Employees"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=EmployeeResponse)
def create(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db, employee)


@router.get("/", response_model=list[EmployeeResponse])
def read_all(db: Session = Depends(get_db)):
    return get_all_employees(db)


@router.get("/{employee_id}", response_model=EmployeeResponse)
def read_one(employee_id: int, db: Session = Depends(get_db)):
    employee = get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    updated = update_employee(db, employee_id, employee)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated


@router.delete("/{employee_id}")
def delete(employee_id: int, db: Session = Depends(get_db)):
    deleted = delete_employee(db, employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}
