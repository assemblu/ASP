# Author: Emirhan Gocturk
# Description: Cascade IIR

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fftpack
import scipy
import copy

# filter parameters
srate   = 1024 # hz
nyquist = srate/2
frange  = [20,45]

b, a = signal.iirfilter(4, [2*np.pi*50, 2*np.pi*200], rs=60, btype='band', analog=True, ftype='cheby2')
