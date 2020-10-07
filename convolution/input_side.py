import matplotlib.pyplot as plt
import numpy as np

debug = True
# lower case means discrete signal
# upper case means continuous signal

# 81 samples of input signal
if debug:
    print("Generating signal x")
x = np.arange(0, 0.81, 0.1)
if debug:
    print("Generated discrete 81 sample input signal 'x'")

# 31 samples of impulse repsonse
if debug:
    print("Generating signal h")
h = np.arange(1, 1.31, 0.1)
if debug:
    print("Generated discrete 31 sample impulse response signal 'h'")

# output signal is 81 + 31 - 1
if debug:
    print("Generating signal y")
y = np.empty(111)
if debug:
    print("Generated discrete 111 sample output signal 'y'")



# zero the output signal
if debug:
    print("[y]: zero the signal")
y = np.zeros(111)
if debug:
    print("[y]: zero the signal complete")
    print("[y]: ", y)

#convolve
# todo: after lunch break or some other time!
for i in x:
    for j in h:
        y[i+j] = y[i+j] + (x[i]*h[j])
    
print(y)