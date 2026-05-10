from config import Config
from utils.initiate_sampling_array import initiate_sampling_array
from simulation.pipeline import run_single_iteration

def main():
    config = Config()          # Alla regler här
    array = initiate_sampling_array()
    run_single_iteration(config, array)
#    results = run_simulation(config, data)
#    print("Klar:", len(results))

if __name__ == "__main__":
    main()