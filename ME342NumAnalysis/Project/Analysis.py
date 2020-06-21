import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import optimize
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
    if P == Pa:
        return 0
    else:
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
    if mw == 0:
        return 0
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
    if mw != 0:
        Vw            = Equation3Vol(mw)            # L Mass of water to volume of water
        Va            = Vtot - Vw                   # L Total volume of bottle - water to get volume of air
        PbAbs         = Equation9(Va, Vw)           # Pa absolute pressure in bottle
        Pb            = Equation6Gage(PbAbs)        # Pa gage pressure in bottle
        vw            = Equation1(Pb)               # m/s velocity of water exiting nozzle
        ma            = Equation3MassAir(PbAbs, Va) # kg mass of air 
        m             = mw + mb + ma                # kg total mass of bottle + water + air
        F             = SumForces(vw, vb, m, Vw)    # Getting net forces acting on bottle
        return F/m
    else: #No thrust force, air mass is 0, only weight and drag
        Vw = 0
        Va = Vtot
        PbAbs = Equation9(Va, Vw)
        Pb = Equation6Gage(PbAbs)
        vw = 0
        ma = Equation3MassAir(Pa, Va)
        m = mb + ma
        F = SumForces(vw, vb, m, Vw)
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
    return 0.5 * rhoa * Vb**2 * Ab * Cd*np.sign(Vb)

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
    if mw == 0:
        P0            = 0
        Va0           = Vtot
    else:
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

def Display(data, lineType, label='', done = True, xLabel=None, yLabel=None, plotLabel=None, f=None, log=False, save=True, show=True):
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

