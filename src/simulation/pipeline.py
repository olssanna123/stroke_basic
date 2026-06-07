from src import config
from src.sampling.pipeline import sample_patient
from src.routing.triage import triage_patient
from src.simulation.metrics import metrics_none, metrics_sensitivity, metrics_specificity
from src.models.route_result import Result
from src.models.variable import Variable
from src.models.patient import Patient
from src.models.triage_result import TriageResult

def run_single_iteration(config, array):

  # 1. Slumpa patient och hämta koordinater
  patient = sample_patient(array)
  point = (patient.latitude, patient.longitude)

  # 2. Triage 
  triage_results = triage_patient(config, point)
  
  print(config.variable)
  print(type(config.variable))

  # 3. Simulera trombektomi diganostik av instrument och beräkna resultatet av det (beroende på vilken variabel som var vald i config)
  match config.variable:
    case Variable.NONE:
      metrics_results = metrics_none(config, point, triage_results.chosen_emergency_hospital)

      if triage_results.chosen_emergency_hospital.name == "Sahlgrenska Universitetssjukhuset":
        calc_time = 0
      else:
        calc_time = (
            metrics_results["Patient to emergency hospital"]
          + metrics_results["Emergency hospital to academic hospital"]
          + config.akut_treatment_time * 60
          - metrics_results["Patient to academic hospital"]
        )
      
      results = Result(
        latitude=point[0],
        longitude=point[1],
        municipality=patient.municipality,
        emergency_hospital=triage_results.chosen_emergency_hospital.name,
        triage_rule=triage_results.triage_rule,
        patient_to_emergency_hospital=metrics_results["Patient to emergency hospital"],
        emergency_hospital_to_academic_hospital=metrics_results["Emergency hospital to academic hospital"],
        patient_to_academic_hospital=metrics_results["Patient to academic hospital"],
        variable=config.variable,
        time=calc_time
      )
      
      return results
    case Variable.SENSITIVITY:
      metrics_sensitivity(config, point, triage_results.chosen_emergency_hospital)
    case Variable.SPECIFICITY:
      metrics_specificity(config, point, triage_results.chosen_emergency_hospital)
    case _:
      print("Invalid variable in config. Please choose 'sensitivity', 'specificity', or 'none'.")
      return  

  return 