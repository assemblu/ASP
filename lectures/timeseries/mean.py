# Author: Emirhan Gocturk
# Description: Mean smooth algorithm

import numpy as np

sampling_rate = 1000 #Hz
# 0 to 3 chop into 1/1000
time = np.arange(0, 3, 1/sampling_rate)
# sample count
n = len(time) 
# number of poles, for interpolation
p = 15

# artifically added noise
noise_amplitude = 5

