from fastapi import FastAPI, HTTPException
import E4

app = FastAPI()

@app.patch("/cancel")
def cancel(driver_roll : str):
    return E4.cancel_ride(driver_roll)

