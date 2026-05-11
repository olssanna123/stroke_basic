from config import Config
from utils.initiate_sampling_array import initiate_sampling_array
from simulation.pipeline import run_single_iteration
from routing.travel_time import get_time

def main():
    config = Config()          # Alla regler här
    
    Stockholm = (59.3293, 18.0686)
    Göteborg = (57.7089, 11.9746)

    travel_time = get_time(Stockholm, Göteborg)
    print(f"Travel time from Stockholm to Göteborg: {travel_time} seconds")

#    results = run_simulation(config, data)
#    print("Klar:", len(results))

if __name__ == "__main__":
    main()