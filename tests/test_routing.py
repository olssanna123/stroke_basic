from src.routing.travel_route import get_route_info

def test_get_route_info():
    su_lat, su_lon = (57.6833, 11.9549)
    dest_lat, dest_lon = (59.3293, 18.0686)

    route_info = get_route_info(su_lon, su_lat, dest_lon, dest_lat)

    assert "routes" in route_info
    assert len(route_info["routes"]) > 0
    assert "duration" in route_info["routes"][0]
    assert "distance" in route_info["routes"][0]