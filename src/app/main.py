from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi import Depends
from db.orm import get_session


app = FastAPI()

@app.get("/cars")
def get_cars(session: Session = Depends(get_session)):
    return {"message": "Hello world"}