import math

import numpy as np
import matplotlib.pyplot as plt

def F(x, Y):
    # return np.asarray([x + Y[0]**2,
    #                    (Y[0] - Y[1])**2])
    return np.asarray([Y[1],
                       math.exp( -x * Y[0])])
def euler(F, u0, tau, T):
    N_t = int(round(T/tau))
    F_ = lambda t, u: np.asarray(F(t, u))
    t = np.linspace(0, N_t*tau, N_t+1)
    u = np.zeros((N_t+1, len(u0)))
    u[0] = np.array(u0)
    for n in range(N_t):
        u[n+1] = u[n] + tau*F_(t[n], u[n])

    return u, t


def eu(f, h, a, b, y_ic):
    x = a
    y = y_ic

    while (x <= b):
        print(x, y)
        y = y + h * f(x, y)
        x = x + h
    return y

print("euler result: ", eu(F, 0.1, 0, 3, [0 , 0]))
