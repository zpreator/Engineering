import numpy as np
from ZachsPackage import Screw

def Problem8_51():
    Pg = 6 # MPa
    A = 20
    B = 20
    d = 12
    Sp = 650
    D = 1.5*d
    l = A + B
    H = 10.8
    # L = H + l + 2*p
    L = 60
    Lt = 2*d + 6
    ld = L - Lt
    lt = l - ld
    Ad = np.pi/4*d**2 #Table 8-7
    At = 84.3 #Table 8-1
    kb = Ad*At*207/(Ad*lt + At*ld)
    kSteel = Screw.SpringRate(207, d, D, A)
    kCastIron = Screw.SpringRate(100, d, D, B)
    kM = 1/(1/kSteel + 1/kCastIron)
    C = kb/(kb + kM)
    Fi = 0.75*At*Sp
    P = Pg*np.pi/4*150**2/10/1000
    sigmaI = Fi/At
    sigmaA = C*P*10**3/(2*At)
    sigmaM = sigmaA + sigmaI

    Sut = 900
    Se = 140
    print(Screw.Goodman(Se, Sut, sigmaI, sigmaA, 0))
    print(Screw.Gerber(Se, Sut, sigmaI, sigmaA))
    print(Screw.ASMEElliptic(Se, Sut, Sp, sigmaI, sigmaA))
    
    # Begin problem 8 - 55
    sigmaI = Fi / At
    sigmaA = C*(P - P/2)*10**3/(2*At)
    sigmaM = sigmaA + sigmaI
    print('Test', Screw.Goodman(Se, Sut, 487.5, 3.675, 498.5))
    print(Screw.Goodman(Se, Sut, sigmaI, sigmaA, sigmaM))
    # print(Screw.Gerber(Se, Sut, sigmaI, sigmaA))
    # print(Screw.ASMEElliptic(Se, Sut, Sp, sigmaI, sigmaA))

Problem8_51()