from Stress import *
from Fracture import *
from GeometricProperties import *

def problem2(Sy, sigmax, sigmay, tauxy):
    """ CORRECT
        Sy = Yield Strength
        Computes sigma1, sigma2 and tau max from mohrs circle2d
        returns n, using MSS"""
    sigma1, sigma2, Tau_m = MohrsCircle2D(sigmax, sigmay, tauxy)
    n = Sy/(2*Tau_m)
    print(n)

def Problem4():
    """ CORRECT"""
    sigma1, sigma2, Tau_m = MohrsCircle2D(45, -28, 19)
    print(BrittleCoulombMohr(sigma1, sigma2, 75, 100))

def Problem5():
    """ CORRECT"""
    sigma1, sigma2, Tau_m = MohrsCircle2D(13, -21, 19)
    print(ModifiedMohr(sigma1, sigma2, 35, 100))

def Problem6(Fy, Lab, Lbc, Sy, FactorOfSafety):
    """ INCORRECT"""
    M = Fy*(2 + Lab)
    T = Fy*Lbc
    FS = []
    dia = []
    for d in np.arange(0.1, 20, 0.01):
        bending = BendingRound(M, d/2, d)
        torsion = TorsionalRound(T, d)
        sigma1, sigma2, taumax = MohrsCircle2D(bending, 0, torsion)
        v = VonMises(sigma1, sigma2)
        n = Sy/v
        FS.append(n)
        dia.append(d)
    print(dia[np.argmin([abs(FactorOfSafety-i) for i in FS])])

def Problem7(b, h, t, Sy, n):
    """ INCORRECT"""
    Q = MomentOfArea1IBeam(b, b, h, t, t, b/3)
    I = MomentOfArea2('ibeam', 1, h+2*t, h, b/3, b).momentEnglish
    TauMax = Sy/(2*n)
    th = b
    V = TauMax*I*th/Q
    print(V)
    
def Problem8(kic, h, a, b, n, beta):
    """ CORRECT"""
    ki = kic/n
    sigma = StressCrackLength(ki, beta, a)
    print(sigma)
    I = MomentOfArea2('rectangle', 0, b, h).momentMetric
    print(I)
    M = I*sigma*2/h
    print(M)

# problem2(75, 36, -9, 29)
# problem2(64, 9, 0, 15) # Problem3
# Problem4()
# Problem5()
# Problem6(228, 10, 6, 50, 1.7)
# Problem7(11, 4, 0.7, 125, 1.9)
Problem8(26000000, 0.01, 0.002, 0.12, 2.4, 1.05)