from Stress import *
from Fracture import *
from GeometricProperties import *

def problem2(Sy, sigmax, sigmay, tauxy):
    """ 
        Sy = Yield Strength
        Computes sigma1, sigma2 and tau max from mohrs circle2d
        returns n, using MSS"""
    sigma1, sigma2, Tau_m = MohrsCircle2D(sigmax, sigmay, tauxy)
    v = VonMises1(sigmax, sigmay, 0, tauxy, 0, 0)
    n = Sy/v
    n2 = DistortionEnergy(sigma1, sigma2, Sy)
    print(n, n2)

def Problem4():
    """ """
    sigma1, sigma2, Tau_m = MohrsCircle2D(47, -21, 5)
    print(BrittleCoulombMohr(sigma1, sigma2, 75, 100))

def Problem5():
    """ """
    sigma1, sigma2, Tau_m = MohrsCircle2D(13, -26, 6)
    print(BrittleCoulombMohr(sigma1, sigma2, 35, 100))

def Problem6Again(Fy, Lab, Lbc, Sy, d):
    M = Fy*(2+Lab)
    T = Fy*Lbc
    bending = BendingRound(M, d/2, d)
    torsion = TorsionalRound(T, d)
    sigma1, sigma2, taum = MohrsCircle2D(bending, 0, torsion)
    n = DistortionEnergy(sigma1, sigma2, Sy)
    print(n)









def Problem6(Fy, Lab, Lbc, Sy, FactorOfSafety):
    """ CORRECT"""
    M = Fy*(2 + Lab)
    T = Fy*Lbc
    FS = []
    dia = []
    for d in np.arange(0.1, 20, 0.01):
        bending = BendingRound(M, d/2, d)
        torsion = TorsionalRound(T, d)
        sigma1, sigma2, taumax = MohrsCircle2D(bending, 0, torsion)
        v = VonMises2(sigma1, sigma2)
        n = Sy/v
        FS.append(n)
        dia.append(d)
    print(dia[np.argmin([abs(FactorOfSafety-i) for i in FS])])

def GetStress(T, d):
    Sy = 320000000
    # bending = BendingRound(-2110.96, d/2, d)
    torsion = TorsionalRound(T, d)
    principles = MohrsCircle2D(0, 0, torsion)
    FS = Sy/(abs(principles[1]-principles[0]))
    return FS

def Loop(T):
    e = 1
    d = 0.03575
    FS = 1
    while d < 0.0358:
        d += 0.000001
        old = FS
        FS = GetStress(T, d)
        print(d, FS)
        e = abs(FS-old)/FS
    
def Problem7(Ta, Tc, Td, Lac, Lcd, Ldb, Sy, n):
    T = Ta - Tc - Td
    Loop(T)
    # d = 0.05
    # torsion = TorsionalRound(T, d)
    # print(torsion)
    # sigma1, sigma2, Tau_m = MohrsCircle2D(0, 0, torsion)
    
    # n = Sy/(2*Tau_m)
    # print(n)
    
    
def Problem8(kic, h, a, b, beta, M):
    """ CORRECT"""
    I = MomentOfArea2('rectangle', 0, b, h).momentMetric
    print(I)
    sigma = M*h/2/I
    print(sigma)
    ki = KiCrackLength(sigma, beta, a)
    print(ki)
    n = kic/ki
    print(n)

def Problem9():
    """Material with epsilon = 0.1in/in, Syc = 10
       Syt = 5 what theory do I use?"""
    return 'Ductile Coulomb-Mohr'

def Problem10():
    """When is the Coulomb-Mohr theory used?"""
    return 'When yield strength in tension and compression are not equal'

def Problem11():
    """Which is the most common mode of crack propagation?"""
    return 'Opening'
    
# problem2(64, 5, 0, 15)
# problem2(75, 36, -15, 10) # Problem3
# Problem4()
# Problem5()
# Problem6Again(223, 6, 5, 40000, 1.01095)
# Problem6(223, 6, 5, 40000, 2)
# Problem6(224, 10, 5, 47000, 2.4)
Problem7(269, 591, 254, 0.3, 0.4, 0.5, 530000000, 2.5)
# Problem8(26000000, 0.01, 0.002, 0.09, 1.05, 300)