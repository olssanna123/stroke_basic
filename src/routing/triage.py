from routing.hospitals import find_nearest_hospital, find_second_nearest
from routing.travel_time import travel_time

def triage_patient(point, data, config):

    su = data.su_hospital

    nearest = find_nearest_hospital(point, data)
    t_su = travel_time(point, su)
    t_nearest = travel_time(point, nearest)

    # 🔴 regel 1: direkt SU
    if t_su < config.su_threshold_minutes:
        chosen = su

    else:
        second = find_second_nearest(point, data)
        t_second = travel_time(point, second)

        # 🔴 regel 2: jämförelse
        if abs(t_nearest - t_su) < config.comparison_threshold_minutes:
            chosen = su
        else:
            chosen = nearest

    return {
        "chosen": chosen,
        "su": su,
        "nearest": nearest,
        "travel_times": {
            "to_su": t_su,
            "to_nearest": t_nearest
        }
    }