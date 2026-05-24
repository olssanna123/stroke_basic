from src.config import Config
from src.database.repository import get_all_iterations, insert_iteration, table_info
from src.database.schema import create_tables
from src.simulation.loop import run_loop
from src.simulation.pipeline import run_single_iteration
from src.utils.init_array import initialize_array

def main(): 
    # Initialize configuration, tables and sampling array
    config = Config()          
    create_tables(config)      
    array = initialize_array() 

    # Kör simuleringen
    run_loop(config, array)

    # Kolla resultat
    rows = get_all_iterations()
    print(rows)

if __name__ == "__main__":
    main()