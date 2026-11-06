# Campus Carpool

## 1. Problem Statement: Campus Carpool

Students often struggle to find affordable and convenient transportation to places like railway stations, bus stands, airports and nearby areas. At the same time, many students travel in their own vehicles with empty seats.

Currently, there is no common platform for students to connect with others travelling to the same destination. This results in higher travel costs, wasted fuel and unused seats.

**Campus Carpool** is a web application that connects student drivers with passengers travelling along similar routes. Drivers can offer rides by providing their roll number, destination, date, time and available seats. Other students can view rides, book seats or cancel their bookings.

Drivers can also cancel rides or mark them as completed. The application also displays popular routes to help students find commonly travelled destinations.

Our goal is to make campus transportation more affordable, convenient and sustainable by helping students share available vehicle seats.

## 2. Database

One SQLite database file: `carpool.db`

It contains two tables:

**rides**

- id
- driver_roll
- from_place
- to_place
- ride_date
- depart_time
- total_seats
- seats_left
- status

**seats**

- id
- ride_id
- roll_no
- booked_on
- cancelled (0 or 1)

## 3. API Endpoints

| # | What it does | Method | Path | Who | Request parameters |
|---|---|---|---|---|---|
| E1 | Get upcoming rides. Filter by from, to and date. | GET | `/Rides` | adib | `from_place`, `to_place`, `ride_date` (optional) |
| E2 | Get one ride by ID along with passenger roll numbers. | GET | `/get_ride` | adib | `ride_id` |
| E3 | Offer a new ride. Initially, seats left equals total seats. | POST | `/offer_ride` | adib | `driver_roll`, `from_place`, `to_place`, `ride_date`, `depart_time`, `total_seats` |
| E4 | Cancel a ride using the driver's roll number. Cancel all its bookings too. | POST | `/cancel_ride` | kaif | `ride_id`, `driver_roll` |
| E5 | Book a seat in a ride using a roll number. Booking date is today. | POST | `/book_ride` | kaif | `ride_id`, `roll_no` |
| E6 | Cancel a student's seat booking. | POST | `/leave_ride` | kaif | `ride_id`, `roll_no` |
| E7 | Mark a ride as completed using the driver's roll number. | PUT | `/complete_ride` | ayushman | `ride_id`, `driver_roll` |
| E8 | Get a student's active rides, including rides they drive and rides they joined. | GET | `/student_rides` | ayushman | `roll_no` |
| E9 | Get popular routes ranked by the number of completed rides. | GET | `/popular_routes` | ayushman | None |

*Note: Request parameters are shown separately from request bodies because the current frontend sends parameters through the URL query string. The proposed endpoint names and methods for E4–E9 should be adjusted if your backend uses different routes.*

## 4. Technologies Used

- **Frontend:** React, JavaScript, HTML, CSS
- **Backend:** Python, FastAPI
- **Database:** SQLite
- **Version Control:** Git and GitHub

## 5. How to run our app

Someone who has never seen this code should be able to follow these steps.

### Backend

Open a terminal at the project root directory and run:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

Backend will run at:

`http://127.0.0.1:8001`

### Frontend

Open a **new terminal** at the project root directory and run:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL displayed in the terminal (usually `http://localhost:5173`) to access the application.

### Requirements

- Python installed
- Node.js and npm installed
- Git (for cloning the repository)


