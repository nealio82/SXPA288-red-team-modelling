import os
import sys
import math

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')

sys.path.append(vendor_dir)

import matplotlib.pyplot as plt

t = 0
x = 2
y = 3
dt = 0.01
tmax = 5
xpts = []
ypts = []
tpts = []

while t < tmax - dt:
    t += dt
    x += (2*x - 3*y + math.sin(t))*dt
    y += (5*x - 7*y)*dt
    xpts.append(x)
    ypts.append(y)
    tpts.append(t)


print xpts
print ypts

plt.plot(tpts, xpts, 'b-', tpts, ypts, 'r-')
plt.axis([0, 5, 0, 3])
plt.show()