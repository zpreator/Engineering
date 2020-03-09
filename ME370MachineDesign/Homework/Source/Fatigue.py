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

def DEA(Kf, Ma, Kfs, Ta):
    return np.sqrt(4*(Kf*Ma)**2 + 3*(Kfs*Ta)**2)

def DEB(Kf, Mm, Kfs, Tm):
    return np.sqrt(4*(Kf*Mm)**2 + 3*(Kfs*Tm)**2)

def DEGoodman(A, B, Se, Sut, d=None, n=None, Mode='n'):
    if Mode == 'n':
        return np.pi*d**3/16*(A/Se+B/Sut)**(-1)
    elif Mode == 'd':
        return (16*n/np.pi*(A/Se + B/Sut))**(1/3)

def DEMorrow(A, B, Se, sigmaF, d=None, n=None, Mode='n'):
    if Mode == 'n':
        return np.pi*d**3/16*(A/Se+B/sigmaF)**(-1)
    elif Mode == 'd':
        return (16*n/np.pi*(A/Se + B/sigmaF))**(1/3)

def DEGerber(A, B, Se, Sut, d=None, n=None, Mode='n'):
    if Mode == 'n':
        n = 8*A/(np.pi*d**3*Se)*(1+(1+(2*B*Se/(A*Sut))**2)*(1/2))
        return 1/n 
    elif Mode == 'd':
        return (8*n*A/(np.pi*Se)*(1+(1+(2*B*Se/(A*Sut))**2)**(1/2)))**(1/3)

def DESWT(A, B, Se, Sut, d=None, n=None, Mode='n'):
    if Mode == 'n':
        return (np.pi*d**3/(16))*Se/(A**2 + A*B)**(1/2)
    elif Mode == 'd':
        return (16*n/(np.pi*Se)*(A**2 + A*B)**(1/2))**(1/3)

def main():
    n = Goodman(596500, 896500, 23984, 120000)
    print(n)

# main()
