from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Beehive App")


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Beehive App API is running"}


# --- Talent Endpoints ---

@app.get("/people", response_model=List[schemas.PersonOut], tags=["People"])
def list_people(db: Session = Depends(get_db)):
    people = db.query(models.Person).all()
    return people

@app.get("/people/{person_id}", response_model=schemas.PersonOut, tags=["People"])
def get_person(person_id: int, db: Session = Depends(get_db)):
    # get a single person by id
    person = db.query(models.Person).filter(models.Person.id == person_id).first()
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@app.post("/people", response_model=schemas.PersonOut, tags=["People"])
def create_person(person_in: schemas.PersonCreate, db: Session = Depends(get_db)):
    """
    Create a new person.

    Right now this only sets the core fields (name, contact info).
    Later we can extend this to also attach departments and jobs.
    """    
    person = models.Person(**person_in.model_dump())
    db.add(person)
    db.commit()
    db.refresh(person)
    return person