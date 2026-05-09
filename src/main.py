from config import Config
from sampling.polygons import extract_polygon_coordinates
from sampling.points import get_origin

def main():
    config = Config()          # Alla regler här
    kommungrans = extract_polygon_coordinates("Öckerö")
    print("Kommungräns:", len(kommungrans), "coordinates")
    origin = get_origin(kommungrans)
    print("Origin:", origin)
#    results = run_simulation(config, data)
#    print("Klar:", len(results))

if __name__ == "__main__":
    main()