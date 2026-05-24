from random import random
from unittest import case

from src.sampling.pipeline import sample_patient
from src.routing.triage import triage_patient
from src.simulation.metrics import metrics_none, metrics_sensitivity, metrics_specificity

def run_single_iteration(config, array):

  # 1. Slumpa plats
  patient = sample_patient(array)
  point = (patient["latitude"], patient["longitude"])

  # 2. Triage 
  triage_results = triage_patient(config, point)

  # 3. Simulera om trombektomi identifieras korrekt och beräkna resultatet av det (beroende på vilken variabel som var vald i config)
  match config.variable:
    case "none":
      metrics_results = metrics_none(config, point, triage_results["Chosen emergency hospital"])
      time = (metrics_results["Patient to emergency hospital"] + metrics_results["Emergency hospital to academic hospital"] + config.akut_treatment_time*60) - metrics_results["Patient to academic hospital"]

      res = {
        "Latitude": point[0],
        "Longitude": point[1],
        "Municipality": patient["municipality"],
        "Chosen emergency hospital": triage_results["Chosen emergency hospital"].name,
        "Triage rule": triage_results["Triage rule"],
        "Patient to emergency hospital": metrics_results["Patient to emergency hospital"],
        "Emergency hospital to academic hospital": metrics_results["Emergency hospital to academic hospital"],
        "Patient to academic hospital": metrics_results["Patient to academic hospital"],
        "Variable": config.variable,
        "Time": time
      }
      
      print(res)
      return res
    case "sensitivity":
      metrics_sensitivity(config, point, triage_results["Chosen emergency hospital"])
    case "specificity":
      metrics_specificity(config, point, triage_results["Chosen emergency hospital"])
    case _:
      print("Invalid variable in config. Please choose 'sensitivity', 'specificity', or 'none'.")
      return  

  # 4. Spara resultat


  return 