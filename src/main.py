from config import Config
from utils.initiate_sampling_array import initiate_sampling_array
from sampling.pipeline import sample_location

def main():
    config = Config()          # Alla regler här
    array = initiate_sampling_array()
    point = sample_location(array)
    print(point)
#    results = run_simulation(config, data)
#    print("Klar:", len(results))

if __name__ == "__main__":
    main()