# Third Script of training on Python how to plot GOES-R Imagery: Script 03 - Adding a map with cartopy (Reading parameters from header)
# -------------------------------------------------------------------------------------------------------------- 
# Created by Melissa Dias 
#----------------------------------------------------------------------------------------------------------------
# Required modules
from netCDF4 import Dataset # Read / Write NetCDF4 files
import matplotlib.pyplot as plt # Plotting Library
from datetime import datetime # Basic Dates and time types
import cartopy, cartopy.crs as ccrs # Plot maps
#----------------------------------------------------------------------------------------------------------------
# Open GOES-R data
file = Dataset("OR_ABI-L2-CMIPF-M6C13_G16_s20230751200209_e20230751209530_c20230751209597.nc")

# Get the pixels values
data = file.variables['CMI'][:] - 273.15 # Convert temperature to Celsius
#-----------------------------------------------------------------------------------------------------------------
# Choose the plot size (width x height, in inches)
plt.figure(figsize=(7,7))

# Use the Geostationary projection in cartopy
ax = plt.axes(projection=ccrs.Geostationary(central_longitude=-75.0, satellite_height=35786023.0))
img_extent = (-5434894.67527, 5434894.67527, -5434894.67527, 5434894.67527)

# Add coastlines, borders and gridlines
ax.coastlines(resolution='10m', color='white', linewidth=0.8)
ax.add_feature(cartopy.feature.BORDERS, edgecolor='white', linewidth=0.5)
ax.gridlines(color='white', alpha=0.5, linestyle='--', linewidth=0.5)

# Plot the image
#img = ax.imshow(data, vmin=-80, vmax=40, origin='upper', extend=img_extent, cmap='Greys')
img = ax.imshow(data, vmin=-80, vmax=40, origin='upper', extent=img_extent, cmap='Greys')

# Add a colorbar
plt.colorbar(img, label='Brightness Temperature (°C)', extend='both', orientation='horizontal', pad=0.05, fraction=0.05)

# Extract the date
date = (datetime.strptime(file.time_coverage_start, '%Y-%m-%dT%H:%M:%S.%fZ'))

# Add a title
plt.title('GOES-16 Band 13 ' + date.strftime('%Y-%m-%d %H:%M') + ' UTC', fontweight= 'bold', fontsize=10, loc='left')
plt.title('Full Disk', fontsize=10, loc='right')
#------------------------------------------------------------------------------------------------------------------
# Save the image
plt.savefig('Image_03.png')

# Show the image
plt.show()