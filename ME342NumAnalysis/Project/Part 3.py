import numpy as np
import matplotlib.pyplot as plt
"""Zachary Preator
"""
# Constants/Givens
T     = 280          # Kelvin (temperature in Rexburg)
Pa    = 84800        # Kpa (air pressure in rexburg gage)
R     = 0.287        # Gas constant (Unitless)
g     = 9.81         # m/s^2
D     = 4.2          # in (Diameter of 2 liter bottle)
mb    = 60           # g (mass of empty bottle)
Cd    = 0.6          # Coefficient of drag (Unitless)
rhow  = 998          # kg/m^3 (water density)
Vtot  = 2            # L (2 liter bottle)
An    = 0            # mm Diameter of the nozzle

# Calculations/Conversions
rhoa  = Pa/(R*T)/1000# kg/m^3 (air density in Rexburg)
Vtot /= 1000         # L to m^3 (initial volume of water)
mb   /= 1000         # g to kg (mass of empty bottle)
D    *= 2.54/100     # in to m (Diameter of 2 liter bottle)
Ab    = np.pi*D**2/4 # m^2 (cross sectional area of bottle)

# Initial conditions (Will be set in bottle_rocket())
P0    = 0
Va0   = 0
def Equation1(P):
    """ returns the velocity in m/s given:
    P = pressure in pa"""
    return np.sqrt(2*P/rhow)

def Equation1Pressure(V):
    """ returns the pressure in pa given:
    V = velocity in m/s"""
    return rhow*V**2/2

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
    # global Va0, Pinter
    # Pinter        = PbAbs                # Setting global variable pressure in bottle
    # Va0           = Va                   # Setting global variable volume of air in bottle
    return Equation4(v)

def Equation3Vol(m):
    """ returns the volume of water given:
    m = mass of water in kg"""
    return m/rhow

def Equation3Mass(V):
    """ returns the mass of water given:
    V = volume of water m^3"""
    return rhow*V

def Equation3MassAir(P, Va):
    """ returns the mass of air given:
    V = volume of air m^3"""
    return P*Va/T/R/1000

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
    Vw            = Equation3Vol(mw)            # L Mass of water to volume of water
    Va            = Vtot - Vw                   # L Total volume of bottle - water to get volume of air
    PbAbs         = Equation9(Va, Vw)           # Pa absolute pressure in bottle
    Pb            = Equation6Gage(PbAbs)        # Pa gage pressure in bottle
    vw            = Equation1(Pb)               # m/s velocity of water exiting nozzle
    ma            = Equation3MassAir(PbAbs, Va) # kg mass of air 
    m             = mw + mb + ma                # kg total mass of bottle + water + air
    F             = SumForces(vw, vb, m, Vw)    # Getting net forces acting on bottle
    return F/m

def Equation12(m):
    """ returns the weight due to gravity given:
    m = mass kg"""
    # if m < 0:
    #     return 0
    return m*g

def Equation13(Vb):
    """ returns the drag force on the bottle given: 
    Vb = velocity of the bottle m/s"""
    return 0.5 * rhoa * Vb**2 * Ab * Cd

def Equation14(vw, Vw):
    """ returns the force of thrust given:
    vw = Velocity of water"""
    return -vw*Equation4(vw)

def Equation15(y):
    """ ODE3
    returns the rate of change of height given:
    vb = velocity of bottle in m/s"""
    mw, vb, yb, t = y
    return vb

def GetPressureFromMassW(mw):
    Vw            = Equation3Vol(mw)     # m^3 Volume of water in bottle
    Va            = Vtot-Vw        # m^3 Volume of air in bottle
    PbAbs         = Equation9(Va, Vw)    # Pa absolute pressure in bottle
    return PbAbs

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

def UpdateValues(x):
    mw, vb, yb = x
    global P0, Va0
    Vw            = Equation3Vol(mw)     # m^3 Volume of water in bottle
    Va            = Vtot-Vw              # m^3 Volume of air in bottle
    P0            = Equation9(Va, Vw)    # Pa absolute pressure in bottle for next time step
    Va0           = Va                   # Setting global variable Volume of air for next time step

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
    T = t + h
    X = [i + h*j for i, j in zip(x, K3)]
    X.append(T)
    K4 = [func(X) for func in f]
    return K4

def RK4(f, t, y, h):
    """ Solves system of ODEs
    f = list of ODEs
    t = independent variable
    x = list of initial values
    h = step size"""
    x = list(y) # I didn't want y to change everytime this was run (Pointer issue)
    k1 = K1(f, t,x)
    k2 = K2(f, t,x , h, k1)
    k3 = K3(f, t,x , h, k2)
    k4 = K4(f, t,x , h, k3)
    xOut = [i + 1/6*(j + 2*k + 2*l + m)*h for i, j, k, l, m in zip(x, k1, k2, k3, k4)]
    # UpdateValues(y)
    return xOut

def Display(data, lineType, label='', done = True, xLabel=None, yLabel=None, plotLabel=None, f=None, log=False, save=True, show=False):
    """ Displays data as [x, y]"""
    t = np.arange(0, 4, 0.01)
    
    plt.plot(data[0], data[1], lineType, label=label)
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
        if save:
            plt.savefig('{0}.pdf'.format(label))
        if show:
            plt.show()

