from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import E1,functions

app = FastAPI()

@app.get("/get_rides")
def get_rides(from_location:str, to_location:str, date:str):
    rides = E1.get_rides(from_location=from_location, to_location=to_location, date=date)
    

    if not rides:
        raise HTTPException(status_code=404, detail="No rides found")
    return rides 