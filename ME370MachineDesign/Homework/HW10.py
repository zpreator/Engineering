import math
import numpy as np
from HW10Util import *
import matplotlib.pyplot as plt

def problem4_15(E = 30E6, I = 1.85, l = 60):
    w1 = 5
    w2 = 5/12
    F = 150
    y1 = CantileverUniformLoadYmax(w1, l, E, I)
    y2 = CantileverUniformLoadYmax(w2, l, E, I)
    y3 = CantileverEndForce(F, l, E, I)
    ytot = y1 + 2*y2 + y3
    print(ytot)


def problem4_58():
    d = 1.5
    I = math.pi/4*(d/2)**4
    E = 30E6
    x = np.arange(0, 39, 0.001)
    val1 = [Shear(i) for i in x]
    plt.plot(x, val1)
    plt.show()

    val2 = [Moment(i) for i in x]
    plt.plot(x, val2)
    plt.show()

    val3 = [Slope(i, E, I) for i in x]
    plt.plot(x, val3)
    plt.show()

    val4 = [Displacement(i, E, I) for i in x]
    plt.plot(x, val4)
    plt.show()
    print(Displacement(15, E, I), Displacement(19.5, E, I))

problem4_15()
problem4_58()