# Hanterar simulering och loop vid eventuella avbrott och återupptar simuleringen från där den slutade.

from src.database.repository import insert_iteration


def accepted_iteration(config, iteration, results):

    iteration_results = {
        "iteration": iteration,
        "latitude": results["latitude"],
        "longitude": results["longitude"],
        "municipality": results["municipality"],
        "emergency_hospital": results["emergency_hospital"],
        "triage_rule": results["triage_rule"],
        "patient_to_emergency_hospital": results["patient_to_emergency_hospital"],
        "emergency_hospital_to_academic_hospital": results["emergency_hospital_to_academic_hospital"],
        "patient_to_academic_hospital": results["patient_to_academic_hospital"],
        "variable": results["variable"],
        "saved_time": results["saved_time"]
    }

    insert_iteration(config, iteration_results)
    return