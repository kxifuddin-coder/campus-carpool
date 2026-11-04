from functions import *
from fastapi import HTTPException

def cancel_ride(driver_roll):

    session = Session(engine)

    ride = session.query(Rides).filter(Rides.driver_roll == driver_roll).first()
    if not ride:
        raise HTTPException(status_code=400, detail="Driver Roll not found")

    seat = session.query(Seats).filter(ride.id == Seats.ride_id).first()

    if not seat:
        raise HTTPException(status_code=400, detail="Seat not found")



    ride.status = "cancelled"
    seat.cancelled = 1

    session.add_all([ride])
    session.commit()
    session.close()
