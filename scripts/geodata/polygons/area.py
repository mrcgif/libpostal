import pyproj

from functools import partial
from shapely.ops import transform
from shapely.geometry import Polygon


def polygon_area(poly):
    return transform(
        partial(
            pyproj.transform,
            pyproj.Proj('EPSG:4326'),
            pyproj.Proj(
                proj='aea',
                lat_1=poly.bounds[1],
                lat_2=poly.bounds[3]
            )
        ),
        poly
    ).area


def polygon_bounding_box_area(poly):
    bbox = poly.bounds
    p = Polygon([(bbox[0], bbox[3]), (bbox[0], bbox[1]),
                 (bbox[2], bbox[1]), (bbox[2], bbox[3]),
                 ])
    return polygon_area(p)
