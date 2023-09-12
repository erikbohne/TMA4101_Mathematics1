import numpy as np
import matplotlib.pyplot as plt

# Define values
T0 = 6 # Initial temperature
TK = 20 # Room temperature
alpha = np.log(2)/2 # Cooling constant

# Define function
def T(t):
    return TK + (T0 - TK)*np.exp(-alpha*t)

# Define time interval
t = np.linspace(0, 24, 240) # 10 min intervals for 24 hours

# Plot
plt.plot(t, T(t))
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (C)')
plt.show()
