from data.emergency_hospitals import hospitals
from routing.travel_route import route
from utils.random_generator import model

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

    sensitivity = model(10)

    match config.sensitivity:
        case 90:
            percentage = sensitivity == 10
        case 80:
            percentage = sensitivity == 10 or sensitivity == 9
        case 50:
            percentage = sensitivity == 10 or sensitivity == 9 or sensitivity == 8 or sensitivity == 7 or sensitivity == 6 
        case _:
            print("Unknown percentage!")
    
    if hospital.name == "Sahlgrenska Universitetssjukhuset":
        print("Patient triaged to SU, no saved time.")
    elif percentage:
        print("Trombektomi not identified, calculating lost time.")
    else:
        print("Trombektomi correctly identified, calculating saved time.")
    return

def metrics_specificity(config, point, hospital):
    print("Varying specificity, keeping sensitivity constant.")
    return