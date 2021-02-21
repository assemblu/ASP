from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

b, a = signal.butter(9, 0.125)

n = 60
sig = np.random.randn(n)**3 + 3*np.random.randn(n).cumsum()
fpad = signal.filtfilt(b, a, sig, padlen=50)
plt.plot(sig, 'k-', label='input')
plt.plot(fpad, 'c-', linewidth=1.5, label='pad')
plt.legend(loc='best')
plt.show()