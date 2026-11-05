from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import E4
import E5
import E6
import E7
import E8
import E9

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- E4: Cancel a ride ---
@app.patch("/cancel")
def cancel(ride_id: int, driver_roll: str):
    return E4.cancel_ride(ride_id, driver_roll)

# --- E5: Join a ride ---
@app.post("/book_ride")
def book_ride(ride_id: int, roll_no: str):
    if ride_id < 1:
        raise HTTPException(status_code=400, detail="Ride id must be greater than 0")
    return E5.join_ride(ride_id, roll_no)

# --- E6: Leave a ride ---
@app.patch("/ride")
def leave_ride(ride_id: int, roll_no: str):
    if ride_id < 1:
        raise HTTPException(status_code=400, detail="Ride id must be greater than 0")
    return E6.leave_ride(ride_id, roll_no)

# --- E1 (via E4): Get all rides ---
@app.get("/Rides")
def get_rides():
    return E4.get_rides()

# --- E2 (via E5): Get one ride with passengers ---
@app.get("/get_ride")
def get_ride(ride_id: int):
    return E5.get_ride(ride_id=ride_id)

# --- E7: Mark a ride completed ---
@app.patch("/complete_ride")
def complete_ride(driver_roll: str, ride_id: int):
    return E7.complete_ride(driver_roll, ride_id)

# --- E8: Get a student's rides ---
@app.get("/student_rides")
def student_rides(roll_no: str):
    return E8.student_rides(roll_no)

# --- E9: Get popular routes ---
@app.get("/popular_routes")
def popular_routes():
    return E9.popular_routes()
