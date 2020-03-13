import numpy as np
from ZachsPackage import ODE
from scipy import special
import matplotlib.pyplot as plt
from math import erf

f1 = lambda x, y: 10*np.exp(-(x-2)**2/(2*(0.075)**2))-0.6*y
f2 = lambda x: 1*np.exp(-0.6*x)-3.12402*np.exp(-0.6*x)*erf(18.888-9.42809*x)
f3 = lambda x: 0.5*np.exp(-0.6*x)


def RungeKutta():
    """ Gets an instance of my NumODESolve
    and executes the RK4Embed method"""
    DE = ODE.NumODESolve()
    RK = DE.RK4Embed(f1, 0.5, 0, 4, 0.5, tol=1E-6)
    plt.plot(RK[0], RK[1], 'ko')
    plt.plot(RK[0], [f2(i) for i in RK[0]])
    plt.show()

RungeKutta()