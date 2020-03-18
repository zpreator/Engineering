import numpy as np
from ZachsPackage import Fatigue, Stress

""" 
20/20
Woooooooo
"""
def Problem2():
    """ CORRECT
    A 2.7 inch diameter rotating bar 
    made of AISI 1040 CD steel is loaded 
    only in torsion. What is the endurance 
    limit of the bar in ksi?"""
    d = 2.7 #in
    Sut = 85 #kpsi

    # from Equation 6 - 10 Se' = {0.5Sut if Sut <= 200 kpsi, ....}
    SePrime = Sut * 0.5

    # Ka (Surface finish) -> cold drawn
    a1 = 2.00
    b1 = -0.217
    Ka = a1 * Sut ** b1

    # Kb (Size factor) -> Kb = {0.91*d^-0.157 if 2 < d < 10 in, ....}
    Kb = 0.91 * d ** -0.157

    # Kc (Loading factor) -> Kc = {0.59 if torsion, ....}
    Kc = 0.59

    Se = SePrime * Ka * Kb * Kc

    print(Se)

def Problem3():
    """CORRECT
     A steel bar with an ultimate strength 
    of 146 kpsi is loaded in bending with a 
    completely reversed amplitude of 39 kpsi. 
    How many cycles (in thousands, or N/10^3) 
    will the bar withstand until failure? 
    Assume a fully corrected endurance limit of 
    29 kpsi is defined at 106 cycles."""
    Sut = 146 #Kpsi
    SigmaAr = 39 #Kpsi
    Se = 29 #Kpsi
    nf = Se/SigmaAr
    # print(nf)
    f = Fatigue.FatigueStrengthFactor(Sut)
    # print(f) 
    a = Fatigue.CyclesA(f, Sut, Se)
    b = Fatigue.CyclesB(f, Sut, Se)
    N = Fatigue.Cycles(SigmaAr, f, Sut, Se)
    print(N)

def Problem4():
    """CORRECT
     Given a stepped shaft under an 
    alternating torsional load, what is 
    the fatigue stress concentration factor 
    at the fillet? The diameters of that 
    shaft are 2 inches and 1 inch with a 
    0.24 inch radius fillet between them.  
    Assume the shaft has an ultimate strength 
    of 84 kpsi."""
    D = 2 # in
    d = 1 # in
    r = 0.24 # in
    Sut = 84 # Kpsi

    a = r/d
    b = D/d
    print(a, b)

def Problem5():
    """ CORRECT
    Given a steel shaft with an ultimate strength of 115 
    kpsi and a fully corrected endurance limit of 50 kpsi, 
    what is the factor of safety against fatigue failure if 
    it undergoes a normal stress that fluctuates between 13 
    kpsi and 49 kpsi? Neglect yielding and use the Goodman 
    failure criterion if needed."""
    Sut = 115 #Kpsi
    Se = 50 #Kpsi
    sigma1 = 13 #Kpsi
    sigma2 = 49 #Kpsi
    sigmaA = Fatigue.AlternatingLoadsAmp(sigma1, sigma2)
    sigmaM = Fatigue.AlternatingLoadsMean(sigma1, sigma2)
    # print(sigmaA, sigmaM)
    # sigmaRev = sigmaA
    # nf = Se/sigmaRev
    # print(abs(nf))
    nf = Fatigue.Goodman(sigmaA, sigmaM, Se, Sut)
    print(nf)

def Problem6():
    """ CORRECT
    Given a steel shaft with an ultimate strength of 119 
    kpsi and a fully corrected endurance limit of 59 kpsi, 
    what is the factor of safety against fatigue failure if 
    it undergoes a normal stress that fluctuates between -65 
    kpsi and 21 kpsi? Neglect yielding and use the Goodman 
    failure criterion if needed."""
    Sut = 119 #Kpsi
    Se = 59 #Kpsi
    sigma1 = -65 #Kpsi
    sigma2 = 21 #Kpsi
    sigmaA = Fatigue.AlternatingLoadsAmp(sigma1, sigma2)
    sigmaM = Fatigue.AlternatingLoadsMean(sigma1, sigma2)
    # print(sigmaA, sigmaM)
    sigmaRev = sigmaA
    nf = Se/sigmaRev
    print(abs(nf))

def Problem7():
    """ CORRECT
    Given the following image of a shaft, 
    what is the critical speed of rotation in 
    units of rad/s if the shaft has the following 
    section lengths and deflections (y) and the 
    centers of the given sections.  Assume the 
    shaft is made of steel and all dimensions are 
    given in inches.  Ignore the weight change due 
    to the keyway. (Do not use average diameter 
    simplification method.)"""
    gamma = 0.282

    L = [2.8, 8, 2.5, 4.7]
    d = [1, 1.25, 1, 0.875]
    y = [i*10**-6 for i in [10, 300, 150, 10]]

    A = [np.pi/4*i**2 for i in d]
    V = [i * j for i, j in zip(A, L)]
    W = [gamma*i*32.2*12 for i in V]

    prod = [i * j for i, j in zip(W, y)]
    top = 32.2 * 12 * sum(prod)
    prodSq = [i * j**2 for i, j in zip(W, y)]
    bottom = sum(prodSq)
    speed = np.sqrt(top/bottom)
    print(speed)

    w = Fatigue.RayleighsLumpedMasses(W, y)
    print(w)

def Problem8():
    """ CORRECT
    Under which type of loading conditions 
    should Miner’s rule be used to estimate the 
    endurance limit?"""
    # Two bending loads are applied one after another

def Problem9():
    """ CORRECT
    If I design a shaft and find out that it 
    deflects too much under a load, what should I do?"""
    # Make it thicker

def Problem10():
    """ CORRECT
    If I were to apply and remove a positive bending 
    moment to a beam, then apply and remove a negative 
    bending moment, how many stress cycles have I applied 
    to the beam?"""
    # 1

# Problem2()
# Problem3()
# Problem4()
# Problem5()
# Problem6()
Problem7()