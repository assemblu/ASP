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


