import matplotlib.pyplot as plt
import numpy as np

debug = False
# lower case means discrete signal
# upper case means continuous signal

# 81 samples of input signal
if debug:
    print("Generating signal x")
x = np.arange(0, 0+8.1, 0.1)
print("x length: ", len(x))
if debug:
    print("Generated discrete 81 sample input signal 'x'")

# 31 samples of impulse repsonse
if debug:
    print("Generating signal h")
h = np.arange(1, 1+3.1, 0.1)
print("y length: ", len(h))
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

# convolve
# todo: after lunch break or some other time!


#foreach x
for i in range(len(x)-1):
    #foreach h
    for j in range(len(h)-1):
        y[i+j] = y[i+j] + (x[i]*h[j])

#title
plt.title("Convolution: Input Side Algorithm")
# x axis text
plt.xlabel("Sample Number")
# y axis text
plt.ylabel("Amplitude")

#plotting
plt.plot(x, 'r', label="Input")
plt.plot(h, 'g', label="Impulse")
plt.plot(y, 'b', label="Output")

plt.legend(loc="upper left")
plt.grid()
plt.show()