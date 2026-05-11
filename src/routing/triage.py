from data.emergency_hospitals import hospitals
from routing.travel_time import get_time

def triage_patient(config, point):

    for hospital in hospitals:
        if hospital.name == "Sahlgrenska Universitetssjukhuset":
            su = hospital.coord()


    # If the travel time to SU is less than 45 minutes, triage to SU
    if get_time(point, su) < config.su_threshold_minutes * 60:
        return "Sahlgrenska Universitetssjukhuset"

    return