from fastapi import FastAPI, status, HTTPException, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi import Depends
from db.orm import get_session
from db.models import CarsTable


app = FastAPI()

@app.get("/cars")
def get_cars(session: Session = Depends(get_session)):
    return {"message": "Hello world"}


@app.get("/brand/{brand}")
def get_cars_by_brand(brand: str, session: Session = Depends(get_session)):
    filtered_cars = session.query(CarsTable).filter_by(brand=brand).all()


    if not filtered_cars:
        message = {"error": f"Cars with brand '{brand}' does not exist!"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    return {"message": filtered_cars}

