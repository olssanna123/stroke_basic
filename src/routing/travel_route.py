import requests

# --------------------------- Get route info ---------------------------

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

