import numpy as np

f1 = lambda x, y: 10*np.exp(-(x-2)**2/(2*(0.075)**2))-0.6*y
# f2 = lambda x: 1*np.exp(-0.6*x)-3.12402*np.exp(-0.6*x)*special.erf_zeros(18.888-9.42809*x)
f3 = lambda x: 0.5*np.exp(-0.6*x)
function1 = lambda t, y: y*(np.sin(t))**3

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
            y, h = self.__RK4E(f, t, y, h, tol=tol)
            RKy.append(y)
            t += h
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
        y4 = y + (37/378*k1 + 250/621 * k3 + 125/594 * k4 + 512/1771*k6)*h
        y5 = y + (2825/27648*k1+18575/48384*k3+13525/55296*k4+277/14336*k5+1/4*k6)*h
        fr = f(t + h, y5)
        if fr < 0 and h < 1:
            yScale = y5 + -((-fr)**h)
        else:
            yScale = y5 + fr**h
        estErr = y5-y4
        desErr = tol*yScale
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

def RK4(f,t0,y0,tf,h):
    """ Runge-Kutta method that takes list of initial values (y0)
    and returns the range of t values, and corresponding y values
    for each item in the original y0 list. An ODE passed in as the
    function must have the correct input parameters"""
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

# DE = NumODESolve()
# print(DE.RK4Embed(f1, 0.5, 0, 4, 0.5))
# print(DE.RK4Embed(function1, 1, 0, 1, 1))