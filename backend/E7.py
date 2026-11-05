from functions import *
from fastapi import HTTPException
from datetime import date


def complete_ride(driver_roll: str, ride_id: int):

    if not driver_roll or not driver_roll.strip():
        raise HTTPException(status_code=422, detail="Driver roll number is required")

    with Session(engine) as session:

        ride = session.query(Rides).filter(
            Rides.id == ride_id
        ).first()

        if not ride:
            raise HTTPException(status_code=404, detail="Ride not found")

        if ride.driver_roll != driver_roll:
            raise HTTPException(status_code=403, detail="You're not allowed to do this")

        if ride.status != "scheduled":
            raise HTTPException(status_code=400, detail="Ride is not scheduled")

        if ride.ride_date > date.today():
            raise HTTPException(status_code=400, detail="Cannot complete ride before its date")

        ride.status = "completed"

        session.commit()

        return {"message": "Ride completed successfully"}