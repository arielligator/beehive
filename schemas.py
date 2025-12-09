# define what API receives and returns
# control which fields are exposed to client
# control which fields are required or optional
# validate input data
# prevent exposing sensitive information

from pydantic import BaseModel, EmailStr
from typing import Optional, List


# --- Department Schemas ---

class DepartmentBase(BaseModel):
    name: str

class DepartmentOut(DepartmentBase):
    id: int

    class Config:
        from_attributes = True

# --- Job Schemas ---

class JobBase(BaseModel):
    name: str

class JobOut(JobBase):
    id: int

    class Config:
        from_attributes = True


# --- Works With Schemas ---

class WorksWithBase(BaseModel):
    name: str

class WorksWithOut(WorksWithBase):
    id: int

    class Config:
        from_attributes = True

# --- Person Schemas ---

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    dob: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class PersonCreate(PersonBase):
    # For now, same as PersonBase – later we can add required fields
    pass


class PersonOut(PersonBase):
    id: int
    departments: List[DepartmentOut] = []
    jobs: List[JobOut] = []
    works_with: List[WorksWithOut] = []

    class Config:
        from_attributes = True
