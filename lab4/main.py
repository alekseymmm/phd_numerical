import math, random
from numpy import arange

func = lambda x: math.cos(x**2)

#https://www.wikiwand.com/ru/%D0%A7%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5_%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5#/%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B_%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8

def method_of_rectangles(func, min_lim, max_lim, delta):
    def integrate(func, min_lim, max_lim, n):
        integral = 0.0
        step = (max_lim - min_lim) / n
        for x in arange(min_lim, max_lim-step, step):
            integral += step * func(x + step / 2)
        return integral

    d, n = 1, 1
    while abs(d) > delta:
        val1 = integrate(func, min_lim, max_lim, n)
        val2 = integrate(func, min_lim, max_lim, n * 2)
        d = (val2 - val1) / 3
        n *= 2
        print("n=%d, integral=%g" % (n, val2))

    return val2

def trapezium_method(func, min_lim, max_lim, delta):
    def integrate(func, min_lim, max_lim, n):
        integral = 0.0
        step = (max_lim - min_lim) / n
        for x in arange(min_lim, max_lim-step, step):
            integral += step*(func(x) + func(x + step)) / 2
        return integral

    d, n = 1, 1
    while abs(d) > delta:
        val1 = integrate(func, min_lim, max_lim, n)
        val2 = integrate(func, min_lim, max_lim, n * 2)
        d = (val2 - val1) / 3
        n *= 2
        print("n=%d, integral=%g" % (n, val2))

    return val2

def simpson_method(func, min_lim, max_lim, delta):
    def integrate(func, min_lim, max_lim, n):
        integral = 0.0
        step = (max_lim - min_lim) / n
        for x in arange(min_lim + step / 2, max_lim - step / 2, step):
            integral += step / 6 * (func(x - step / 2) + 4 * func(x) + func(x + step / 2))

        return integral

    d, n = 1, 1
    while abs(d) > delta:
        val1 = integrate(func, min_lim, max_lim, n)
        val2 = integrate(func, min_lim, max_lim, n * 2)
        d = (val2 - val1) / 15
        n *= 2
        print("n=%d, integral=%g" % (n, val2))

    return val2

print("rectangles method")
print("rectangles method result : %g\n" % method_of_rectangles(func, 0.0, 1.0, 0.0001))

print("trapezium method")
print("trapezium method result: %g\n" % trapezium_method(func, 0.0, 1.0, 0.0001))

print("simpson method")
print("simpson method result: %g\n" % simpson_method(func, 0.0, 1.0, 0.0001))
