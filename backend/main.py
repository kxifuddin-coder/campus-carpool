from datetime import date, time

from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import E1
import E2
import E3

app = FastAPI()

@app.get("/get_rides")
def get_rides(from_location:str, to_location:str, date:str):
    rides = E1.get_rides(from_location=from_location, to_location=to_location, date=date)
    

    if not rides:
        raise HTTPException(status_code=404, detail="No rides found")
    return rides 

@app.get("/get_ride")
def get_ride(id:int):
    return E2.get_ride(ride_id=id)


@app.post("/offer_ride")
def offer_ride(driver_roll:str, from_place:str, to_place:str, ride_date:date, depart_time:time, total_seats:int):
    return E3.offer_ride(driver_roll=driver_roll, from_place=from_place, to_place=to_place, ride_date=ride_date, depart_time=depart_time, total_seats=total_seats)  
