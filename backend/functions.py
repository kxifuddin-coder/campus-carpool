from sqlalchemy import Integer, String, Column, create_engine, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, Session
from datetime import date, datetime

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

session = Session(engine)



