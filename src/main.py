from config import Config
from utils.initiate_sampling_array import initiate_sampling_array
from simulation.pipeline import run_single_iteration
from sampling.pipeline import sample_location
from data.emergency_hospitals import hospitals
from routing.travel_route import route

def main():
    config = Config()          # Alla regler här
    array = initiate_sampling_array()  # Skapa en array 
    run_single_iteration(config, array)
#    print("Klar:", len(results))

if __name__ == "__main__":
    main()