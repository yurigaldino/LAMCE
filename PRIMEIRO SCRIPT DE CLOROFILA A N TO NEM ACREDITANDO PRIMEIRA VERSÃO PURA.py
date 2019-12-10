# Required libraries
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as np # Import the Numpy package

# Path to the GOES-R simulated image file
path = r"C:\Users\Administrator\Desktop\A2019241171500.L2_LAC_OC.nc"

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
#lat=nd.variables['latitude']
#lon=nd.variables['longitude']

#bmap = Basemap(projection='stere',width= 10000000, height=8000000, lon_0=-41, lat_0=0, ellps='GRS80')

# Plot the GOES-16 channel with the converted CPT colors
#bmap.imshow(data, cmap='rainbow', origin='upper', vmin=0, vmax=5)

# Show data
plt.imshow(data_rot)