import numpy as np
import matplotlib.pyplot as plt
# spizheno tut http://digital.auraria.edu/content/IR/00/00/01/95/00001/NumAnPython_Aug_09_2020.pdf
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

xaxis = np.linspace(0, 3, 120)
x = np.array([0, 0.4, 1, 2, 2.6, 3])
y = np.array([1, 0.735, 2.17, 8.30, 14.2, 19.1])
yprime = np.array([11, -5.04, -5.67, 11.5, 19.9, 21.6])
funct = np.exp(xaxis)+np.sin(10 * xaxis)
interp = hermite(x, y, yprime, xaxis)
plt.plot(xaxis, interp, label='Hermite interpolation')
plt.plot(xaxis, funct, label="e^x+sin(10x)")
plt.plot(x, y, 'o', label='data')
plt.legend(loc='upper right');
plt.show()