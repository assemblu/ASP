# Author: Emirhan Gocturk
# Description: Two channel mixing

"""
*** Application notes ***
A real time platform requires buffered
short term application where as the
buffer is filled, the application is then
applied to that section of the 

*** Pseudo code ****
load channel X samples
load channel Y samples

mixed_signal = (X + Y) / num_of_channels

playback mixed_signal
plot mixed_signal

exit
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

# read channels both at 44100 Hz
fs_channel_1, data_channel_1 = wavfile.read('C:\dev\ASP\channel_mixing\samples\synth.wav')
fs_channel_2, data_channel_2 = wavfile.read('C:\dev\ASP\channel_mixing\samples\piano.wav')

# measure length
length_channel_1 = len(data_channel_1)
length_channel_2 = len(data_channel_2)

sample_length = 0
# match sample length
if length_channel_1 > length_channel_2:
    # ch1 is longer than ch2
    sample_length = length_channel_2
else:
    sample_length = length_channel_1


# mix two channels


# plot result
plt.plot(data_channel_2)
plt.show()
