# Author: Emirhan Gocturk
# Description: Sawtooth wave lookup table data dumper

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

import sounddevice as sd

frequency = 1

t = np.arange(0, np.pi*2*frequency, 0.001534*4*frequency)
y = signal.sawtooth(t)*30000

index = 0
while index < len(y):
    y[index] = int(y[index])
    index += 1

    
plt.plot(t, y)  
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("Sawtooth Wave Sample")
plt.show()

f = open("sawtoothwave.txt", "w+")
count = 0
while count < len(y):
    f.write(str(int(y[count])))
    f.write(", ")
    count += 1


print(str(len(y)))