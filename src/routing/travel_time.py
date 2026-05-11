import requests

def get_route(start_lon, start_lat, end_lon, end_lat, profile="driving"):
    url = f"http://localhost:5000/route/v1/{profile}/{start_lon},{start_lat};{end_lon},{end_lat}"
    params = {
        "overview": "false",
        "alternatives": "false",
        "steps": "false"
    }

    response = requests.get(url, params=params)

    # Check if the HTTP request was successful
    if response.status_code != 200:
        raise Exception(f"OSRM request failed: {response.status_code} - {response.text}")

    data = response.json()

    # Check if OSRM returned a valid route
    if "routes" not in data or len(data["routes"]) == 0:
        raise Exception("No routes found in OSRM response")

    # Extract total travel time in seconds
    travel_time_seconds = data["routes"][0]["duration"]

    return travel_time_seconds


def get_time(origin, dest):
    start_long = origin[1]
    start_lat = origin[0]
    end_long = dest[1]
    end_lat = dest[0]
    travel_time = get_route(start_long, start_lat, end_long, end_lat)
    return travel_time

