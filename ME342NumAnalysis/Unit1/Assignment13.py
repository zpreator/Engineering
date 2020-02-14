import numpy as np
import math
import matplotlib.pyplot as plt
import sys

def equation1(x):
    """ Returns the evaluation of x in the following equation"""
    return x*math.sin(10*x)-x+1

def sign(x):
    """ Returns -1 if negative and 1 if positive"""
    if x < 0:
        return -1
    else:
        return 1

def bisection(f, x1, x2, errorMax=1e-20, printIterations = False):
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
        if printIterations:
            print('Iteration number: ', count)
            print('Estimated root: ', xnew)
            print('Evaluation at estimate', f(xnew))
            print('Relative error: ', e)
    print('The number of iterations was: {0:3d}, the root is: {1:6.6f}, and the error was: {2:6.4e}'.format(int(math.floor(n)), xnew, e))
    return pakige

def secant(f, x0, x1, errorMax=1e-6, printIterations = False):
    """ Iterates through the secant method """
    e = errorMax + 1
    n = 0
    pakige = []
    while e > errorMax:
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
    return pakige

def ridders(funct, x0, x1, maxError = 1E-6, printIterations = False):
    if sign(funct(x0))==sign(funct(x1)):
        print("Inital guess must evaluate to different signs")
        sys.exit()
    e = maxError+1
    pakige = []
    n = 0
    while e > maxError:
        f0 = funct(x0)
        f1 = funct(x1)
        x2 = (x0 + x1)/2
        f2 = funct(x2)
        x = x2 + (x2-x0)*sign(f0-f1)*f2/math.sqrt(f2**2-f0*f1)
        f = funct(x) 
        n += 1
        if sign(f2) != sign(f):
            x0 = x2
            f0 = f2
            x1 = x
            f1 = f
            e = abs(x0 - x1)/x0
        elif sign(f1) != sign(f):
            xold = x0
            x0 = x
            f0 = f
            e = abs(x0 - xold)/x0
        else:
            xold = x1
            x1 = x
            f1 = f
            e = abs(x1-xold)/x1
        pakige.append([n, x, funct(x), e])
        if printIterations:
            print('Iteration number: ', n)
            print('Estimated root: ', x)
            print('Evaluation at estimate', f(x))
            print('Relative error: ', e)
    return pakige

def display(pakige):
    # Change plt font family and text size
    plt.rc('font', family='serif', size=10)

    # Example data
    t = np.linspace(0,1,num=100,endpoint=True)
    s = np.cos(4 * np.pi * t) + 2

    # Example descreate data
    tData = np.linspace(0,1,num=20,endpoint=True)
    sData = np.cos(4 * np.pi * tData) + 2+np.random.random(len(tData))/10
    uData = np.random.random(len(tData))/10

    # Make the plot
    plt.figure(figsize=(5,3)) #set the figuer size (width,height)(inches)
    plt.plot(t,s,'-.',label='Modeled values')
    plt.errorbar(tData,sData,yerr=uData,fmt='o',capsize=5,label='Mesured Values')

    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (mV)')
    #plt.xlabel(r'Time ($s$)') #the r'...' alows for LaTeX math input
    #plt.ylabel(r'Voltage ($mV$)')
    plt.legend(loc='lower right')
    #plt.grid()
    plt.tight_layout()
    plt.show()
    # plt.savefig('goodPlot.pdf') # save the image as a vecortized pdf

def displayGuessIterations(bisection, secant, ridders):
    # Bisection method
    iterations1 = [i[0] for i in bisection]
    values1 = [i[1] for i in bisection]
    plt.plot(iterations1, values1, 'r')
    plt.plot(iterations1, values1, 'r.')


    # Secant method
    iterations2 = [i[0] for i in secant]
    values2 = [i[1] for i in secant]
    plt.plot(iterations2, values2, 'b')
    plt.plot(iterations2, values2, 'b.')


    # Ridders method
    iterations3 = [i[0] for i in ridders]
    values3 = [i[1] for i in ridders]
    plt.plot(iterations3, values3, 'g')
    plt.plot(iterations3, values3, 'g.')

    plt.legend(['Bisection','','Secant','', 'Riddler\'s',''])
    plt.xlabel('Iterations')
    plt.ylabel('Approximations')
    plt.show()
    plt.savefig('Guesses.pdf')

def displayErrorIterations(bisection, secant, ridders):
    # Bisection method
    iterations1 = [i[0] for i in bisection]
    values1 = [i[3] for i in bisection]
    plt.plot(iterations1, values1, 'r')

    iterations2 = [i[0] for i in secant]
    values2 = [i[3] for i in secant]
    plt.plot(iterations2, values2, 'b')

    iterations3 = [i[0] for i in ridders]
    values3 = [i[3] for i in ridders]
    plt.plot(iterations3, values3, 'g')

    plt.legend(['Bisection','Secant','Riddler\'s'])
    plt.xlabel('Iterations')
    plt.ylabel('Approximate Error')
    plt.yscale('log')
    plt.show()
    plt.savefig('Error.pdf')

def main():
    pakige1 = bisection(equation1, 0.6, 1.2)
    pakige2 = secant(equation1, 0.6, 1.2)
    pakige3 = ridders(equation1, 0.6, 1.2)
    for i in pakige1:
        print(i[0], 'Root: {0:6.4f} Error: {1:7.2E}'.format(i[1], i[3]))
    displayGuessIterations(pakige1, pakige2, pakige3)
    displayErrorIterations(pakige1, pakige2, pakige3)

    
main()