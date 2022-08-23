# Author: Emirhan Gocturk
# Description: Sawtooth wave lookup table data dumper

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

import sounddevice as sd

t = np.arange(0, np.pi*2, 0.001534)
y = signal.sawtooth(t)*65536/2

t = np.linspace(0, 2 * np.pi, 4096)
y = 2048 * signal.sawtooth(t) + 2048

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