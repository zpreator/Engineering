import numpy as np
from ZachsPackage import ODE
from scipy import special
import matplotlib.pyplot as plt
from math import erf

"""
Zachary Preator
Mastery Level 10
"""

f1 = lambda x, y: 10*np.exp((-(x-2)**2)/(2*(0.075)**2))-0.6*y
f2 = lambda x: 1*np.exp(-0.6*x)-3.12402*np.exp(-0.6*x)*erf(18.888-9.42809*x)
f3 = lambda x: 0.5*np.exp(-0.6*x)
truefunc = lambda x: 3.12402*np.exp(-0.6*x)*(1.16005 + erf(0.053033*(-356.156 + 177.778*x)))

def RungeKutta():
    """ Gets an instance of my NumODESolve
    and executes the RK4Embed method"""
    # DE = ODE.NumODESolve()
    # RK = DE.RK4Embed(f1, 0.5, 0, 4, 0.5, tol=1E-6)
    DE = NumODESolve()
    RK = DE.RK4Embed(f1, 0.5, 0, 4, 0.5, tol=1E-6)
    plt.plot(RK[0], RK[1], 'ko')
    plt.plot(RK[0], [truefunc(i) for i in RK[0]])
    plt.show()

class NumODESolve:
    def RK4(self, f, y0, T1, T2, h):
        """ Gets the y values incrementally from
        the Runge-Kutta method and Euler method 
        and returns them in a list"""
        y = y0
        # Runge-kutta
        RKy = []
        RKt = []
        RKy.append(y)
        for i in np.arange(T1, T2, h):
            RKt.append(i)
            y = self.__RK4(f, i, y, h)
            RKy.append(y)
        RKt.append(T2)
        RK = [RKt, RKy]
        return RK

    def RK4Embed(self, f, y0, T1, T2, h, tol=1E-5):
        """ Gets the y values from the Runge-Kutta
        method and returns them in a list"""
        y = y0
        RKt = []
        RKy = []
        RKy.append(y)
        t = T1
        while t < T2:
            
            RKt.append(t)
            y, hnew = self.__RK4E(f, t, y, h, tol=tol)
            t += h
            h = hnew
            RKy.append(y)
            
        RKt.append(T2)
        RK = [RKt, RKy]
        return RK

    def __RK4E(self, f, t, y, h, tol=1E-5, FS=0.8):
        """ Calls the k functions and calculates the
        next y and returns that y and new step size
        for an ODE f"""
        k1 = self.__K1(f, t, y, h)
        k2 = self.__K2E(f, t, y, h, k1)
        k3 = self.__K3E(f, t, y, h, k1, k2)
        k4 = self.__K4E(f, t, y, h, k1, k2, k3)
        k5 = self.__K5E(f, t, y, h, k1, k2, k3, k4)
        k6 = self.__K6E(f, t, y, h, k1, k2, k3, k4, k5)
        y4 = y + (37/378*k1 + 250/621 * k3 + 125/594 * k4 + 512/1771*k6) * h
        y5 = y + (2825/27648*k1+18575/48384*k3+13525/55296*k4+277/14336*k5+1/4*k6)*h
        fr = f(t + h, y5)
        yScale = abs(y5) + abs(fr*h)
        estErr = abs(y5 - y4)
        desErr = tol * yScale
        if abs(estErr) < desErr:
            alpha = 0.2
        else:
            alpha = 0.25
        hNew = FS*h*abs(desErr/estErr)**alpha
        return y5, hNew

    def __K2E(self, f, t, y, h, K1):
        T = t + 1/5*h
        Y = y + 1/5*K1*h
        return f(T, Y)

    def __K3E(self, f, t, y, h, K1, K2):
        T = t + 3/10*h
        Y = y + 3/40*K1*h+ 9/40*K2*h
        return f(T, Y)

    def __K4E(self, f, t, y, h, K1, K2, K3):
        T = t + 3/5*h
        Y = y + 3/10*K1*h - 9/10*K2*h + 6/5*K3*h
        return f(T, Y)

    def __K5E(self, f, t, y, h, K1, K2, K3, K4):
        T = t + h
        Y = y - 11/54*K1*h + 5/2*K2*h -70/27*K3*h + 35/27*K4*h
        return f(T, Y)

    def __K6E(self, f, t, y, h, K1, K2, K3, K4, K5):
        T = t + 7/8*h
        Y = y + 1631/55296*K1*h + 175/512*K2*h + 575/13824*K3*h + 44275/110592*K4*h + 253/4096*K5*h
        return f(T, Y)

    def __K1(self, f, t, y, h):
        """ Returns the k1 calculations"""
        return f(t, y)

    def __K2(self, f, t, y, h, K1):
        """ Returns the k2 calculations"""
        a = t + .5*h
        b = y + .5*h*K1
        return f(a, b)

    def __K3(self,f, t, y, h, K2):
        """ Returns the k3 calculations"""
        a = t + .5*h
        b = y + .5*h*K2
        return f(a, b)

    def __K4(self,f, t, y, h, K3):
        """ Returns the k4 calculations"""
        a = t + h
        b = y + h*K3
        return f(a, b)

    def __RK4(self, f, t, y, h):
        """ Calls the k functions and calculates the
        next y (y+1) and returns that y for an ODE f"""
        k1 = self.__K1(f, t, y, h)
        k2 = self.__K2(f, t, y, h, k1)
        k3 = self.__K3(f, t, y, h, k2)
        k4 = self.__K4(f, t, y, h, k3)
        y1 = y + 1/6*(k1 + 2*k2 + 2*k3 + k4)*h
        return y1

    def __Eulers(self, f, t, y, h):
        """ Returns the Euler's method for the ODE f"""
        return y + f(t, y)*h

RungeKutta()