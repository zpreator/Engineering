import numpy as np

def Goodman(SigmaA, SigmaM, Se, Sut):
    """ """
    return 1/(SigmaA/Se+SigmaM/Sut)

def Gerber(SigmaA, SigmaM, Se, Sut):
    return .5*(Sut/SigmaM)**2*(SigmaA/Se)*(-1+np.sqrt(1+(2*SigmaM*Se/(Sut*SigmaA))**2))

def Morrow(SigmaA, SigmaM, Se, SigmaF):
    """ SigmaF can be crudely calculated with 
        SigmaF = Sut + 50 kpsi"""
    return 1/(SigmaA/Se+SigmaM/SigmaF)

def FatigueStrengthFactor(Sut, Mode='kpsi'):
    """ Equation 6-11 or fig 6-23 (f)"""
    if Mode == 'kpsi':
        if Sut < 70:
            return 0.9
        elif Sut < 200:
            return 1.06 - 2.8*(1E-3)*Sut+6.9*(1E-6)*Sut**2
        else:
            return 0.77
    elif Mode == 'mpa' or Mode == 'MPa':
        if Sut < 500:
            return 0.9
        elif Sut < 1400:
            return 1.06 - 4.1*1e-4*Sut+1.5*1e-7*Sut**2
        else:
            return 0.77

def AlternatingLoadsMean(sigma1, sigma2):
    """ Finds the mean load"""
    return (sigma1+sigma2)/2

def AlternatingLoadsAmp(sigma1, sigma2):
    """ Finds the amplitude (max load - mean load)"""
    return abs(sigma1-sigma2)/2

def AlternatingLoadsGoodman(sigmaA, sigmaM, Sut):
    """ Equation 6-59"""
    return sigmaA/(1-sigmaM/Sut)

def AlternatingLoadsVonMises(sigmaBending, sigmaAxial, tauTorsion, KfBend=1, KfAxial=1, KfsTorsion=1):
    """ Equation 6-66/67"""
    return np.sqrt((KfBend*sigmaBending+KfAxial*sigmaAxial)**2 + 3*(KfsTorsion*tauTorsion)**2)

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
    """ Mode, 'n' = will return the design factor, n
        Mode, 'd' = will return the diameter, d"""
    if Mode == 'n':
        return np.pi*d**3/16*(A/Se+B/Sut)**(-1)
    elif Mode == 'd':
        return (16*n/np.pi*(A/Se + B/Sut))**(1/3)

def DEMorrow(A, B, Se, sigmaF, d=None, n=None, Mode='n'):
    """ Mode, 'n' = will return the design factor, n
        Mode, 'd' = will return the diameter, d"""
    if Mode == 'n':
        return np.pi*d**3/16*(A/Se+B/sigmaF)**(-1)
    elif Mode == 'd':
        return (16*n/np.pi*(A/Se + B/sigmaF))**(1/3)

def DEGerber(A, B, Se, Sut, d=None, n=None, Mode='n'):
    """ Mode, 'n' = will return the design factor, n
        Mode, 'd' = will return the diameter, d"""
    if Mode == 'n':
        n = 8*A/(np.pi*d**3*Se)*(1+(1+(2*B*Se/(A*Sut))**2)*(1/2))
        return 1/n 
    elif Mode == 'd':
        return (8*n*A/(np.pi*Se)*(1+(1+(2*B*Se/(A*Sut))**2)**(1/2)))**(1/3)

def DESWT(A, B, Se, Sut, d=None, n=None, Mode='n'):
    """ Mode, 'n' = will return the design factor, n
        Mode, 'd' = will return the diameter, d"""
    if Mode == 'n':
        return (np.pi*d**3/(16))*Se/(A**2 + A*B)**(1/2)
    elif Mode == 'd':
        return (16*n/(np.pi*Se)*(A**2 + A*B)**(1/2))**(1/3)

def CriticalSpeedShaft(l, E, T, m):
    """ for uniform shaft"""
    return (np.pi/l)**2*np.sqrt(E*T/m)
    
def RayleighsLumpedMasses(wList, yList, Units=1):
    """ Units, 1 = English (inches)
    For lumped masses on a shaft, use for all loads 
    and then once for the shaft"""
    if Units == 1:
        sums = sum([i*j for i, j in zip(wList, yList)])
        sums2 = sum([i*j**2 for i, j in zip(wList, yList)])
        omega = np.sqrt(32.2*12*sums/sums2)
        return omega
    
def RayleighsAddSpeeds(omegaL, omegaS):
    """To combine omegas us the relationship, 1/omegaTotal^2 = 1/omegaShaft^2 + 1/omegaLoads^2
    Equation 7-32"""
    return np.sqrt(1/(1/omegaS**2 + 1/omegaL**2))
		

