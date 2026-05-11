from sampling.pipeline import sample_location
from routing.triage import triage_patient

def run_single_iteration(config, array):
  # 1. Slumpa plats
  point = sample_location(array)

  # 2. Triage (här sker beslutet från flödesschemat)
  res = triage_patient(config, point)
  print("Triage result:", res)
  
  # 3. Simulera om trombektomi identifieras korrekt
  # 4. Beräkna tid
  # 5. Spara resultat
 
  return 