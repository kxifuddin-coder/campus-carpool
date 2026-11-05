import {useState} from "react";

function AddRides(){
    const [driverRoll, setDriverRoll] = useState("");
    const [fromPlace, setFromPlace] = useState("");
    const [toPlace, setToPlace] = useState("");
    const [Date, setDate] = useState("")
    const [Time, setTime] = useState("")
    const [error, setError] = useState("");
    const [msg, setMsg] = useState("");

  function handleSubmit(){

  }
  return (
      <>
      <form className="add-form" onSubmit={handleSubmit}>
          <div>
          <label>Roll No</label>
          <input
            type="text"
            value={driverRoll}
            onChange={(e) => setDriverRoll(e.target.value)}
          />
        </div>
          <div>
              <label>From</label>
              <input
                type="text"
                value={fromPlace}
                onChange={(e) => setFromPlace(e.target.value)}
              />
          </div>
          <div>
              <label>To</label>
              <input
                type="text"
                value={toPlace}
                onChange={(e) => setToPlace(e.target.value)}
              />
          </div>
          <div>
              <label>Date</label>
              <input
                type="date"
                value={Date}
                onChange={(e) => setDate(e.target.value)}
              />
          </div>
          <div>
              <label>Depart Time</label>
              <input
                type="time"
                value={Time}
                onChange={(e) => setTime(e.target.value)}
              />
          </div>
          <button type="submit" className="btn-primary">Add Ride</button>
          </form>
      </>
  )
}


export default AddRides