from src.data.emergency_hospitals import hospitals
from src.routing.route_time import get_route_time
from src.models.triage_result import TriageResult
from src.models.hospital import Hospital    

def triage_patient(config, point):
    for h in hospitals:
        if h.name == "Sahlgrenska Universitetssjukhuset":
            su = h.coord()
            su_hospital_object = h

    time_to_sahl = get_route_time(point, su)

    # If the travel time to SU is less than 45 minutes, triage to SU
    if time_to_sahl < config.su_threshold_minutes * 60:
        res = TriageResult(
            chosen_emergency_hospital=su_hospital_object,
            triage_rule="Sahlgrenska Universitetssjukhuset is within given time threshold"
        )
        return res
    
    # Decision rule "Choose the closest emergency hospital. Exception, if another emergency hospital is closer to Sahlgrenska,
    # and the time difference between the that hospital and the closest emergency hospital is less than 15 minutes,
    # the emergency hospital closer to Sahlgrenska is chosen."

    # Create a list of (hospital, travel_time) tuples
    travel_times = [(hospital, get_route_time(point, hospital.coord())) for hospital in hospitals]
   
     # Sort by travel time
    travel_times.sort(key=lambda x: x[1])

    time_to_sahl1 = travel_times[0][1] + get_route_time(travel_times[0][0].coord(), su)
    time_to_sahl2 = travel_times[1][1] + get_route_time(travel_times[1][0].coord(), su)

    if time_to_sahl2 < time_to_sahl1:
        if travel_times[1][1] < config.comparison_threshold_minutes * 60:
            res = TriageResult(
                chosen_emergency_hospital=travel_times[1][0],
                triage_rule="Shorter total time to Sahlgrenska and less than 15 minutes longer than the closest hospital"
            )
            return res
        else:
            res = TriageResult(
                chosen_emergency_hospital=travel_times[0][0],
                triage_rule="Closest emergency hospital"
            )
            return res
    else:
        res = TriageResult(
            chosen_emergency_hospital=travel_times[0][0],
            triage_rule="Closest emergency hospital"
        )
        
    return res