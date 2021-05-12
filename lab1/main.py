import numpy
import pylab
import math
from typing import Callable

func = lambda x: 2 * x**2 - x**4 - 1 - math.log(x)
d_func = lambda x: - (1 - 2 * x**2)**2 / x
dd_func = lambda x: 1 / (x**2) - 4

a1, b1 = 0.001, 1.5
eps = 0.005

def half_divide_method(a, b, f):
    x = (a + b) / 2
    while math.fabs(f(x)) >= eps:
        x = (a + b) / 2
        a, b = (a, x) if f(a) * f(x) < 0 else (x, b)
    return (a + b) / 2


def secant_method(f: Callable[[float], float], x0: float, eps: float = 1e-7, kmax: int = 1e3) -> float:
    """
    solves f(x) = 0 by secant method with precision eps
    :param f: f
    :param x0: starting point
    :param eps: precision wanted
    :return: root of f(x) = 0
    """
    x, x_prev, i = x0, x0 + 2 * eps, 0

    while abs(x - x_prev) >= eps and i < kmax:
        x, x_prev, i = x - f(x) / (f(x) - f(x_prev)) * (x - x_prev), x, i + 1

    return x

def newtons_method(a, b, f, f1):
    x0 = (a + b) / 2
    x1 = x0 - (f(x0) / f1(x0))
    while True:
        if math.fabs(x1 - x0) < eps:
            return x1
        x0 = x1
        x1 = x0 - (f(x0) / f1(x0))

# http://cyclowiki.org/wiki/%D0%9A%D0%BE%D0%BC%D0%B1%D0%B8%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BC%D0%B5%D1%82%D0%BE%D0%B4
def newton_and_secant(a, b, f, f1, f2):
    while math.fabs(a - b) > 2 * eps:
        if f(a) * f2(a) < 0:
            a = a - f(a)*(a-b) / (f(a) - f(b))
        elif f(a) * f2 (a) > 0:
            a = a - f(a) / f1(a)

        if f(b) * f2(b) < 0:
            b = b - f(b)*(b-a) / (f(b) - f(a))
        elif f(b) * f2 (b) > 0:
            b = b - f(b) / f1(b)

    return (a + b) / 2


X = numpy.arange(0.001, 4.0, 0.01)
pylab.plot([x for x in X], [func(x) for x in X])
pylab.grid(True)
pylab.show()

print ('root of the equation half_divide_method %s' % half_divide_method(a1, b1, func))
print ('root of the equation secant method %s' % secant_method(func, 0.5, eps))
print ('root of the equation newtons_method %s' % newtons_method(a1, b1, func, d_func))
print ('root of the equation combined %s' % newton_and_secant(a1, b1, func, d_func, dd_func))