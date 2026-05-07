import geopandas as gpd
from shapely import polygons

def extract_polygon_coordinates(municipality_name):
    # Load shapefile
    gdf = gpd.read_file("src/data/Kommuner.shp")
    
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

    print(coords_list)

    return 
