import math

import numpy as np
np.set_printoptions(precision=8)

def F(x, Y):
    return np.asarray([math.sin(Y[1]),
                       math.cos(Y[0])])

def rk(f, h, a, b, y_ic):
    x = a
    y = y_ic

    while (x <= b):
        print("x=%.8f" % x, " y=", y)
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h / 2 * k1)
        k3 = f(x + h / 2, y + h / 2 * k2)
        k4 = f(x + h, y + h * k3)

        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h
    return y

print("rk result: ", rk(F, 0.1, 1, 3, [0.5 , -0.5]))
