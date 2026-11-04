from fastapi import FastAPI, HTTPException
import E4
import E5

app = FastAPI()

@app.patch("/cancel")
def cancel(driver_roll : str):
    return E4.cancel_ride(driver_roll)

@app.post("/book_ride")
def book_ride(ride_id: int, roll_no : str):
    return E5.join_ride(ride_id, roll_no)