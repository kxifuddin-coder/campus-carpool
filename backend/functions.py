from sqlalchemy import Integer, String, Column, create_engine, ForeignKey, DateTime, Date, Time
from sqlalchemy.orm import declarative_base
from datetime import date, timedelta, time

DB_PATH = "carpool.db"
engine = create_engine(f"sqlite:///{DB_PATH}")
Base = declarative_base()

class Rides(Base):
    __tablename__ = "rides"
    id = Column(Integer, primary_key=True)
    driver_roll = Column(String)
    from_place = Column(String)
    to_place = Column(String)
    ride_date = Column(Date, default=date.today )
    depart_time = Column(Time)
    total_seats = Column(Integer)
    seats_left = Column(Integer)
    status = Column(String)



class Seats(Base):
    __tablename__ = "seats"
    id = Column(Integer, primary_key=True)
    ride_id = Column(Integer, ForeignKey("rides.id"), nullable=False)
    roll_no = Column(String, nullable=False)
    booked_on = Column(DateTime, default=date.today)
    cancelled = Column(Integer, nullable=False, default=0)


Base.metadata.create_all(engine)

# session = Session(engine)




