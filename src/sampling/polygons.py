import geopandas as gpd

def extract_polygon_coordinates(municipality_name):
# Ladda shapefile
    gdf = gpd.read_file("src/data/Kommuner.shp")
    # Convert to WGS84 (lat/lon)
    gdf = gdf.to_crs(epsg=4326)
    # Select municipality
    municipality = gdf[gdf["KnNamn"] == municipality_name]
    if municipality.empty:
        raise ValueError(f"Municipality '{municipality_name}' not found in the shapefile.")
    print(municipality)
    return 
