# Author: Emirhan Gocturk
# Description: Triangular wave lookup table data dumper

# ************DRAFT************

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0, 4, 400)
plt.plot(t,2* signal.sawtooth(2 * np.pi * 1 * t,0.5))  
plt.grid()
plt.xlabel("Time[s]")
plt.ylabel("Amplitude [V]")
plt.title("Singal for sampling")
plt.show()