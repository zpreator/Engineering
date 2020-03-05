import Stress

def GetStress(d):
    Sy = 67000
    bending = Stress.BendingRound(-2110.96, d/2, d)
    torsion = Stress.TorsionalRound(999, d)
    principles = Stress.MohrsCircle2D(bending, 0, torsion)
    FS = Sy/(abs(principles[1]-principles[0]))
    return FS

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

def Loop():
    e = 1
    d = 0.5
    FS = 1
    while d < 1.0:
        d += 0.001
        old = FS
        FS = GetStress(d)
        print(d, FS)
        e = abs(FS-old)/FS

def main():
    print(secant(GetStress, .5, 1, printIterations=True))

Loop()