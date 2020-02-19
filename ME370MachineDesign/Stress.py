import numpy as np
from MomentOfArea2 import MomentOfArea2

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

def Centroid(shape, r):
    if shape == 'circle':
        return  4*r/(3*np.pi)

def MomentOfArea1Round(d, r=None):
    """ d = diameter
        r = radius to point of interest"""
    A1 = np.pi/8*d**2
    y1 = Centroid('circle', d/2)
    if r != None:
        A2 = np.pi/4*(d/2-r)**2
        y2 = Centroid('circle', (d/2-r))+r
        return A1*y1+A2*y2
    return A1*y1
    
def VonMises(sigmaA, sigmaB):
    return np.sqrt(sigmaA**2-sigmaA*sigmaB+sigmaB**2)

def MohrsCircle2D(Sx, Sy, Txy):
    Save     = (Sx + Sy) / 2.0
    R        = (((Sx - Sy) / 2.0)**2 + Txy**2)**0.5
    S_first  = Save + R
    S_second = Save - R
    return [S_first, S_second]
    
    