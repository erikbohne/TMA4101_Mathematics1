import numpy as np
import matplotlib.pyplot as plt

# Define constants
h0 = 101000 # Pa
m = 28*1.66*10e-27
T = 288 # Kelvin
k = 1.38 * 1e-23
g = 9.81

def p(h):
    return h0 * np.exp(-(m*g*h)/(T*k))

h_values = np.arange(0,50000, 100)
p_values = p(h_values)

plt.plot(h_values, p_values)
plt.show()