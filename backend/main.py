from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import E4
import E5
import E6

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.patch("/cancel")
def cancel(ride_id : int,driver_roll : str):
    return E4.cancel_ride(ride_id, driver_roll)

@app.post("/book_ride")
def book_ride(ride_id: int, roll_no : str):
    if ride_id < 1:
        raise HTTPException(status_code=400, detail="Ride id must be greater than 0")
    return E5.join_ride(ride_id, roll_no)

@app.patch("/ride")
def leave_ride(ride_id: int,roll_no : str):
    if ride_id < 1:
        raise HTTPException(status_code=400, detail="Ride id must be greater than 0")
    return E6.leave_ride(ride_id, roll_no)

@app.get("/Rides")
def get_rides():
    return E4.get_rides()