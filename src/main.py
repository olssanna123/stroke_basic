from src.config import Config
from src.utils.initiate_sampling_array import initiate_sampling_array
from src.simulation.pipeline import run_single_iteration
from src.data.db import Base, engine
import src.data.models

def main():
    
    # Initialize the database
    Base.metadata.create_all(bind=engine)
    print("Database initialized")
    
    # Initialize configuration and sampling array
    config = Config()          # Alla regler här
    array = initiate_sampling_array()

    # Run the simulation for a specified number of iterations
    

if __name__ == "__main__":
    main()