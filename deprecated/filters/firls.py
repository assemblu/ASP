# Author: Emirhan Gocturk
# Description: FIR least squares

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.signal
from scipy import *
import copy

srate = 1024 #Hz
nyquist = srate/2
frange = [20, 45]
transw = 0.1
order = int(5*srate/frange[0])

shape = [0, 0, 1, 1, 0, 0]
frex = [
    0,
    frange[0]-frange[0]*transw,
    frange,
    frange[1]+frange[1]*transw,
    nyquist
]

for i in range(len(frex)):
    frex[i] = frex[i] / nyquist

print(frex)