from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models

app = FastAPI()

def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"message": "Hello World!"} 
