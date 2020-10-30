# transform coordinates from web mercator to EPSG 4326 (decimal degrees)


# test the Transformer
from pyproj import Transformer
transformer = Transformer.from_crs('epsg:3857', 'epsg:4326')
transformer.transform(47.516, 14.550)


def trans_func(lat_long_string) -> str:
    """transform coordinate system

    Parameters:
    ---------
    lat_long_string: e.g. '-38.416, -63.616'

    """
    # instantiate transformer
    transformer = Transformer.from_crs('epsg:3857', 'epsg:4326')

    lat_str = lat_long_string.split(',')[0]
    long_str = lat_long_string.split(',')[1]
    transformed = transformer.transform(lat_str, long_str)  # returns a tuple

    coords_str = (str(transformed[0])) + ', ' + (str(transformed[1]))
    return coords_str  # in decimal degrees !
