import numpy as np

def TorqueRaiseThread(F, dm, ft, l):
    return F*dm/2*(l + np.pi*ft*dm)/(np.pi*dm - ft*l)

def TorqueLowerThread(F, dm, ft, l):
    return F*dm/2*(np.pi*ft*dm-l)/(np.pi*dm+ft*l)

def TorqueCollar(F, fc, dc):
    return F*fc*dc/2

def TorqueToRaiseWCollar(F, ft, fc, dm, dc, l):
    return TorqueRaiseThread(F, dm, ft, l) + TorqueCollar(F, fc, dc)

def TorqueToLowerWCollar(F, ft, fc, dm, dc, l):
    return TorqueLowerThread(F, dm, ft, l) + TorqueCollar(F, fc, dc)

def ForceFromTorqueRaiseCollar(T, dm, dc, ft, fc, l):
    return T/(dm/2*(l+np.pi*ft*dm)/(np.pi*dm-ft*l) + fc*dc/2)
    
def Efficiency(F, l, Tr):
    return F*l/(2*np.pi*Tr)

def Example8_10():
    """ Example from 8th edition book
    Power in = 3 KW
    lead = 1
    omega (w) = 1 rev/s
    screw diameter = 36 mm
    pitch = 6 mm
    friction thread = 0.09
    friction collar = 0.09
    Find F (combined efficiency)"""
    Pin = 3 #Kw
    Pin = Pin * 1000 # W
    lead = 1 # Also n = 1
    w = 1 # Rev/s
    w = w * 2*np.pi # rad/s
    screwD = 36 #mm
    screwD = screwD/1000 #m
    pitch = 6 #mm
    pitch = pitch/1000 #m
    ft = 0.09
    fc = 0.09
    rc = 45 #mm (Mean collar radius)
    rc = rc/1000
    dc = 2*rc

    l = lead * pitch

    dm = screwD-pitch/2

    F = 65035.5 # Guess
    Tt = TorqueRaiseThread(F, dm, ft, l)
    Tc = TorqueCollar(F, fc, dc)
    Tr = Tt + Tc
    Power = Tr*w
    print(Power)

def Example8_1():
    """ Example 8_1 11th edition
    
    """
    d = 32 #mm
    pitch = 4 #mm
    lead = 2 # double threads
    f = 0.08
    dc = 40 #mm
    F = 6.4

    dm = d - pitch/2
    dr = d - pitch
    l = pitch * lead

    # Getting torque to raise
    Tt = TorqueRaiseThread(F, dm, f, l)
    Tc = TorqueCollar(F, f, dc)
    Tr = Tt + Tc
    print(Tr)
    Tr2 = TorqueToRaiseWCollar(F, f, f, dm, dc, l)
    print(Tr2) #Should be the same as Tr

# Example8_1()