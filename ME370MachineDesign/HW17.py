import numpy as np

def StressCrackLength(ki, beta, a):
    return ki/(beta*np.sqrt(np.pi*a))

def PressureVesselStressT(r, ri, ro, pi):
    return (ri**2*pi/(ro**2-ri**2))*(1-ro**2/r**2)

def PressureVesselStressP(r, ri, ro, sigma):
    """ Tangential stress solved for inner pressure"""
    return (sigma*(ro**2-ri**2)/(1+ro**2/r**2))/ri**2

def PressureVesselStressR(r, ri, ro, pi):
    return (ri**2*pi/(ro**2-ri**2))*(1+ro**2/r**2)

def Problem5_85():
    sigma = StressCrackLength(72, 2.3, 0.5)
    pressure = PressureVesselStressP(7, 6, 7, sigma)
    print(sigma,pressure)

Problem5_85()