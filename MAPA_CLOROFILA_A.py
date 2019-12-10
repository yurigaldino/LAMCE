"""OS DADOS VEM UM POCUO DIFERENTES DO PRIMEIRO SCRIPT E É PRECISO COLOCAR LAT E LON NOS DADOS PARA APARECEREM CORRETAMENTE NO GRÁFICO"""
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
fig = plt.figure()

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

lat=nd.variables['latitude']
lon=nd.variables['longitude']

# setup mercator basemap focusing in Brazil.
#m = Basemap(projection='merc', llcrnrlat=-40, urcrnrlat=10,
               # llcrnrlon=-80, urcrnrlon=-20, resolution='l')

# setup mercator basemap world.
m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')

#define which projection the data will appear
bmap = Basemap(projection='merc')


m.drawcoastlines()
m.fillcontinents(color='#cc9966',lake_color='aqua')
# draw parallels and meridians.
m.drawparallels(np.arange(-20,100,10),labels=[1,0,0,0])
m.drawmeridians(np.arange(-100,20,20),labels=[1,0,0,1])
m.drawmapboundary(fill_color='white')
plt.title("Clorofila A")

x0, y0 = map(40, 70)
x1, y1 = map(50, 5.965)

# Plot the GOES-16 channel with the converted CPT colors
bmap.imshow(data_rot, origin = 'upper', extent = (x0, x1, y0, y1), cmap='rainbow',  vmin=0, vmax=5)

# Insert the legend at the bottom
#bmap.colorbar(location='right', label='')






