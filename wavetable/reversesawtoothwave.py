# Author: Emirhan Gocturk
# Description: Reverse sawtooth wave lookup table data dumper
# it is a bit weird..

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 6.3, 0.01)
y = signal.sawtooth(t, 0.1)
plt.plot(t, y)  
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("Sawtooth Wave Sample")
plt.show()

print("DATA DUMP= ", y)