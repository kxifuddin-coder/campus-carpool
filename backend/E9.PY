from functions import *
from sqlalchemy import func, desc


def popular_routes():

    with Session(engine) as session:

        results = session.query(
            Rides.from_place,
            Rides.to_place,
            func.count(Rides.id).label("rides")
        ).filter(
            Rides.status == "completed"
        ).group_by(
            Rides.from_place,
            Rides.to_place
        ).order_by(
            desc("rides")
        ).all()

        popular = []

        for ride in results:

            popular.append({
                "from_place": ride[0],
                "to_place": ride[1],
                "rides": ride[2]
            })

        return popular