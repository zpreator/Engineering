import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz
"""
Zachary Preator
10/10
"""
def GetData(textFile):
    file = u"C:/Repos/Engineering/ME342NumAnalysis/Unit4/{0}".format(textFile)
    return np.loadtxt(file, unpack=True)


def Friction(Cf):
    """ Returns discrete data for theta, Tw, and Sin(theta)
        Tw is based on Equation 6""" 
    Uf = 21 # Free Stream Velocity (m/s)
    d = 0.0523 # diameter (m)
    nu = 1.79E-5 # Kinematic Viscosity (m^2/s)
    Re = Uf*d/nu
    rho = 1.02 # Density (kg/m^3)
    temp = np.sqrt(Re)/(.5*rho*Uf**2)
    Tw = [i/temp for i in Cf[1]]
    sinTheta = [np.sin(np.deg2rad(i)) for i in Cf[0]]
    return Cf[0], Tw, sinTheta

def Pressure(Cp):
    """ Returns discrete data for theta, P, and Cos(theta)
        P is based on Equation 4"""
    Uf = 21 # Free Stream Velocity (m/s)
    rho = 1.02 # Density (kg/m^3)
    P = [.5*rho*Uf**2*i for i in Cp[1]]
    cosTheta = [np.cos(np.deg2rad(i)) for i in Cp[0]]
    return Cp[0], P, cosTheta

def main():
    Cp = GetData("Laminar.txt")
    Cf = GetData("Cf.txt")
    F = 2.9 # Measured Force
    L = 0.245 # Length (m)
    d = 0.0523 # Diameter (m)

    # I am using trapezoidal method of calculating the integral 
    # because the step size is not consistent

    # Data for the pressure coeffecient and Pressure difference
    thetaPressure, P, cosTheta = Pressure(Cp)
    stuffPressure = [i*j for i, j in zip(P, cosTheta)]
    Fpressure = trapz(stuffPressure, thetaPressure*L*d/2)

    # Data for the friction value and shear stress distribution
    thetaFriction, Tw, sinTheta = Friction(Cf)
    stuffFriction = [i*j for i, j in zip(Tw, sinTheta)]
    Ffriction = trapz(stuffFriction, thetaFriction*L*d/2)

    # Summing the two integrals to get the total force
    Ftot = Fpressure + Ffriction
    e = abs(Ftot-F)/F
    print(Fpressure, Ffriction, Ftot, e)
    

main()