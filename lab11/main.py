import math

import numpy as np
np.set_printoptions(precision=8)

def F(x, Y):
    return np.asarray([2 * Y[0] + Y[1] * Y[2],
                       Y[0]*Y[1]*Y[2] + Y[0]**2,
                       x * Y[0] + Y[1] - Y[2]**2 ])
    # return np.asarray([-Y[1] + math.sin(x * Y[2]),
    #                    Y[0]**2,
    #                    -Y[2] - Y[0]])

def rk(f, h, a, b, y_ic):
    x = a
    y = y_ic

    while (x < b):
        print("x=%.8f" % x, " y=", y)
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h / 2 * k1)
        k3 = f(x + h / 2, y + h / 2 * k2)
        k4 = f(x + h, y + h * k3)

        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h

    print("x=%.8f" % x, " y=", y)
    return y

def admsb(f, h, a, b, y_ic):
    x_3 = a
    y_3 = y_ic
    print("x=%.8f" % x_3, " y=", y_3)

    y_2 = rk(f, h, a, a+h, y_3)
    x_2 = x_3 + h
    a = a + h
    print("x=%.8f" % x_2, " y=", y_2)

    y_1 = rk(f, h, a, a+h, y_2)
    x_1 = x_2 + h
    a = a + h
    print("x=%.8f" % x_1, " y=", y_1)

    y = rk(f, h, a, a+h, y_1)
    x = x_1 + h
    a = a + h
    # print("x=%.8f" % x, " y=", y)

    while (x < b):
        print("x=%.8f" % x, " y=", y)

        y = y + (h / 24) * (55 * f(x, y) - 59 * f(x_1, y_1) +
                            37 * f(x_2, y_2) - 9 * f(x_3, y_3))
        x_3 = x_3 + h
        x_2 = x_2 + h
        x_1 = x_1 + h
        x = x + h

        y_3 = y_2
        y_2 = y_1
        y_1 = y

    print("x=%.8f" % x, " y=", y)


print("adams result: ", rk(F, 0.1, 0, 1, [0.2, 0, 0]))
