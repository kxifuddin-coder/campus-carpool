from functions import *
from fastapi import HTTPException


def leave_ride(ride_id: int):

    session = Session(engine)
    ride = session.query(Seats).filter(Seats.id == ride_id).first()

    if ride is None:
        raise HTTPException(status_code=404, detail="Ride not found")

    ride.cancelled = True
    session.add(ride)
    session.commit()
    session.close()