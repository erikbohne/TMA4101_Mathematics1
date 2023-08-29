import matplotlib.pyplot as plt
import numpy as np

# Generate a set of x values for each function within the domain of [-3, 3]
x1 = np.linspace(-3, 3, 400)
x2 = np.linspace(-3, -0.1, 200).tolist() + np.linspace(0.1, 3, 200).tolist()  # Avoid division by zero
x3 = np.linspace(0.25, 3, 200)  # Domain starts from 0.25 to avoid sqrt of negative number
x4 = np.linspace(-1, 1, 400)  # Domain is [-1, 1] to avoid sqrt of negative number

# Calculate the y values based on the functions
y1 = x1 - 1
y2 = (x1 + 2)**2
y3 = x1**3 - 1
y4 = 1 + np.sqrt(4 * x3 - 1)
y5 = 1 - np.cbrt(x1)  # Using cube root function np.cbrt
y6 = 2 - (1 / np.array(x2))
y7 = 1 - np.sqrt(1 - x4**2)
y8 = 1 + np.abs(x1 + 1)

# Create the plots
plt.figure(figsize=(12, 8))

plt.plot(x1, y1, label='x-1', color='r')
plt.plot(x1, y2, label='(x+2)^2', color='g')
plt.plot(x1, y3, label='x^3 - 1', color='b')
plt.plot(x3, y4, label='1+sqrt(4x-1)', color='c')
plt.plot(x1, y5, label='1-x^(1/3)', color='m')
plt.plot(x2, y6, label='2-(1/x)', color='y')
plt.plot(x4, y7, label='1-sqrt(1-x^2)', color='k')
plt.plot(x1, y8, label='1+abs(x+1)', color='orange')

# Setting the x and y axis limits
plt.xlim(-3, 3)
plt.ylim(-3, 3)

# Adding grid, title, and labels
plt.grid(True)
plt.title('Plotting Multiple Functions')
plt.xlabel('x')
plt.ylabel('y')

# Add a legend
plt.legend()

# Show the plot
plt.show()
