# Author: Emirhan Gocturk
# Description: Spectral anaylsis

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.signal
from scipy import *
import copy

srate = 1234 #Hz
npnts = srate * 2
time = np.arange(0, npnts)/srate

# frequencies to be included
frex = [12, 18, 30]

# signal dummy
signal = np.zeros(len(time))