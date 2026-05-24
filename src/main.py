from src.config import Config
from src.database.repository import get_all_iterations, insert_iteration
from src.database.schema import create_tables
from src.simulation.pipeline import run_single_iteration
from src.utils.init_array import initialize_array

def main(): 
    # Skapa databas
    create_tables()  # Skapa tabeller i databasen om de inte redan finns    

    # Testa databas
    iteration = 1
    municipality = "Göteborg"  
    response_time = 15.5  # Exempel på responstid i minuter
    insert_iteration(iteration, municipality, response_time)   
    
    # Kolla databas ok
    rows = get_all_iterations()
    print(rows)  # Skriv ut alla iterationer i databasen

    # Initialize configuration and sampling array
    #config = Config()          # Alla regler här
    #array = initialize_array()  # Skapa en array som representera populationsdensiteten för kommunerna i VGR
    # Kör simuleringen
    #run_single_iteration(config, array)

if __name__ == "__main__":
    main()