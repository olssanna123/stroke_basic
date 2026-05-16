from src.sampling.municipality import draw_sample
from src.sampling.polygons import extract_polygon_coordinates 
from src.sampling.points import get_point

def sample_location(array):
    municipality = draw_sample(array)
    borders = extract_polygon_coordinates(municipality)
    point = get_point(borders)
    return point
