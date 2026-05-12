from random import random
from unittest import case

from sampling.pipeline import sample_location
from routing.triage import triage_patient
from simulation.metrics import metrics_none, metrics_sensitivity, metrics_specificity

def run_single_iteration(config, array):
  # 1. Slumpa plats
  point = sample_location(array)

  # 2. Triage (här sker beslutet från flödesschemat)
  res = triage_patient(config, point)
  
  # 3. Simulera om trombektomi identifieras korrekt och beräkna resultatet av det (beroende på vilken variabel som var vald i config)
  match config.variable:
    case "none":
      metrics_none(config, point, res["Chosen emergency hospital"])
    case "sensitivity":
      metrics_sensitivity(config, point, res["Chosen emergency hospital"])
    case "specificity":
      metrics_specificity(config, point, res["Chosen emergency hospital"])
    case _:
      print("Invalid variable in config. Please choose 'sensitivity', 'specificity', or 'none'.")
      return  

  # 4. Spara resultat
 
  return 