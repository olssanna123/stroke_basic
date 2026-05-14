from config import Config
from routing.plot_route import build_routes
from utils.initiate_sampling_array import initiate_sampling_array
from simulation.pipeline import run_single_iteration

def main():
    config = Config()          # Alla regler här
    build_routes()

if __name__ == "__main__":
    main()