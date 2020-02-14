from Util import secant
import math

def function1(f, eps = 4.5E-5, D = 0.0525, Re = 0):
    return -2*math.log10((eps/D)/3.7+2.51/(Re*math.sqrt(f)))

def reynolds(V, D, v):
    return 1
    
def main():
    root = secant(function1, 0, 1)