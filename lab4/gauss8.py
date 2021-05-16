import math

# https://www.wolframalpha.com/input/?i=integrate+cos%28x%29+%2F+%281%2Bx%5E2%29+from+0+to+1

func = lambda x: math.cos(x) / (1 + x**2)

ag = [0.10122854, 0.22238104,
      0.31370664, 0.36278378,
      0.36268378, 0.31370664,
      0.22238104, 0.10122854]

xg = [-0.96028986, -0.79666648,
      -0.52553242, -0.18343464,
      0.18343464, 0.52553242,
      0.79666648, 0.96028986]

def gaus8(func, a, b):
    a1 = (a + b) * 0.5
    a2 = (b - a) * 0.5

    g = 0
    for i in range(8):
        x = a1 + a2 * xg[i]
        g = g + ag[i] * func(x)

    return g * a2

print("Gauss 8 result: ", gaus8(func, 0, 1))