# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 10:19:30 2020

@author: smith
"""

import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

def findRe(U,D,nu):
    """Finds Reynolds number given freestram velocity, Diameter, and kinemetic viscosity"""
    return U*D/nu

def calcPressure(Cp,rho,U):
    """Calculates dynamic pressure given freestream velocity, density, and a Cp array"""
    return Cp*rho*U**2 / 2

def shearstress(F,rho,U,Re):
    """Calculates shear stress distribution from force, density,freestream and reynolds number"""
    return F*rho*U**2/2/np.sqrt(Re)

def GetData(textFile):
    file = u"C:/Repos/Engineering/ME342NumAnalysis/Unit4/{0}".format(textFile)
    return np.loadtxt(file, unpack=True)

def trapezoidal(x,y):
    """Trapezoidal integral of discrete data"""
    integral = 0
    for i in range(len(x)-1):
        integral += (y[i+1]+y[i])/2*(x[i+1]-x[i])
    return integral

def main(D,L,U,rho,nu,F):
    """Main function to call all other functions and return desired outputs"""
    #Unit conversions
    D /= 100
    L /= 100
    
    #Calculate Re to determine whether flow is turbuent or laminar
    Re = findRe(U,D,nu)
    #Depending on Re, grab laminar or turbulent data for Cp
    if Re < 3e5:    #Laminar flow
        Cpdata = GetData('Laminar.txt')
    else:
        Cpdata = GetData('Turbulent.txt')
    
    #Get Force data
    Fdata = GetData('Cf.txt')
    
    #Get Fdp, from dynamic pressure and cosine of angle
    P = calcPressure(Cpdata[1],rho,U)
    costheta = np.cos(np.radians(Cpdata[0]))
    Fdp = trapezoidal(Cpdata[0],P*costheta*L*D/2)
    print('Fdp:')
    print(Fdp)
    #Get Fdf, from shear stress and sine of angle
    tw = shearstress(Fdata[1],rho,U,Re)
    sintheta = np.sin(np.radians(Fdata[0]))
    Fdf = trapezoidal(Fdata[0],tw*sintheta*L*D/2)
    print('Fdf:')
    print(Fdf)
    #Add Fdp and Fdf together to get Fd
    Fd = Fdp + Fdf
    print('Fd:')
    print(Fd)
    
    #Find Error
    error = abs(F - Fd)/F
    print('Error:')
    print(error)
    return Fd

main(5.23,25.4,21.0,1.02,1.79e-5,2.9)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
