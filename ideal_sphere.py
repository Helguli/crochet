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
    if num == 0:
        continue
    if i == 1:
        print("Row 1: sc", num, "into magic ring")
        continue
    prev = y2[i - 1]
    if prev < num:
        # increase
        d = num - prev
        avail = prev - d
        even = i % 2 + 1
        if d == 1:
            print("Row", str(i) + ': sc', int(avail / 3) * even, ', inc, sc', avail - int(avail / 3) * even, end='')
        else:
            k = int(avail / d)
            r = avail % d
            print('Row', str(i) + ': repeat', d, 'times [sc', k, ', inc]', end='')
            if r > 0:
                print(', sc', r, end='')
        print(' (', d * 2 + avail, ')', sep= '')
    elif prev > num:
        # decrease
        d = prev - num
        avail = prev - d * 2
        even = i % 2 + 1
        if d == 1:
            print("Row", str(i) + ': sc', int(avail / 3) * even, ', dec, sc', avail - int(avail / 3) * even, end='')
        else:
            k = int(avail / d)
            r = avail % d
            print('Row', str(i) + ': repeat', d, 'times [sc', k, ', dec]', end='')
            if r > 0:
                print(', sc', r, end='')
        print(' (', d + avail, ')', sep= '')
    else:
        print("Row ", i, ': sc around (', num, ')', sep='')


print(y2)

fig = plt.figure(num="Sphere", figsize=(10,6))
plt.plot(x, y)
plt.scatter(x2, y2)
plt.margins(0)
plt.show()
