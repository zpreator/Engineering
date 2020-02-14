import math
import matplotlib.pyplot as plt
import numpy as np

def equation1(x, k = 10, c = -1):
    """ Returns the value of the function given an x value"""
    return x*math.sin(k*x) - x - c

def function2(x):
    return x**2+x-5

def function3(x):
    return x**3-2*x**2

def function4(x, g= 9.81, L = 4, t = 2.5, v = 5):
    return math.sqrt(2*g*x)*math.tanh(math.sqrt(2*g*x)/(2*L)*t)-v

def function5(coefs):
	return np.roots(coefs)

def secant(f, x0, x1, errorMax=1e-6, printIterations = False):
    """ Iterates through the secant method """
    e = errorMax + 1
    n = 0
    pakige = []
    while n < 10:
        xnew = x1 - (f(x1)*(x0-x1))/(f(x0)-f(x1))
        x0 = x1
        x1 = xnew
        e = abs((xnew-x0)/xnew)
        n += 1
        pakige.append([n, xnew, f(xnew), e])
        if printIterations:
            print('Iteration number: ', n)
            print('Estimated root: ', xnew)
            print('Evaluation at estimate', f(xnew))
            print('Relative error: ', e)
    return xnew

def display(f, roots):
    """ displays the plot from 0 to 3 and shows the points"""
    r = np.arange(0.0, 3.0, 0.01)
    values = [f(i) for i in r]
    # plt.plot(r, values, 'b', roots, [f(i) for i in roots], 'g^')
    plt.plot(r, values, 'b', roots, f(roots), 'g^')
    plt.legend(['Equation 1'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def main():
    """ calls the secant function, compiles several points into a list
    and calls the display function"""
    root1 = secant(equation1, 0.6, 1.2)
    # root2 = secant(function1, 2.2, 2.7)
    display(equation1, root1)
#     root1 = secant(function1, 1.6, 2.1)
#     root2 = secant(function2, 0, 6)
#     root3 = secant(function3, 1, 3)
#     root4 = secant(function4, 0, 2)
#     roots = function5([5.0, -14, 8.25, 4.25, -3.875])
#     print(root1, root2, root3, root4, roots)
    

main()