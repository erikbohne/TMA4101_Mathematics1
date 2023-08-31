import matplotlib.pyplot as plt
import numpy as np

# Constants (For demonstration purposes)
n = 1       # Amount of moles
R = 8.314   # Ideal gas constant
T = 100     # Temperature
p = 100     # Pressure

# Generate temperature and pressure values
V_values = np.linspace(0.1, 100, 500)  # Volume must be above zero

# Pressure and Volume at constant temperature
p_values_at_const_T = n * R * T / V_values

# Temperature and Volume at constant pressure
T_values_at_const_p = p * V_values / (n * R)

plt.figure(figsize=(12, 6))

# Plot pressure as a function of volume at constant temperature
plt.subplot(1, 2, 1)
plt.plot(V_values, p_values_at_const_T)
plt.title('Pressure as a function of Volume (at constant temperature)')
plt.xlabel('Volume (V)')
plt.ylabel('Pressure (p)')

# Plot temperature as a function of volume at constant pressure
plt.subplot(1, 2, 2)
plt.plot(V_values, T_values_at_const_p)
plt.title('Temperature as a function of Volume (at constant pressure)')
plt.xlabel('Volume (V)')
plt.ylabel('Temperature (T)')

plt.tight_layout()
plt.show()
