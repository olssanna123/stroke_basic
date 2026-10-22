from src.data.emergency_hospitals import hospitals
from src.routing.plot_route import build_routes
from src.utils.random_generator import model
from src.routing.route_time import get_all_route_times
from src.models.metrics_result import MetricsResult

def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return hours, minutes, secs

def metrics_none(config, point, hospital):  
    for x in hospitals:
        if x.name == "Sahlgrenska Universitetssjukhuset":
            su = x.coord()

    for y in hospitals:
        if y.name == hospital.name:
            hospital_coordinates = y.coord()

    metrics = get_all_route_times(point, hospital_coordinates, su)

    build_routes(point, hospital_coordinates,   su)

    return metrics
