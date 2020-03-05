import numpy as np

def Goodman(SigmaA, SigmaM, Se, Sut):
    return 1/(SigmaA/Se+SigmaM/Sut)

def Gerber(SigmaA, SigmaM, Se, Sut):
    return .5*(Sut/SigmaM)**2*(SigmaA/Se)*(-1+np.sqrt(1+(2*SigmaM*Se/(Sut*SigmaA))**2))

def Problem6_28():
    Hardness = 400
    F1 = 0.040 # klbf
    F2 = 0.020 # klbf
    L = 12 # in
    d = 0.375 # in

    Sut = 0.5*Hardness
    Sep = 0.5*Sut
    a = 11
    b = -0.65
    Ka = a*(Sut)**b
    Kb = 1
    Kc = 1
    Se = Ka*Kb*Kc*Sep
    Fa = (F1-F2)/2
    Fm = (F1+F2)/2
    SigmaA = 32*Fa*L/(np.pi*d**3)
    SigmaM = 32*Fm*L/(np.pi*d**3)
    nf1 = Goodman(SigmaA, SigmaM, Se, Sut)
    nf2 = Gerber(SigmaA, SigmaM, Se, Sut)
    print(nf1, nf2)

    f = 0.77
    a1 = (f*Sut)**2/Se
    b1 = -1/3*np.log10(f*Sut/Se)
    Sf = SigmaA/(1-SigmaM/Sut)
    N = (Sf/a1)**(1/b1)
    print(N)

Problem6_28()