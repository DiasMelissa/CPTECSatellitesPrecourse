# Second Script of training on Python how to plot GOES-R Imagery: Script 02 - Basic Operation / Colorbar / Title / Date
# -------------------------------------------------------------------------------------------------------------- 
# Created by Melissa Dias 
#----------------------------------------------------------------------------------------------------------------
# Required modules
from netCDF4 import Dataset # Read / Write NetCDF4 files
import matplotlib.pyplot as plt # Plotting Library
from datetime import datetime # Basic Dates and time types
#----------------------------------------------------------------------------------------------------------------
# Open GOES-R data
file = Dataset("OR_ABI-L2-CMIPF-M6C13_G16_s20230751200209_e20230751209530_c20230751209597.nc")

# Get the pixels values
data = file.variables['CMI'][:] - 273.15 # Convert temperature to Celsius
#-----------------------------------------------------------------------------------------------------------------
# Choose the plot size (width x height, in inches)
plt.figure(figsize=(10,10))

# Plot the image
plt.imshow(data, vmin=-80, vmax=40, cmap='jet')

# Add a colorbar
plt.colorbar(label='Brightness Temperature (°C)', extend='both', orientation='horizontal', pad=0.05, fraction=0.05) # pad é a distancia relativa ao plot e a fraction é o tamanho relativo do plot

# Extract the date
date = (datetime.strptime(file.time_coverage_start, '%Y-%m-%dT%H:%M:%S.%fZ'))

# Add a title
plt.title('GOES-16 Band 13 ' + date.strftime('%Y-%m-%d %H:%M') + ' UTC', fontweight= 'bold', fontsize=10, loc='left')
plt.title('Full Disk', fontsize=10, loc='right')
#------------------------------------------------------------------------------------------------------------------
# Save the image
plt.savefig('Image_02.png')

# Show the image
plt.show()