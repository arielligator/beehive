# define how data is stored in the database
# control table structure
# control column types
# handle reading/writing DB data
# convert between python objects and sql rows
# map python classes to SQLite tables

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# association / join tables (many to many)

person_departments = Table(
    "person_departments",
    Base.metadata,
    Column("person_id", Integer, ForeignKey("people.id"), primary_key=True),
    Column("department_id", Integer, ForeignKey("departments.id"),primary_key=True),
)

person_jobs = Table(
    "person_jobs",
    Base.metadata,
    Column("person_id", Integer, ForeignKey("people.id"), primary_key=True),
    Column("job_id", Integer, ForeignKey("jobs.id"), primary_key=True),
)

person_works_with = Table(
    "person_works_with",
    Base.metadata,
    Column("person_id", Integer, ForeignKey("people.id"), primary_key=True),
    Column("works_with_id", Integer, ForeignKey("works_with.id"), primary_key=True),
)

# create talent model - turns each database row into a python object
class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(Date, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    address = Column(String, nullable=True)

    # relationships
    departments = relationship(
        "Department",
        secondary=person_departments,
        back_populates="people",
        lazy="joined"
    )
    jobs = relationship(
        "Job",
        secondary=person_jobs,
        back_populates="people",
        lazy="joined",
    )
    works_with = relationship(
        "Works With",
        secondary=person_works_with,
        back_populates="people",
        lazy="joined",
    )

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=True)

    people = relationship(
        "Person",
        secondary=person_departments,
        back_populates="departments"
    )

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    people = relationship(
        "Person",
        secondary=person_jobs,
        back_populates="jobs",
    )

class WorksWith(Base):
    __tablename__ = "works_with"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=True)

    people = relationship(
        "Person",
        secondary=person_works_with,
        back_populates="works_with"
    )