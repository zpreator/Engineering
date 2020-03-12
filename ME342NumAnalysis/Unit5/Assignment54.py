import numpy as np
import matplotlib.pyplot as plt
"""
Zachary Preator
Accuracy 4/4
Plots 2/2
Tables 1/1
Code Quality 3/3
"""
functionx = lambda x, y, t: -0.5 * x + y * t

functiony = lambda x, y, t: 4 - 0.1 * x - 0.2 * y

def Eulers(f, t, x, y, h, Mode='x'):
    """ Returns the Euler's method for the ODE f"""
    if Mode == 'x':
        return x + f(x, y, t)*h
    else:
        return y + f(x, y, t)*h

def K1(f1, f2, t, x, y, h):
    """ Returns the k1 calculations"""
    return f1(x, y, t), f2(x, y, t)

def K2(f1, f2, t, x, y, h, K1x, K1y):
    """ Returns the k2 calculations"""
    T = t + .5*h
    X = x + .5*h*K1x
    Y = y + .5*h*K1y
    return f1(X, Y, T), f2(X, Y, T)

def K3(f1, f2, t, x, y, h, K2x, K2y):
    """ Returns the k3 calculations"""
    T = t + .5*h
    X = x + .5*h*K2x
    Y = y + .5*h*K2y
    return f1(X, Y, T), f2(X, Y, T)

def K4(f1, f2, t, x, y, h, K3x, K3y):
    """ Returns the k4 calculations"""
    T = t + h
    X = x + h*K3x
    Y = y + h*K3y
    return f1(X, Y, T), f2(X, Y, T)


def RK4(f1, f2, t, x, y, h):
    """ Calls the k functions and calculates the
    next y (y+1) and returns that y for an ODE f"""
    
    k1x, k1y = K1(f1, f2, t, x, y, h)
    k2x, k2y = K2(f1, f2, t, x, y, h, k1x, k1y)
    k3x, k3y = K3(f1, f2, t, x, y, h, k2x, k2y)
    k4x, k4y = K4(f1, f2, t, x, y, h, k3x, k3y)
    xOut = x + 1/6*(k1x + 2*k2x + 2*k3x + k4x)*h
    yOut = y + 1/6*(k1y + 2*k2y + 2*k3y + k4y)*h
    return xOut, yOut
    
    # else:
    #     k1 = K1(f, t, x, y, h)
    #     k2 = K2(f, t, y, h, k1)
    #     k3 = K3(f, t, y, h, k2)
    #     k4 = K4(f, t, y, h, k3)
    #     y1 = y + 1/6*(k1 + 2*k2 + 2*k3 + k4)*h
    #     return y1

def GetEuler(f1, f2, x0, y0, endT, h):
    """ Gets the y values incrementally from
    the Euler method and returns them in a list"""
    g = endT
    y1 = y0
    x1 = x0
    Ex = []
    Ey = []
    Et = []
    Ex.append(x1)
    Ey.append(y1)
    for t in np.arange(0, g, h):
        Et.append(t)
        x2 = Eulers(f1, t, x1, y1, h, Mode='x')
        y2 = Eulers(f2, t, x1, y1, h, Mode='y')
        x1 = x2
        y1 = y2
        Ex.append(x1)
        Ey.append(y1)
    Et.append(g)
    E = [Et, Ex, Ey]
    return E

def GetRK4(f1, f2, x0,  y0, desiredY, h):
    """ Gets the y values incrementally from
    the Runge-Kutta method and Euler method 
    and returns them in a list"""
    g = desiredY
    y1 = y0
    x1 = x0

    # Runge-kutta
    RKx = []
    RKy = []
    RKt = []
    RKx.append(x1)
    RKy.append(y1)
    for t in np.arange(0, g, h):
        RKt.append(t)
        x, y = RK4(f1, f2, t, x1, y1, h)
        # y = RK4(f2, t, x1, y1, h)
        x1 = x
        y1 = y
        RKx.append(x1)
        RKy.append(y1)
    RKt.append(g)
    RK = [RKt, RKx, RKy]
    return RK

def main():
    E = GetEuler(functionx, functiony, 1, 2, 10, 1)
    with plt.xkcd():
        plt.figure(figsize=(5, 3))
        plt.plot(E[0], E[1], ':', label='x')
        plt.plot(E[0], E[2], '-.', label='y')
        plt.xlabel('t')
        plt.ylabel('x, y')
        plt.legend(loc='best')
        plt.savefig('Eulers.pdf')
        plt.show()

        RK = GetRK4(functionx, functiony, 1, 2, 10, 1)
        plt.figure(figsize=(5, 3))
        plt.plot(RK[0], RK[1], ':', label='x')
        plt.plot(RK[0], RK[2], '-.', label='y')
        plt.xlabel('t')
        plt.ylabel('x, y')
        plt.legend(loc='best')
        plt.savefig('RK4.pdf')
        plt.show()

    print('======================================================')
    print('            t = 2s          t = 6s          t = 10s   ')
    print('Method   x(m)    y(m)     x(m)   y(m)     x(m)   y(m) ')
    print('Euler    {0:4.3f}   {1:4.3f}  {2:8.3f} {3:5.3f}  {4:7.3f} {5:6.3f}'.format(E[1][2], E[2][2], E[1][6], E[2][6], E[1][10], E[2][10]))
    print('RK4      {0:4.3f}   {1:4.3f}  {2:8.3f} {3:5.3f}  {4:7.3f} {5:6.3f}'.format(RK[1][2], RK[2][2], RK[1][6], RK[2][6], RK[1][10], RK[2][10]))

main()
