import matplotlib.pyplot as plt
import numpy as np

# Constants (For demonstration purposes)
n = 1       # Amount of moles
R = 8.314   # Ideal gas constant
V = 1       # Volume

# Generate temperature and pressure values
T_values = np.linspace(0.01, 100, 500)  # Temperature must be above zero
p_values = (n * R * T_values) / V       # Pressure at constant volume

plt.figure(figsize=(12, 6))

# Plot pressure as a function of temperature at constant volume
plt.subplot(1, 2, 1)
plt.plot(T_values, p_values)
plt.title('Pressure as a function of Temperature (at constant volume)')
plt.xlabel('Temperature (T)')
plt.ylabel('Pressure (p)')

# Plot temperature as a function of pressure at constant volume
plt.subplot(1, 2, 2)
plt.plot(p_values, T_values)
plt.title('Temperature as a function of Pressure (at constant volume)')
plt.xlabel('Pressure (p)')
plt.ylabel('Temperature (T)')

plt.tight_layout()
plt.show()
