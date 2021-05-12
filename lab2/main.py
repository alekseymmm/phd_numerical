import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, List
from math import *
import math

func = lambda x: 2 * x**2 - x**4 - 1 - math.log(x)
g = lambda x: math.exp(2 * x**2 - x**4 - 1)

def iteration(given_function, x0, min_error=0.005, max_iteration=100) -> Tuple[float, List]:
    i = 0
    error = 1
    xp = []
    x = None
    while error > min_error and i < max_iteration:
        x = given_function(x0)
        error = abs(x0 - x)
        x0 = x
        xp.append(x0)
        print(x0)
        i += 1
    print(xp)
    return x, xp


def plot(xf, xp, x_start, given_function):
    function_v = np.vectorize(given_function)

    x = np.linspace(0, 2, 100)
    y = function_v(x)
    plt.plot(x, y)
    plt.plot(xp, function_v(xp), 'bo')
    plt.plot(x_start, given_function(x_start), 'ro')
    plt.plot(xf, given_function(xf), 'go')
    plt.plot(x, x, 'k')
    plt.show()


def main():
    x_start = 0.5
    xf, xp = iteration(g, x_start)

    plot(xf, xp, x_start, g)


if __name__ == '__main__':
    main()