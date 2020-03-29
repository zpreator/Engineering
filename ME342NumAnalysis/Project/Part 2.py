import numpy as np
import matplotlib.pyplot as plt
"""Zachary Preator
"""
# Constants/Givens
T     = 280          # Kelvin (temperature in Rexburg)
Pa    = 84800        # Kpa (air pressure in rexburg gage)
R     = 0.287        # Gas constant (Unitless)
g     = 9.807        # m/s^2
D     = 4.2          # in (Diameter of 2 liter bottle)
mb    = 60           # g (mass of empty bottle)
Cd    = 0.82         # Coefficient of drag (Unitless)
rhow  = 998          # kg/m^3 (water density)
Vtot  = 2            # L (2 liter bottle)

# Calculations/Conversions
rhoa  = Pa/(R*T)/1000# kg/m^3 (air density in Rexburg)
Ab    = np.pi*D**2/4 # m^2 (cross sectional area of bottle)
Vtot /= 1000         # L to m^3 (initial volume of water)
mb   /= 1000         # g to kg (mass of empty bottle)
D    /= 39.37        # in to m (Diameter of 2 liter bottle)

# Initial conditions (Will be set in bottle_rocket())
P0    = 0
An    = 0
Vw0   = 0
Va0   = 0
def Equation1(P):
    """ returns the velocity in m/s given:
    P = pressure in pa"""
    return np.sqrt(2*P/rhow)

def Equation2(y):
    """ ODE1
    returns the rate of change of mass of water given: 
    mw = mass of water in the bottle
    (Each ODE takes all three parameters mw, vb, and yb)"""
    mw, vb, yb, t = y
    Vw            = Equation3Vol(mw)     # m^3 Volume of water in bottle
    Va            = Vtot-Vw        # m^3 Volume of air in bottle
    PbAbs         = Equation9(Va, Vw)    # Pa absolute pressure in bottle
    Pb            = Equation6Gage(PbAbs) # Pa gage pressure in bottle
    v             = Equation1(Pb)        # m/s velocity of water exiting nozzle
    global P0, Va0
    P0            = PbAbs                # Setting global variable pressure in bottle
    Va0           = Va                   # Setting global variable volume of air in bottle
    return Equation4(v)

def Equation3Vol(m):
    """ returns the volume of water given:
    m = mass of water in kg"""
    return m/rhow

def Equation3Mass(V):
    """ returns the mass of water given:
    V = volume of water m^3"""
    return rhow*V

def Equation3MassAir(V):
    """ returns the mass of water given:
    V = volume of water m^3"""
    return rhoa*V

def Equation4(v):
    """ returns the mass flow rate of water given:
    v = velocity in m/s"""
    return -rhow*v*An

def Equation5(Va):
    """ returns the pressure of air in the bottle given:
    Va = Volume of air"""
    ma = Equation3Mass(Va)
    P = ma*R*T/Va # Absolute pressure
    return P - Pa # Converting to gage

def Equation6Abs(Pg):
    """ returns the absolute pressure given:
    Pg = gage pressure in bottle in pascals"""
    return Pg + Pa

def Equation6Gage(Pabs):
    """ returns the gage pressure given:
    Pabs = absolute pressure in pascals"""
    return Pabs - Pa
    
def Equation9(Va, Vw):
    """ returns the pressure in the bottle at the next time step"""
    Pnew = P0*Va0/Va # Update global pressure variable
    return Pnew

def Equation10(y):
    """ ODE2
    returns the rate of change of the velocity of the bottle given:
    mw = mass of water in bottle
    vb = velocity of bottle
    (Each ODE takes all three parameters mw, vb, and yb)"""
    mw, vb, yb, t = y
    Vw            = Equation3Vol(mw)     # L Mass of water to volume of water
    Va            = Vtot - Vw            # L Total volume of bottle - water to get volume of air
    PbAbs         = Equation9(Va, Vw)    # Pa absolute pressure in bottle
    Pb            = Equation6Gage(PbAbs) # Pa gage pressure in bottle
    vw            = Equation1(Pb)        # m/s velocity of water exiting nozzle
    ma            = Equation3MassAir(Va) # kg mass of air 
    m             = mw + mb + ma         # kg total mass of bottle + water + air
    return SumForces(vw, vb, m, Vw)/m

def Equation12(m):
    """ returns the weight due to gravity given:
    m = mass kg"""
    return m*g

