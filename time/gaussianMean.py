# Author: Emirhan Gocturk
# Date: 27 March 2021
# Description: Gaussian mean algorithm

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

fwhm = 25 #ms
k = 100
#todo
gtime = 0
# gaussian
gaussianWindow = numpy.exp(-(4*np.log(2)*gtime**2)/fwhm**2)


plt.plot(time, signal, label="o")
plt.plot(time, filteredSignal, label="f")
plt.show()
