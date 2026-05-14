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

    if "routes" not in data or not data["routes"]:
        raise ValueError(f"No route found: {data}")

    route = data["routes"][0]

    coords = route["geometry"]["coordinates"]
    duration = route["duration"]      # sekunder
    distance = route["distance"]      # meter

    return {
        "routes": coords,
        "distance": distance,
        "duration": duration
    }
