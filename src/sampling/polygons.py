import geopandas as gpd
from shapely import polygons
from pathlib import Path
import geopandas as gpd
from src.utils.random_generator import model

def extract_polygon_coordinates(municipality_name):
    # Load shapefile
    BASE_DIR = Path(__file__).resolve().parent.parent
    shapefile = BASE_DIR / "data" / "Kommuner.shp"
    gdf = gpd.read_file(shapefile)
    
    # Sweden uses SWEREF 99, globally usually uses WGS84, convert to WGS84 (lat/lon)
    gdf = gdf.to_crs(epsg=4326)
    
    # Get municipality
    municipality = gdf[gdf["KnNamn"] == municipality_name]
    
    if municipality.empty:
        raise ValueError(f"Municipality '{municipality_name}' not found in the shapefile.")
    
    # Extract geometry
    geom = municipality.geometry.iloc[0]

    # Handle MultiPolygon, file contains Polygon and MultiPolygon (islands)
    polygons = geom.geoms if geom.geom_type == "MultiPolygon" else [geom]

    coords_list = []
    for poly in polygons:
        coords_list.append(list(poly.exterior.coords))

        # Sample one polygon if there are multiple 
    index = model(len(coords_list))
    sample = coords_list[index]
    
    return sample




