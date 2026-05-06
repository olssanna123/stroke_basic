from config import Config
from utils.initiate_sampling_array import initiate_sampling_array

def main():
    config = Config()          # Alla regler här
    array = initiate_sampling_array()
    print(array)

#    results = run_simulation(config, data)
#    print("Klar:", len(results))

if __name__ == "__main__":
    main()