from pydantic import BaseModel
from typing import Optional


class TalentBase(BaseModel):
    first_name: str
    last_name: str
    dob: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class TalentCreate(TalentBase):
    # For now, same as TalentBase – later we can add required fields
    pass


class TalentOut(TalentBase):
    id: int

    class Config:
        orm_mode = True
