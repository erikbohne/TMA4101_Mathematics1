import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.linspace(-10, 10, 500)
Y = np.linspace(-10, 10, 500)
X, Y = np.meshgrid(X, Y)

# Remove zeros to avoid division by zero error in log.
X[X==0] = np.nan
Y[Y==0] = np.nan

# Define Z based on the given function f(x, y) = x + y - ln|x| - ln|y|
Z = X + Y - np.log(np.abs(X)) - np.log(np.abs(Y))

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(np.nanmin(Z), np.nanmax(Z))
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
