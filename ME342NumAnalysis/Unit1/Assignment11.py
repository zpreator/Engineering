import math
import sys
import matplotlib.pyplot as plt
import numpy as np

def equation1(x):
    """ Returns the evaluation of x in the following equation"""
    return x*math.sin(10*x)-x+1

def equation2(x):
    return 2*x-4*math.log(4*x)

def equation3(x):
		return x**2+x-5
		
def equation4(x):
		return x**3-2*x**2
		
def equation5(x, g= 9.81, L = 4, t = 2.5, v = 5):
		return math.sqrt(2*g*x)*math.tanh(math.sqrt(2*g*x)/(2*L)*t)-v
		
def sign(s):
    """ Returns 0 if negative and 1 if positive"""
    if s < 0:
        return 0
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
    return pakige

def display(f, root1, root2):
    """ Plots the equation and shows the two roots as green triangles"""
    r = np.arange(0.0, 3.0, 0.01)
    values = [equation1(i) for i in r]
    plt.plot(r, values, 'b--', [root1, root2], [f(root1), f(root2)], 'g^')
    plt.show()

# def main():
#     """ Calls the bisection method"""
#     root1 = bisection(equation1, 0.6, 1.2)
#     root2 = bisection(equation1, 2.2, 2.7)
#     display(equation1, root1, root2)
    # bisection(equation1, 1.6, 2.1)
    # bisection(equation3, 0, 6)
    # bisection(equation4, 1, 3)
    # pakige = bisection(equation5, 0, 2)
    # display(pakige)

# main()
