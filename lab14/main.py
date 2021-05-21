from numpy import linspace
import matplotlib.pyplot as plt
import numpy as np

#rename something here

def spline(x, y):
    n = len(x) - 1

    h = [x[i+1] - x[i] for i in range(n)]

    alpha = [0.0 for i in range(0, n)]
    for i in range(1, n):
        alpha[i] = (3 / h[i]) * (y[i+1] - y[i]) - (3 / h[i-1]) * (y[i] - y[i-1])

    l = [1] * (n+1)
    mu = [0] * (n + 1)
    z = [0] * (n + 1)
    for i in range(1, n):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]

    b = [0] * (n + 1)
    c = [0] * (n + 1)
    d = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        c[i] = z[i] - mu[i] * c[i+1]
        b[i] = (y[i+1] - y[i]) / h[i] - h[i] * (c[i+1] + 2 * c[i]) / 3
        d[i] = (c[i+1] - c[i]) / (3 * h[i])
    return y, b, c, d

def eval_spline(a, b, c, d, x, xx):
    yy = [0.0 for i in range(0, len(xx))]
    for i in range(0, len(x)-1):
        for j in range(0, len(xx)):
            if x[i] <= xx[j] <= x[i+1]:
                yy[j] = a[i] + b[i] * (xx[j] - x[i]) + c[i] * (xx[j] - x[i])** 2 + d[i] * (xx[j] - x[i]) ** 3
    return yy

def f(x):
    return np.cos(x + np.cos(x)**3)

n = 25
m = 10
point_a = -1
point_b = 4
x = linspace(point_a, point_b, m)
y = [f(x[i]) for i in range(0, m)]
xx = linspace(point_a, point_b, n)
a, b, c, d = spline(x, y)
yy = eval_spline(a, b, c, d, x, xx)
plt.figure()
line1 = plt.plot(xx, yy, 'bo-', label='Spline')
line2 = plt.plot(x, y, 'r+-', label='Initial values')
f_x = f(xx)
plt.legend()
plt.show()
print('x', xx)
print('spline,', yy)
print('function', f_x)