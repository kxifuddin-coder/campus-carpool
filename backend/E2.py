from functions import *


def get_ride(ride_id):

    session=Session(engine)   
    ride=session.query(Rides).filter(Rides.id==ride_id).first()
    if not ride:
        return None

    passengers_no=session.query(Seats).filter(Seats.ride_id==ride.id).all()

    response=[]
    for passenger in passengers_no:
        response.append({
            "roll_no": passenger.roll_no
        })

    
    session.commit()
    session.close() 
    return response
    



    
