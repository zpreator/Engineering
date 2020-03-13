from ZachsPackage import ODE
import numpy as np

f1 = lambda x, y, t: (t + y + 2*x)/7
f2 = lambda x, y, t: x

def FindNewX(x0, x1, yDes, y0, y1):
    return x0 + (yDes - y0)/(y1-y0)*(x1-x0)

def FindStuff():
    DE = ODE.NumODESystemSolve()
    ans = DE.RK4(f1, f2, 0, 5, 0, 20, 1)

class NumODESystemSolve:
    def RK4(self, f1, f2, x0,  y0, T1, T2, h):
        """ Gets the y values incrementally from
        the Runge-Kutta method from T1 to T2 
        and returns them in a list"""
        y1 = y0
        x1 = x0
        # Runge-kutta
        RKx = []
        RKy = []
        RKt = []
        RKx.append(x1)
        RKy.append(y1)
        for t in np.arange(T1, T2, h):
            RKt.append(t)
            x, y = self.__RK4(f1, f2, t, x1, y1, h)
            # y = RK4(f2, t, x1, y1, h)
            x1 = x
            y1 = y
            RKx.append(x1)
            RKy.append(y1)
        RKt.append(T2)
        RK = [RKt, RKx, RKy]
        return RK

    def Eulers(self, f1, f2, x0, y0, T1, T2, h):
        """ Determines the Eulers method from time 1 to 2
        with a step size of h"""
        y1 = y0
        x1 = x0
        Ex = []
        Ey = []
        Et = []
        Ex.append(x1)
        Ey.append(y1)
        for t in np.arange(T1, T2, h):
            Et.append(t)
            x2 = self.__Eulers(f1, t, x1, y1, h, Mode='x')
            y2 = self.__Eulers(f2, t, x1, y1, h, Mode='y')
            x1 = x2
            y1 = y2
            Ex.append(x1)
            Ey.append(y1)
        Et.append(T2)
        E = [Et, Ex, Ey]
        return E

    def __Eulers(self, f, t, x, y, h, Mode='x'):
        """ Returns the Euler's method for the ODE f"""
        if Mode == 'x':
            return x + f(x, y, t)*h
        else:
            return y + f(x, y, t)*h

    def __K1(self, f1, f2, t, x, y, h):
        """ Returns the k1 calculations"""
        return f1(x, y, t), f2(x, y, t)

    def __K2(self, f1, f2, t, x, y, h, K1x, K1y):
        """ Returns the k2 calculations"""
        T = t + .5*h
        X = x + .5*h*K1x
        Y = y + .5*h*K1y
        return f1(X, Y, T), f2(X, Y, T)

    def __K3(self, f1, f2, t, x, y, h, K2x, K2y):
        """ Returns the k3 calculations"""
        T = t + .5*h
        X = x + .5*h*K2x
        Y = y + .5*h*K2y
        return f1(X, Y, T), f2(X, Y, T)

    def __K4(self, f1, f2, t, x, y, h, K3x, K3y):
        """ Returns the k4 calculations"""
        T = t + h
        X = x + h*K3x
        Y = y + h*K3y
        return f1(X, Y, T), f2(X, Y, T)


    def __RK4(self, f1, f2, t, x, y, h):
        """ Calls the k functions and calculates the
        next y (y+1) and returns that y for an ODE f"""
        
        k1x, k1y = self.__K1(f1, f2, t, x, y, h)
        k2x, k2y = self.__K2(f1, f2, t, x, y, h, k1x, k1y)
        k3x, k3y = self.__K3(f1, f2, t, x, y, h, k2x, k2y)
        k4x, k4y = self.__K4(f1, f2, t, x, y, h, k3x, k3y)
        xOut = x + 1/6*(k1x + 2*k2x + 2*k3x + k4x)*h
        yOut = y + 1/6*(k1y + 2*k2y + 2*k3y + k4y)*h
        return xOut, yOut

FindStuff()