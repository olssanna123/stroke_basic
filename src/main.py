from src.config import Config
from src.simulation.pipeline import run_single_iteration
from src.utils.init_array import initialize_array

def main(): 
    # Skapa databas
    
    # Initialize configuration and sampling array
    config = Config()          # Alla regler här
    array = initialize_array()  # Skapa en array som representera populationsdensiteten för kommunerna i VGR
    # Kör simuleringen
    #    run_single_iteration(config, array)

if __name__ == "__main__":
    main()