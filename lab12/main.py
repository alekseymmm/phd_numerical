import math, random
import numpy as np

# fp = lambda x: (math.exp(x))
# fq = lambda x: (x / 2)
# f = lambda x: x**2
#
# a = 0.1
# b = 1.1
#
# c1 = 1
# c2 = -1.2
# c = 0
# d1 = 2
# d2 = -2.5
# d = -4

fp = lambda x: 1 / (math.log(x) - 1)
fq = lambda x: math.exp(-x)
f = lambda x: math.atan(x)

a = 3
b = 5

c1 = 1
c2 = -1
c = 0
d1 = 0.94
d2 = 0.53
d = 0.2

def prog(a, b, c1, c2, c, d1, d2, d, fp, fq, f, n):
    X, h = np.linspace(a, b, n, retstep=True)
    Y = np.zeros(len(X)+1)
    p = np.zeros(len(X) + 1)
    q = np.zeros(len(X) + 1)

    r1 = h**2
    r2 = h / 2
    p[0] = -c2 / (c1 * h - c2)
    q[0] = -c * h * p[0] / c2

    x = a
    for i in range(1, n):
        x = x + h
        t = 1 - fp(x) * r2
        p[i] = (t - 2) / (fq(x) * r1 + t * p[i - 1] - 2)
        q[i] = (f(x) * r1 - t * q[i - 1]) * p[i] / (t - 2)

    p[n] = 0
    q[n] = (d * h + d2 * q[n - 1]) / (d1*h + d2 - d2 * p[n - 1])

    Y[n] = q[n]
    for i in range(n - 1, 0, -1):
        Y[i] = q[i] + Y[i + 1] * p[i]

    # u[0] = c * h / (c1 * h - c2)
    # v[0] = c2 / (c1 * h  - c2)
    #
    # x = a
    # for i in range(1, n):
    #     x = x + h
    #     alpha_i = 1 - p(x) * h / 2
    #     beta_i = h**2 * q(x) - 2
    #     gama_i = 1 + p(x) * h / 2
    #     phi_i = h**2 * f(x)
    #
    #     v[i] = -gama_i / (beta_i - alpha_i * v[i-1])
    #     u[i] = (phi_i - alpha_i * u[i-1]) / (beta_i + alpha_i * v[i])
    #
    # alpha_n = -d2
    # beta_n = h * d1 + d2
    # phi_n = h * b
    #
    # v[n] = 0
    # u[n] = (phi_n - alpha_n * u[n - 1]) / beta_n
    # Y[n] = u[n]
    #
    # for i in range(n - 1, 0, -1):
    #     Y[i] = u[i] + Y[i + 1] * v[i]

    return X, Y

x, y = prog(a, b, c1, c2, c, d1, d2, d ,fp, fq, f, 21)

print("x = ", x)
print("y = ", y[1:])