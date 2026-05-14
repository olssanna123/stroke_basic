import folium
from routing.travel_route import get_route_info

# --------------------------- Plot routes ---------------------------

def plot_route(m, coords, color="blue", weight=5):

    latlon = [[c[1], c[0]] for c in coords]
    folium.PolyLine(latlon, color=color, weight=weight).add_to(m)

    return m

def plot_three_routes(route1, route2, route3):

    coords1 = route1["routes"]
    duration1 = route1["duration"]
    distance1 = route1["distance"]

    coords2 = route2["routes"]
    duration2 = route2["duration"]
    distance2 = route2["distance"]

    coords3 = route3["routes"]
    duration3 = route3["duration"]
    distance3 = route3["distance"]

    start = [coords1[0][1], coords1[0][0]]

    m = folium.Map(location=start, zoom_start=6)

    plot_route(m, coords1, color="blue")
    plot_route(m, coords2, color="red")
    plot_route(m, coords3, color="green")

    m.save("three_routes.html")

    return m

def build_routes(point, emergency_hospital, academic_hospital):
    point_lat, point_lon = point  # Latitude and longitude for the specified point
    emergency_hospital_lat, emergency_hospital_lon = emergency_hospital  # Latitude and longitude for the emergency hospital
    academic_hospital_lat, academic_hospital_lon = academic_hospital  # Latitude and longitude for the academic hospital

    route1 = get_route_info(point_lon, point_lat, emergency_hospital_lon, emergency_hospital_lat)
    route2 = get_route_info(point_lon, point_lat, academic_hospital_lon, academic_hospital_lat)
    route3 = get_route_info(emergency_hospital_lon, emergency_hospital_lat, academic_hospital_lon, academic_hospital_lat)

    plot_three_routes(route1, route2, route3)

    return 