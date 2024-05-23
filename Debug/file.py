import numpy as np
import geopandas as gp
from geopandas.tools import sjoin, overlay
from osgeo import gdal, gdalnumeric, ogr, osr
df = gp.read_file('./file.shp')
