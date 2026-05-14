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

def build_routes():
    Göteborg_lat, Göteborg_lon = (57.7089, 11.9733)  # Latitude and longitude for Gothenburg
    Stockholm_lat, Stockholm_lon = (59.3293, 18.0686)  # Latitude and longitude for Stockholm
    Malmö_lat, Malmö_lon = (55.6050, 13.0038)       # Latitude and longitude for Malmö

    route1 = get_route_info(Göteborg_lon, Göteborg_lat, Stockholm_lon, Stockholm_lat)
    route2 = get_route_info(Göteborg_lon, Göteborg_lat, Malmö_lon, Malmö_lat)
    route3 = get_route_info(Stockholm_lon, Stockholm_lat, Malmö_lon, Malmö_lat)

    plot_three_routes(route1, route2, route3)

    return 