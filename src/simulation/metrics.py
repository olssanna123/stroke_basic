from routing.travel_time import get_time
from data.emergency_hospitals import hospitals

def metrics_none(config, point, hospital):  

    for hospital in hospitals:
        if hospital.name == "Sahlgrenska Universitetssjukhuset":
            su = hospital.coord()

    if hospital.name == "Sahlgrenska Universitetssjukhuset":
        res = {
                "Saved time": 0
            }
        return res

    for h in hospitals:
        if h.name == hospital.name:
            hospital_coordinates = h.coord()

    time_point_to_hospital = get_time(point, hospital_coordinates)
    time_point_to_sahl = get_time(point, su)
    time_hospital_to_sahl = get_time(hospital_coordinates, su)

    saved_time = (time_point_to_hospital + config.akut_treatment_time*60 + time_hospital_to_sahl) - time_point_to_sahl
    
    res = {
        "Saved time": saved_time    }       
    return res

def metrics_sensitivity(point, hospital):
    pass

def metrics_specificity(point, hospital):
    pass    
