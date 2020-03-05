import numpy as np

def Goodman(SigmaA, SigmaM, Se, Sut):
    return 1/(SigmaA/Se+SigmaM/Sut)

def Gerber(SigmaA, SigmaM, Se, Sut):
    return .5*(Sut/SigmaM)**2*(SigmaA/Se)*(-1+np.sqrt(1+(2*SigmaM*Se/(Sut*SigmaA))**2))