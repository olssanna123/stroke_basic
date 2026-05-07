from config import Config
from sampling.polygons import extract_polygon_coordinates

def main():
    config = Config()          # Alla regler här
    kommungrans = extract_polygon_coordinates("Ale")
#    results = run_simulation(config, data)
#    print("Klar:", len(results))

if __name__ == "__main__":
    main()