import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the ODE system
def system(t, y, mu):
    # y[0] is x and y[1] is x_dot (velocity)
    x, x_dot = y
    g = 9.81  # assuming the constant g is the gravitational acceleration
    x_double_dot = g - mu*x_dot - x
    return [x_dot, x_double_dot]

# Initial conditions
x0 = 0
x_dot0 = 0

# Time span for the solution
t_span = np.linspace(0, 20, 1000)

# Solve and plot for each value of mu
mus = [3, 2, 1]
plt.figure(figsize=(10,6))

for mu in mus:
    sol = solve_ivp(system, [t_span[0], t_span[-1]], [x0, x_dot0], t_eval=t_span, args=(mu,))
    plt.plot(sol.t, sol.y[0], label=f"mu = {mu}")

plt.xlabel("Time (s)")
plt.ylabel("x(t)")
plt.title("Solution of the ODE for different values of mu")
plt.legend()
plt.grid(True)
plt.show()
