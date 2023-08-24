import cmath
import matplotlib.pyplot as plt
import numpy as np

real_parts = []
imag_parts = []

for k in range(0, 6):
    point = cmath.sqrt(2) * cmath.exp(1j * (np.pi/3 * k + np.pi/4))
    real_parts.append(point.real)
    imag_parts.append(point.imag)
    plt.text(point.real, point.imag, f'k={k}', fontsize=9, ha='right')

plt.scatter(real_parts, imag_parts, color='blue')
plt.axhline(0, color='grey', linestyle='--')
plt.axvline(0, color='grey', linestyle='--')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Plot of z^k * w for k = 0 to 5')
plt.grid(True)
plt.show()
