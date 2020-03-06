import numpy as np

def Goodman(SigmaA, SigmaM, Se, Sut):
    return 1/(SigmaA/Se+SigmaM/Sut)

def Gerber(SigmaA, SigmaM, Se, Sut):
    return .5*(Sut/SigmaM)**2*(SigmaA/Se)*(-1+np.sqrt(1+(2*SigmaM*Se/(Sut*SigmaA))**2))

def CyclesA(f, Sut, Se):
    return (f*Sut)**2/Se

def CyclesB(f, Sut, Se):
    return -1/3*np.log10(f*Sut/Se)

def Cycles(sigmaRev, f, Sut, Se):
    a = CyclesA(f, Sut, Se)
    b = CyclesB(f, Sut, Se)
    N = (sigmaRev/a)**(1/b)
    return N

def main():
    n = Goodman(596500, 896500, 23984, 120000)
    print(n)

main()