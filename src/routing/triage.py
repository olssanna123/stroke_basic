from data.emergency_hospitals import hospitals
from routing.travel_time import get_time

def triage_patient(config, point):

    for hospital in hospitals:
        if hospital.name == "Sahlgrenska Universitetssjukhuset":
            su = hospital.coord()

    time_to_sahl = get_time(point, su)


    # If the travel time to SU is less than 45 minutes, triage to SU
    if time_to_sahl < config.su_threshold_minutes * 60:
        res = {
                "Chosen emergency hospital": "Sahlgrenska Universitetssjukhuset",
                "Rule": "Sahlgrenska Universitetssjukhuset is within given time threshold"
            }
        return res
    
    
    # Decision rule "Choose the closest emergency hospital. Exception, if another emergency hospital is closer to Sahlgrenska,
    # and the time difference between the that hospital and the closest emergency hospital is less than 15 minutes,
    # the emergency hospital closer to Sahlgrenska is chosen."

    # Create a list of (hospital, travel_time) tuples
    travel_times = [(hospital, get_time(point, hospital.coord())) for hospital in hospitals]
   
     # Sort by travel time
    travel_times.sort(key=lambda x: x[1])

    time_to_sahl1 = travel_times[0][1] + get_time(travel_times[0][0].coord(), su)
    time_to_sahl2 = travel_times[1][1] + get_time(travel_times[1][0].coord(), su)

    if time_to_sahl2 < time_to_sahl1:
        if travel_times[1][1] < config.comparison_threshold_minutes * 60:
            res = {
                "Chosen emergency hospital": travel_times[1][0].name,
                "Rule": "Shorter total time to Sahlgrenska and less than 15 min."
            }
            return res
        else:
            res = {
                "Chosen emergency hospital": travel_times[0][0].name,
                "Rule": "Closest emergency hospital."
            }
            return res
    else:
        res = {
            "Chosen emergency hospital": travel_times[0][0].name,
            "Rule": "Closest emergency hospital."
        }


    return res