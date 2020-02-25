import numpy as np
from MomentOfArea2 import MomentOfArea2
from GeometricProperties import *

def TorsionalRound(T, d, r=None):
    """ T = Torsional force
        d = diameter
        r = radius to point in question """
    j = np.pi/2*(d/2)**4
    if r == None:
        return T*(d/2)/(j)
    return T*r/j

def AxialRound(F, d=None, A=None):
    if A == None:
        A = np.pi/4*d**2
    return F/A

def BendingRound(M, y, d):
    I = MomentOfArea2('circle', 0, dim1=d).momentMetric
    return M*y/I

def TransverseShearRound(V, d, r):
    Q = MomentOfArea1Round(d)
    I = MomentOfArea2('circle', 0, dim1=d).momentMetric
    return V*Q/(I*d)
    
def VonMises(sigmaA, sigmaB):
    return np.sqrt(sigmaA**2-sigmaA*sigmaB+sigmaB**2)

def MohrsCircle2D(Sx, Sy, Txy):
    """ Returns Sigma1, Sigma2 and Tau_max"""
    Save     = (Sx + Sy) / 2.0
    R        = (((Sx - Sy) / 2.0)**2 + Txy**2)**0.5
    S_first  = Save + R
    S_second = Save - R
    return [S_first, S_second, R]
    
    