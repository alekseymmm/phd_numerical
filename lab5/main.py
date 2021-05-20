
import numpy as np
import matplotlib.pyplot as plt
#http://itnovella.com/post/2020/1/13/lagranz-interpolation-python-61/

x = np.array([0, 10, -1, 7, 4, 3, 8, 9, 1, -2], dtype=float)
y = np.array([-1, 77, -20, 29, 33, 9, 39, 73, -3, -21], dtype=float)

def lagr(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1;
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1;
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z

xnew = np.linspace(np.min(x), np.max(x), 100)
ynew = [lagr(x, y, i) for i in xnew]
plt.plot(x, y, 'o', xnew, ynew)
plt.grid(True)
plt.show()