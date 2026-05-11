from data.emergency_hospitals import hospitals
from routing.travel_time import get_time

def triage_patient(config, point):

    for hospital in hospitals:
        if hospital.name == "Sahlgrenska Universitetssjukhuset":
            su = hospital.coord()


    # If the travel time to SU is less than 45 minutes, triage to SU
    if get_time(point, su) < config.su_threshold_minutes * 60:
        return "Sahlgrenska Universitetssjukhuset"
    
    
    # Decision rule "Choose the closest emergency hospital. Exception, if another emergency hospital is closer to Sahlgrenska,
    # and the time difference between the that hospital and the closest emergency hospital is less than 15 minutes,
    # the emergency hospital closer to Sahlgrenska is chosen."

    # Create a list of (hospital, travel_time) tuples
    travel_times = [(hospital, get_time(point, hospital.coord())) for hospital in hospitals]
    print("Travel times to hospitals:", [(h.name, t) for h, t in travel_times])
    

    return "No suitable hospital found"