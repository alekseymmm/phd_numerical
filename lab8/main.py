import numpy as np
import matplotlib.pyplot as plt

# https://www-users.york.ac.uk/~mijp1/teaching/2nd_year_Num_Methods/lecture_2_handout.pdf
def Aitken(xData,yData,x):
    m=len(xData)
    y=yData.copy()
    for k in range(1,m):
        y[0:m-k]=(xData[k:m]-x)*y[0:m-k]+(x-xData[0:m-k])*y[1:m-k+1]
        y[0:m-k]=y[0:m-k]/(xData[k:m]-xData[0:m-k])
    return y[0]

xaxis = np.linspace(0, 3, 120)
x = np.array([0, 0.2, 0.4, 1, 1.2, 2, 2.2, 2.6, 3])
y = np.array([1, 2.13, 0.735, 2.17, 2.7853, 8.30, 9.016162190143719,  14.2, 19.1])

funct = np.exp(xaxis)+np.sin(10 * xaxis)

interp = np.zeros(len(xaxis))
i = 0
for xi in xaxis:
    interp[i] = Aitken(x, y, xi)
    i = i + 1
plt.plot(xaxis, interp, label='Aitken interpolation')
plt.plot(xaxis, funct, label="e^x+sin(10x)")
plt.plot(x, y, 'o', label='data')
plt.legend(loc='upper right');
plt.show()