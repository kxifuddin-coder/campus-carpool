from functions import *
from fastapi import HTTPException
from datetime import date

def complete_ride(driver_roll: str, ride_id: int):

    session = Session(engine)
    ride = session.query(Rides).filter(Rides.ride_id == ride_id).first()
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    ride.status = "completed"
    session.commit()
    session.close()
    return {"message": "Ride completed successfully"}