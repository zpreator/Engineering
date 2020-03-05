import math

def CastiglianoAxial(F, l, A, E):
    return F**2*l/(2*A*E)

def deflection(F, l, A, E, e, R):
    return F*l/(A*E) + R*math.pi/(4*A*e*E)