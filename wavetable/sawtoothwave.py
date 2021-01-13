# Author: Emirhan Gocturk
# Description: Sawtooth wave lookup table data dumper

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

import sounddevice as sd

t = np.arange(0, np.pi*2, 0.00156)
y = signal.sawtooth(t)
plt.plot(t, y)  
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("Sawtooth Wave Sample")
plt.show()

print("DATA DUMP= ", y)
np.savetxt("wavetable\\datadumps\\sawtooth.txt", y, delimiter=',')

fs = 44100
sd.play(y, fs)