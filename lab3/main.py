import numpy as np
# http://hplgit.github.io/prog4comp/doc/pub/p4c-sphinx-Python/._pylight007.html
def Newton_system(F, J, x, eps):
    """
    Solve nonlinear system F=0 by Newton's method.
    J is the Jacobian of F. Both F and J must be functions of x.
    At input, x holds the start value. The iteration continues
    until ||F|| < eps.
    """
    F_value = F(x)
    F_norm = np.linalg.norm(F_value, ord=2)  # l2 norm of vector
    iteration_counter = 0
    while abs(F_norm) > eps and iteration_counter < 100:
        delta = np.linalg.solve(J(x), -F_value)
        x = x + delta
        print(x)
        F_value = F(x)
        F_norm = np.linalg.norm(F_value, ord=2)
        iteration_counter += 1

    # Here, either a solution is found, or too many iterations
    if abs(F_norm) > eps:
        iteration_counter = -1
    return x, iteration_counter

def test_Newton_system1():
    from numpy import cos, sin, pi, exp

    def F(x):
        return np.array(
            [sin(x[0]) * (x[0] - 1) - 1.3 + x[1],
             x[0] - sin(x[1] + 1) - 0.8])

    def J(x):
        return np.array(
            [[cos(x[0])*(x[0]-1) + sin(x[0]), 1],
             [1, -cos(x[1])]])

    x, n = Newton_system(F, J, x=np.array([0.5, 0.5]), eps=0.0001)
    print("number of iterations ", n)
    print("solution: ", x)



if __name__ == '__main__':
    test_Newton_system1()