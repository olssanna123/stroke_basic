from routing.travel_time import get_time
from data.emergency_hospitals import hospitals

def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    return hours, minutes, secs

def metrics_none(config, point, hospital):  
    print(hospital)

    for x in hospitals:
        if x.name == "Sahlgrenska Universitetssjukhuset":
            su = x.coord()

    for y in hospitals:
        if y.name == hospital.name:
            hospital_coordinates = y.coord()

    time_point_to_hospital = get_time(point, hospital_coordinates)
    h, m, s = seconds_to_hms(time_point_to_hospital)
    print(f"Time from point to hospital: {h} hours, {m} minutes, {s} seconds")

    time_hospital_to_su = get_time(hospital_coordinates, su)
    h, m, s = seconds_to_hms(time_hospital_to_su)
    print(f"Time from hospital to Sahlgrenska: {h} hours, {m} minutes, {s} seconds")

    time_point_to_su = get_time(point, su)
    h, m, s = seconds_to_hms(time_point_to_su)
    print(f"Time from point to Sahlgrenska: {h} hours, {m} minutes, {s} seconds")


    return 
