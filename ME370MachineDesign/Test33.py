from Stress import *
from Fracture import *
from GeometricProperties import *

def problem2(Sy, sigmax, sigmay, sigmaz, tauxy, tauxz):
    """ 
        Sy = Yield Strength
        Computes sigma1, sigma2 and tau max from mohrs circle2d
        returns n, using MSS"""
    # sigma1, sigma2, Tau_m = MohrsCircle2D(sigmax, sigmay, tauxy)
    v = VonMises1(sigmax, sigmay, sigmaz, tauxy, tauxz, 0)
    n = Sy/v
    # n2 = DistortionEnergy(sigma1, sigma2, Sy)
    print(n)

def problem3(Sy, sigmax, sigmay, tauxy):
    """ CORRECT
        Sy = Yield Strength
        Computes sigma1, sigma2 and tau max from mohrs circle2d
        returns n, using MSS"""
    sigma1, sigma2, Tau_m = MohrsCircle2D(sigmax, sigmay, tauxy)
    n = Sy/(2*Tau_m)
    print(n)

def problem4(sigmax, sigmay, tauxy):
    """ """
    sigma1, sigma2, Tau_m = MohrsCircle2D(sigmax, sigmay, tauxy)
    print(BrittleCoulombMohr(sigma1, sigma2, 75, 100))

def problem5(sigmax, sigmay, tauxy):
    """ """
    sigma1, sigma2, Tau_m = MohrsCircle2D(sigmax, sigmay, tauxy)
    print(BrittleCoulombMohr(sigma1, sigma2, 35, 100))

def Problem6(Fy, Lab, Lbc, Sy, FactorOfSafety):
    """ CORRECT"""
    M = Fy*(2 + Lab)
    T = Fy*Lbc
    FS = []
    dia = []
    for d in np.arange(1, 1.2, 0.01):
        bending = BendingRound(M, d/2, d)
        torsion = TorsionalRound(T, d)
        sigma1, sigma2, taumax = MohrsCircle2D(bending, 0, torsion)
        v = VonMises2(sigma1, sigma2)
        n = Sy/v
        FS.append(n)
        dia.append(d)
        # print(FS)
    print(dia[np.argmin([abs(FactorOfSafety-i) for i in FS])])

def problem7(T, d, Sy):
    torsion = 16*T/(np.pi*d**3)
    n = Sy/torsion
    print(n)

def Problem8(kic, h, a, b, n, beta):
    """ CORRECT"""
    ki = kic/n
    sigma = StressCrackLength(ki, beta, a)
    print(sigma)
    I = MomentOfArea2('rectangle', 0, b, h).momentMetric
    print(I)
    M = I*sigma*2/h
    print(M)


# problem2(60, -13, -17, 15, 26, 4)
# problem3(64, 6, 0, 14)
# problem4(39, -25, 12)
# problem5(24, -10, 12)
# Problem6(224, 10, 5, 47000, 2.4)
# problem7(466, 0.0223704, 530e6)
problem7(576, 0.0284, 320e6)
# Problem8(26e6, 0.01, 0.002, 0.16, 1.8, 1.05)
