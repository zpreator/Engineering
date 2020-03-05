import math
from HW12Util import deflection

def Problem4_85():
    d = 0.002
    R = 0.04
    F = 9.81
    l = 0.08
    I = math.pi/4*(d/2)**4
    E = 207E6
    A = math.pi/4*d**2
    rc = R+d/2
    rn = R**2/(2*(rc-math.sqrt(rc**2-R**2)))
    e = abs(rc-rn)
    d = deflection(F, l, A, E, e, R)
    print(d)


Problem4_85()
