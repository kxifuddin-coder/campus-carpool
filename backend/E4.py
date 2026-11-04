from functions import *
from fastapi import HTTPException

def cancel_ride(ride_id,driver_roll):

    session = Session(engine)

    ride = session.query(Rides).filter(Rides.id == ride_id, Rides.driver_roll == driver_roll).first()

    if not ride:
        raise HTTPException(status_code=400, detail="Ride not found (check ride_id and driver_roll)")

    seats = session.query(Seats).filter(ride.id == Seats.ride_id).all()
    for seat in seats:
        if not seat:
            raise HTTPException(status_code=400, detail="No Seats booked for this ride")

        seat.cancelled = 1

    if ride.status != "scheduled":
        raise HTTPException(status_code=400, detail="This ride is currently not scheduled")

    ride.status = "cancelled"

    session.add_all([ride])
    session.commit()
    session.close()
