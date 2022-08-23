# Author: Emirhan Gocturk
# Description: DFT Analysis
#               (forward DFT)

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# complicated debuggers? 
# NO.
# let's use print!
debug = True

# generate a sine in time domain
t = np.arange(0, 100, 0.1)
y = np.sin(t)

# hold the real part of the frequency domain
# fill with zeros
ReY = np.zeros(int(y.size/2))
# hold the imaginary part of the frequency domain
# fill with zeros
ImY = np.zeros(int(y.size/2))

# constant value for the PI
PI = 3.14159265
# N is the number of points in y
N = y.size

# cool debugging technique
if debug:
    print("Number of points in time domain signal (y): ",N)

# show time domain signal
plt.plot(t, y)
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [A]")
plt.title("Sine Wave Sample")
plt.show()

# correlate y with the cosine and sine waves
# Equations below
# 
# i is 0 to N-1
# ReY[k] = x[i]cos(2*PI*k*i/N)
# ImY[k] = -(x[i]sin(2*PI*k*i/N))

for k in range(int(y.size/2)):
    for i in range(int(y.size-1)):
        ReY[k] = ReY[k] + y[i] * np.cos(2*PI*k*i/N)
        ImY[k] = ImY[k] - (y[i] * np.sin(2*PI*k*i/N))
    
plt.plot(ReY)
plt.grid()
plt.xlabel("Frequency [f]")
plt.ylabel("Amplitude [A]")
plt.title("Cosin wave")
plt.show()

plt.plot(ImY)
plt.grid()
plt.xlabel("Frequency [f]")
plt.ylabel("Amplitude [A]")
plt.title("Sine wave")
plt.show()
