# Author: Emirhan Gocturk
# Description: Spectral anaylsis

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.signal
from scipy import *
import copy

srate = 1234 #Hz
npnts = srate * 2 # 2 seconds of data
time = np.arange(0, npnts-1)/srate

# frequencies to be included
frex = [0, 50, 100, 150] #excl. first

signal = np.zeros(len(time))

# populate
for i in range(len(frex)):
    signal = signal + i*np.sin(2*np.pi*frex[i]*time)

# add noise
signal = signal + np.random.randn(len(signal))

# take FFT
signalF = np.fft.fft(signal)
# extract amplitude
signalA = np.abs(signalF)

hz = np.linspace(0, srate/2, int(npnts/2)+1)
hzA = np.zeros(len(hz))

for i in range(len(hzA)):
    hzA[i] = signalA[i]

plt.plot(hz, hzA)
plt.show()