def Equation13(Vb):
    """ returns the drag force on the bottle given: 
    Vb = velocity of the bottle m/s"""
    return 0.5*rhoa*Vb**2*Ab*Cd

def Equation14(vw, Vw):
    """ returns the force of thrust given:
    Vw = Volume of water"""
    return -vw*Equation4(vw)

def Equation15(y):
    """ ODE3
    returns the rate of change of height given:
    vb = velocity of bottle in m/s"""
    mw, vb, yb, t = y
    return vb

def SumForces(vw, vb, mb, Vw):
    """ returns the sum of forces given:
    Vw = the Volume of water m^3
    vb = velocity of the bottle m/s
    mb = mass of the bottle kg"""
    # + Thrust - drag - weight
    return Equation14(vw, Vw)-Equation13(vb)-Equation12(mb)

def Area(d):
    """ Returns the circular area given:
    d = diameter"""
    return np.pi/4 * d**2

def Eulers(f, y, tf, h):
    """ 
    f  = list of functions with the form f(y[0], y[1], ... y[n])
    y  = list of initial values y[0] = initial value for first variable
    tf = time final
    h  = step size"""
    plot = []
    for i in np.arange(0, tf+h, h):
        yOld = list(y)
        # y[0] = y[0] + h*f[0](y)
        
        # y = [y + h*func(y) for func in f]
        y = [y[i] + h*f[i](y) for i in range(len(y))]
        plot.append(y)
    return plot

def K1(f, t, x):
    """ Returns the k1 calculations
    f = list of functions
    t = independent variable
    x = list of dependent variables"""
    x.append(t)
    k1 = [func(x) for func in f]
    return k1

def K2(f, t, x, h, K1):
    """ Returns the k2 calculations
    f = list of functions
    t = independent variable
    x = list of dependent variables"""
    T = t + .5*h
    X = [i + .5*h*j for i, j in zip(x, K1)]
    X.append(T)
    K2 = [func(X) for func in f]
    return K2

def K3(f, t, x, h, K2):
    """ Returns the k2 calculations
    f = list of functions
    t = independent variable
    x = list of dependent variables"""
    T = t + .5*h
    X = [i + .5*h*j for i, j in zip(x, K2)]
    X.append(T)
    K3 = [func(X) for func in f]
    return K3

def K4(f, t, x, h, K3):
    """ Returns the k2 calculations
    f = list of functions
    t = independent variable
    x = list of dependent variables"""
    T = t + .5*h
    X = [i + .5*h*j for i, j in zip(x, K3)]
    X.append(T)
    K4 = [func(X) for func in f]
    return K4

def RK4(f, t, x, h):
    """ Solves system of ODEs
    f = list of ODEs
    t = independent variable
    x = list of initial values
    h = step size"""
    k1 = K1(f, t,x)
    k2 = K2(f, t,x , h, k1)
    k3 = K3(f, t,x , h, k2)
    k4 = K4(f, t,x , h, k3)
    xOut = [i + 1/6*(j + 2*k + 2*l + m)*h for i, j, k, l, m in zip(x, k1, k2, k3, k4)]
    return xOut

def bottle_rocket(P_init, vw_init, dn, h, tf=0.03):
    """ Calculates the mass of water, velocity and position
    of a 2 liter bottle rocket
    P_init  = initial pressure of air (psig)
    vw_init = initial volume of water (L)
    dn      = diameter of the nozzle (mm)"""
    global An, P0, Vw0, Va0  # Setting global variables because why not
    P0 = P_init*6895         # Convert from psi to kpa
    P0 += Pa                 # Convert to absolute pa
    An = Area(dn/1000)       # Convert from mm to m
    Vw0 = vw_init*1e-6       # Convert from mL to m^3
    Va0 = Vtot - Vw0         # Setting volume of air
    vb0 = 0                  # Initial velocity of the bottle

    mw0 = Equation3Mass(Vw0) # Getting mass of water given initial volume of water

    plot = []
    x = [mw0, vb0, 0]
    for t in np.arange(0, tf, h):
        row = [t + h]
        x = RK4([Equation2, Equation10, Equation15], t, x, h)
        row.extend(x)
        plot.append(row)
    print(plot[-1][1])
    plots = np.array(plot).T
    print(plots[1])
    # plt.plot(plots[0], plots[1], '-')
    # plt.show()
        

def main():
    bottle_rocket(80, 100, 4.64, 0.001, tf=0.003)
    bottle_rocket(80, 100, 4.64, 0.001, tf=0.180)

main()