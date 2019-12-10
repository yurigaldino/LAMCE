from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
fig = plt.figure()

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
#bmap.imshow(data_rot, cmap='rainbow', origin='upper', vmin=0, vmax=5)

map = Basemap(projection='merc', 
              lat_0=0, lon_0=0)

map.drawlsmask(land_color = "#ddaa66", 
               ocean_color="#7777ff",
               resolution = 'l')

x0, y0 = map(-59.6330, -14.9472)
x1, y1 = map(-34.8146, 5.965)

plt.imshow(data_rot,  extent = (x0, x1, y0, y1))
        
axicon = fig.add_axes([0.1, 0., 0.15, 0.15])
axicon.imshow(data_rot, origin = 'upper')
axicon.set_xticks([])
axicon.set_yticks([])