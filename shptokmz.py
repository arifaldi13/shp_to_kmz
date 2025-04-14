import geopandas as gpd
import simplekml
import os

def shp_to_kmz(shp_path, kmz_path):
    gdf = gpd.read_file(shp_path)
    kml = simplekml.Kml()
    for _, row in gdf.iterrows():
        geom = row.geometry
        extended_data = {key: str(value) for key, value in row.items() if key != "geometry"}        
        if geom.geom_type == "Point":
            pnt = kml.newpoint(name=row.index[0], coords=[(geom.x, geom.y)])
            for key, value in extended_data.items():
                pnt.extendeddata.newdata(name=key, value=value)
        elif geom.geom_type == "LineString":
            line = kml.newlinestring(name=row.index[0], coords=list(geom.coords))
            for key, value in extended_data.items():
                line.extendeddata.newdata(name=key, value=value)
        elif geom.geom_type == "Polygon":
            pol = kml.newpolygon(name=row.index[0], outerboundaryis=list(geom.exterior.coords))
            for key, value in extended_data.items():
                pol.extendeddata.newdata(name=key, value=value)
    kml.savekmz(kmz_path)
    print(f"KMZ file saved at: {kmz_path}")
