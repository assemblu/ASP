import numpy as np
import matplotlib.pyplot as plt

from scipy.io.wavfile import read

import sounddevice as sd

(fs, x) = read('C:\\dev\\ASP\\wavetable\\samples\\guitar-passage.wav')

y = x[0:15000]
t = np.arange(0, 1, 1/fs)[:len(y)]

plt.plot(t, y)
plt.title("Guitar Passage Sample")
plt.grid()
plt.show()

sd.play(y, fs)