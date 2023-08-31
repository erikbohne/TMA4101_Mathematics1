import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definer gridet for plotting
x1, x2 = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))

# Beregn f1 og f2 basert på x1 og x2
f1 = 2 * x1 + 3 * x2
f2 = 4 * x1 + 5 * x2

# Opprett en 3D-plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot f1 og f2 i 3D-rommet
ax.plot_surface(x1, x2, f1, alpha=0.5, rstride=100, cstride=100)
ax.plot_surface(x1, x2, f2, alpha=0.5, rstride=100, cstride=100, facecolors='g')

# Aksetitler og plot tittel
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('F(x)')
ax.set_title('3D-plot av f1 og f2')

# Vis plottet
plt.show()
