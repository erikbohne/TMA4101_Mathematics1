# Task 3 in Repetisjonsforelesening_TMA4101.pdf

import numpy as np
import matplotlib.pyplot as plt

# Define functions
def f(y):
    return y**2 - y**3

# Define variables
T = 200
n = 1000
h = T / n

y = np.zeros(n + 1)
y[0] = 0.01

for k in range(n):
    
    # Initial guess using Eulers explicit method
    y[k+1] = y[k] + h*f(y[k])
    z = 100
    
    # Using fixpoint iteration to find the correct solution with precision 0.001
    while abs(y[k+1] - z) > 0.001:
        y[k+1] = y[k] + (h/2) * (f(y[k]) + f(y[k+1]))
        z = y[k+1]
        
# Plot solution
plt.plot(y)
plt.show()