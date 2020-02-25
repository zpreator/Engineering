import numpy as np


def BrittleCoulombMohr(sigmaA, sigmaB, Sut, Suc):
    """ Sut -> yield strength in tension
        Suc -> yield strength in compression
        returns the factor of safety"""
    if sigmaA > sigmaB and sigmaB > 0:
        n = Sut/sigmaA
    elif sigmaA > 0 and sigmaB < 0:
        n = 1/(sigmaA/Sut-sigmaB/Suc)
    elif sigmaA < 0 and sigmaA > sigmaB:
        n = -Suc/sigmaB
    return n


def ModifiedMohr(sigmaA, sigmaB, Sut, Suc):
    if sigmaA > sigmaB and sigmaB > 0:
        n = Sut/sigmaA
    elif sigmaA > 0 and sigmaA > sigmaB:
        n = 1/((Suc-Sut)*sigmaA/(Suc*Sut)-sigmaB/Suc)
    elif sigmaA < 0 and sigmaA > sigmaB and abs(sigmaB/sigmaA) > 1:
        n = -Suc/sigmaB
    return n


def DistortionEnergy(sigmaA, sigmaB, Sy):
    vonMises = np.sqrt(sigmaA**2-sigmaA*sigmaB+sigmaB**2)
    n = Sy/vonMises
    return n


def StressCrackLength(ki, beta, a):
    """ Crack length equation solved for sigma"""
    return ki/(beta*np.sqrt(np.pi*a))


def PressureVesselStressT(r, ri, ro, pi):
    return (ri**2*pi/(ro**2-ri**2))*(1-ro**2/r**2)


def PressureVesselStressP(r, ri, ro, sigma):
    """ Tangential stress solved for inner pressure"""
    return (sigma*(ro**2-ri**2)/(1+ro**2/r**2))/ri**2


def PressureVesselStressR(r, ri, ro, pi):
    return (ri**2*pi/(ro**2-ri**2))*(1+ro**2/r**2)