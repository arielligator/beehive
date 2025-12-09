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

@app.get("/talent", response_model=List[schemas.TalentOut])
def list_talent(db: Session = Depends(get_db)):
    return db.query(models.Talent).all()

@app.get("/talent/{talent_id}", response_model=schemas.TalentOut)
def get_talent(talent_id: int, db: Session = Depends(get_db)):
    talent = db.query(models.Talent).filter(models.Talent.id == talent_id).first()
    if not talent:
        raise HTTPException(status_code=404, detail="Talent not found")
    return talent

@app.post("/talent", response_model=schemas.TalentOut)
def create_talent(talent_in: schemas.TalentCreate, db: Session = Depends(get_db)):
    talent = models.Talent(**talent_in.model_dump())
    db.add(talent)
    db.commit()
    db.refresh(talent)
    return talent