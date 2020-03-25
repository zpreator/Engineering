import numpy as np

def HallandFriction(epsilon, D, Re):
    """ Returns the friction factor given:
    epsilon = roughness (ft/mm)
    D = diameter (ft/mm)
    Re = Reynolds Number"""
    f = 18/11/(np.log((epsilon/D/3.7)**1.11 + 6.9/Re))**2
    return f

def ReynoldsNumber(V, D, nu):
    """ Returns the reynolds number given V, D, nu
    for flow rate reynolds number, use ReynoldsNumber2
    V = velocity (ft/s, m/s)
    D = diameter (ft, m)
    nu = kinematic viscosity (m^2/s, ft^2/s)"""
    Re = V*D/nu
    return Re

def ReynoldsNumber2(Vdot, D, nu):
    """ Returns the reynolds number given Vdot, D, nu
    for velocity input, use ReynoldsNumber
    Vdot = volume flow rate (ft^3/s, m^3/s)
    D = diameter (ft, m)
    nu = kinematic viscosity (m^2/s, ft^2/s)"""
    Re = 4*Vdot/(np.pi*nu*D)
    return Re

def HeadLoss(f, L, D, sumK, V, units='english'):
    """ Returns the head loss
    f = friction factor
    L = length of pipe (ft, m)
    D = diameter (ft, m)
    sumK = sum of minor loses
    V = velocity of fluid in pipe (ft/s, m/s)
    units = english/metric (lowercase)"""
    if units == 'english':
        return (f*L/D + sumK)*V**2/(2*32.174)
    elif units == 'metric':
        return (f*L/D + sumK)*V**2/(2*9.81)
    else: return np.nan