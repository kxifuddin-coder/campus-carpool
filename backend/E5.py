from functions import *
from fastapi import HTTPException


def join_ride(ride_id,roll_no):
    session = Session(engine)

    ride = session.query(Rides).filter(Rides.id == ride_id).first()
    seats = session.query(Seats).filter(Seats.ride_id == ride_id).all()
    existing_booking = (session.query(Seats).join(Rides, Seats.ride_id == Rides.id).filter(
            Seats.roll_no == roll_no,
            Seats.cancelled == 0,
            Rides.ride_date == ride.ride_date ).first()  )

    if not ride:
        raise HTTPException(status_code=400, detail="Ride not found")

    if ride.seats_left == 0:
        raise HTTPException(status_code=400, detail="Ride has no seats")

    for seat in seats:
        if seat.roll_no == roll_no:
            raise HTTPException(status_code=400, detail="Ride has already been booked")



    if ride.driver_roll == roll_no:
        raise HTTPException(status_code=400, detail="Cannot book own ride")

    if ride.status in ["cancelled","completed"] or ride.ride_date < date.today():
        raise HTTPException(status_code=400, detail="Ride not available")

    if existing_booking:
        raise HTTPException(status_code=400, detail="Student has already joined another ride on this date")

    book = Seats(ride_id=ride.id,roll_no=roll_no,booked_on=date.today(),cancelled=0)
    session.add(book)

    ride.seats_left = ride.seats_left -1

    response = {
        "id": book.id,
        "ride_id": book.ride_id,
        "roll_no": book.roll_no,
        "booked_on": book.booked_on,
        "cancelled": book.cancelled
    }

    session.commit()
    session.close()
    return response


def get_ride(ride_id):
    session = Session(engine)
    ride = session.query(Rides).filter(Rides.id == ride_id).first()
    if not ride:
        return None

    passengers_no = session.query(Seats).filter(Seats.ride_id == ride.id).all()

    response = []
    for passenger in passengers_no:
        response.append({
            "roll_no": passenger.roll_no
        })

    session.commit()
    session.close()
    return response