from functions import *
def popular_routes():
    session = Session(engine)
    rides = session.query(Rides).filter(Rides.status == "completed" ).all()
    routes = {}
    for ride in rides:
        route = (ride.from_place, ride.to_place)
        if route in routes:
            routes[route] = routes[route] + 1
        else:
            routes[route] = 1
    popular = []
    for route, total in routes.items():
        popular.append({
            "from_place": route[0],
            "to_place": route[1],
            "total_rides": total
        })
    for i in range(len(popular)):
        for j in range(i + 1, len(popular)):
            if popular[i]["total_rides"] < popular[j]["total_rides"]:
                temp = popular[i]
                popular[i] = popular[j]
                popular[j] = temp
                session.close()
                return popular