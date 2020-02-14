import math
import sys
import matplotlib.pyplot as plt
import numpy as np

def equation2(x):
    """ Returns the evaluation of x in the following equation"""
    return x*math.sin(10*x)-x+1

def sign(s):
    """ Returns 0 if negative and 1 if positive"""
    if s < 0:
        return 0
    else:
        return 1

def bisection(f, x1, x2, errorMax=1e-6):
    """ Calculates the root of the function given two initial root
    bounding guesses"""
    f1 = f(x1)
    f2 = f(x2)
    if (f1 > 0 and f2 > 0) or (f1 < 0 and  f2 < 0):
        print('Error, the two root bounds must have values of opposite sign')
        sys.exit()
    
    n = math.log(abs(f2-f1)/errorMax)/math.log(2)
    xold = 0
    e = errorMax + 1
    while e > errorMax:
        xnew = (x2+x1)/2
        if sign(f(xnew)) == sign(f(x1)):
            xold = x1
            x1 = xnew
        else:
            xold = x2
            x2 = xnew
        e = abs((xnew-xold)/xnew)
    print('The number of iterations was: {0:3d}, the root is: {1:6.4f}, and the error was: {2:6.4e}'.format(int(math.floor(n)), xnew, e))
    return xnew

def polynomialRoots(coefs):
    """ Returns the roots of the polynomial function whose 
    coefficients are passed in as parameters"""
    return np.roots(coefs)

def display(f, roots):
    """ Plots the equation and shows the two roots as green triangles"""
    r = np.arange(0.0, 3.0, 0.01)
    values = [equation2(i) for i in r]
    plt.plot(r, values, 'b--', roots, [f(i) for i in roots], 'g^')
    plt.show()

def main():
    """ Calls the secant method"""

    ### Problem 1 #########################
    # root1 = bisection(equation2, 0.6, 1.2)
    # root2 = bisection(equation2, 1.8, 2.0)
    # root3 = bisection(equation2, 1.2, 1.35)
    # root4 = bisection(equation2, 1.45, 1.6)
    # root5 = bisection(equation2, 2.1, 2.2)
    # display(equation2, [root1, root2, root3, root4, root5])

    ### Problem 2 #########################
    coefs = [-120, -46, 79, -3, -7, 1]
    print(polynomialRoots(coefs))


main()
