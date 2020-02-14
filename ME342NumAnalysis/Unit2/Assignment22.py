import numpy as np
import scipy
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from time import perf_counter as time

""" Self grade:
9/10
Everything works, but something is off about the 2D plots
"""
def equation1(y):
    return math.sqrt((120-y)/8)

def equation2(x):
    return x**3-1

def equation3(x2, x3):
    return (2*x2-3*x3-1)/5

def equation3_1(x2, x3):
    """ Equation3 solved for x1 """
    return (2*x2-1-3*x3)/5

def equation4(x1, x3):
    return (3*x1-x3+2)/9

def equation4_1(x2, x3):
    """ Equation4 solved for x1 """
    return (9*x2-2 + x3)/3

def equation5(x1, x2):
    return (2*x1-x2-3)/7

def equation5_1(x2, x3):
    """ Equation5 solved for x1 """
    return (x2+3 + 7*x3)/2

def gaussSeidel(equations, guesses, maxError = 1E-6):
    """ Takes a list of equations and a list of guesses
    and solves them using the Gauss Seidel method until all 
    the errors reach maxError"""
    errors = [True]
    n = len(equations)
    ans = list(guesses)
    count = 0
    while any(errors):
        count += 1
        err = []
        old = list(ans)
        for i in range(0, n):
            var = []
            for j in range(0, n-1):
                if i + j >= n-1:
                    var.append(ans[i + j-1])
                else:
                    var.append(ans[i+j+1])
            ans[i] = equations[i-1](*var)
            e = abs(ans[i]-old[i])/ans[i]
            if abs(e) < maxError:
                err.append(False)
            else:
                err.append(True)
        errors = err
    # print(ans)
    return ans

def display3D(equations):
    """ Displays the 3 functions in 3D """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    bX21 = np.arange(-10, 10, 0.25)
    bX31 = np.arange(-10, 10, 0.25)
    X21, X31 = np.meshgrid(bX21, bX31)
    X11 = equations[0](X21, X31)
    ax.plot_surface(X11, X21, X31)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    bX12 = np.arange(-10, 10, 0.25)
    bX32 = np.arange(-10, 10, 0.25)
    X12, X32 = np.meshgrid(bX12, bX32)
    X22 = equations[1](X12, X32)
    ax.plot_surface(X12, X22, X32)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    bX13 = np.arange(-10, 10, 0.25)
    bX23 = np.arange(-10, 10, 0.25)
    X13, X23 = np.meshgrid(bX13, bX23)
    X33 = equations[2](X13, X23)
    ax.plot_surface(X13, X23, X33)


    plt.show()

def displayReg(ans):
    """ Displays the 3 equations solved for x1
    holding x3 constant"""
    x = np.arange(-10, 10, 0.25)
    x3 = ans[0]
    y1 = equation3_1(x, x3)
    y2 = equation4_1(x, x3)
    y3 = equation5_1(x, x3)
    plt.plot(x, y1, 'b', x, y2, 'y', x, y3, 'r', ans[2], ans[1], 'g^')
    plt.legend(['Equation 1', 'Equation 2', 'Equation 3', 'Intersecting point'])
    plt.xlabel('x2')
    plt.ylabel('x1')
    plt.show()

def main():
    """ Calls the gaussSeidel method referencing equations 1-5
    and then displays them"""
    t1 = time()
    ans = gaussSeidel([equation1, equation2], [0, 3])
    t2 = time()
    tot = t2-t1
    print(ans, tot)
    # ans = gaussSeidel([equation3, equation4, equation5], [1, 2, 3])
    # display3D([equation3, equation4, equation5])
    # displayReg(ans)

main()