from fastapi import FastAPI, HTTPException
import E4
import E5
import E6

app = FastAPI()

@app.patch("/cancel")
def cancel(ride_id : int,driver_roll : str):
    return E4.cancel_ride(ride_id, driver_roll)

@app.post("/book_ride")
def book_ride(ride_id: int, roll_no : str):
    if ride_id < 1:
        raise HTTPException(status_code=400, detail="Ride id must be greater than 0")
    return E5.join_ride(ride_id, roll_no)

@app.patch("/ride")
def leave_ride(ride_id: int):
    if ride_id < 1:
        raise HTTPException(status_code=400, detail="Ride id must be greater than 0")
    return E6.leave_ride(ride_id)