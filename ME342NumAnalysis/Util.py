import math
import sys

def sign(x):
    """ Returns -1 if negative and 1 if positive"""
    if x < 0:
        return -1
    else:
        return 1

def bisection(f, x1, x2, errorMax=1e-20):
    """ Calculates the root of the function given two initial root
    bounding guesses"""
    f1 = f(x1)
    f2 = f(x2)
    if (f1 > 0 and f2 > 0) or (f1 < 0 and  f2 < 0):
        print('Error, the two root bounds must have values of opposite sign')
        sys.exit()
    
    pakige = []
    n = math.log(abs(f2-f1)/errorMax)/math.log(2)
    xold = 0
    count = 0
    e = errorMax + 1
    while count < 20:
        xnew = (x2+x1)/2
        if sign(f(xnew)) == sign(f(x1)):
            xold = x1
            x1 = xnew
        else:
            xold = x2
            x2 = xnew
        e = abs((xnew-xold)/xnew)
        count += 1
        pakige.append([count, xnew, f(xnew), e])
    print('The number of iterations was: {0:3d}, the root is: {1:6.6f}, and the error was: {2:6.4e}'.format(int(math.floor(n)), xnew, e))
    return xnew

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