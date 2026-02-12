from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeePatch


def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_all_employees(db: Session):
    return db.query(Employee).all()


def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def update_employee(db: Session, employee_id: int, employee: EmployeeUpdate):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return None

    db_employee.name = employee.name
    db_employee.email = employee.email
    db_employee.position = employee.position

    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return None

    db.delete(db_employee)
    db.commit()
    return db_employee
