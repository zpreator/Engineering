import numpy as np
import matplotlib.pyplot as plt
import re
from scipy.stats import linregress
from scipy.optimize import curve_fit

def K1(f, t, y, h):
    """ Returns the k1 calculations"""
    return f(t, y)

def K2(f, t, y, h, K1):
    """ Returns the k2 calculations"""
    a = t + .5*h
    b = y + .5*h*K1
    return f(a, b)

def K3(f, t, y, h, K2):
    """ Returns the k3 calculations"""
    a = t + .5*h
    b = y + .5*h*K2
    return f(a, b)

def K4(f, t, y, h, K3):
    """ Returns the k4 calculations"""
    a = t + h
    b = y + h*K3
    return f(a, b)

function1 = lambda t, y: y*(np.sin(t))**3

function2 = lambda t, y0: y0*np.exp(1/3*np.cos(t)**3-np.cos(t) + 2/3)

def RK4(f, t, y, h):
    """ Calls the k functions and calculates the
    next y (y+1) and returns that y for an ODE f"""
    k1 = K1(f, t, y, h)
    k2 = K2(f, t, y, h, k1)
    k3 = K3(f, t, y, h, k2)
    k4 = K4(f, t, y, h, k3)
    y1 = y + 1/6*(k1 + 2*k2 + 2*k3 + k4)*h
    return y1

def Eulers(f, t, y, h):
    """ Returns the Euler's method for the ODE f"""
    return y + f(t, y)*h

def Display(data, f, plotName):
    """ Displays the two plots for each Case"""
    plotType = ['Runge-Kutta method', 'Euler\'s Method']
    lineType = ['yo-', 'b^:']
    for i in range(len(data[0])):
        plt.plot(data[i][0], data[i][1], lineType[i], label=plotType[i])
        
    t = np.arange(0, 4, 0.01)
    plt.plot(t, f(t, 1), 'k', label='Exact solution')
    plt.legend(loc='upper left')
    plt.xlabel(r'Time $(s)$')
    plt.ylabel(r'Location $(m)$')
    plt.tight_layout()
    plt.savefig('{0}.pdf'.format(plotName))
    plt.show()

def GetRK4(f, y0, desiredY, h):
    """ Gets the y values incrementally from
    the Runge-Kutta method and Euler method 
    and returns them in a list"""
    g = desiredY
    y = y0

    # Runge-kutta
    RKy = []
    RKt = []
    RKy.append(y)
    for i in np.arange(0, g, h):
        RKt.append(i)
        y = RK4(f, i, y, h)
        RKy.append(y)
    RKt.append(g)
    RK = [RKt, RKy]
    return RK

def GetEuler(f, y0, desiredY, h):
    """ Gets the y values incrementally from
    the Euler method and returns them in a list"""
    g = desiredY
    y1 = y0
    Ey = []
    Et = []
    Ey.append(y1)
    for i in np.arange(0, g, h):
        Et.append(i)
        y1 = Eulers(f, i, y1, h)
        Ey.append(y1)
    Et.append(g)
    E = [Et, Ey]
    return E

def ProduceLatexTable(columnHeadings, data, title='', label=''):
    """ Prints latex table"""
    # Adds a catption and begins table
    caption = '{' + title + '}'
    print('\\begin{table}')
    print('   \centering')
    print('   \caption{0}'.format(caption))

    # Sets the columns in \begin{tabular} (cccc...)
    cols = ''
    for i in range(len(data[0])):
        cols += 'c'
    print('   \\begin{tabular}{@{}', cols, '@{}}\\toprule')

    # Sets the column headings
    line = ''
    for i in range(len(columnHeadings)-1):
        line += columnHeadings[i] + ' & '
    line += columnHeadings[-1]
    print('      ', line, '\\\\ \midrule')

    # Prints the rows with the data provided
    for i in range(len(data)):
        row = ''
        for j in range(len(columnHeadings)-1):
            row += str(data[i][j]) + ' & '
            # row += '{0:6.4G}'.format(data[i][j]) + ' & '
        row += str(data[i][-1])
        # row += '{0:5.4G}'.format(data[i][-1])
        print('      ', row, '\\\\')

    # Ends the table schema
    print('      \\bottomrule')
    print('   \end{tabular}')
    label = '{' + label + '}'
    print('   \label{0}'.format(label))
    print('\end{table}')
    
