from config import Config
from utils.initiate_sampling_array import initiate_sampling_array
#from simulation.loop import run_simulation
from sampling.municipality import draw_sample

def main():
    config = Config()          # Alla regler här
    array = initiate_sampling_array()
    sample = draw_sample(array)
    print(sample)
    
#    results = run_simulation(config, data)
#    print("Klar:", len(results))

if __name__ == "__main__":
    main()