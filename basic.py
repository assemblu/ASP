import matplotlib.pyplot as plt
import numpy as np

A = 10
f0 = 0.10
phi = np.pi/2
fs = 44100
t = np.arange(-20, .20, 1/fs)
x = A * np.cos(2*np.pi*f0*t+phi)

plt.plot(t, x)
plt.show()