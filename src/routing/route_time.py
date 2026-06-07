# --------------------------- Get travel times ---------------------------
from src.routing.travel_route import get_route_info
from src.models.metrics_result import MetricsResult

def get_route_time(origin_latlon, dest_latlon):
    origin_lat, origin_lon = origin_latlon
    dest_lat, dest_lon = dest_latlon

    route_info = get_route_info(
        origin_lon, origin_lat,
        dest_lon, dest_lat
    )

    return route_info["duration"]

def get_all_route_times(point, emergency_hospital, academic_hospital):
    time_to_emergency = get_route_time(point, emergency_hospital)
    time_to_academic = get_route_time(point, academic_hospital)
    time_emergency_to_academic = get_route_time(emergency_hospital, academic_hospital)

    return MetricsResult(
        patient_to_emergency_hospital=time_to_emergency,
        emergency_hospital_to_academic_hospital=time_emergency_to_academic,
        patient_to_academic_hospital=time_to_academic
    )
