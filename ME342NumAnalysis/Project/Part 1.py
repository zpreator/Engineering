import numpy as np
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
rhoa  = Pa/(R*T)     # kg/m^3 (air density in Rexburg)
Ab    = np.pi*D**2/4 # m^2 (cross sectional area of bottle)
Vtot /= 1000         # L to m^3 (initial volume of water)
mb   /= 1000         # g to kg (mass of empty bottle)
D    /= 39.37        # in to m (Diameter of 2 liter bottle)

# Initial conditions (Will be set in bottle_rocket())
P0    = 0
An    = 0
Vw0   = 0

def Equation1(P):
    """ returns the velocity in m/s given:
    P = pressure in pa"""
    return np.sqrt(2*P/rhow)

def Equation2(y):
    """ ODE1
    returns the rate of change of mass of water given: 
    mw = mass of water in the bottle
    (Each ODE takes all three parameters mw, vb, and yb)"""
    mw, vb, yb = y
    volWater   = Equation3Vol(mw)     # m^3 Volume of water in bottle
    volAir     = Vtot-volWater        # m^3 Volume of air in bottle
    PbAbs      = Equation9(volAir)    # Pa absolute pressure in bottle
    Pb         = Equation6Gage(PbAbs) # Pa gage pressure in bottle
    v          = Equation1(Pb)        # m/s velocity of water exiting nozzle
    return Equation4(v)

def Equation3Vol(m):
    """ returns the volume of water given:
    m = mass of water in kg"""
    return m/rhow

def Equation3Mass(V):
    """ returns the mass of water given:
    V = volume of water m^3"""
    return rhow*V

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
    
def Equation9(Va):
    """ returns the pressure in the bottle at the next time step"""
    return P0*(Vtot - Vw0)/Va



def Equation10(y):
    """ ODE2
    returns the rate of change of the velocity of the bottle given:
    mw = mass of water in bottle
    vb = velocity of bottle
    (Each ODE takes all three parameters mw, vb, and yb)"""
    mw, vb, yb = y
    Vw = Equation3Vol(mw)  # L Mass of water to volume of water
    Va = Vtot - Vw         # L Total volume of bottle - water to get volume of air
    ma = Equation3Mass(Va) # kg mass of air 
    m = mw + mb + ma       # kg total mass of bottle + water + air
    return SumForces(Vw, vb, m)/m

def Equation12(m):
    """ returns the weight due to gravity given:
    m = mass kg"""
    return m*g

def Equation13(Vb):
    """ returns the drag force on the bottle given: 
    Vb = velocity of the bottle m/s"""
    return 0.5*rhoa*Vb**2*Ab*Cd

def Equation14(Vw):
    """ returns the force of thrust given:
    Vw = Volume of water"""
    return Vw*Equation4(Vw)

def Equation15(y):
    """ ODE3
    returns the rate of change of height given:
    vb = velocity of bottle in m/s"""
    mw, vb, yb = y
    return vb

def SumForces(Vw, vb, mb):
    """ returns the sum of forces given:
    Vw = the Volume of water m^3
    vb = velocity of the bottle m/s
    mb = mass of the bottle kg"""
    # + Thrust - drag - weight
    return Equation14(Vw)-Equation13(vb)-Equation12(mb)

def Area(d):
    """ Returns the circular area given:
    d = diameter"""
    return np.pi/4 * d**2

def Eulers(f, y, tf, h):
    """ f = list of functions with the form f(y[0], y[1], ... y[n])
        y = list of initial values y[0] = initial value for first variable
        tf = time final
        h = step size"""
    plot = []
    for i in np.arange(0, tf+h, h):
        yOld = list(y)
        # y[0] = y[0] + h*f[0](y)
        
        # y = [y + h*func(y) for func in f]
        y = [y[i] + h*f[i](y) for i in range(len(y))]
        plot.append(y)
    return plot

def bottle_rocket(P_init, vw_init, dn, h, tf=0.03, mode='RK4'):
    """ Calculates the mass of water, velocity and position
    of a 2 liter bottle rocket
    P_init = initial pressure of air (psig)
    vw_init = initial volume of water (L)
    dn = diameter of the nozzle (mm)"""
    global An, P0, Vw0       # Setting global variables because why not
    P0 = P_init*6895         # Convert from psi to kpa
    P0 += Pa                 # Convert to absolute pa
    An = Area(dn/1000)       # Convert from mm to m
    Vw0 = vw_init*1e-6       # Convert from mL to m^3
    vb0 = 0                  # Initial velocity of the bottle

    mw0 = Equation3Mass(Vw0) # Getting mass of water given initial volume of water

    if mode == 'eulers':
        plot = Eulers([Equation2, Equation10, Equation15], [mw0, vb0, 0], tf, h)
        print(plot[2][0])
    elif mode == 'RK4':
        

def main():
    # Part 1
    bottle_rocket(80, 100, 4.64, 0.001, tf=0.003, mode='eulers')
    bottle_rocket(80, 100, 4.64, 0.01, mode='eulers')

    # Part 2
    bottle_rocket(80, 100, 4.64, 0.001, tf=0.003)
    bottle_rocket(80, 100, 4.64, 0.01)

main()