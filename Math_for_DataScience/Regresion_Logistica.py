import matplotlib.pyplot as plt  # The main plotting module in Matplotlib
from mpl_toolkits.mplot3d import Axes3D # Provides tools for 3D plotting
from matplotlib import cm # Colormap handling for creating colored plots
import numpy as np # Numerical library for array operations
import pandas as pd # Data manipulation library

# Calculate the likelihood based on two input values, 'y' and 'yp' 
def likelihood (y, yp):
    return yp*y+(1-yp)*(1-y)

# Create a new figure and adds a 3D subplot it
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

# Create a meshgrid of 'Y' and 'YP' values. A meshgrid is a way of creating a 2D grid form two 1D arrays, which is useful for evaluating functions on a grid
Y = np.arange(0,1,0.01)
YP = np.arange (0,1,0.01)
Y, YP = np.meshgrid(Y, YP)

# Calculate the likelihood values using the 'likelihood' function for each combination of 'Y' and 'YP'
Z = likelihood(Y, YP)

surf = ax.plot_surface(Y, YP, Z, cmap = cm.coolwarm)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
