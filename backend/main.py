from fastapi import FastAPI, HTTPException
import E7
import E8

app = FastAPI ()

@app.patch("/complete_ride")
def complete_ride(driver_roll: str, ride_id: int):
    return E7.complete_ride(driver_roll, ride_id)

@app.get("/student_rides")
def student_rides(roll_no: str):
    return E8.student_rides(roll_no)