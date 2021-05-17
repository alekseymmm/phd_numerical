import math

import numpy as np
np.set_printoptions(precision=8)

def F(x, Y):
    return np.asarray([math.sin(x * Y[1]),
                       x+math.cos(x*Y[0])])



def eu(f, h, a, b, y_ic):
    x = a
    y = y_ic

    while (x <= b):
        print("x=%.8f" % x, " y=", y)
        y = y + h * f(x, y)
        x = x + h
    return y

print("euler result: ", eu(F, 0.1, 0, 2, [0 , 0]))
