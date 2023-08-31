import matplotlib.pyplot as plt
import numpy as np

# Definer t-verdier
t_values = np.linspace(-10, 10, 500)

# Definer z1(t) = t^3 og z2(t) = t^2
z1_values = t_values ** 3
z2_values = t_values ** 2

# Plot vektorverdiert funksjon z(t) = [z1(t), z2(t)]
plt.figure()
plt.title('Plot of Vector-Valued Function z(t) = [t^3, t^2]')
plt.xlabel('z1(t) = t^3')
plt.ylabel('z2(t) = t^2')
plt.grid(True)
plt.plot(z1_values, z2_values)
plt.show()
