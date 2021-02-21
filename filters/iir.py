from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Butter worth filter creation
b, a = signal.butter(8, 0.125)

# Sample count
n = 60

# Noise signla
sig = np.random.randn(n)**3 + 3*np.random.randn(n).cumsum()

# Back and forth filtering
fpad = signal.filtfilt(b, a, sig, padlen=50)

# Visualize
plt.plot(sig, 'k-', label='input')
plt.plot(fpad, 'c-', linewidth=1.5, label='pad')
plt.legend(loc='best')
plt.show()