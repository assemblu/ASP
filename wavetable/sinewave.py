# Author: Emirhan Gocturk
# Description: Sine wave lookup table data dumper

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 6.3, 0.01)
y = np.sin(t)
plt.plot(t, y)
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("Sine Wave Sample")
plt.show()

print("DATA DUMP= ", y)