import folium

from routing.travel_route import get_route_info

# --------------------------- Plot routes ---------------------------

def plot_route(coords, duration, distance):

    start = [coords[0][1], coords[0][0]]
    end = [coords[-1][1], coords[-1][0]]

    m = folium.Map(location=start, zoom_start=6)

    # rutt
    latlon = [[c[1], c[0]] for c in coords]
    folium.PolyLine(latlon, color="blue", weight=5).add_to(m)

    # format
    hours = duration / 3600
    km = distance / 1000

    return m

def route(origin_latlon, dest_latlon):

    origin_lat, origin_lon = origin_latlon
    dest_lat, dest_lon = dest_latlon

    coords, duration, distance = get_route_info(
        origin_lon, origin_lat,
        dest_lon, dest_lat
    )

    m = plot_route(coords, duration, distance)
    m.save("route.html")

    return duration


