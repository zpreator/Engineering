from scipy.optimize import newton_krylov
from time import perf_counter as time
import math
import numpy as np

constants = {}

def f1(x):
    var = x[1]
    return np.emath.sqrt((120-var)/8)-x[0]

def f2(x):
    return x[0]**3-1-x[1]

def f(x):
    return [f1(x), f2(x)]

def Friction(x):
    """ Friction equation"""
    eps = constants["epsilon"]
    D = constants["D"]
    return -2*np.log10((eps/D)/3.7+2.51/(x[2]*np.emath.sqrt(x[0])))-1/np.emath.sqrt(x[0])
    

def ReynoldsNum(x):
    """ Reynolds number"""
    nu = constants["nu"]
    D = constants["D"]
    return 4*x[1]/(math.pi*nu*D)
    

def EnergyVdot(x):
    """ Energy equation to return Vdot"""
    # P1, P2, z1, z2, L, hp, Km, epsilon, rho, nu, g, boo = constants
    # f, Vdot, Re = variables 
    P1 = constants["P1"]
    rho = constants["rho"]
    g = constants["g"]
    z1 = constants["z1"]
    hp = constants["hp"]
    P2 = constants["P2"]
    z2 = constants["z2"]
    Km = constants["Km"]
    L = constants["L"]
    D = constants["D"]
    return np.emath.sqrt((P1/(rho*g)+z1+hp-P2/(rho*g)-z2)/(x[0]*L/D+Km)*(math.pi**2*g*D**4)/8)

def funct(x):
    return [Friction(x), ReynoldsNum(x), EnergyVdot(x)]

def Question1():
    t0 = time()
    x = [1, 1]
    sol = newton_krylov(f, x)
    print(sol)
    t1 = time()
    times = t1-t0
    print(times)

def Question2(P1, P2, z1, z2, L, hp, Km, epsilon, rho, nu, g, f, D, Vdot):
    global constants
    constants = {"P1":P1, "P2":P2, "z1":z1, "z2":z2, "L":L, "hp":hp, "Km":Km, "epsilon":epsilon, "rho":rho, "nu":nu, "g":g, "D":D}
    x = [f, Vdot, 0]
    sol = newton_krylov(funct, x)
    print(sol)

Question1()
Question2(350, 425, 0, 12, 225, 56, 16.2, 0.045, 998, 1.004E-6, 9.81, 0.01, 5.25, 0.05)