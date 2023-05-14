import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
n = 100
x = np.random.rand(n)
y = np.random.rand(n)
a = np.linspace(1,1,101)
b = np.linspace(1,1,101)
aa, bb = np.meshgrid(x, y)
zz = np.sqrt(aa**2 + bb**2)
plt.contour(aa, bb, zz)
plt.axis('scaled')
plt.colorbar()
plt.title("contourf")
plt.xlim(0,1)
plt.ylim(0,1)
area = 15*(x+y)
colors = [(0,1,0) if cond else (1,0,0) for cond in (x**2+y**2) < 1]
plt.scatter(x, y, s=area, c=colors)
plt.show()
