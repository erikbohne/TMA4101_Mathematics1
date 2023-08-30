import matplotlib.pyplot as plt
import numpy as np

# Generate a set of y values
y = np.linspace(-30, 30, 400)

# Calculate the x values based on the equation x = y * sin(y)
x = y * np.sin(y)

# Create the plot
plt.figure(figsize=(12, 8))

plt.plot(x, y, label='x = y * sin(y)', color='r')

# Setting the x and y axis limits for better visualization
plt.xlim(-30, 30)
plt.ylim(-30, 30)

# Adding grid, title, and labels
plt.grid(True)
plt.title('Plotting the curve x = y * sin(y)')
plt.xlabel('x')
plt.ylabel('y')

# Add a legend
plt.legend()

# Show the plot
plt.show()
