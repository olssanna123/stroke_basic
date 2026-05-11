from config import Config
from utils.initiate_sampling_array import initiate_sampling_array
from simulation.pipeline import run_single_iteration
from routing.triage import triage_patient

def main():
    config = Config()          # Alla regler här
    vallgraven = (57.7028, 11.9624)
    stenungsund = (58.0705, 11.8181)
    triage_result = triage_patient(config, stenungsund)
    print("Triage result:", triage_result)

#    results = run_simulation(config, data)
#    print("Klar:", len(results))

if __name__ == "__main__":
    main()