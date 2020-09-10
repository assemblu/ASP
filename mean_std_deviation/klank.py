
# Libraries used
import numpy as np
import matplotlib.pyplot as plt

# To read audio file
from scipy.io.wavfile import read

def get_flute_sound():
    # fs is sampling rate of 44100
    # x is the array of samples (94803)
    (fs, x) = read('stage_one\\flute-a4.wav')

    # Getting time per sample
    t = np.arange(x.size)/float(fs)

    return t, x, fs
