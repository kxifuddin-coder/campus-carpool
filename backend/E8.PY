from functions import *
from fastapi import HTTPException


def student_rides(roll_no: str):

    if not roll_no or not roll_no.strip():
        raise HTTPException(status_code=422, detail="Roll number is required")

    with Session(engine) as session:

        driving = session.query(Rides).filter(
            Rides.driver_roll == roll_no,
            Rides.status != "cancelled"
        ).all()

        joined = session.query(Rides).join(
            Seats, Seats.ride_id == Rides.id
        ).filter(
            Seats.roll_no == roll_no,
            Seats.cancelled == 0,
            Rides.status != "cancelled"
        ).all()

        return {
            "driving": driving,
            "joined": joined
        }