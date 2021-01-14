# Author: Emirhan Gocturk
# Description: Sine wave lookup table data dumper

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import math

import sounddevice as sd

t = np.arange(0, np.pi*2, 0.001534)
y = 4000/2+np.sin(t)*4000/2
index = 0
while index < len(y):
    y[index] = int(y[index])
    index += 1
plt.plot(t, y)
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("Sine Wave Sample")
plt.show()

print("DATA DUMP= ", y)

f = open("sinewave.txt", "w+")
count = 0
while count < len(y):
    f.write(str(int(y[count])))
    f.write(", ")
    count += 1

print(str(len(y)))