import random
from shapely.geometry import Point
from shapely.geometry import Polygon

def coords_to_polygon(coords):
    print(f"Converting {len(coords)} coordinates to polygon.")
    if len(coords) < 3:
        raise ValueError("At least three coordinates are needed to form a polygon.")

    # Close polygon if not closed already
    if coords[0] != coords[-1]:
        coords = coords + [coords[0]]

    return Polygon(coords)

# Generate a random point within polygon and return coordinates
def get_origin(borders):
    poly = coords_to_polygon(borders)
    min_x, min_y, max_x, max_y = poly.bounds
    while (True):
        point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (point.within(poly)):
            break
        else:
            continue
    point_tuple = (point.x, point.y)
    return point_tuple
