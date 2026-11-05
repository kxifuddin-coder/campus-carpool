from functions import *
from fastapi import HTTPException


def leave_ride(ride_id: int,roll_no: str):

    session = Session(engine)
    seat = session.query(Seats).filter(Seats.id == ride_id, Seats.roll_no == roll_no).first()

    if seat is None:
        raise HTTPException(status_code=404, detail="Seat not found")

    ride = session.query(Rides).filter(Rides.id == ride_id).first()

    if ride.status in ["cancelled", "completed"]:
        raise HTTPException(status_code=404, detail="cannot leave ride which is completed/cancelled")

    seat.cancelled = True
    session.add(seat)
    session.commit()
    session.close()