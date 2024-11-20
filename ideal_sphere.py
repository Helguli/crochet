#! /bin/python

import numpy as np
from matplotlib import pyplot as plt

n = int(input("How many rows do you want your sphere to have?\n"))
angle = np.pi / (n + 1)

x = np.arange(0, np.pi + 0.01, 0.02)
y = np.sin(x) * n * 2

x2 = np.arange(0, np.pi + 0.01, angle)
y2 = np.around(np.sin(x2) * n * 2, 0).astype(int)

for i, num in enumerate(y2):
    if (i == 0):
        continue
    if (i == 1):
        print("Row 1: sc", num, "into magic ring")
        continue
    prev = y2[i - 1]
    if (prev < num):
        # increase
        d = num - prev
        avail = prev - d
        if (d == 1):
            print("Row", i, ': sc', int(avail / 3), ', inc, sc', avail - int(avail / 3))
        else:
            k = int(avail / d)
            r = avail % d
            print('Row', str(i) + ': repeat', d, 'times [sc', k, ', inc]', '' if r > 0 else '\n', end='')
            if r > 0:
                print('sc', r)


print(y2)

fig = plt.figure(num="Sphere", figsize=(10,6))
plt.plot(x, y)
plt.scatter(x2, y2)
plt.margins(0)
plt.show()
