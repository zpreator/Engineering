import math
from HW11Util import *

def Problem4_15():
    print(CastiglianoBending(60, 30E6, 3.7))

def Problem4_70():
    C = 7 # in
    D = 15 # in
    F = 15 # lbf
    d = 0.5 # diameter
    A = math.pi/4*d**2 # area
    E = 30E6 # Modulus of elasticity (Table A5)
    I = math.pi/4*((d/2)**4) # 2nd moment of area
    j = 2*I # polar 2nd moment of area
    G = 11.5E6 # Modulus of rigidity
    #       Bending          Bending             Constant Bending     Bending            Torsion              Axial
    delta = F*C**3/(3*E*I) # Bending
    delta += 3*F*D*C**2/(5*E*I) # Const Bending
    delta += 4*F*D**3/(5*E*I) # Bending
    delta += 4*F*C**2*D/(5*G*j) # Torsion
    delta += 3*F*D/(5*A*E) # Axial
    print(delta)

Problem4_15()
Problem4_70()