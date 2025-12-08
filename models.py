from sqlalchemy import Column, Integer, String
from .database import Base

# create talent model - turns each database row into a python object
class Talent(Base):
    __tablename__ = "talent"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(String)
    phone = Column(String)
    email = Column(String)
    address = Column(String)

# create pydantic schema - determines what API returns or accepts
class TalentOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    dob: str
    phone: str
    email: str
    address: str

    class Config:
        orm_mode = True