# Required libraries
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as np # Import the Numpy package

# Path to the GOES-R simulated image file
path = r"F:\LAMCE\18.11.19\A2019241171500.L2_LAC_OC.nc"

# Open the file using the NetCDF4 library
nc = Dataset(path)
#print (nc)

# Create two variables to find what we want
gd=nc.groups['geophysical_data']
#print(gd)
nd=nc.groups['navigation_data']
#print(nd)

#Extract the Chrolophyll A values from the NetCDF
data = gd.variables['chlor_a'][:]
data_rot = np.rot90(data,2)

lat=nd.variables['latitude']
print(lat)
lon=nd.variables['longitude']
print(lon)

bmap = Basemap(projection='merc')

# Read some variables from the NetCDF header in order to use it in the plot
#geo_extent = nc.variables['geospatial_lat_lon_extent']
 
#center = str(geo_extent.geospatial_lon_center)
#west = str(geo_extent.geospatial_westbound_longitude)
#east = str(geo_extent.geospatial_eastbound_longitude)
#north = str(geo_extent.geospatial_northbound_latitude)
#south = str(geo_extent.geospatial_southbound_latitude)


# Plot the GOES-16 channel with the converted CPT colors
bmap.imshow(data_rot, cmap='rainbow', origin='upper', vmin=0, vmax=5)


