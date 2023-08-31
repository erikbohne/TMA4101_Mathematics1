import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create data points for x1 and x2
x1 = np.linspace(-10, 10, 50)
x2 = np.linspace(-10, 10, 50)

# Create a meshgrid for (x1, x2)
X1, X2 = np.meshgrid(x1, x2)

# Calculate the values of f(x) = 2*x1 + 3*x2 + x1*x2
F = 2 * X1 + 3 * X2 + X1 * X2

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X1, X2, F, cmap='viridis')

# Add labels and title
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('F(x)')
ax.set_title('Plot of f(x) = 2*x1 + 3*x2 + x1*x2')

# Show the plot
plt.show()
