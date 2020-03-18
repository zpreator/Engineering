import numpy as np
from ZachsPackage import Fatigue, Stress

def Problem2():
    """ CORRECT
    A 3.7 inch diameter rotating 
    bar made of AISI 1040 CD steel is 
    loaded only in torsion. What is the 
    endurance limit of the bar in ksi?"""
    d = 3.7 #in
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
     A steel bar with an ultimate 
    strength of 109 kpsi is loaded in 
    bending and failed after 3,890 completely 
    reversed stress cycles. What is the stress 
    amplitude that caused the failure? Assume 
    a fully corrected endurance limit of 33 kpsi 
    is defined at 106 cycles."""
    Sut = 109 # Kpsi
    Se = 33 # Kpsi
    N = 3890 # Cycles

    # From equation 6-11
    f = Fatigue.FatigueStrengthFactor(Sut)

    a = Fatigue.CyclesA(f, Sut, Se)
    b = Fatigue.CyclesB(f, Sut, Se)
    Sf = a * N ** b
    print(Sf)

def Problem4():
    """CORRECT
     Given a stepped shaft under an 
    alternating torsional load, what is 
    the fatigue stress concentration factor 
    at the fillet? The diameters of that 
    shaft are 2 inches and 1 inch with a 
    0.22 inch radius fillet between them.  
    Assume the shaft has an ultimate strength 
    of 103 kpsi."""
    D = 2 # in
    d = 1 # in
    r = 0.22 # in
    Sut = 103 # Kpsi

    a = r/d
    b = D/d
    print(a, b)

def Problem5(d):
    """ WRONG
    Given a uniform diameter shaft made of 
    steel with an ultimate strength of 55 kpsi, 
    a yield strength of 44 kpsi, and a fully corrected 
    endurance limit of 22 kpsi, what is the minimum 
    diameter of the shaft needed to ensure the shaft 
    will not yield and will have infinite life given 
    a fully reversed bending moment of 621 in-lbs and 
    a steady torsional load of 1,812 in-lbs? Use a design 
    factor of 2.0, assume there are no stress concentrations, 
    and use the Morrow failure criterion if needed."""
    Sut = 55000 # psi
    Sy = 44000 # psi
    Se = 22000 # psi
    Mrev = 621 # in-lbs
    T = 1812 # in-lbs

    sigmaF = Sut + 50000

    # Convert to stress
    sigma = Stress.BendingRound(Mrev, d/2, d)
    Tau = Stress.TorsionalRound(T, d)

    sigmaA = sigma
    sigmaM = 0
    TauA = 0
    TauM = Tau

    sigmaAp = Fatigue.AlternatingLoadsVonMises(1, 1, 1, sigmaA, 0, TauA)
    sigmaMp = Fatigue.AlternatingLoadsVonMises(1, 1, 1, sigmaM, 0, TauM)
    sigmaMax = sigmaAp + abs(sigmaMp)
    
    ny = Sy/sigmaMax
    print('ny', ny)

    # nf = Fatigue.Morrow(sigmaAp, sigmaMp, Se, sigmaF)
    # print('nf', nf)

    nf = Se/sigmaAp
    print('nf', nf)

def Problem6():
    """ CORRECT
    Analyze a steel shaft with an ultimate 
    strength of 81 kpsi and fully corrected endurance 
    limit of 34 kpsi if it undergoes a bending stress 
    with mean and amplitude stresses of 9 and 10, 
    respectively, while also undergoing a torsional shear 
    with mean and amplitude stresses of -10 and 6, 
    respectively. Assume there are no stress concentrations 
    or axial loads. Neglect yielding and use the Goodman 
    failure criterion if needed.  Report either the fatigue 
    factor of safety if it is predicted to have infinite life, 
    or the number of cycles to failure in thousands of cycles (N/103)."""
    Sut = 81 # Kpsi
    Se = 34 # Kpsi
    sigmaM = 9
    sigmaA = 10
    TauM = -10
    TauA = 6

    sigmaM = Fatigue.AlternatingLoadsVonMises(sigmaM, 0, TauM)
    sigmaA = Fatigue.AlternatingLoadsVonMises(sigmaA, 0, TauA)

    sigmaMax = sigmaA + abs(sigmaM)
    
    nf = Fatigue.Goodman(sigmaA, sigmaM, Se, Sut)
    print(nf)
    
def Problem7():
    """ WRONG
    Given the following image of a shaft, 
    what is the critical speed of rotation in 
    units of rad/s if the shaft has the following 
    section lengths and deflections (y) and the 
    centers of the given sections.  Assume the 
    shaft is made of steel and all dimensions are 
    given in inches.  Ignore the weight change due 
    to the keyway. (Do not use average diameter 
    simplification method.)"""
    L1 = 2.2 # in
    L2 = 9 # in
    L3 = 1.8 # in
    L4 = 4.8 # in
    y1 = 10*10**-6
    y2 = 300*10**-6
    y3 = 150*10**-6
    y4 = 10*10**-6
    gamma = 0.282

    L = [L1, L2, L3, L4]
    d = [1, 1.25, 1, 0.875]
    y = [y1, y2, y3, y4]

    A = [np.pi/4*i**2 for i in d]
    V = [i * j for i, j in zip(A, L)]
    W = [gamma*i for i in V]

    prod = [i * j for i, j in zip(W, y)]
    top = 32.2 * 12 * sum(prod)
    prodSq = [i * j**2 for i, j in zip(W, y)]
    bottom = sum(prodSq)
    speed = np.sqrt(top/bottom)
    print(speed)

def Problem8():
    """CORRECT
    What is the endurance limit of aluminum and other 
    non-ferrous metals?"""
    # Does not exist

def Problem9():
    """CORRECT
     What is the endurance limit of an R. R. Moore 
    rotating beam specimen made of AISI 1030 CD steel 
    in units of kpsi?"""
    Sut = 76 # kpsi

    # from Equation 6 - 10 Se' = {0.5Sut if Sut <= 200 kpsi, ....}
    SePrime = Sut * 0.5

    print(SePrime)

def Problem10():
    """CORRECT
     When designing a shaft, where is it best to 
    place the bearings?"""
    # Near te ends of the shaft

# Problem2()
# Problem3()
# Problem4()
# Problem5(0.8316)
# Problem5(1.0047) # Don't use
# Problem6()
# Problem7()
# Problem9()