def bottle_rocket(P_init, vw_init, dn, h, tf=0.03, showPlot=True):
    """ Calculates the mass of water, velocity and position
    of a 2 liter bottle rocket
    P_init  = initial pressure of air (psig)
    vw_init = initial volume of water (L)
    dn      = diameter of the nozzle (mm)
    h       = time increment (accuracy)
    tf      = final time desired, put None if full path is desired
    showPlot= True shows all plots, False will not"""
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
    mdot_list = []
    waterExausted = False
    te = 0
    ye = 0
    if tf != None:
        for t in np.arange(h, tf+h, h):
            row = [t]
            var = list(x)
            mdot_list.append(Equation2(var.extend([1])))
            x = RK4([Equation2, Equation10, Equation15], t_list[-1], x, h)
            UpdateValues(x)
            row.extend(x)
            row.extend([P0])
            plot.append(row)
            t_list.append(t_list[-1]+h)
    else:
        while x[2] + x[1]*h > 0 or t_list[-1] == 0:
            row = [t_list[-1]+h]
            var = list(x)
            var.append(0)
            mdot_list.append(Equation2(var))
            x = RK4([Equation2, Equation10, Equation15], t_list[-1], x, h)
            UpdateValues(x)
            row.extend(x)
            row.extend([P0])
            plot.append(row)
            t_list.append(t_list[-1]+h)
            if x[0]-(plot[-2][1]-plot[-1][1]) < 0 and not waterExausted: # Runs once to interpolate and append the values when the water runs out
                te = t_list[-1] # This will get the time just before the water runs out
                waterExausted = True
                guess = RK4([Equation2, Equation10, Equation15], te, x, h)
                dtf = (x[0] - 0)/(x[0]-guess[0])*h
                x = RK4([Equation2, Equation10, Equation15], te, x, dtf)
                UpdateValues(x)
                te = te + dtf
                ye = x[2]
                row = [t_list[-1]+dtf]
                row.extend(x)
                row.extend([P0])
                plot.append(row)
                t_list.append(t_list[-1]+dtf)
                x[0] = 0
    # This will interpolate the last value run in the loop
    guess = RK4([Equation2, Equation10, Equation15], t_list[-1], x, h)
    dtf = abs((x[2] - 0)/(x[2]-guess[2])*h)
    x = RK4([Equation2, Equation10, Equation15], t_list[-1], x, dtf)
    UpdateValues(x)
    row = [t_list[-1] + dtf]
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
    ma = [Equation3MassAir(i+Pa, j) for i, j in zip(P, Va)]              # Mass of air
    vw = [Equation1(i+Pa) for i in P]                                 # Velocity of water
    m  = [mb + i + j for i, j in zip(mw, ma)]                         # Total mass of all components
    Th = [Equation14(i, j) for i, j in zip(vw, Vw)]                   # Thrust on bottle
    Df = [Equation13(i) for i in vb]                                  # Drag force on bottle
    F  = [SumForces(i, j, k, l) for i, j, k, l in zip(vw, vb, m, Vw)] # Sum of forces
    ab = np.diff(vb)/np.diff(t)                                       # Acceleration of bottle

    


    # Values at t = 0.003
    i = 3
    # print('At t            = 0.003 s:')
    # # print('t   = {0:4.8f} s  '.format(t [i]))
    # print('Mass of Water   = {0:4.8f} kg  '.format(mw[i]))
    # print('Bottle Velocity = {0:4.8f} m/s '.format(vb[i]))
    # print('Drag Force      = {0:4.8f} N   '.format(Df[i]))
    # print('Altitude        = {0:4.8f} mm  '.format(y [i]))
    # print('Thrust          = {0:4.8f} N \n'.format(Th[i]))

    # print('Water Runs out  = {0:4.8f} s   '.format(te))
    # print('Altitude        = {0:4.8f} m \n'.format(ye))

    # print('Max Velocity    = {0:4.8f} m/s '.format(max(vb)))
    # print('Max Altitude    = {0:4.8f} m   '.format(max(y)))
    # print('Time at Max Alt = {0:4.8f} s \n'.format(t[np.argmax(y)]))
    # print('End of Flight:')
    # j = -1
    # print('Impact Time     = {0:4.8f} s  '.format(t [j]))
    # # print('Mass of Water   = {0:4.8f} kg '.format(mw[j]))
    # print('Bottle Velocity = {0:4.8f} m/s'.format(vb[j]))
    # # print('Altitude        = {0:4.8f} m  '.format(y [j]))

    # print('Integrated mass flow rate= ', -np.trapz(mdot_list)/1000)
    # print('Beginning mass of water= ', mw0)

    # maxIndex = np.argmax(y)
    # ascent = vb[0:maxIndex]
    # descent = vb[maxIndex:-1]
    # int1 = np.trapz(ascent, dx=h)
    # int2 = -np.trapz(descent, dx=h)
    # dist = int1+int2
    # print('Integrated velocity= ', dist)
    # print('Total distance traveled= ', max(y)*2)

    intMass = -np.trapz(mdot_list)/1000
    print('Integrated mass flow rate = {0:4.5f} kg  '.format(intMass))
    print('Beginning mass of water =   {0:4.5f} kg  '.format(mw0))
    e = abs(mw0 - intMass)/mw0*100
    print('Absolute error = {0:4.5f} %  '.format(e))

    maxIndex = np.argmax(y)
    ascent = vb[0:maxIndex]
    descent = vb[maxIndex:-1]
    int1 = np.trapz(ascent, dx=h)
    int2 = -np.trapz(descent, dx=h)
    dist = int1+int2
    print('Integrated velocity =     {0:4.5f} m  '.format(dist))
    print('Total distance traveled = {0:4.5f} m  '.format(max(y)*2))
    e = abs(dist - max(y)*2)/dist*100
    print('Absolute error = {0:4.5f} %  '.format(e))

    if showPlot:
        plt.figure(figsize=(5,3)) 
        Display([t, P ], 'b-', label='Pressure in bottle',       xLabel='Time (s)', yLabel=r'Pressure $(Kpa)$')
        plt.figure(figsize=(5,3)) 
        Display([t, Th], 'g-', label='Volume of water',       xLabel='Time (s)', yLabel=r'Volume $(m^3)$')
        plt.figure(figsize=(5,3)) 
        Display([t, vw], 'r-', label='Velocity of water',       xLabel='Time (s)', yLabel=r'Velocity $(m/s)$')
        plt.figure(figsize=(5,3)) 
        Display([t, Th], 'c-', label='Thrust on Bottle',       xLabel='Time (s)', yLabel=r'Thrust $(N)$')
        plt.figure(figsize=(5,3)) 
        Display([t, Df], 'm-', label='Drag Force on Bottle',   xLabel='Time (s)', yLabel=r'Drag Force $(N)$')
        plt.figure(figsize=(5,3)) 
        Display([t, vb], 'y-', label='Velocity of Bottle',     xLabel='Time (s)', yLabel=r'Velocity $(m/s)$')
        plt.figure(figsize=(5,3)) 
        Display([t, y ],  'k-', label='Altitude of Bottle',     xLabel='Time (s)', yLabel=r'Altitude $(m)$')

        plt.figure(figsize=(5, 3))
        tnew = [t[i] for i in range(len(t)-2)]
        acc = [ab[i] for i in range(len(ab)-1)]
        Display([tnew, acc], 'b-', label='Acceleration of Bottle', xLabel='Time (s)', yLabel=r'Acceleration $(m/s^2)$')
    return max(y)

