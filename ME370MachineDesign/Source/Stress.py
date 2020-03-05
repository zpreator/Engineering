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
    
def VonMises2(sigmaA, sigmaB):
    return np.sqrt(sigmaA**2-sigmaA*sigmaB+sigmaB**2)

def VonMises1(sigmaX, sigmaY, sigmaZ, tauXY, tauYZ, tauZX):
    return 1/np.sqrt(2)*((sigmaX-sigmaY)**2 + (sigmaY-sigmaZ)**2 + (sigmaZ-sigmaX)**2+6*(tauXY**2 + tauYZ**2 + tauZX**2))**(1/2)

def MohrsCircle2D(sigmaX, sigmaY, tauXY):
    """ Returns Sigma1, Sigma2 and Tau_max"""
    Save     = (sigmaX + sigmaY) / 2.0
    R        = (((sigmaX - sigmaY) / 2.0)**2 + tauXY**2)**0.5
    S_first  = Save + R
    S_second = Save - R
    return [S_first, S_second, R]
    
    