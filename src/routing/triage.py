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
   
     # Sort by travel time
    travel_times.sort(key=lambda x: x[1])
    print("Travel times to hospitals:", [(h.name, t) for h, t in travel_times])


    time_to_sahl1 = travel_times[0][1] + get_time(travel_times[0][0].coord(), su)
    time_to_sahl2 = travel_times[1][1] + get_time(travel_times[1][0].coord(), su)

    print(f"Time to Sahlgrenska via {travel_times[0][0].name}: {time_to_sahl1} seconds")
    print(f"Time to Sahlgrenska via {travel_times[1][0].name}: {time_to_sahl2} seconds")

    if time_to_sahl2 < time_to_sahl1:
        if travel_times[1][1] < config.comparison_threshold_minutes * 60:
            res = {
                "Chosen emergency hospital": travel_times[1][0],
                "Option": "Decision rule: Shorter total time to Sahlgrenska and less than 15 min.",
                "Closest emergency hospital": travel_times[0][0]
            }
            return res
        else:
            res = {
                "Chosen emergency hospital": travel_times[0][0],
                "Option": "Decision rule: Closest emergency hospital.",
                "Closest emergency hospital": travel_times[0][0]
            }
            return res
    else:
        res = {
            "Chosen emergency hospital": travel_times[0][0],
            "Option": "Decision rule: Closest emergency hospital.",
            "Closest emergency hospital": travel_times[0][0]
        }


    return res