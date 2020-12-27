# Author: Emirhan Gocturk
# Description: Experimenting with DFT
#              - ANALYSIS
#              TODO: inverse DFT

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# debugging the script
printing = false

# signal length (samples)
N = 128
# cosine
ReX = np.zeros(int(N/2))
# sine
ImX = np.zeros(int(N/2))

if printing:
    print(ImX)

# the formula for analysis
for k in N/2:
    for i in (N-1):
        # ReX[k] = ReX[k] + x[i]cos(2pi*k*i/N)
        # ImX[k] = -(ImX[k] + x[i]sin(2pi*k*i/N))


