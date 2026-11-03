from functions import *
from fastapi import HTTPException

def cancel_ride(driver_roll):

    session = Session(engine)

    ride = session.query(Rides).filter(Rides.driver_roll == driver_roll).first()
    seat = session.query(Seats).filter(ride.id == Seats.ride_id).first()

    if not ride:
        raise HTTPException(status_code=400, detail="Driver Roll not found")

    ride.status = "cancelled"
    seat.cancelled = 1

    session.add_all([ride])
    session.commit()
    session.close()

def join_ride(ride_id,roll_no):
    session = Session(engine)

    ride = session.query(Rides).filter(Rides.id == ride_id).first()
    print(ride)
    if not ride:
        raise HTTPException(status_code=400, detail="Ride not found")

    book = Seats(ride_id=ride.id,roll_no=roll_no,booked_on=date.today(),cancelled=0)
    session.add(book)
    session.commit()
    response = {
        "id": book.id,
        "ride_id": book.ride_id,
        "roll_no": book.roll_no,
        "booked_on": book.booked_on,
        "cancelled": book.cancelled
    }
    session.close()
    return response

