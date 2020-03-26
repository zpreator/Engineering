from ZachsPackage import Fluids
import numpy as np

def Problem1():
    #Givens
    D1 = 3.068/12 #in to ft
    D2 = 1.610/12 #in to ft
    Vin = 3.4 #ft/s
    L1 = 78 #ft
    L2 = 10 #ft

    #Constants
    nu = 1.081e-5

    #Calculations
    #******************************************
    Vout = Vin*D1**2/D2**2
    
    Re1 = Fluids.ReynoldsNumber(Vin, D1, nu)
    Re2 = Fluids.ReynoldsNumber(Vout, D2, nu)
    print('Look up f in moody chart using Re1 and Re2: ', Re1, Re2)

    #From moody chart
    f1 = Fluids.HallandFriction(0, D1, Re1)
    f2 = Fluids.HallandFriction(0, D2, Re2)

    h1 = Fluids.HeadLoss(f1, L1, D1, 0, Vin)
    h2 = Fluids.HeadLoss(f2, L2, D2, 0, Vout)

    headLoss = h1 + h2
    fraction = h2/headLoss
    print('Headloss =', headLoss)
    print('Fraction h1/htotal =', fraction)

def func1(f, L, D, sumK, rho, vDot):
    return (f*L/D + sumK)*rho*8*vDot**2/(np.pi**2*D**4)

def Problem2():
    #Given
    L = 57 #m
    D = 4.75/100 #cm to m
    z = 17 #m

    #Constants
    epsilon = 0.15/1000 #mm to m (Surface roughness for galvanized iron)
    k = [] #minor losses
    k.append(0.5) #Sharp edge
    k.append(3*0.9) #3 threaded 90 degree elbows (0.9 loss)
    k.append(10) #Fully open globe valve
    nu = 1.004E-6 #m^2/s
    rho = 998 #kg/m^3
    
    #Calculations
    vdot = 0.01 #m^3/s initial guess
    Re = Fluids.ReynoldsNumber2(vdot, D, nu)
    print(Re)
    f = Fluids.HallandFriction(epsilon, D, Re)
    print(f)
    P1 = func1(f, L, D, sum(k), rho, vdot)
    print(P1)

def Problem3():
    vDot = 5/449 # gpm to ft^3/s
    L = 108 # ft
    g = 32.174 # ft/s^2
    nu = 1.081E-5 # ft^2/s
    epsilon = 0.00015 # ft
    Pmax = 32*144 # psi to lb/ft^2
    gamma = 62.3 # lbf/ft^3

    dx = 0.0001

    D = .25/12 # in to ft
    e = 1
    while e > 1E-2:
        Dold = D
        Re = Fluids.ReynoldsNumber2(vDot, D, nu)
        f = Fluids.HallandFriction(epsilon, D, Re)
        P = (f*L/D)*8*gamma*vDot**2/(np.pi**2*g*D**4)
        print('Diameter = ', D*12)
        print('Pressure = ', P/144)
        if P > Pmax:
            D += dx
        else:
            D -= dx
        e = abs(Pmax - P)/P

    D = 0.622/12 #schedule 40 1/8 in nominal size (Problem 3)
    Re = Fluids.ReynoldsNumber2(vDot, D, nu)
    f = Fluids.HallandFriction(epsilon, D, Re)
    P = f*L*8*gamma*vDot**2/(D*np.pi**2*g*D**4)
    print(P/144)
    
def Problem4():
    vDot = 5/449 # gpm to ft^3/s
    L = 108 # ft
    g = 32.174 # ft/s^2
    nu = 1.081E-5 # ft^2/s
    epsilon = 0.00015 # ft
    Pmax = 32*144 # psi to lb/ft^2
    gamma = 62.3 # lbf/ft^3

    dx = 0.0001

    #Minor losses (Problem 4)
    k = []
    k.append(10) # Fully open globe valve
    k.append(7*0.9) # Threaded Smooth 90 bends (qty 7)

    D = .25/12 # in to ft
    e = 1
    while e > 1E-2:
        Dold = D
        Re = Fluids.ReynoldsNumber2(vDot, D, nu)
        f = Fluids.HallandFriction(epsilon, D, Re)
        P = (f*L/D + sum(k))*8*gamma*vDot**2/(np.pi**2*g*D**4)
        print('Diameter = ', D*12)
        print('Pressure = ', P/144)
        if P > Pmax:
            D += dx
        else:
            D -= dx
        e = abs(Pmax - P)/P

    D = 0.622/12 #schedule 40 1/8 in nominal size (Problem 3)
    Re = Fluids.ReynoldsNumber2(vDot, D, nu)
    f = Fluids.HallandFriction(epsilon, D, Re)
    P = (f*L/D + sum(k))*8*gamma*vDot**2/(np.pi**2*g*D**4)
    print(P/144)

def Test():
    vDot = 5/449 # gpm to ft^3/s
    L = 108 # ft
    g = 32.174 # ft/s^2
    nu = 1.081E-5 # ft^2/s
    epsilon = 0.00015 # ft
    Pmax = 32*144 # psi to lb/ft^2
    gamma = 62.3 # lbf/ft^3

    dx = 0.0001

    #Minor losses (Problem 4)
    k = []
    k.append(10) # Fully open globe valve
    k.append(7*0.9) # Threaded Smooth 90 bends (qty 7)

    D = .25/12 # in to ft
    e = 1
    while e > 1E-2:
        Dold = D
        Re = Fluids.ReynoldsNumber2(vDot, D, nu)
        f = Fluids.HallandFriction(epsilon, D, Re)
        P = (f*L/D + sum(k))*8*gamma*vDot**2/(np.pi**2*g*D**4)
        print('Diameter = ', D*12)
        print('Pressure = ', P/144)
        if P > Pmax:
            D += dx
        else:
            D -= dx
        e = abs(Pmax - P)/P

    D = 0.622/12 #schedule 40 1/8 in nominal size (Problem 3)
    Re = Fluids.ReynoldsNumber2(vDot, D, nu)
    f = Fluids.HallandFriction(epsilon, D, Re)
    P = (f*L/D + sum(k))*8*gamma*vDot**2/(np.pi**2*g*D**4)
    print(P/144)

Problem1()