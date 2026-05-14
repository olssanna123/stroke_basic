import requests

def get_route_info(start_lon, start_lat, end_lon, end_lat, profile="driving"):
    url = f"http://localhost:5000/route/v1/{profile}/{start_lon},{start_lat};{end_lon},{end_lat}"

    params = {
        "overview": "full",
        "geometries": "geojson"
    }

    response = requests.get(url, params=params)
    data = response.json()

    route = data["routes"][0]

    coords = route["geometry"]["coordinates"]
    duration = route["duration"]      # sekunder
    distance = route["distance"]      # meter

    return coords, duration, distance

import folium

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

    popup_text = f"""
    ⏱️ Tid: {hours:.1f} h<br>
    📏 Avstånd: {km:.0f} km
    """

    # start
    folium.Marker(
        start,
        tooltip="Start",
        popup="Startpunkt"
    ).add_to(m)

    # mål
    folium.Marker(
        end,
        tooltip="Mål",
        popup=popup_text
    ).add_to(m)

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

def get_route_time(origin_latlon, dest_latlon):
    origin_lat, origin_lon = origin_latlon
    dest_lat, dest_lon = dest_latlon

    _, duration, _ = get_route_info(
        origin_lon, origin_lat,
        dest_lon, dest_lat
    )

    return duration

def get_all_travel_times(point, emergency_hospital, academic_hospital):
    time_to_emergency = get_route_time(point, emergency_hospital)
    time_to_academic = get_route_time(point, academic_hospital)
    time_emergency_to_academic = get_route_time(emergency_hospital, academic_hospital)

    res = {
        "time_to_emergency": time_to_emergency, 
        "time_to_academic": time_to_academic,
        "time_emergency_to_academic": time_emergency_to_academic
    } 

    return res