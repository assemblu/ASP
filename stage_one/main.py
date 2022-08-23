# Author: Emirhan Gocturk
# Date  : Aug 26, 2020

# To pick 1000 samples as a demo
select_samples = False

import numpy as np
import matplotlib.pyplot as plt

# To read audio file
from scipy.io.wavfile import read

# fs is sampling rate of 44100
# x is the array of samples (94803)
(fs, x) = read('stage_one\\flute-a4.wav')

# Getting time per sample
t = np.arange(x.size)/float(fs)

if select_samples:
    t = x[44100:45100]

# Plot window
if select_samples:
    plt.plot(t)
else:
    plt.plot(t, x)

plt.title('Flute-A4.wav Audio File')
plt.legend('Signal')
plt.grid()

# Write new sound to file
from scipy.io.wavfile import write

if select_samples:
    write('stage_one\\flute_output.wav', fs, t)
    
# Show window
plt.show()



