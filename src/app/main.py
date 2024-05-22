from fastapi import FastAPI, status, HTTPException, Response, Query
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
def get_cars_by_brand(brand: str,
                      price_min: int = Query(None, alias="priceMin"),
                      price_max: int = Query(None, alias="priceMax"),
                      mileage_min: int = Query(alias="mileageMin"),
                      mileage_max: int = Query(alias="mileageMax"),
                      session: Session = Depends(get_session)):
    query_cars = session.query(CarsTable).filter_by(brand=brand)
    if price_min is not None:
        query_cars = query_cars.filter(CarsTable.price >= price_min)
    if price_max is not None:
        query_cars = query_cars.filter(CarsTable.price <= price_max)

    query_cars = query_cars.filter(CarsTable.mileage <= mileage_max,
                                   CarsTable.mileage >= mileage_min)

    filtered_cars = query_cars.all()

    if not filtered_cars:
        message = {"warning": "No cars found"}
        return JSONResponse(status_code=status.HTTP_200_OK, content=message)

    return {"debug": price_min, "message": filtered_cars}