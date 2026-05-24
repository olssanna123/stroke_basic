from src.config import Config
from src.database.repository import get_all_iterations, insert_iteration, table_info
from src.database.schema import create_tables
from src.simulation.pipeline import run_single_iteration
from src.utils.init_array import initialize_array

def main(): 
    # Initialize configuration and sampling array
    config = Config()          # Alla regler här

    # Skapa databas
    create_tables(config)  # Skapa tabeller i databasen om de inte redan finns    

    # Kolla databas ok
    table_info()
 #   rows = get_all_iterations()
 #   print(rows)  # Skriv ut alla iterationer i databasen

    array = initialize_array()  # Skapa en array som representera populationsdensiteten för kommunerna i VGR
    # Kör simuleringen
#    run_single_iteration(config, array)

if __name__ == "__main__":
    main()