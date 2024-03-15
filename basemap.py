import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


# creating a flat world map
my_map = Basemap()

my_map.drawcoastlines()
# plt.show()


# creating a spherical globe map
globe = Basemap(projection="ortho", lat_0=0, lon_0=0)   #lat and lon show which are should be on the top

globe.drawmapboundary(fill_color="blue")    #fill globe with blue color
globe.fillcontinents(color="green", lake_color="aqua")  #filling continents with green

globe.drawcoastlines()

# plt.show()


# Plotting on the map
# lets point barcelona
my_globe = Basemap(projection="ortho", lat_0=0, lon_0=0)   #lat and lon show which are should be on the top
my_globe.drawmapboundary(fill_color="aqua")    #fill my_globe with blue color
my_globe.fillcontinents(color="coral")  #filling continents with green
my_globe.drawcoastlines()

barc_x_cordinate, barc_y_cordinate = my_globe(2, 41)
text_x, text_y = (-90, 10)

plt.annotate("Barcelona", 
             xy=(barc_x_cordinate, barc_y_cordinate), 
             xycoords="data", 
             xytext=(text_x, text_y),
             arrowprops={"arrowstyle":"fancy", "color": "g"},
             color="r")
plt.show()