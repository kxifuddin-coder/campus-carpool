from functions import *

def get_rides(from_location, to_location, date):
     
    session = Session(engine)
    rides=session.query(Rides).filter(Rides.from_place==from_location, 
    Rides.to_place==to_location, 
    Rides.ride_date==date).all()
    
    response = []

    for ride in rides:
            response.append({
                "id": ride.id,
                "driver_roll": ride.driver_roll,
                "from_place": ride.from_place,
                "to_place": ride.to_place,
                "ride_date": ride.ride_date,
                "depart_time": ride.depart_time,
                "total_seats": ride.total_seats,
                "seats_left": ride.seats_left,
                "status": ride.status
                })

    session.commit()
    session.close()
    return response
      