# # for changing pressure
# press = [i for i in range(60, 160, 10)]
# altPress = [bottle_rocket(i, 100, 4.64, 0.001, tf=None, showPlot=False) for i in press]

# # changing water volume
# vol = [i for i in range(100, 1300, 100)]
# altvol = [bottle_rocket(80, i, 4.64, 0.001, tf=None, showPlot=False) for i in vol]

# # changing diameter
# dia = [i for i in np.arange(1.5, 6.5, 0.5)]
# altDia = [bottle_rocket(80, 100, i, 0.001, tf=None, showPlot=False) for i in dia]

print(bottle_rocket(150, 900, 3, 0.001, tf=None, showPlot=False))

# def func(x, a, b, c, d):
#     return a + b*x + c*x**2 + d*x**3

# def func2(x, a, b, c, d, e, f, g):
#     return a + b*x + c*x**2 + d*x**3 + e*x**4 + f*x**5 + g*x**6

# plt.figure(figsize=(5,3))
# p = np.arange(press[0], press[-1]+.1, 0.1)
# plt.plot(press, altPress, 'ro--', label='Pressure')
# popt, pcov = optimize.curve_fit(func, press, altPress)
# plt.plot(p, func(p, *popt), 'c-', label='Curve Fit')
# plt.xlabel(r'Pressure $(psi)$')
# plt.ylabel(r'Altitude $(m)$')
# plt.legend()
# plt.tight_layout()
# plt.savefig('PressureParam.pdf')
# plt.show()

# plt.figure(figsize=(5,3))
# v = np.arange(vol[0], vol[-1]+.1, 0.1)
# plt.plot(vol, altvol, 'yo--', label='Volume')
# popt, pcov = optimize.curve_fit(func, vol, altvol)
# plt.plot(v, func(v, *popt), 'c-', label='Curve Fit')
# plt.xlabel(r'Volume $(mL)$')
# plt.ylabel(r'Altitude $(m)$')
# plt.legend()
# plt.tight_layout()
# plt.savefig('VolumeParam.pdf')
# plt.show()

# plt.figure(figsize=(5,3))
# d = np.arange(dia[0], dia[-1]+.1, 0.1)
# plt.plot(dia, altDia, 'go--', label='Diameter')
# popt, pcov = optimize.curve_fit(func2, dia, altDia)
# plt.plot(d, func2(d, *popt), 'c-', label='Curve Fit')
# plt.xlabel(r'Nozzle Diameter $(mm)$')
# plt.ylabel(r'Altitude $(m)$')
# plt.legend()
# plt.tight_layout()
# plt.savefig('DiameterParam.pdf')
# plt.show()