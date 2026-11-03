# campus-carpool


- ### Problem Statement: Campus Carpool – A Smarter Way to Travel

Every day, students at our college struggle to find convenient and affordable 
transportation to reach places like railway stations, bus stands, airports, 
and nearby hostels. At the same time, many students travel in their own vehicles 
with empty seats available. Imagine a student named Rahul who is driving from the 
college to the railway station but has three empty seats in his car. 
Meanwhile, another student, Arjun, needs to reach the railway station but cannot 
find reliable transportation. Currently, there is no common platform where these students 
can connect. This leads to unnecessary travel expenses, wasted fuel, and increased traffic. 
To solve this problem, we propose Campus Carpool, a web-based platform that connects 
student drivers with passengers travelling along similar routes. Drivers can offer rides
by sharing their roll number, destination, date, time, and available seats. 
Other students can browse available rides, book seats, or cancel their bookings when 
plans change. Drivers can also cancel rides or mark trips as completed. 
The platform will display popular routes to help students identify frequently 
travelled destinations. By providing a simple and accessible carpooling system without
requiring login accounts, we aim to reduce transportation costs, make better use of 
available vehicle seats, and encourage a more connected and sustainable campus community.

## Database

One SQLite file, carpool.db, with two tables:

*rides;*
id, driver_roll, from_place, to_place, ride_date, depart_time, total_seats, seats_left, status
*seats;*
id, ride_id, roll_no, booked_on, cancelled (0 or 1)

## API Endpoints

| # | What it does | Method | Path | Who      | Request body |
|---|--|--------|------|----------|--------------|
| E1 | Get the upcoming rides: scheduled and today or later. Can be filtered by from, to and date. | | | adib     | |
| E2 | Get one ride by its id, with the roll numbers of its passengers | | | adib     | |
| E3 | Offer a ride: driver's roll number, from, to, date, time and total seats. Seats left start equal to total seats | | | adib     | |
| E4 | Cancel a ride, with the driver's roll number. All its seats are cancelled too. | | | kaif     | |
| E5 | Join a ride with a roll number. The booking date is today | | | kaif     | |
| E6 | Leave a ride (cancel a seat). | | | kaif     | |
| E7 | Mark a ride completed, with the driver's roll number | | | ayushman | |
| E8 | Get one student's rides that aren't cancelled, by roll number: the ones they drive and the ones they joined. | | | ayushman | |
| E9 | Get the popular routes: the number of completed rides for each from → to pair, most first | | | ayushman | |


