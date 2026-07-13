import geopandas as gpd
from shapely import polygons
from pathlib import Path
import geopandas as gpd
from src.utils.random_generator import model

def extract_polygon_coordinates(municipality_name):
    # Ladda shapefile
    BASE_DIR = Path(__file__).resolve().parent.parent
    shapefile = BASE_DIR / "data" / "Kommuner.shp"
    gdf = gpd.read_file(shapefile)
    
    # Konvertera från SWEREF 99 till to WGS84
    gdf = gdf.to_crs(epsg=4326)
    
    # Hämta datan för kommunen
    municipality = gdf[gdf["KnNamn"] == municipality_name]
    
    if municipality.empty:
        raise ValueError(f"Municipality '{municipality_name}' not found in the shapefile.")
    
    # Hämta geometrin för kommunen
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




