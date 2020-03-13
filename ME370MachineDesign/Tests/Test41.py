from ZachsPackage import Fatigue, Stress
import numpy as np

def Problem2(BrinellHardness):
    """ WRONG
    
    Used if wanted in MPa otherwise use 0.5 for kpsi"""
    print(3.41 * BrinellHardness)

def Problem3(Sut, SigmaAr, Se):
    """ CORRECT
    A steel bar with an ultimate strength of 142 kpsi 
    is loaded in bending with a completely reversed amplitude 
    of 39 kpsi. How many cycles (in thousands, or N/10^3) 
    will the bar withstand until failure? Assume a fully 
    corrected endurance limit of 28 kpsi is defined at 106 cycles."""
    nf = Se/SigmaAr
    # print(nf)
    f = Fatigue.FatigueStrengthFactor(Sut)
    # print(f) 
    a = Fatigue.CyclesA(f, Sut, Se)
    b = Fatigue.CyclesB(f, Sut, Se)
    N = Fatigue.Cycles(SigmaAr, f, Sut, Se)
    print(N)

def Problem5(Sut, Se, sigma1, sigma2):
    """ CORRECT
    Given a steel shaft with an ultimate strength of 100 
    kpsi and a fully corrected endurance limit of 55 kpsi, 
    what is the factor of safety against fatigue failure if 
    it undergoes a normal stress that fluctuates between -50 
    kpsi and 15 kpsi? Neglect yielding and use the Goodman 
    failure criterion if needed."""
    sigmaA = Fatigue.AlternatingLoadsAmp(sigma1, sigma2)
    sigmaM = Fatigue.AlternatingLoadsMean(sigma1, sigma2)
    # print(sigmaA, sigmaM)
    sigmaRev = sigmaA
    nf = Se/sigmaRev
    print(abs(nf))

def Problem6(Sut, Sy, Se, Mrev, T, nf):
    """ WRONG
    Given a uniform diameter shaft made of steel with an 
    ultimate strength of 76 kpsi, a yield strength of 42 kpsi, 
    and a fully corrected endurance limit of 22 kpsi, what is 
    the minimum diameter of the shaft needed to ensure the shaft 
    will not yield and will have infinite life given a fully 
    reversed bending moment of 633 in-lbs and a steady torsional 
    load of 2,346 in-lbs? Use a design factor of 1.4, assume 
    there are no stress concentrations, and use the Morrow failure 
    criterion if needed."""
    # sigmaA = Fatigue.AlternatingLoadsAmp(sigmaRev, 0)
    # sigmaM = Fatigue.AlternatingLoadsMean(sigmaRev, 0)
    # tauA = Fatigue.AlternatingLoadsAmp(tau, 0)
    # tauM = Fatigue.AlternatingLoadsMean(tau, 0)
    # sigmaAp = Fatigue.AlternatingLoadsVonMises(1, 1, 1, sigmaA, 0, tauA)
    # sigmaMp = Fatigue.AlternatingLoadsVonMises(1, 1, 1, sigmaM, 0, tauM)
    # sigmaMax = sigmaAp + abs(sigmaMp)
    # print(sigmaMax)
    # ny = Sy/sigmaMax
    # print(ny)

    A = Fatigue.DEA(1, Mrev, 1, 0)
    B = Fatigue.DEB(1, 0, 1, T)
    d = Fatigue.DEMorrow(A, B, Se, 122, n=nf, Mode='d')
    print(d)
    
def Problem7():
    """ WRONG
    Given the following image of a shaft, what is the critical 
    speed of rotation in units of rad/s if the shaft has the 
    following section lengths and deflections (y) and the centers 
    of the given sections.  Assume the shaft is made of steel and 
    all dimensions are given in inches.  Ignore the weight change 
    due to the keyway.

    L1 = 1.7 in, y1 = 10 x 10-6 in

    L2 = 9 in, y2 = 300 x 10-6 in

    L3 = 2.1 in, y3 = 150 x 10-6 in

    L4 = 2.7 in, y4 = 10 x 10-6 in"""
    L1 = 1.7
    L2 = 9
    L3 = 2.1
    L4 = 2.7
    lengths = [L1, L2, L3, L4]
    dia = [1, 1.25, 1, 7./8.]
    Weights = [32.2*12*0.282*np.pi/4*d**2 for d in dia]
    y = [i*10**(-6) for i in [10, 300, 150, 10]]

    w = Fatigue.RayleighsLumpedMasses(Weights, y)
    print(w)

def Problem8():
    """ CORRECT
    If a material with a stress concentration undergoes 
    a fluctuating stress and shows to have zero sensitivity 
    to the stress concentration, what is the fatigue stress 
    concentration factor?"""
    return '1'

def Problem9():
    """ WRONG
    If I were to apply and remove a positive bending moment 
    to a beam, then apply and remove a negative bending moment, 
    how many stress cycles have I applied to the beam?"""
    return '2'

def Problem10():
    """ CORRECT
    Why should you only use one bearing to support an axial 
    load in a shaft?"""
    
# Problem2(420)
# Problem3(142, 39, 28)
# Problem5(100, 55, -50, 15)
# Problem6(76000, 42000, 22000, 633, 2346, 1.4)
# Problem7()