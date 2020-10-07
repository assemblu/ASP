# Author: Emirhan Gocturk
# Description: This software is written to verify the understand of convolution
#               It is adives to solve the equation on paper first before verifying

import matplotlib.pyplot as plt
import numpy as np

# x is the discrete time input signal
# has the values from 5~20 incremented by 1
x = np.arange(4, 8, 1)
print("x = ", x)

# y is the impulse response discrete time signal
# will be used in convolution
# has the values from 1~5 incremented by 1
h = np.arange(1, 3, 1)
print("h = ", h)

# output signal, all zeros
y = np.zeros(len(x) + len(h) - 1)

for i in range(len(x)):
    print(i)
    for j in range(len(h)):
        y[i+j] = y[i+j] + (x[i]*h[j])

print("y = ", y)