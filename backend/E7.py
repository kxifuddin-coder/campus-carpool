from functions import * 
from fastapi import HTTPException


def complete_ride(driver_roll, ride_id):
    session = Session(engine)
    ride = session.query(Rides).filter(Rides.id == ride_id).first()
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    if ride.driver_roll != driver_roll:
        raise HTTPException(status_code=404, detail="Driver not found")
    if ride.status != "scheduled":
        raise HTTPException(status_code=404, detail="Ride not found")
    ride.status = "completed"
    session.commit()
    session.close()
   