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

def Parabolic(P, l, C, E, Sy):    
    return 2*(P/(math.pi*Sy)+Sy*l**2/(math.pi**2*C*E))**(1/2)

def ParabolicP(d, l, C, E, Sy):
    return (Sy-(Sy/(2*math.pi*(d/4)))**2/(C*E))*(math.pi*d**2/4)

def ParabolicRectb(P, h, Sy, l, C, E):
    return P/(h*Sy*(1-3*l**2*Sy/(math.pi**2*C*E*h**2)))

def ParabolicRecth(P, b, Sy, l, C, E):
    return P/(2*b*Sy)+((P/(2*b*Sy))**2+3*l**2*Sy/(math.pi**2*C*E))**(1/2)

def ParabolicRectP(Sy, b, h, C, E):
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
    db = Parabolic(P, 16, C, E, Sy)
    print("\nNew Diameters:", da, db)
    da = 1.2
    db = 0.8
    Pa = EulersP(da, 50, C, E)
    Pb = ParabolicP(db, 16, C, E, Sy)
    print("\nForce 1:", Pa, "Force 2:", Pb)

def Problem4_109():
    C = 1.4
    E = 207E9
    l = 0.35
    b = 0.03
    Sy = 180E6
    P = 19899
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
    print("Factor of Safety", P1)

Problem4_109()
