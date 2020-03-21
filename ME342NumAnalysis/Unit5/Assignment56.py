import numpy as np
import matplotlib.pyplot as plt
L = 0.15 # Fin length
Tb = 500 # Base temperature K
k = 16.0 # Thermal conductivity W/mK
Ac = 1.67e-4 # Cross sectional area m^2
P = 0.066 # Perimeter length m
Tf = 300 # Free stream temperature K
h = 25 # Heat transfer coefficient W/m^2
TL = 350 # Fixed tip temperature K
dx = 0.03 # Step size

def dTdUdx(x, var):
    """ ODE represented as two first order ODEs"""
    T = var[0]
    U = var[1]
    dTdx = U
    dUdx = h*P/k/Ac*(T-Tf)
    return np.array([dTdx,dUdx])
    

def RK4(f,t0,y0,tf,h):
    """ Runge-Kutta method"""
    t = np.arange(t0,tf+h,h)
    n = len(t)
    m = len(y0)
    y = np.zeros([n,m])
    y[0] = y0
    
    for i in range(n-1):
        k1 = f(t[i],y[i])
        k2 = f(t[i]+.5*h,y[i]+k1*.5*h)
        k3 = f(t[i]+.5*h,y[i]+k2*.5*h) 
        k4 = f(t[i]+h,y[i]+k3*h)
        y[i+1] = y[i] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        
    return t, y.transpose()

def FuncTempFixedT(x):
    """ Function for temperature with fixed temperature TL"""
    m = np.sqrt(h*P/(k*Ac))

    #Finding the constants thetaL an thetab
    thL = TL-Tf
    thb = Tb-Tf
    return thL*np.sinh(m*x)/np.sinh(m*L)+thb*np.sinh(m*(L-x))/np.sinh(m*L) + Tf

def FuncGradientFixedT(x):
    """ Function for temperature gradient"""
    m = np.sqrt(h*P/(k*Ac))
    thL = TL-Tf
    thb = Tb-Tf
    return m*thL*np.cosh(m*x)/np.sinh(m*L)-m*thb*np.cosh(m*(L-x))/np.sinh(m*L)

def FuncTempAdiabatic(x):
    m = np.sqrt(h*P/(k*Ac))
    thb = Tb-Tf
    return thb*(np.cosh(m*(L-x))/(np.cosh(m*L)))+Tf

def FuncGradientAdiabatic(x):
    m = np.sqrt(h*P/(k*Ac))
    thb = Tb-Tf
    return k*Ac*m*thb*(np.sinh(m*(L-x))/(np.cosh(m*L)))

# def Display(x, qa, Ta, x3, var3):
#     plt.plot(x, qa, '-',label='Analytical')
#     plt.plot(x3,-k*Ac*var3[1], '--', label='Numerical')
#     plt.legend()
#     plt.title('q(x)')
#     plt.xlabel('Position')
#     plt.ylabel('Q')
#     # plt.savefig('q.pdf')

#     plt.plot(x, Ta, '-',label='Analytical')
#     plt.plot(x3,var3[0], '--', label='Numerical')
#     plt.legend()
#     plt.title('T(x)')
#     plt.xlabel('Position')
#     plt.ylabel('Temp')
#     plt.show()
#     # plt.savefig('T.pdf')

def Display(data, lineType, label='', done = False, xLabel=None, yLabel=None, plotLabel=None, f=None, log=False):
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
        plt.savefig('{0}.pdf'.format(plotLabel))
        plt.show()

def ShootingMethod(guess1, guess2, desiredVal, der):
    """ Performs the shooting method with runge-kutta.
    desiredVal = value to shoot for
    der = order of the dependent variable sought
    FOR EXAMPLE: To find what input guess for T' will
    give a value of T = TL, then my input would be:
    ShootingMethod(guess1, guess2, TL, 1). If I wanted
    to get the value of T' = 0 then: ShootingMethod(.., 0, 2)"""
    i = der - 1
    x1, var1 = RK4(dTdUdx, 0, [Tb,guess1], L, dx)
    x2, var2 = RK4(dTdUdx, 0, [Tb,guess2], L, dx)
    guess3 = (desiredVal-var1[i,-1])/(var2[i,-1]-var1[i,-1])*(guess2-guess1) + guess1
    x3, var3 = RK4(dTdUdx, 0, [Tb, guess3], L, dx)
    return x3, var3, guess3

def main():
    tFixedT, valFixedT, guessFixedT = ShootingMethod(0, -1000, TL, 1) # We want the Temperature to be TL @ L
    tAdiabatic, valAdiabatic, guessAdiabatic = ShootingMethod(0, -1000, 0, 2) # We want the derivative to be 0 @ L
    print('2.')
    print('  (a) @ x = 0, T\' = {0:5.4f} @ x = {1:4.2f}, T = {2:5.4f}'.format(guessFixedT, L, valFixedT[0][-1]))
    print('  (b) @ x = 0, T\' = {0:5.4f} @ x = {1:4.2f}, T\' = {2:5.4f}'.format(guessAdiabatic, L, valAdiabatic[1][-1]))

    x = np.arange(0,L,0.0001)
    q = FuncGradientFixedT(x)
    T = FuncTempFixedT(x)
    qa = FuncGradientAdiabatic(x)
    Ta = FuncTempAdiabatic(x)
    # Display(x, qa, Ta, x3, var3)

    # Plot of temperature using fixed temperature guess
    plt.figure(figsize=(5, 3))
    Display([x, T], '-', label='Analytical') 
    Display([tFixedT, valFixedT[0]], '--', label='Numerical', done=True, xLabel='Position', yLabel='Temperature', plotLabel='Temperature(x)')

    # Plot of temp gradient using fixed temperature guess
    plt.figure(figsize=(5, 3))
    Display([x, q], '-', label='Analytical')
    Display([tFixedT, valFixedT[1]], '--', label='Numerical', done=True, xLabel='Position', yLabel='Temperature', plotLabel='Temp Gradient(x)')

    # Plot of temperature using adiabatic guess
    plt.figure(figsize=(5, 3))
    Display([x, Ta], '-', label='Analytical') 
    Display([tFixedT, valFixedT[0]], '--', label='Numerical', done=True, xLabel='Position', yLabel='Temperature', plotLabel='Temperature(x)')

    # Plot of temp gradient using adiabatic guess
    plt.figure(figsize=(5, 3))
    Display([x, qa], '-', label='Analytical') 
    Display([tFixedT, valFixedT[0]], '--', label='Numerical', done=True, xLabel='Position', yLabel='Temperature', plotLabel='Temp Gradient(x)')

    # q3a = FuncGradientAdiabatic(x3a)
    # T3= FuncTempAdiabatic(x3a)
    # errq = abs((q3a+k*Ac*var3a[1])/q3a)
    # errT = abs((T3-var3a[0])/T3)
    # print(errT)
    # print(errq)

    # q3b = FuncGradientAdiabatic(x3b)
    # T3b = FuncTempAdiabatic(x3b)
    # errq = abs((q3b+k*Ac*var3b[0])/q3b)
    # errT = abs((T3b-var3b[0])/T3b)
    # print(errT)
    # print(errq)


main()
