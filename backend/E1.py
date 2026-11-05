
from functions import *
from datetime import date as today_date

def rides(from_place=None, to_place=None, date=None):

    session = Session(engine)

    try:
        rides = session.query(Rides).filter(
            Rides.status == "scheduled",
            Rides.ride_date >= today_date.today()
        )

        if from_place:
            rides = rides.filter(Rides.from_place == from_place)

        if to_place:
            rides = rides.filter(Rides.to_place == to_place)

        if date:
            rides = rides.filter(Rides.ride_date == date)

        return [
            {
                "id": r.id,
                "driver_roll": r.driver_roll,
                "from_place": r.from_place,
                "to_place": r.to_place,
                "ride_date": r.ride_date,
                "depart_time": r.depart_time,
                "total_seats": r.total_seats,
                "seats_left": r.seats_left,
                "status": r.status
            }
            for r in rides.all()
        ]

    finally:
        session.close()
