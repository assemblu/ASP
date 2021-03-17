# Author: Emirhan Gocturk
# Description: Running mean smooth filter algorithm 

import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

# Pure signal
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# Noise at time length
noise = np.random.normal(0, 1, len(x))

y = y + noise

# Window
plt.plot(x, y)
plt.grid()
plt.xlabel("Time")
plt.ylabel("Amplitude")
# plt.show()


# Smoothing section
# Filtered output zeroed at input length
filtered = np.zeros(len(y))

# running mean filter algorithm
k = 20 # window = k*2+1
for i=k+1