def PowerCurve(x, a, b):
    """ Is used for the curve_fit 
    function in 'PowerCurveFitScipy'"""
    return a*x**b

def PowerCurveFitScipy(data):
    """ Computes the power law curve fit for the data"""
    popt, pcov = curve_fit(PowerCurve, data[0], data[1])
    residuals = data[1]-PowerCurve(data[0], popt[0], popt[1])
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((data[1]-np.mean(data[1]))**2)
    r_squared = 1 - (ss_res / ss_tot)
    return [popt[0], popt[1], r_squared]

def Error(y0, y1):
    """ Computes error
    y1 = next iteration for relative
    y1 = true value for true"""
    return abs(y1-y0)/y1

def Display2(data, lineType, label='', done = False, xLabel=None, yLabel=None, plotLabel=None, f=None, log=False):
    """ Displays the function parameter f"""
    t = np.arange(0, 4, 0.01)
    
    plt.plot(data[0], data[1], lineType, label=label)
    # plt.show()
    if (done):
        if f != None:
            plt.plot(t, f(t, 1), 'k', label='Exact')
        if log:
            plt.xscale("log")
            plt.yscale("log")
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend(loc='best')
        plt.tight_layout()
        plt.savefig('{0}.pdf'.format(plotLabel))
        plt.show()

def Question1():
    """ Plot the Euler solution, the RK4 solution, and the exact solution on the same graph using
    a step size of h=1 over a range of t=[0,4]"""
    plt.figure(figsize=(5, 3))
    Display([GetRK4(function1, 1, 4, 1),GetEuler(function1, 1, 4, 1)] , function2, 'StepSize1')

def Question2():
    """ 2. Plot the Euler solution using several different step-sizes, and exact solution, on the
    same graph to show the solution is converging on the exact solution"""
    h = 1
    plt.figure(figsize=(5, 3))
    lineType = ['g^--', 'bo--', 'rs--', 'yP--', 'g^:', 'm:']
    for i in range(6):
        Display2(GetEuler(function1, 1, 4, h), lineType[i], label=str(h))
        h = h/2
    Display2(GetEuler(function1, 1, 4, h), 'c-.', label=str(h), done=True, 
             xLabel=r'Time $(s)$',
             yLabel=r'Location $(m)$',
             f=function2,
             plotLabel='Question2')

def Question3():
    """3. Plot the RK4 solution using several different step-sizes, and the exact solution on
    the same graph to show the solution is converging on the exact solution"""
    h = 1
    plt.figure(figsize=(5, 3))
    lineType = ['g^--', 'bo-.', 'rs:']
    for i in range(3):
        Display2(GetRK4(function1, 1, 4, h), lineType[i], label=str(h))
        h = h/2
    Display2(GetRK4(function1, 1, 4, h), 'cP--', label=str(h), 
             done=True, 
             xLabel=r'Time $(s)$',
             yLabel=r'Location $(m)$',
             f=function2,
             plotLabel='Question3')

def Question4():
    """4. For each step-size, compute the true error and the relative error in the numerical solutions at t=4.0.
    Produce a table with these values..."""
    h = 1
    listOfStepSize = []
    den = 1
    table = []
    yTrue = function2(4, 1)
    y1E = 0
    y1RK4 = 0
    hString = ['1']
    for i in range(10):
        den *= 2
        hString.append('1/{0}'.format(den))
    for i in range(10):
        E = GetEuler(function1, 1, 4, h)
        y0E = y1E
        y1E = E[1][-1]
        RK4 = GetRK4(function1, 1, 4, h)
        y0RK4 = y1RK4
        y1RK4 = RK4[1][-1]
        if i > 0:
            ErrorEulerRel = Error(y0E, y1E)
            ErrorRK4Rel = Error(y0RK4, y1RK4)
        else:
            ErrorEulerRel = 0
            ErrorRK4Rel = 0
        ErrorEulerTrue = Error(y1E, yTrue)
        ErrorRK4True = Error(y1RK4, yTrue)
        listOfStepSize.append(h)
        h /= 2
        
        
        row = [y1E, ErrorEulerRel, ErrorEulerTrue, y1RK4, ErrorRK4Rel, ErrorRK4True]
        row = ['{0:4.4G}'.format(i) for i in row]
        row = [hString[i]] + row
        table.append(row)
    ProduceLatexTable([r'$h(s)$', r'$y(m)$', r'$e_{rel}$', r'$e_{true}$', r'$y(m)$', r'$e_{rel}$', r'$e_{true}$'],
                      table,
                      title='Relative and absolute errors for Eulers and Runge-Kutta methods with respect to step size, (h)')
    return table, listOfStepSize
        
