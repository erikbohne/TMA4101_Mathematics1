"""
Use pytplot quiver to plot a vector field F(x) where F_1(x) = x(1-y) and F_2(x) = y(x-1)
"""
import numpy as np
import matplotlib.pyplot as plt

# Definer x og y verdier
x_values = np.linspace(-10, 10, 20)
y_values = np.linspace(-10, 10, 20)

# Definer F_1(x) = x(1-y) og F_2(x) = y(x-1)
F_1_values = x_values * (1 - y_values)
F_2_values = y_values * (x_values - 1)

# Plot vektorfeltet F(x) = [F_1(x), F_2(x)]
plt.figure()
plt.title('Plot of Vector Field F(x) = [x(1-y), y(x-1)]')
plt.xlabel('F_1(x) = x(1-y)')
plt.ylabel('F_2(x) = y(x-1)')
plt.grid(True)
plt.quiver(x_values, y_values, F_1_values, F_2_values)
plt.show()
