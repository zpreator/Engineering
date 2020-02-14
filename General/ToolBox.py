import math
import MomentOfArea2
import Util
# import MomentOfArea2.MomentOfArea2 as M

def MomentOfArea2nd(shape, units, dim1, dim2, dim3, dim4):
    m = MomentOfArea2.MomentOfArea2(shape, units, dim1, dim2, dim3, dim4)
    return m

def MomentOfArea2ndTrapezoid(top, bottom, height):
    return height**3/36*(top**2+4*top*bottom+bottom**2)/(top+bottom)

def StressBending(M, y, I):
    return M*y/I

def StressAxial(F, A):
    return F/A

def StressTorsional(F, d, c, j):
    return F*d*c/j

def StressTransverseShearMaxCircular(V, A):
    return 4*V/(3*A)

def StressTransverseShear(V, Q, I, t):
    return V*Q/(I*t)

def MohrsCircleMaxShearStress(sigmax, sigmay, shear):
    a = abs(sigmax - sigmay)/2
    return math.sqrt(a**2+shear**2)

def Problem5(F, L, do = 0.05, di = 0.04):
    """ Cantilevered bar"""
    j = math.pi/2*(do**4 - di**4)
    tau = F*L*do/j
    tau = tau/1000000
    print(tau)

def Problem6(b, h, t):
    """ YBar of a c channel"""
    A1 = t*(h-t)
    A2 = b*t
    y1 = ((h-t)/2+t)
    y2 = t/2
    yBar = (2*A1*y1 + A2*y2)/(2*A1 + A2)
    print("Y bar =", yBar)
    d1 = abs(h/2-yBar)
    d2 = abs(t/2 - yBar)
    I1 = MomentOfArea2nd("rectangle", 1, 0.6, 4, 0, 0).momentEnglish
    I2 = MomentOfArea2nd("rectangle", 1, (7-1.2), .6, 0, 0).momentEnglish
    I = 2*(I1+A1*d1) + I2 + A2*d2
    print("Moment of Inertia =", I)

def Problem7(h, t, b, V):
    """ Calculating shear for symmetrical I beam with
    h = height of web
    t = thickness of top and bottom
    b = width of beam """
    A1 = h*b/6
    A2 = b*t
    y1 = h/4
    y2 = h/2+t/2
    Q = y1*A1 + y2*A2
    print("Q value at centroid: ", Q)
    I = Util.momentIBeam(h+2*t, h, b/3, b)
    t = b/3
    shear = StressTransverseShear(V, Q, I, t)
    print("Shear at centroid: ", shear)


def Problem8(h, t, ri, g, gc, rho):
    """ Pressure in liquid tank"""
    p = rho*g/gc*h
    ro = ri+t
    stressTangent = ((p*ri**2+ri**2*ro**2*p)/ri**2)/(ro**2-ri**2)
    print("The stress on the inside is: ", stressTangent)
    stressTangent = ((p*ri**2+ri**2*ro**2*p)/ro**2)/(ro**2-ri**2)
    print("The stress on the outside is: ", stressTangent)

def Problem9(M, ri, h = 2, bo = 0.5, bi = 1.5):
    """ Curved beam normal stress"""
    A= (bo+bi)/2*h
    ro=ri+h
    rc=ri+(h/3)*((bi+2*bo)/(bi+bo))
    rn=A/(bo-bi+((bi*ro-bo*ri)/h)*math.log(ro/ri))
    e = abs(rn - rc)
    # y = rn-ri
    y = ro-rn
    I = MomentOfArea2ndTrapezoid(bo, bi, h)
    sigma = StressBending(M, y, I)
    print("The stress due to bending is: ", sigma)

def Problem10(r1, r2, r3, r4, E=30, v=.292):
    """ Pressure fit concentric rings"""
    R = (r2+r3)/2
    delta = abs(r3-r2)
    P = (E*delta/(2*R**3))*(((r4**2-R**2)*(R**2-r1**2))/(r4**2-r1**2))
    sigma = 1000*P*(r4**2+R**2)/(r4**2-R**2)
    print("The stress at the contact point of the outer cylinder is: ", sigma)

def Problem11(Fx, Fy, Fz, dia, d1 = 8, d2 = 12):
    """ Combined loading cantilevered bar"""
    A = math.pi/4*dia**2
    I = MomentOfArea2nd("circle", 1, dia, 0, 0, 0).momentEnglish
    j = I*2
    bending = StressBending(Fx*d1, dia/2, I) + StressBending(Fy*d2, dia/2, I)
    axial = StressAxial(Fy, A)
    torsional = StressTorsional(Fz, d2, dia/2, j)
    transverse = StressTransverseShearMaxCircular(Fz, A)
    print("Bending: ", bending, "Axial", axial, "Torsional: ", torsional, "Transverse: ", transverse)
    totalBending = bending + axial
    totalShear = torsional + transverse
    print("Total Bending: ", totalBending, "Total Shear: ", totalShear)
    maxi = MohrsCircleMaxShearStress(totalBending, 0, totalShear)
    print(maxi)

# print(MomentOfArea2nd("circle", 1, 1, 0, 0, 0).momentEnglish)
# Problem5(5723, 0.7)
# Problem6(6, 3.8, 0.5)
# Problem7(6, 1, 10, 2270)
# Problem8(23, 0.4, 25, 386, 386, 0.03613)
# Problem9(57, 9)
# Problem10(0.52, 1.02, 0.97, 1.28)
Problem11(484, 805, 490, 2)