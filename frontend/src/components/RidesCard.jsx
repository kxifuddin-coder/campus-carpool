import {useState} from "react";

function RidesCard({item,apiUrl}){
    const [passengers, setPassengers] = useState(null)
    const [showPassengers, setShowPassengers] = useState(false)
    const [rollNo, setRollNo] = useState("")
    const [error, setError] = useState("");
    const [msg, setMsg] = useState("");

    function handle_book(){

    }

    function show_passengers(){

    }
    return (
    <li>
        <h3>{item.driver_roll}</h3>
        <p>From : {item.from_place} --- To : {item.to_place}</p>
        <p>Date : {item.ride_date} | Time : {item.depart_time}</p>
        <p> Seats left : {item.seats_left}</p>
        <div>
            <button className="rides" onClick={handle_book}>Join Ride</button>
        </div>
        <div>
            <button className="showPassengers" onClick={show_passengers}>Show Passengers</button>
        </div>
    </li>
)
}

export default RidesCard