def Question6(table, listOfStepSize):
    """6. Plot the error (true and relative) as a function of step size on a log-log scale plot, for both the Euler
    and RK4 methods."""
    Erel = [float(i) for i in np.array(table)[:, 2]]
    Eabs = [float(i) for i in np.array(table)[:, 3]]
    Rrel = [float(i) for i in np.array(table)[:, 5]]
    Rabs = [float(i) for i in np.array(table)[:, 6]]
    Erel1 = Erel.copy()
    Erel1.reverse()
    Erel1.remove(0.0)
    Eabs1 = Eabs.copy()
    Eabs1.reverse()
    Rrel1 = Rrel.copy()
    Rrel1.reverse()
    Rrel1.remove(0.0)
    Rabs1 = Rabs.copy()
    Rabs1.reverse()
    stepsizes1 = listOfStepSize.copy()
    stepsizes2 = stepsizes1.copy()
    stepsizes2.reverse()
    stepsizes1.reverse()
    stepsizes1.remove(1)
    plt.figure(figsize=(5, 3))
    Display2([stepsizes1, Erel1], 'g^--', label='Euler Relative')
    Display2([stepsizes2, Eabs1], 'bo--', label='Euler Absolute')
    Display2([stepsizes1, Rrel1], 'rs--', label='RK4 Relative')
    Display2([stepsizes2, Rabs1], 'yP--', label='RK4 Absolute', done=True, xLabel=r'Step size $(m)$', yLabel='Error (-)', log=True, plotLabel='Question6')
    

def Question7(table, listOfStepSize):
    """# 7. Using least-squares regression, compute the convergence rate based on the true error and the relative
    # error of both the Euler’s and RK4 methods. Produce a table with these values as shown below."""
    Erel = [float(i) for i in np.array(table)[:, 2]]
    Eabs = [float(i) for i in np.array(table)[:, 3]]
    Rrel = [float(i) for i in np.array(table)[:, 5]]
    Rabs = [float(i) for i in np.array(table)[:, 6]]
    ErelVals = PowerCurveFitScipy([listOfStepSize, Erel])
    EabsVals = PowerCurveFitScipy([listOfStepSize, Eabs])
    RrelVals = PowerCurveFitScipy([listOfStepSize, Rrel])
    RabsVals = PowerCurveFitScipy([listOfStepSize, Rabs])
    row1 = [EabsVals[0], EabsVals[1], RabsVals[0], RabsVals[1]]
    row1 = ['{0:5.4f}'.format(i) for i in row1]
    row2 = [ErelVals[0], ErelVals[1], RrelVals[0], RrelVals[1]]
    row2 = ['{0:5.4f}'.format(i) for i in row2]

    ProduceLatexTable([r'$M$', r'$\alpha$', r'$M$', r'$\alpha$'], [row1, row2])


def main():
    Question1()
    Question2()
    Question3()
    table, listOfStepSize = Question4()
    # 5. From the results, determine what step-size is required for Euler’s method to achieve an absolute error
    # that is similar to the RK4 method error with a step-size of h=1.0.

    #A step size of between 1/16 and 1/32 for the Euler method analysis of the function would yield results
    #close to the results of the Runge-Kutta method at step size of 1
    
    Question6(table, listOfStepSize)
    Question7(table, listOfStepSize)
    

main()
# ProduceLatexTable(['Heading1', 'Heading2', 'Heading3'], [[1, 2, 3],[2, 3, 4]])