import numpy as np
from sympy import *

def SolveODE():
    x = symbols('x')
    f = symbols('f', cls=Function)
    diffEq = Eq(f(x).diff(x, x), sin(x))
    print(diffEq)

SolveODE()