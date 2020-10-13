# Author: Emirhan Gocturk
# Description: Sine wave lookup table data dumper

import matplotlib.pyplot as plt
import numpy as np

Fs = 8000
f = 5
sample = 8000
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)*2
plt.plot(x, y)
plt.grid()
plt.xlabel("Sample [n]")
plt.ylabel("Amplitude [V]")
plt.show()
