# Author: Emirhan Gocturk
# Description: Running mean filter

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.signal
from scipy import *
import copy

# signal creation
srate = 1000 #Hz
time = np.arange(0, 3, 1/srate)
n = len(time)
p = 15 #num of poles

noiseamp = 5

ampl = np.interp(np.linspace(0, p, n), np.arange(0, p), np.random.rand(p)*30)
noise = noiseamp * np.random.randn(n)
signal = ampl + noise

# init filtered signal
filteredSignal = np.zeros(n)

# running mean
k = 20


plt.plot(time, signal, label="o")
plt.plot(time, filteredSignal, label="f")
plt.show()