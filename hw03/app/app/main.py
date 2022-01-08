from fastapi import FastAPI, Request, Depends, status
from fastapi.exceptions import HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/health")
def health(request: Request):
    return {"status": "ok", "host": request.client.host}


@app.post("/user")
def create_user(body: schemas.UserCreate, db: Session = Depends(get_db)):
    crud.create_user(db, body)


@app.get("/user/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@app.put("/user/{user_id}")
def put_user(user_id: int, body: schemas.UserUpdate, db: Session = Depends(get_db)):
    crud.update_user(db, user_id, body)


@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db, user_id)


# Prometheus
Instrumentator().instrument(app).expose(app)
