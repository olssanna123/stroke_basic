from xml.parsers.expat import model

from sqlalchemy import case

from src import config
from src.sampling.pipeline import sample_patient
from src.routing.triage import triage_patient
from src.simulation.metrics import metrics_none, metrics_sensitivity, metrics_specificity
from src.models.route_result import Result
from src.models.variable import Variable
from src.models.patient import Patient
from src.models.triage_result import TriageResult
from src.models.metrics_result import MetricsResult
from src.models.time_status import TimeStatus, SAVED, LOST

def run_single_iteration(config, array):

  # 1. Slumpa patient och hämta koordinater
  patient = sample_patient(array)
  point = (patient.latitude, patient.longitude)

 
  # 2. Triage 
  triage_results = triage_patient(config, point)
 
  # 3. Simulera trombektomi diganostik av instrument och beräkna resultatet av det (beroende på vilken variabel som var vald i config)
  match config.variable:
    case Variable.NONE:
      metrics_results = metrics_none(config, point, triage_results.chosen_emergency_hospital)

      if triage_results.chosen_emergency_hospital.name == "Sahlgrenska Universitetssjukhuset":
        calc_time = 0
      else:
        calc_time = (
            metrics_results.patient_to_emergency_hospital
          + metrics_results.emergency_hospital_to_academic_hospital
          + config.akut_treatment_time * 60
          - metrics_results.patient_to_academic_hospital
        )
      
      results = Result(
        latitude=point[0],
        longitude=point[1],
        municipality=patient.municipality,
        emergency_hospital=triage_results.chosen_emergency_hospital.name,
        triage_rule=triage_results.triage_rule,
        patient_to_emergency_hospital=metrics_results.patient_to_emergency_hospital,
        emergency_hospital_to_academic_hospital=metrics_results.emergency_hospital_to_academic_hospital,
        patient_to_academic_hospital=metrics_results.patient_to_academic_hospital,
        variable=config.variable,
        time=calc_time
      )

      return results
    case Variable.SENSITIVITY:
      metrics_results = metrics_none(config, point, triage_results.chosen_emergency_hospital)

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
    
      if triage_results.chosen_emergency_hospital.name == "Sahlgrenska Universitetssjukhuset":
        calc_time = 0
        print("Patient triaged to SU, no saved time.")
      elif percentage:
        calc_time = 0
        print("Trombektomi not identified, no saved time.")
      else:
        calc_time = (
            metrics_results.patient_to_emergency_hospital
          + metrics_results.emergency_hospital_to_academic_hospital
          + config.akut_treatment_time * 60
          - metrics_results.patient_to_academic_hospital
        )
        print("Trombektomi correctly identified, calculating saved time.")

      results = Result(
        latitude=point[0],
        longitude=point[1],
        municipality=patient.municipality,
        emergency_hospital=triage_results.chosen_emergency_hospital.name,
        triage_rule=triage_results.triage_rule,
        patient_to_emergency_hospital=metrics_results.patient_to_emergency_hospital,
        emergency_hospital_to_academic_hospital=metrics_results.emergency_hospital_to_academic_hospital,
        patient_to_academic_hospital=metrics_results.patient_to_academic_hospital,
        variable=config.variable,
        time=calc_time
      )


    case Variable.SPECIFICITY:
      metrics_results = metrics_none(config, point, triage_results.chosen_emergency_hospital)
      
      specificity = model(10)

      match config.specificity:
        case 90:
            percentage = specificity == 10
        case 80:
            percentage = specificity == 10 or specificity == 9
        case 50:
            percentage = specificity == 10 or specificity == 9 or specificity == 8 or specificity == 7 or specificity == 6 
        case _:
            print("Unknown percentage!")

      if triage_results.chosen_emergency_hospital.name == "Sahlgrenska Universitetssjukhuset":
        calc_time = 0
        time_status = SAVED
        print("Patient triaged to SU, no saved time.")
      elif percentage:
        calc_time = (metrics_results.patient_to_academic_hospital - metrics_results.patient_to_emergency_hospital)
        time_status = LOST
        print("Trombektomi falsely identified, calculating lost time.")     
      else:
        calc_time = (
            metrics_results.patient_to_emergency_hospital
          + metrics_results.emergency_hospital_to_academic_hospital
          + config.akut_treatment_time * 60
          - metrics_results.patient_to_academic_hospital
        )
        time_status = SAVED
        print("Trombektomi correctly identified, no lost time.")


      results = Result(
        latitude=point[0],
        longitude=point[1],
        municipality=patient.municipality,
        emergency_hospital=triage_results.chosen_emergency_hospital.name,
        triage_rule=triage_results.triage_rule,
        patient_to_emergency_hospital=metrics_results.patient_to_emergency_hospital,
        emergency_hospital_to_academic_hospital=metrics_results.emergency_hospital_to_academic_hospital,
        patient_to_academic_hospital=metrics_results.patient_to_academic_hospital,
        variable=config.variable,
        time=calc_time,
        time_status=time_status
      )
      
    case _:
      print("Invalid variable in config. Please choose 'sensitivity', 'specificity', or 'none'.")
      return  

  return 