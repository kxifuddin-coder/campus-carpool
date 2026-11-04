import { useState, useEffect } from "react";
import RidesCard from "./components/RidesCard.jsx";

const API_URL = "http://127.0.0.1:8001";

function App() {
  const [Ride, setRide] = useState([]);
  const [FromFilter, setFromFilter] = useState("");
  const [ToFilter, setToFilter] = useState("");
  const [DateFilter, setDateFilter] = useState("");

  function loadRides(from,to,date){
    const url = from
      ? `${API_URL}/Rides?from_place=${from}&to_place=${to}&ride_date=${date}`
      : `${API_URL}/Rides`;
    fetch(url)
        .then((res) => res.json())
        .then((data) => setRide(data));
    }
     useEffect(() => {
    loadRides(FromFilter,ToFilter,DateFilter);
  }, [FromFilter,ToFilter,DateFilter]);
  return (
      <>
      <div className="app-header">
        <h1> Carpool Booking</h1>
      </div>
        <ul className="equipment-list">
          {Ride.map((item) => (
            <RidesCard
              key={item.id}
              item={item}
              apiUrl={API_URL}
               />
          ))}
        </ul>
        </>
  );
}

export default App;

