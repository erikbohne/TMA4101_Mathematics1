import matplotlib.pyplot as plt
import numpy as np

# Define values
m = 4.8e-26 # molecule mass for air [kg/mol]
g = 9.81 # gravitational acceleration [m/s^2]
k = 1.38e-23 # Boltzmann constant [J/K]
T = 288 # room temperature [K]
p0 = 1.013e5 # atmospheric pressure [Pa]

def p(h):
    return p0 * np.exp(-m*g*h/(k*T))

# Define values
h = np.linspace(0, 50000, 1000) # height [m]

# Plot
plt.plot(h, p(h))
plt.xlabel('Height [m]')
plt.ylabel('Pressure [Pa]')
plt.title('Pressure as a function of height')
plt.show()
