#! /bin/python

import sys
import numpy as np
from matplotlib import pyplot as plt

if (len(sys.argv) < 2):
    print("Please specify a number as command line argument. This number will be the row number of the sphere.")
    exit()

n = int(sys.argv[1])
angle = np.pi / (n + 1)

x = np.arange(0, np.pi + 0.01, 0.02)
y = np.sin(x) * n * 2

x2 = np.arange(0, np.pi + 0.01, angle)
y2 = np.around(np.sin(x2) * n * 2, 0)

print(y2)

fig = plt.figure(num="Sphere", figsize=(10,6))
plt.plot(x, y)
plt.scatter(x2, y2)
plt.margins(0)
plt.show()
