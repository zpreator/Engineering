# -*- coding: utf-8 -*-
"""
Zachary Preator
"""

import numpy as np
import matplotlib.pyplot as plt

def linearTrendline(x, y, xline):
    solutionLinear = linearregression(linear(x),y)
    linsola = solutionLinear[0]
    linsolb = solutionLinear[1]
    ylin = linsola*xline + linsolb
    codlin = linearcod(linsola,linsolb,x,y)
    print('Linear Solution')
    print('y = {0:.6f} x + {1:.6f}'.format(linsola,linsolb))
    print('r^2 = {0:.12f}'.format(codlin))
    return ylin

def QuadraticDisplay(x, y, xline):
    sol = linearregression(quadratic(x),y)
    sola = sol[0]
    solb = sol[1]
    solc = sol[2]
    yquad = sola*xline**2 + solb*xline + solc
    cod = polynomialcod(sol,x,y)
    print('Quadratic')
    print('y = {0:.6f} x^2 + {1:.6f} x + {2:.6f}'.format(sola,solb,solc))
    print('r^2 = {0:.12f}'.format(cod))
    return yquad

def PowerDisplay(x, y, xline):
    powersol = powerlaw(x,y)
    powersola = powersol[0]
    powersolb = np.exp(powersol[1])
    ypower = powersolb*xline**powersola
    powcod = linearcod(powersol[0],powersol[1],np.log(x),np.log(y))
    print('Power Law Solution')
    print('y = {0:.6f} x ^ {1:.6f}'.format(powersolb,powersola))
    print('r^2 = {0:.12f}'.format(powcod))
    return ypower

def ExponentialDisplay(x, y, xline):
    expsol = exponential(x,y)
    expsola = expsol[0]
    expsolb = np.exp(expsol[1])
    yexp = expsolb*np.exp(expsola * xline)
    expcod = linearcod(expsol[0],expsol[1],x,np.log(y))
    print('Exponential Solution')
    print('y = {0:.6f}*exp({1:.6f} x)'.format(expsolb,expsola))
    print('r^2 = {0:.12f}'.format(expcod))
    return yexp

def LogarithmicDispaly(x, y, xline):
    logsol = logarithmic(x,y)
    logsola = logsol[0]
    logsolb = logsol[1]
    ylog =logsola*np.log(xline) + logsolb
    logcod = linearcod(logsola,logsolb,np.log(x),y)
    print('Logarithmic Solution')
    print('y = {0:.6f} + {1:.6f} ln(x)'.format(logsolb,logsola))
    print('r^2 = {0:.12f}'.format(logcod))
    return ylog

def getData(datafile):
    """Gets data from text file"""
    data = np.loadtxt(datafile)
    return data

def linearregression(X,Y):
    """Does linear regression"""
    A = np.matrix.transpose(X) @ X
    b = np.matrix.transpose(X) @ Y
    return np.linalg.solve(A,b)
    

def linear(x):
    """Maxes quare x-matrix of a linear funciton for the linear regression"""
    ones = np.array([1 for i in x])
    xmat = np.matrix.transpose(np.array([x,ones]))
    return xmat

def quadratic(x):
    """Maxes square matrix for linear regression"""
    ones = np.array([1 for i in x])
    xsquared = x**2
    xmat = np.matrix.transpose(np.array([xsquared,x,ones]))
    return xmat

def powerlaw(x,y):
    """Makes square matrix and y vector for linear regression, and performs regression"""
    lnx = np.log(x)
    lny = np.log(y)
    xmat = linear(lnx)
    return linearregression(xmat,lny)

def exponential(x,y):
    """Makes matrix and y vector for linear regression, and performs regression"""
    lny = np.log(y)
    xmat = linear(x)
    return linearregression(xmat,lny)

def logarithmic(x,y):
    """Makes x matrix and y vector and performs regression"""
    lnx = np.log(x)
    xmat = linear(lnx)
    return linearregression(xmat,y)

def linearcod(a,b,x,y):
    """Finds coefficient of determination for a linear regression"""
    n = len(x)
    sumy = sum(y)
    cod = (b*sumy + a*sum(x*y) - 1/n*sumy**2)/(sum(y**2) - 1/n*sumy**2)
    return cod

def polynomialcod(sol,x,y):
    """Calculates coefficient of determination from general form"""
    #Compute ybar
    n = len(x)
    ybar = 1/n*sum(y)
    #Compute SStot
    SStot = sum([(y[i] - ybar)**2 for i in range(len(y))])
    #Calculate SSres
    power = len(sol)
    SSres = sum([(y[i] - sum([sol[j]*x[i]**(power - (j+1)) for j in range(power)]))**2 for i in range(len(y))])
    #Calculate CoD
    cod = 1- SSres/SStot
    return cod

def Echo(x, y, xline, plots):
    plt.plot(x,y,'ko',label='Data')
    plt.plot(xline,plots[0],label='Linear')
    plt.plot(xline,plots[1],label='Quadratic')
    plt.plot(xline,plots[2],label='Power Law')
    plt.plot(xline,plots[3],label='Exponential')
    plt.plot(xline,plots[4],label='Logarithmic')
    plt.legend(loc='lower right')
    plt.show()

def main():
    """Main function to call all other functions"""
    array = [np.array([0.5, 0.9, 1.7, 2.4]), np.array([8.7, 9.3, 10.6, 12.1]), np.arange(0.25,2.5,0.01)]
    ylin = linearTrendline(*array)
    yquad = QuadraticDisplay(*array)
    ypower = PowerDisplay(*array)
    yexp = ExponentialDisplay(*array)
    ylog = LogarithmicDispaly(*array)
    plots=[ylin, yquad, ypower, yexp, ylog]
    Echo(*array, plots)
    
    
    

main()