def bottle_rocket(P_init, vw_init, dn, h, tf=0.03):
    """ Calculates the mass of water, velocity and position
    of a 2 liter bottle rocket
    P_init  = initial pressure of air (psig)
    vw_init = initial volume of water (L)
    dn      = diameter of the nozzle (mm)"""
    global An, P0, Va0       # Setting global variables because why not
    P0 = P_init*6895         # Convert from psi to kpa
    P0 += Pa                 # Convert to absolute pa
    An = Area(dn/1000)       # Convert from mm to m
    Vw0 = vw_init*1e-6       # Convert from mL to m^3
    Va0 = Vtot - Vw0         # Setting volume of air
    # vb0 = Equation1(P0)    # Initial velocity of the bottle
    vb0 = 0

    mw0 = Equation3Mass(Vw0) # Getting mass of water given initial volume of water

    plot = []
    x = [mw0, vb0, 0]
    plot.append([0, mw0, vb0, 0, P0])
    t_list = [0]
    for t in np.arange(h, tf+h, h):
        row = [t]
        x = RK4([Equation2, Equation10, Equation15], t_list[-1], x, h)
        UpdateValues(x)
        row.extend(x)
        row.extend([P0])
        plot.append(row)
        t_list.append(t_list[-1]+h)
    guess = RK4([Equation2, Equation10, Equation15], tf, x, h)
    dtf = (x[0] - 0)/(x[0]-guess[0])*h
    x = RK4([Equation2, Equation10, Equation15], tf, x, dtf)
    UpdateValues(x)
    row = [tf + dtf]
    row.extend(x)
    row.extend([P0])
    plot.append(row)

    # Extracting all lists of items at each time step
    t  = [plot[i][0]      for i in range(len(plot))] # Time at each step
    mw = [plot[i][1]      for i in range(len(plot))] # Mass of water
    vb = [plot[i][2]      for i in range(len(plot))] # Velocity of bottle
    y  = [plot[i][3]      for i in range(len(plot))] # Distance y
    P  = [plot[i][4]      for i in range(len(plot))] # Pressure in bottle

    # Calculations to get various values in list form at each time step
    Vw = [Equation3Vol(plot[i][1]) for i in range(len(plot))]         # Volume of water
    Va = [Vtot - i for i in Vw]                                       # Volume of air
    ma = [Equation3MassAir(i, j) for i, j in zip(P, Va)]              # Mass of air
    vw = [Equation1(i-Pa) for i in P]                                 # Velocity of water
    m  = [mb + i + j for i, j in zip(mw, ma)]                         # Total mass of all components
    Th = [Equation14(i, j) for i, j in zip(vw, Vw)]                   # Thrust on bottle
    Df = [Equation13(i) for i in vb]                                  # Drag force on bottle
    F  = [SumForces(i, j, k, l) for i, j, k, l in zip(vw, vb, m, Vw)] # Sum of forces
    ab = np.diff(vb)/np.diff(t)                                       # Acceleration of bottle

    


    # Values at t = 0.003
    i = 3
    print('t   = {0:4.8f} s  '.format(t [i]))
    print('m_w = {0:4.8f} kg '.format(mw[i]))
    print('vb  = {0:4.8f} m/s'.format(vb[i]))
    print('Df  = {0:4.8f} N  '.format(Df[i]))
    print('Y   = {0:4.8f} mm '.format(y [i]))
    print('Th  = {0:4.8f} N  '.format(Th[i]))
    print('When Water is Gone:')
    print('t   = {0:4.8f} s  '.format(t [-1]))
    print('m_w = {0:4.8f} kg '.format(mw[-1]))
    print('vb  = {0:4.8f} m/s'.format(vb[-1]))
    print('Y   = {0:4.8f} m  '.format(y [-1]/1000))

    
    plt.figure(figsize=(5,3)) 
    Display([t, P ], '-', label='Pressure in bottle',       xLabel='Time (s)', yLabel=r'Pressure $(Kpa)$')
    plt.figure(figsize=(5,3)) 
    Display([t, Th], '-', label='Volume of water',       xLabel='Time (s)', yLabel=r'Volume $(m^3)$')
    plt.figure(figsize=(5,3)) 
    Display([t, Vw], '-', label='Velocity of water',       xLabel='Time (s)', yLabel=r'Velocity $(m/s)$')
    plt.figure(figsize=(5,3)) 
    Display([t, Th], '-', label='Thrust on Bottle',       xLabel='Time (s)', yLabel=r'Thrust $(N)$')
    plt.figure(figsize=(5,3)) 
    Display([t, Df], '-', label='Drag Force on Bottle',   xLabel='Time (s)', yLabel=r'Drag Force $(N)$')
    plt.figure(figsize=(5,3)) 
    Display([t, vb], '-', label='Velocity of Bottle',     xLabel='Time (s)', yLabel=r'Velocity $(m/s)$')
    plt.figure(figsize=(5,3)) 
    Display([t, y ],  '-', label='Altitude of Bottle',     xLabel='Time (s)', yLabel=r'Altitude $(m)$')

    plt.figure(figsize=(5, 3))
    del t[-1] # This must be done..
    Display([t, ab], '-', label='Acceleration of Bottle', xLabel='Time (s)', yLabel=r'Acceleration $(m/s^2)$')  

def main():
    # bottle_rocket(80, 100, 4.64, 0.001, tf=0.003)
    bottle_rocket(80, 100, 4.64, 0.001, tf=0.180)

main()