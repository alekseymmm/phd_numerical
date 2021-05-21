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