def CantileverUniformLoadYmax(w, l, E, I):
    """ w = distributed load
        l = length of cantilever beam
        E = Modulus of Elasticity
        I = 2nd Moment of area"""
    return -w*l**4/(2 * 8*E*I)

def CantileverUniformLoadY(w, l, E, I, x):
    """ w = distributed load
        l = length of cantilever beam
        E = Modulus of Elasticity
        I = 2nd Moment of area
        x = point in question """
    return -w*x**2/(2*24*E*I)*(4*l*x-x**2-6*l**2)

def CantileverEndForce(F, l, E, I):
    """ F = load
        l = length of cantilever beam
        E = Modulus of Elasticity
        I = 2nd Moment of area """
    return -F * l**3/(2 * 3 * E * I)

def ConcentratedMoment(x, a):
    """ <x-a>^-2 """
    if x == a:
        return 10000000000
    else:
        return 0

def ConcentratedForce(x, a):
    """ <x-a>^-1 """
    if x != a:
        return 0
    else:
        return 100000000000

def UnitStep(x, a):
    """ <x-a>^0 """
    if x < a:
        return 0
    else:
        return 1

def Ramp(x, a):
    """ <x-a>^1 """
    if x < a:
        return 0
    else:
        return x-a

def Load(x):
    F1 = 340
    W = 12.5
    return -W * UnitStep(x,0) - F1 * ConcentratedForce(x,15) + W * UnitStep(x,39)

def Shear(x):
    F1 = 340
    W = 12.5
    R1 = 452.981
    return -W * Ramp(x, 0) - F1 * UnitStep(x, 15) + W * Ramp(x, 39) + R1

def Moment(x):
    F1 = 340
    W = 12.5
    R1 = 452.981
    return -W/2 * Ramp(x, 0)**2 -F1 * Ramp(x, 15) + W/2 * Ramp(x, 39)**2 + R1 * x

def Slope(x, E, I):
    F1 = 340
    W = 12.5
    R1 = 452.981
    C3 = -63850
    return (-W/6 * Ramp(x, 0)**3 - F1/2 * Ramp(x, 15)**2 + W/6 * Ramp(x, 39)**3 + R1/2 * x**2)/(E*I)  + C3

def Displacement(x, E, I):
    F1 = 340
    W = 12.5
    R1 = 452.981
    C3 = -63850
    return (-W/24 * Ramp(x, 0)**4 - F1/6 * Ramp(x, 15)**3 + W/24 * Ramp(x, 39)**4 +R1/6 * x**3 + C3 * x)/(E*I)

