import {useState} from "react";

function RidesCard({item,apiUrl}){
    const [passengers, setPassengers] = useState(null)
    const [showPassengers, setShowPassengers] = useState(false)
    const [rollNo, setRollNo] = useState("")
    const [error, setError] = useState("");
    const [msg, setMsg] = useState("");

    return (
    <li>
        <h3>{item.driver_roll}</h3>
    </li>
)
}

export default RidesCard

