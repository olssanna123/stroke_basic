from src.routing.travel_route import get_route_info

def test_get_route_info():
    su_lat, su_lon = (57.6833, 11.9549)
    dest_lat, dest_lon = (59.3293, 18.0686)

    route_info = get_route_info(
        su_lon,
        su_lat,
        dest_lon,
        dest_lat
    )

    # Kontrollera att förväntade nycklar finns
    assert "routes" in route_info
    assert "duration" in route_info
    assert "distance" in route_info

    # Kontrollera att rutten innehåller koordinater
    assert len(route_info["routes"]) > 0

    # Kontrollera att värden är rimliga
    assert route_info["duration"] > 0
    assert route_info["distance"] > 0

    # Kontrollera att första koordinatpunkten innehåller lon, lat
    first_point = route_info["routes"][0]
    assert len(first_point) == 2