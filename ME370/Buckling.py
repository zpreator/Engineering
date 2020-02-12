import math

def Eulers(P, l, C, E):
    return (64*P*l**2/(math.pi**3*C*E))**(1/4)

def EulersP(d, l, C, E):
    return C*math.pi**2*E/(l/(d/4))**2*(math.pi/4*d**2)

def Parabolic(P, l, C, E, Sy):    
    return 2*(P/(math.pi*Sy)+Sy*l**2/(math.pi**2*C*E))**(1/2)

def ParabolicP(d, l, C, E, Sy):
    return (Sy-(Sy/(2*math.pi*(d/4)))**2/(C*E))*(math.pi*d**2/4)

def LdivK(l, d):
    k = d/4
    return l/k
    

def LdivKsub1(C, E, Sy):
    return (2*math.pi**2*C*E/Sy)**(1/2)

def secant(f, x0, x1, errorMax=1e-6, printIterations = False):
    """ Iterates through the secant method """
    e = errorMax + 1
    n = 0
    pakige = []
    while e > errorMax:
        xnew = x1 - (f(x1)*(x0-x1))/(f(x0)-f(x1))
        x0 = x1
        x1 = xnew
        e = abs((xnew-x0)/xnew)
        n += 1
        pakige.append([n, xnew, f(xnew), e])
        if printIterations:
            print('Iteration number: ', n)
            print('Estimated root: ', xnew)
            print('Evaluation at estimate', f(xnew))
            print('Relative error: ', e)
    return xnew

def main():
    C = 1
    P = 11780.972450961724
    E = 30E6
    Sy = 37700
    da = Eulers(P, 50, C, E)
    db = Eulers(P, 16, C, E)
    print("\nInitial diameters:", da, db)
    da = 1.2
    db = 0.8
    lka = LdivK(50, da)
    lkb = LdivK(16, db)
    print("\nl/k:", lka, lkb)
    lk1 = LdivKsub1(C, E, Sy)
    print("\nl/k sub 1:", lk1)
    da = Eulers(P, 50, C, E)
    db = Parabolic(P, 16, C, E, Sy)
    print("\nNew Diameters:", da, db)
    da = 1.2
    db = 0.8
    Pa = EulersP(da, 50, C, E)
    Pb = ParabolicP(db, 16, C, E, Sy)
    print("\nForce 1:", Pa, "Force 2:", Pb)

main()