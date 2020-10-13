# Author: Emirhan Gocturk
# Description: Pulse wave lookup table data dumper

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 6.5, 0.1)
y = signal.square(t, 0.5)
plt.plot(t, y)  
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("Pulse Wave Sample")
plt.show()

print("DATA DUMP= ", y)