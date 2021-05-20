import numpy as np
import matplotlib.pyplot as plt

def hdiff(x, y, yprime):
    m = x.size # here m is the number of data points. Note n=m-1
    # and 2n+1=2m-1
    l = 2*m
    z = np.zeros(l)
    a = np.zeros(l)
    for i in range(m):
        z[2*i] = x[i]
        z[2*i+1] = x[i]
    for i in range(m):
        a[2 * i] = y[i]
        a[2 * i + 1] = y[i]
    for i in np.flip(np.arange(1, m)):  # computes the first divided
        # differences using derivatives
        a[2 * i + 1] = yprime[i]
        a[2 * i] = (a[2 * i] - a[2 * i - 1]) / (z[2 * i] - z[2 * i - 1])
    a[1] = yprime[0]
    for j in range(2, l):  # computes the rest of the divided differences
        for i in np.flip(np.arange(j, l)):
            a[i] = (a[i] - a[i - 1]) / (z[i] - z[i - j])
    return a


def hermite(x, y, yprime, w):
    m = x.size # here m is the number of data points. not the
    # degree of the polynomial
    a = hdiff(x, y, yprime)
    z = np.zeros(2*m)
    for i in range(m):
        z[2*i] = x[i]
        z[2*i+1] = x[i]
    sum = a[0]
    pr = 1.0
    for j in range(2*m-1):
        pr *= w-z[j]
        sum += a[j+1]*pr
    return sum

xaxis = np.linspace(-np.pi/2, 3*np.pi/2, 120)
x = np.array([-1.5, 1.6, 4.7])
y = np.array([0.071,-0.029,-0.012])
yprime = np.array([1, -1, 1])
funct = np.cos(xaxis)

interp = hermite(x, y, yprime, xaxis)
plt.plot(xaxis, interp, label='Hermite interpolation')
plt.plot(xaxis, funct, label="cos(x)")
plt.plot(x, y, 'o', label='data')
plt.legend(loc='upper right');
plt.show()