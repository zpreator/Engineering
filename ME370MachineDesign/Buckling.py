import math

def EulersRound(P, l, C, E):
    return (64*P*l**2/(math.pi**3*C*E))**(1/4)

def EulersRectb(P, l, C, E, h):
    return (12*P*l**2/(math.pi**2*C*E*h**3))

def EulersRecth(P, l, C, E, b):
    return (12*P*l**2/(math.pi**2*C*E*b))**(1/3)

def EulersRectP(l, C, E, b, h):
    return C*math.pi**2*E*b*h/(l/(h/math.sqrt(12)))**2

def EulersP(d, l, C, E):
    return C*math.pi**2*E/(l/(d/4))**2*(math.pi/4*d**2)

def ParabolicRound(P, l, C, E, Sy):    
    return 2*(P/(math.pi*Sy)+Sy*l**2/(math.pi**2*C*E))**(1/2)

def ParabolicRoundP(d, l, C, E, Sy):
    return (Sy-(Sy*l/(2*math.pi*(d/4)))**2/(C*E))*(math.pi*d**2/4)

def ParabolicRectb(P, h, Sy, l, C, E):
    return P/(h*Sy*(1-3*l**2*Sy/(math.pi**2*C*E*h**2)))

def ParabolicRecth(P, b, Sy, l, C, E):
    return P/(2*b*Sy)+((P/(2*b*Sy))**2+3*l**2*Sy/(math.pi**2*C*E))**(1/2)

def ParabolicRectP(Sy, l, b, h, C, E):
    return (Sy-(Sy/(2*math.pi*(h/math.sqrt(12))))**2/(C*E))*b*h

def LdivKRound(l, d):
    k = d/4
    return l/k
    
def LdivKRect(l, h):
    return math.sqrt(12)*l/h

def LdivKsub1(C, E, Sy):
    return (2*math.pi**2*C*E/Sy)**(1/2)

def Problem4_108():
    C = 1
    P = 11780.972450961724
    E = 30E6
    Sy = 37700
    da = EulersRound(P, 50, C, E)
    db = EulersRound(P, 16, C, E)
    print("\nInitial diameters:", da, db)
    da = 1.2
    db = 0.8
    lka = LdivKRound(50, da)
    lkb = LdivKRound(16, db)
    print("\nl/k:", lka, lkb)
    lk1 = LdivKsub1(C, E, Sy)
    print("\nl/k sub 1:", lk1)
    da = EulersRound(P, 50, C, E)
    db = ParabolicRound(P, 16, C, E, Sy)
    print("\nNew Diameters:", da, db)
    da = 1.2
    db = 0.8
    Pa = EulersP(da, 50, C, E)
    Pb = ParabolicRoundP(db, 16, C, E, Sy)
    print("\nForce 1:", Pa, "Force 2:", Pb)
    FS = Pa/(P/2.5)
    print("Factor of Safety", FS)
    FS = Pb/(P/2.5)
    print("Factor of Safety", FS)

def Problem4_109():
    C = 1.4
    E = 207E9
    l = 0.35
    b = 0.03
    Sy = 180E6
    P = 9949.52
    h = EulersRecth(P, l, C, E, b)
    print("Initial width:", h)
    lk = LdivKRect(l, 0.007)
    print("l/k:", lk)
    lk1 = LdivKsub1(C, E, Sy)
    print("l/k sub1:", lk1)
    h = ParabolicRecth(P, b, Sy, l, C, E)
    print("New h: ", h)
    P1 = EulersRectP(l, C, E, b, h)
    FS = P1/(P/3.5)
    print("Factor of Safety", FS)

def test2Problem9():
    """ Correct"""
    C= 1
    l = 10
    E = 30E6
    Sy = 65E3
    F = 9226
    FS = 1.9
    P = F*FS 
    d = EulersRound(P, l, C, E)
    lk = LdivKRound(l, d)
    lk1 = LdivKsub1(C, E, Sy)
    print("Initial Diameter: ", d, "l/k :", lk, "l/k sub1 :", lk1)
    dnew = ParabolicRound(P, l, C, E, Sy)
    print(dnew)

def test2Attempt2Problem9():
    """ Suppose you are designing a component 
    that may fail in buckling. What is the minimum 
    diameter in inches (and not using preferred sizes) 
    in order to prevent the column from buckling with 
    a factor of safety of 1.6? Assume a solid and 
    round cross section with pinned-pinned 
    (both ends rounded) end conditions, supporting a 
    load P = 8,613 lbs, with the length L = 7 in,
    E = 30 Mpsi, and Sy = 71 kpsi.  Give your answer 
    in units of inches. """
    C= 1
    l = 7
    E = 30E6
    Sy = 71E3
    F = 8613
    FS = 1.6
    P = F*FS 
    d = EulersRound(P, l, C, E)
    lk = LdivKRound(l, d)
    lk1 = LdivKsub1(C, E, Sy)
    print("Initial Diameter: ", d, "l/k :", lk, "l/k sub1 :", lk1)
    dnew = ParabolicRound(P, l, C, E, Sy)
    print(dnew)

def test2Attempt3Problem9():
    """ Suppose you are designing a component 
    that may fail in buckling. What is the minimum 
    diameter in inches (and not using preferred sizes) 
    in order to prevent the column from buckling with 
    a factor of safety of 1.6? Assume a solid and 
    round cross section with pinned-pinned 
    (both ends rounded) end conditions, supporting a 
    load P = 8,613 lbs, with the length L = 7 in,
    E = 30 Mpsi, and Sy = 71 kpsi.  Give your answer 
    in units of inches. """
    C= 1
    l = 18
    E = 30E6
    Sy = 60E3
    F = 936
    FS = 2.7
    P = F*FS 
    d = EulersRound(P, l, C, E)
    lk = LdivKRound(l, d)
    lk1 = LdivKsub1(C, E, Sy)
    print("Initial Diameter: ", d, "l/k :", lk, "l/k sub1 :", lk1)
    dnew = ParabolicRound(P, l, C, E, Sy)
    print(dnew)


test2Attempt2Problem9()
