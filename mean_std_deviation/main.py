'''
    Author: Emirhan Gocturk
    Description: Mean and standard deviation
                of a signal
'''

# Libraries used
import numpy as np
import matplotlib.pyplot as plt
import importlib
import math

# To read audio file
from scipy.io.wavfile import read

def get_flute_sound():
    # fs is sampling rate of 44100
    # x is the array of samples (94803)
    (fs, x) = read('stage_one\\flute-a4.wav')

    # Getting time per sample
    t = np.arange(x.size)/float(fs)

    return t, x, fs


#------------------------------------#


t, x, fs = get_flute_sound()

# Number of samples
N = x.size - 1
sum = 0
sumsqr = 0

# Mean
mean = 0
# Standard deviation
stdev = 0

for i in x:
    N = N + 1
    sum = sum + i
    sumsqr = sumsqr + (i ** 2)

mean = sum/N
stdev = math.sqrt((sumsqr - ((sum ** 2)/N))/(N-1))

print("Mean: ", mean)
print("Standard Deviation: ", stdev)

plt.plot(t, x)

plt.title('Flute sound')
plt.legend('Signal')
plt.grid()

from scipy.io.wavfile import write
write('flute_output.wav', fs, t)

# Show window
plt.show()

