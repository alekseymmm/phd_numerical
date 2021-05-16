import math

import numpy as np


def F(x, Y):
    return np.asarray([x * math.sin(Y[1]),
                       x+math.cos(x*Y[0])])

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

# print("euler result: ", eu(F, 0.1, 0, 3, [0 , 0]))
print("euler result: ", eu(F, 0.1, 0, 2, [0 , 0]))