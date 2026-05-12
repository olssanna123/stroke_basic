from data.emergency_hospitals import hospitals
from routing.travel_route import route

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

    time_point_to_hospital = route(point, hospital_coordinates)
    h, m, s = seconds_to_hms(time_point_to_hospital)
    print(f"Time from point to hospital: {h} hours, {m} minutes, {s} seconds")

    return 

def metrics_sensitivity(config, point, hospital):   
    print("Varying sensitivity, keeping specificity constant.")
    return

def metrics_specificity(config, point, hospital):
    print("Varying specificity, keeping sensitivity constant.")
    return