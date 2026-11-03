from sqlalchemy import Integer, String, Column, create_engine, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, Session
from datetime import date, datetime, time, timedelta

DB_PATH = "carpool.db"
engine = create_engine(f"sqlite:///{DB_PATH}")
Base = declarative_base()

class Rides(Base):
    __tablename__ = "riders"
    id = Column(Integer, primary_key=True)
    driver_roll = Column(String)
    from_place = Column(String)
    to_place = Column(String)
    ride_date = Column(DateTime, default=date.today )
    depart_time = Column(DateTime)
    total_seats = Column(Integer)
    seats_left = Column(Integer)
    status = Column(String)



class Seats(Base):
    __tablename__ = "seats"
    id = Column(Integer, primary_key=True)
    ride_id = Column(Integer, ForeignKey("riders.id"), nullable=False)
    roll_no = Column(String, nullable=False)
    booked_on = Column(DateTime, default=date.today)
    cancelled = Column(Integer, nullable=False, default=0)


Base.metadata.create_all(engine)

def add_starting_values():
    with Session(engine) as session:

        # Prevent duplicate sample data every time the API restarts
        if session.query(Rides).first():
            print("Starting data already exists.")
            return

        today = date.today()

        # Sample rides
        rides_data = [
            {
                "driver_roll": "AT101",
                "from_place": "main_gate",
                "to_place": "railway_station",
                "ride_date": today + timedelta(days=1),
                "depart_time": time(9, 30),
                "total_seats": 4,
                "seats_left": 2,
                "status": "scheduled",
                "passengers": ["AT102", "AT103"]
            },
            {
                "driver_roll": "AT201",
                "from_place": "hostels",
                "to_place": "bus_stand",
                "ride_date": today + timedelta(days=2),
                "depart_time": time(10, 0),
                "total_seats": 3,
                "seats_left": 0,
                "status": "scheduled",
                "passengers": ["AT202", "AT203", "AT204"]
            },
            {
                "driver_roll": "AT301",
                "from_place": "main_gate",
                "to_place": "airport",
                "ride_date": today - timedelta(days=1),
                "depart_time": time(8, 0),
                "total_seats": 4,
                "seats_left": 2,
                "status": "completed",
                "passengers": ["AT302", "AT303"]
            },
            {
                "driver_roll": "AT401",
                "from_place": "tech_park",
                "to_place": "hostels",
                "ride_date": today - timedelta(days=2),
                "depart_time": time(18, 0),
                "total_seats": 3,
                "seats_left": 1,
                "status": "scheduled",
                "passengers": ["AT402", "AT403"]
            },
            {
                "driver_roll": "AT501",
                "from_place": "railway_station",
                "to_place": "main_gate",
                "ride_date": today + timedelta(days=3),
                "depart_time": time(7, 30),
                "total_seats": 2,
                "seats_left": 2,
                "status": "cancelled",
                "passengers": []
            },
            {
                "driver_roll": "AT601",
                "from_place": "bus_stand",
                "to_place": "main_gate",
                "ride_date": today + timedelta(days=1),
                "depart_time": time(11, 0),
                "total_seats": 4,
                "seats_left": 3,
                "status": "scheduled",
                "passengers": ["AT602"]
            },
            {
                "driver_roll": "AT701",
                "from_place": "hostels",
                "to_place": "railway_station",
                "ride_date": today + timedelta(days=4),
                "depart_time": time(16, 0),
                "total_seats": 2,
                "seats_left": 1,
                "status": "scheduled",
                "passengers": ["AT702"]
            },
            {
                "driver_roll": "AT801",
                "from_place": "main_gate",
                "to_place": "tech_park",
                "ride_date": today + timedelta(days=5),
                "depart_time": time(14, 0),
                "total_seats": 3,
                "seats_left": 3,
                "status": "scheduled",
                "passengers": []
            }
        ]

        for data in rides_data:

            passengers = data.pop("passengers")

            ride = Rides(
                **{
                    **data,
                    "ride_date": datetime.combine(
                        data["ride_date"], time.min
                    ),
                    "depart_time": datetime.combine(
                        today, data["depart_time"]
                    )
                }
            )

            session.add(ride)

            # Generate the ride ID before creating seat records
            session.flush()

            for passenger in passengers:
                seat = Seats(
                    ride_id=ride.id,
                    roll_no=passenger,
                    booked_on=datetime.now(),
                    cancelled=0
                )

                session.add(seat)

        session.commit()
        print("8 starting rides added successfully!")



if __name__ == "__main__":
    add_starting_values()