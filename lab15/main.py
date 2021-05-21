import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plot
from scipy import interpolate

def derivative(f,a,method='central',h=0.01):
    if method == 'central':
        return (f(a + h) - f(a - h))/(2*h)
    elif method == 'right':
        return (f(a + h) - f(a))/h
    elif method == 'left':
        return (f(a) - f(a - h))/h
    else:
        raise ValueError("Method must be 'central', 'right' or 'left'.")

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

def ddf(f, a, h):
    return (f(a+h) - 2 * f(a) + f (a-h)) / h / h

def f(x):
    return np.sin(x)

x = np.linspace(0, math.pi , 20)
y = f (x)
y1 = np.cos(x)
plt.figure()
l1 = plt.plot(x, y, label="sin")
l2 = plt.plot(x, y1, label="cos")
f2 = interpolate.splrep(x, y)
ynew_der = interpolate.splev(x, f2, der=1) # Added to compute first derivative
plot.plot(x, ynew_der, '--r', label="deriv_spline") # Derivative Added
plt.legend()
plt.grid()
plt.show()

def run_1st_der(h):
    x = np.linspace(0, math.pi, 1000)
    y = f(x)
    f2 = interpolate.splrep(x, y)
    ynew_der = interpolate.splev(x, f2, der=1)  # Added to compute first derivative
    #ynew_der2 = interpolate.splev(x, f2, der=2)  # Added to compute first derivative

    left = derivative(f, 0.5, "left", h)
    right = derivative(f, 0.5, "right", h)
    central = derivative(f, 0.5, "central", h)
    for i in range(len(x)):
        if x[i] >= 0.5:
            print("h: %g, left: %g, right: %g central: %g, spline: %g" %
                  (h, left, right,  central, ynew_der[i]))
            break

def run_2nd_der(h):
    x = np.linspace(0, math.pi, 1000)
    y = f(x)
    f2 = interpolate.splrep(x, y)
    #ynew_der = interpolate.splev(x, f2, der=1)  # Added to compute first derivative
    ynew_der2 = interpolate.splev(x, f2, der=2)  # Added to compute first derivative

    ddf_val = ddf(f, 0.5, h)
    for i in range(len(x)):
        if x[i] >= 0.5:
            print("h: %g raznost: %g, spline: %g" %
                  (h, ddf_val, ynew_der2[i]))
            break

print("first derivative")
print("exact :", math.cos(0.5))
for i in range(-1, -9, -1):
    run_1st_der(10 **(i))

print("second derivative")
print("exact :", -math.sin(0.5))
for i in range(-1, -9, -1):
    run_2nd_der(10 **(i))