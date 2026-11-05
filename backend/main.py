from datetime import datetime, time, date

from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import E1
import E2
import E3

app = FastAPI()

@app.get("/rides")
def get_rides(from_place:str = None, to_place:str = None, date:str = None):
    try:
        parsed_date = datetime.strptime(date,"%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid date format. Please use YYYY-MM-DD.")    
    return E1.rides(from_place=from_place, to_place=to_place, date=parsed_date)
    

@app.get("/get_ride")
def get_ride(id:int):
    return E2.get_ride(ride_id=id)


@app.post("/offer_ride")
def offer_ride(driver_roll:str, from_place:str, to_place:str, ride_date:date, depart_time:time, total_seats:int):
    return E3.offer_ride(driver_roll=driver_roll, from_place=from_place, to_place=to_place, ride_date=ride_date, depart_time=depart_time, total_seats=total_seats)