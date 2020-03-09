from Source import Fatigue


def Problem7_1():
    Kf = 2.2
    Kfs = 1.8
    Ma = 70
    Ta = 45
    Mm = 55
    Tm = 35
    Sut = 700
    Sy = 560
    Se = 210
    A = Fatigue.DEA(Kf, Ma, Kfs, Ta)
    B = Fatigue.DEB(Kf, Mm, Kfs, Tm)
    d = Fatigue.DEGoodman(A, B, Se, Sut, n=2, Mode='d')
    print('Goodman', d)
    d2 = Fatigue.DEGerber(A, B, Se, Sut, n=2, Mode='d')
    print('Gerber', d2)
    d3 = Fatigue.DEMorrow(A, B, Se, Sut, n=2, Mode='d')
    print('Morrow', d3)
    d4 = Fatigue.DESWT(A, B, Se, Sut, n=2, Mode='d')
    print('SWT', d4)

def Problem7_2(d):
    Sut = 175e3
    Ma = 600
    Mm = 0
    Ta = 0
    Tm = 400
    Seprime = 0.5*Sut/1000
    Ka = 2*(Sut/1000)**(-0.217)
    Kb = 0.879*d**(-0.107)
    Se = Ka*Kb*Seprime
    Kf = 1.81
    Kfs = 1.46
    A = Fatigue.DEA(Kf, Ma, Kfs, Ta)
    B = Fatigue.DEB(Kf, Mm, Kfs, Tm)
    d = Fatigue.DEGoodman(A, B, Se*1000, Sut, n=2.5, Mode='d')
    D = d/0.65
    dFinal = 0.75*D
    print(dFinal)

# Problem7_2(0.851)
Problem7_1()
