from src.routing.plot_route import build_routes

point = [58.52242069827435, 13.004078046446764]  # Example coordinates (longitude, latitude)
em_hospital = [57.928649, 12.521170]  # Example coordinates for Alingsås lasarett (longitude, latitude)
su_hospital = [57.6833, 11.9549]  # Example coordinates for Sahlgrenska Universitetssjukhuset (longitude, latitude)

build_routes(point, em_hospital, su_hospital)