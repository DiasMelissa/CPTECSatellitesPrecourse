# First Script of training on Python how to plot GOES-R Imagery: Script 01 - Basic Plot / Extracting Pixel Values
# -------------------------------------------------------------------------------------------------------------- 
# Created by Melissa Dias 
#----------------------------------------------------------------------------------------------------------------
# Required modules
from netCDF4 import Dataset # Read / Write NetCDF4 files
import matplotlib.pyplot as plt # Plotting Library
#----------------------------------------------------------------------------------------------------------------
# Open GOES-R data
file = Dataset("OR_ABI-L2-CMIPF-M6C13_G16_s20230751200209_e20230751209530_c20230751209597.nc")

# Show the available variables
print(file.variables.keys())

# Get the pixels values
data = file.variables['CMI'][:]

# Data dimensions
print(data.shape)
#-----------------------------------------------------------------------------------------------------------------
# Choose the plot size (width x height, in inches)
plt.figure(figsize=(10,10))

# Plot the image
plt.imshow(data, vmin=193, vmax=313, cmap='Greys') # vmin e vmax definem os valores da barra de cores em Kelvin
#------------------------------------------------------------------------------------------------------------------
# Save the image
plt.savefig('Image_01.png')

# Show the image
plt.show()