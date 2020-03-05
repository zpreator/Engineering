import numpy as np

def GoodmanDesign(SigmaA, SigmaM, Se, Sut):
    """ Returns the factor of safety n"""
    return 1/(SigmaA/Se+SigmaM/Sut)

def GerberDesign(SigmaA, SigmaM, Se, Sut):
    """ Returns the factor of safety n"""
    return .5*(Sut/SigmaM)**2*(SigmaA/Se)*(-1+np.sqrt(1+(2*SigmaM*Se/(Sut*SigmaA))**2))

def DEGoodman(A, B, d, Se, Sut):
    """ Returns the factor of safety n"""
    return np.pi*d**3/16*(A/Se + B/Sut)**(-1)

def VonMisesA()