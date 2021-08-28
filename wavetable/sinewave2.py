# Author: Emirhan Gocturk
# Description: Sine wave lookup table data dumper

import os
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import math

sample_rate = 4096

start_time = 0
end_time = 1

time = np.arange(start_time, end_time, 1/sample_rate)

frequency = 1
amplitude = 4000
theta = 0

x = np.linspace(0, 2 * np.pi * frequency, 4096)
sinewave = 2048 * np.sin(x) + 2048
#sinewave = map(lambda x: int(np.round((x+1.0)*2048)), sinewave)
#sinewave = amplitude * np.sin(2 * np.pi * frequency * time + theta)

print("Sample count: ", len(sinewave))
for i in range(0, len(sinewave)):
    sinewave[i] = int(sinewave[i])

plt.plot(sinewave)
plt.show()

# delete output file
if os.path.exists("sinewave2.txt"):
    print("The output file exists. Deleting...")
    os.remove("sinewave2.txt")
else:
    print("The output file doesn't exist. Nothing to delete.")

# write to file
f = open("sinewave2.txt", "w+")
count = 0
while count < len(sinewave):
    f.write(str(int(sinewave[count])))
    f.write(", ")
    count += 1

print("Write complete.")
print("Written element count: ", str(len(sinewave)))
