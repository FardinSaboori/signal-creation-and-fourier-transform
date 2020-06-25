import numpy as np
import numexpr as ne
import matplotlib.pyplot as plt
from numpy.fft import fft
import math
plt.rcParams["xtick.labelsize"] = 14
plt.rcParams["ytick.labelsize"] = 14


def signal(F, A, T, Sr):
    time = np.arange(0, T, T/Sr)
    X = A*np.sin(2*np.pi*F*time)
    return time, X


fig = plt.figure(figsize=(10,5))
ax = fig.add_axes([0,0,1,1])
ax.set_ylim([-5, 5])

# here we can create a complex signal by adding 3 below signals together.
time1, y = signal(3, 4, 5, 50)
# time2, ampli2 = signal(1.5, 4, 5, 1, 1000)
# time3, ampli3 = signal(2, 6, 5, 0, 1000)
# amplitude = ampli1 + ampli2 + ampli3
n = len(y)
print(n)
# Fourier transform
p = fft(y)
mag = np.sqrt(p.real**2 + p.imag**2)
mag = mag * 2 / n

x = np.arange(0, len(mag), 1) * (10/n)
plt.bar(x, mag, color = 'r')
plt.grid()
plt.show()