# Author: Emirhan Gocturk
# Description: Reverse sawtooth wave lookup table data dumper
# it is a bit weird..

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

import sounddevice as sd

t = np.arange(0, np.pi*2, 0.001534)
y = 4000/2+signal.sawtooth(t, 0.1)*4000/2

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

f = open("reversawtooth.txt", "w+")
count = 0
while count < len(y):
    f.write(str(int(y[count])))
    f.write(", ")
    count += 1

print(str(len(y)))