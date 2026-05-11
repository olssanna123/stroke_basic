from random import random
from unittest import case

from sampling.pipeline import sample_location
from routing.triage import triage_patient
from simulation.metrics import loop_none

def run_single_iteration(config, array):
  # 1. Slumpa plats
  point = sample_location(array)

  # 2. Triage (här sker beslutet från flödesschemat)
  res = triage_patient(config, point)
  print(f"Triage result: {res}")
  
  # 3. Simulera om trombektomi identifieras korrekt
  match config.variable:
    case "none":
      res_none = loop_none(config, point, res["Chosen emergency hospital"])
      print(f"Result (no variation): {res_none}")
    case "sensitivity":
      print("Varying sensitivity, keeping specificity constant.")
    case "specificity":
      print("Varying specificity, keeping sensitivity constant.")

  # 4. Beräkna tid
  # 5. Spara resultat
 
  return 