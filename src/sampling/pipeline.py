from src.sampling.municipality import draw_sample
from src.sampling.polygons import extract_polygon_coordinates 
from src.sampling.points import get_point

def sample_patient(array):
    municipality = draw_sample(array)
    borders = extract_polygon_coordinates(municipality)
    point = get_point(borders)

    patient = {
        "latitude": point[0],
        "longitude": point[1],
        "municipality": municipality
    }

    return patient
