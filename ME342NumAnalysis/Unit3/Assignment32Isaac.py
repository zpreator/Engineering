# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:38:30 2020

@author: smith
"""

import numpy as np
import matplotlib.pyplot as plt

def getfiledata(datafile):
    """Gets data from text file and splits them into the different columns representing time and the 4 strain gauges."""
    data = np.loadtxt(datafile)
    return data

def linearregression(xmat,y):
    """Performs linear regression of data"""
    A = np.matrix.transpose(xmat) @ xmat
    b = np.matrix.transpose(xmat) @ y
    sol = np.linalg.solve(A,b)
    return sol

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


def main():
    """Main function to call all other functions"""
    #data = getfiledata('data_day2.txt')
    # 0.5 8.7
    # 0.9 9.3
    # 1.7 10.6
    # 2.4 12.1

    x = np.array([0.5, 0.9, 1.7, 2.4])
    y = np.array([8.7, 9.3, 10.6, 12.1])
    xline = np.arange(0.25,2.5,0.01)
    #Linear trendline
    linsol = linearregression(linear(x),y)
    linsola = linsol[0]
    linsolb = linsol[1]
    ylin = linsola*xline + linsolb
    codlin = linearcod(linsola,linsolb,x,y)
    print('Linear Solution')
    print('y = {0:.6f} x + {1:.6f}'.format(linsola,linsolb))
    print('r^2 = {0:.12f}'.format(codlin))
    
    #Quadratic trendline
    quadsol = linearregression(quadratic(x),y)
    quadsola = quadsol[0]
    quadsolb = quadsol[1]
    quadsolc = quadsol[2]
    yquad = quadsola*xline**2 + quadsolb*xline + quadsolc
    codquad = polynomialcod(quadsol,x,y)
    print('Quadratic Solution')
    print('y = {0:.6f} x^2 + {1:.6f} x + {2:.6f}'.format(quadsola,quadsolb,quadsolc))
    print('r^2 = {0:.12f}'.format(codquad))
    
    #Power Law
    powersol = powerlaw(x,y)
    powersola = powersol[0]
    powersolb = np.exp(powersol[1])
    ypower = powersolb*xline**powersola
    powcod = linearcod(powersol[0],powersol[1],np.log(x),np.log(y))
    print('Power Law Solution')
    print('y = {0:.6f} x ^ {1:.6f}'.format(powersolb,powersola))
    print('r^2 = {0:.12f}'.format(powcod))
    
    #Exponential 
    expsol = exponential(x,y)
    expsola = expsol[0]
    expsolb = np.exp(expsol[1])
    yexp = expsolb*np.exp(expsola * xline)
    expcod = linearcod(expsol[0],expsol[1],x,np.log(y))
    print('Exponential Solution')
    print('y = {0:.6f}*exp({1:.6f} x)'.format(expsolb,expsola))
    print('r^2 = {0:.12f}'.format(expcod))
    
    #Logarithmic
    logsol = logarithmic(x,y)
    logsola = logsol[0]
    logsolb = logsol[1]
    ylog =logsola*np.log(xline) + logsolb
    logcod = linearcod(logsola,logsolb,np.log(x),y)
    print('Logarithmic Solution')
    print('y = {0:.6f} + {1:.6f} ln(x)'.format(logsolb,logsola))
    print('r^2 = {0:.12f}'.format(logcod))
    
    
    plt.plot(x,y,'ko',label='Data')
    plt.plot(xline,ylin,label='Linear')
    plt.plot(xline,yquad,label='Quadratic')
    plt.plot(xline,ypower,label='Power Law')
    plt.plot(xline,yexp,label='Exponential')
    plt.plot(xline,ylog,label='Logarithmic')
    plt.legend(loc='lower right')
    plt.show()
    

main()