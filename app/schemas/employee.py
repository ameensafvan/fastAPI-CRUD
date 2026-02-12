from pydantic import BaseModel
from typing import Optional

class EmployeeCreate(BaseModel):
    name: str
    email: str
    position: str


class EmployeeUpdate(BaseModel):
    name: str
    email: str
    position: str


class EmployeePatch(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    position: Optional[str] = None


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    position: str

    class Config:
        from_attributes = True
