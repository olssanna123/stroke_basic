from random import random
from unittest import case

from sampling.pipeline import sample_location
from routing.triage import triage_patient

def run_single_iteration(config, array):
  # 1. Slumpa plats
  point = sample_location(array)

  # 2. Triage (här sker beslutet från flödesschemat)
  res = triage_patient(config, point)
  
  # 3. Simulera om trombektomi identifieras korrekt
  match config.variable:
    case "none":
      print("No variation in sensitivity or specificity.")
    case "sensitivity":
      print("Varying sensitivity, keeping specificity constant.")
    case "specificity":
      print("Varying specificity, keeping sensitivity constant.")

  # 4. Beräkna tid
  # 5. Spara resultat
 
  return 