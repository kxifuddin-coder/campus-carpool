
from functions import *
from fastapi import HTTPException


def get_ride(ride_id):

    session = Session(engine)

    try:
        ride = session.query(Rides).filter(
            Rides.id == ride_id
        ).first()

        if not ride:
            raise HTTPException(
                status_code=404,
                detail="Ride not found"
            )

        passengers_no = session.query(Seats).filter(
            Seats.ride_id == ride.id,
            Seats.cancelled == 0
        ).all()

        response = {
            "id": ride.id,
            "driver_roll": ride.driver_roll,
            "from_place": ride.from_place,
            "to_place": ride.to_place,
            "ride_date": ride.ride_date,
            "depart_time": ride.depart_time,
            "total_seats": ride.total_seats,
            "seats_left": ride.seats_left,
            "status": ride.status,
        
        }

        for passenger in passengers_no:
            response["passengers"].append({
                "roll_no": passenger.roll_no
            })

        return response

    finally:
        session.close()
