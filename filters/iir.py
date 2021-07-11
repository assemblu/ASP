# Author: Emirhan Gocturk
# Description: Butterworth IIR filter

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fftpack
import scipy
import copy


# filter parameters
srate   = 1024 # hz
nyquist = srate/2
frange  = [20,45]

# create filter coefficients
fkernB,fkernA = signal.butter(4,np.array(frange)/nyquist,btype='bandpass')

# generate an impulse signal
impres = np.zeros(1001)
impres[501] = 1

# apply filtering
fimp = signal.lfilter(fkernB, fkernA, impres, axis=-1)

frange = [90, 130]
fkernB, fkernA = signal.butter(4, np.array(frange)/nyquist, btype='bandpass')
fimp = signal.lfilter(fkernB, fkernA, fimp, axis=-1)

# power spectrum
fimpX = np.abs(fftpack.fft(fimp))**2
hz = np.linspace(0, nyquist, int(np.floor(len(impres)/2)+1))


# plot
plt.plot(impres, 'k', label="impulse")
plt.plot(fimp, 'r', label="Filtered")
plt.xlim([1, len(impres)])
plt.ylim([-0.06, 0.06])
plt.legend()
plt.show()

plt.plot(hz, fimpX[0:len(hz)], 'ks-')
plt.xlim([0, 100])
plt.show