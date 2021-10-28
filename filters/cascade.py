# Author: Emirhan Gocturk
# Description: Butterworth IIR filter

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fftpack
import scipy
import copy

def outputFileWrite(buffer, fileName):
    # delete output file
    fileName = "impulse"
    if os.path.exists(fileName + ".txt"):
        print("The " + fileName + " output file exists. Deleting...")
        os.remove(fileName + ".txt")
    else:
        print("The " + fileName + " output file doesn't exist. Nothing to delete.")

    # write to file
    f = open(fileName + ".txt", "w+")
    count = 0
    while count < len(buffer):
        f.write(str(int(buffer[count])))
        f.write(", ")
        count += 1

    print("Write complete.")
    print("Written element count: ", str(len(buffer)))

# filter parameters
srate   = 1024 # hz
nyquist = srate/2

# create filter coefficients
# fkernB,fkernA = signal.butter(4,np.array(frange)/nyquist,btype='bandpass')
b, a = signal.iirfilter(1, 10/nyquist, btype='lowpass')
outputFileWrite(b, "b")
outputFileWrite(a, "a")
b1, a1 = signal.iirfilter(1, 15/nyquist, btype='lowpass')
outputFileWrite(b1, "b1")
outputFileWrite(a1, "a1")
b2, a2 = signal.iirfilter(1, 20/nyquist, btype='lowpass')
outputFileWrite(b2, "b2")
outputFileWrite(a2, "a2")

# generate an impulse signal
impres = np.zeros(2001)
impres[1001] = 1

outputFileWrite(impres, "impulse")

fimp = signal.lfilter(b, a, impres, axis=-1)
fimp1 = signal.lfilter(b, a, fimp, axis=-1)
fimp2 = signal.lfilter(b1, a1, fimp1, axis=-1)
fimp3 = signal.lfilter(b1, a1, fimp2, axis=-1)
fimp4 = signal.lfilter(b2, a2, fimp3, axis=-1)
fimp5 = signal.lfilter(b2, a2, fimp4, axis=-1)


# power spectrum
fimpX = np.abs(fftpack.fft(fimp5))**2
hz = np.linspace(0, nyquist, int(np.floor(len(impres)/2)+1))

# plot
plt.plot(impres, 'k', label="impulse")
plt.plot(fimp, 'r', label="bq 1")
plt.plot(fimp1, 'b', label="bq 2")
plt.plot(fimp2, 'g', label="bq 3")
plt.plot(fimp3, 'm', label="bq 4")
plt.plot(fimp4, 'y', label="bq 5")
plt.plot(fimp5, 'c', label="bq 6")
plt.xlim([1, len(impres)])
plt.ylim([-0.06, 0.06])
plt.legend()
plt.show()

