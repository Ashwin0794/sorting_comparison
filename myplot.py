#!/usr/bin/python3

from numpy import random
import time
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([200, 400, 800, 1600, 3200, 6400])
y1points = np.array([0.0400, 0.0780, 0.1600, 2.6089, 11.0897, 19.7864])
y2points = np.array([0, 0, 0, 0, 0, 0])

figure, axis = plt.subplots(2,1)
axis[0].plot(xpoints, y1points)
axis[0].set_title("runtime")

axis[1].plot(xpoints, y2points)
axis[1].set_title("mem")

plt.savefig('trial_graph2.png')
#plt.plot(xpoints, ypoints)
#plt.xlabel('dataset sizes')
#plt.ylabel('runtime')
#plt.title('Bubble Sort (size vs runtime)')
#plt.savefig('trial_graph1.png')
#plt.show()
