import numpy as np

def Problem6_4(f, Sut, SigmaAr, Se):
    a = (f*Sut)**2/Se
    b = -1/3*np.log10(f*Sut/Se)
    N = (SigmaAr/a)**(1/b)
    print(N)

def Problem6_5(f, Sut, N, Se):
    a = (f*Sut)**2/Se
    b = -1/3*np.log10(f*Sut/Se)
    Sf = a*N**b
    print(Sf)

Problem6_4(0.82, 120, 70, 60)
Problem6_4(0.77, 1600, 900, 700)
Problem6_5(0.77, 230, 150e3, 700)

