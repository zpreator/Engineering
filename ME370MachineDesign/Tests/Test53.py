import numpy as np
from ZachsPackage import Screw

def Problem2():
    """What is the torque, in pound-inches, 
    required to raise a 6 kip load using a 
    square thread power screw with a major 
    diameter of 1.7 inches and a pitch of 
    0.6 inches? Assume the screw to be single 
    threaded and the friction on the thread 
    to be 0.10. There is no collar."""
    F = 6000 #kips
    p = 0.6 #in
    d = 1.7 #in
    dm = d - p/2
    f = 0.1
    l = p*1 # lead for single threaded
    Tr = F*dm/2*(l+np.pi*f*dm)/(np.pi*dm-f*l)
    Tr2 = Screw.TorqueRaiseThread(F, dm, f, l)
    print(Tr, Tr2)

def Problem3():
    """Supposing that you need to clamp a 0.6" 
    thick steel plate with a 0.6" thick brass 
    plate using a 1/4"-20 through-hole bolt and 
    nut, what is the stiffness of the members 
    in Mlbf/in? Assume there isn't a need for a 
    washer."""
    tan = 0.5773502692
    t1 = 0.6 #in steel plate
    t2 = 0.6 #in brass plate
    # lg = A + B #grip length
    d = 1/4
    D2 = 7/16 # Table A-29
    l = t1 + d/2
    D1 = D2 + l*tan
    a = t1 - l/2
    b = l - t1
    D3 = D1 - 2*a*tan
    k1 = Screw.SpringRate(30, d, D2, l/2)
    k2 = Screw.SpringRate(30, d, D3, a)
    k3 = Screw.SpringRate(15.4, d, D2, b)
    ans = 1/(1/k1 + 1/k2 + 1/k3)
    print(ans)

def Problem4():
    """Given a non-permanent bolted joint with a 
    bolt stiffness of 1.3 Mlbf/in and a member 
    stiffness of 2.6 Mlbf/in, what is the factor 
    of safety against the joint opening if one 
    1/2"-20, SAE grade 5 bolt is used to support 
    a tensile load of 7 kip? """
    kbolt = 1300 #Klbf/in
    km = 2600 #Klbf/in
    F = 7 #kip
    At = 0.1419 #in^2
    Ps = 85 #kpsi change this value for the different SAE specs (7=105 proof strength)
    C = kbolt/(kbolt+km)
    Fi = 0.75*At*Ps
    n = Fi/(F*(1-C))
    print(n)

def Problem5():
    """ Given a non-permanent bolted joint with a 
    bolt stiffness of 2.4 Mlbf/in and a member 
    stiffness of 4 Mlbf/in that is supporting a 
    tensile load that fluctuates repeatedly between 
    0 and 1.5 kip, what is the factor of safety 
    against yielding if one, 5/16”-18, SAE grade 8 
    bolt is used? """
    kb = 2.4 #Mlbf/in
    km = 4 #Mlbf/in
    P = 1.5 #kip
    Sp = 120 #kpsi Because fatigue, we must use minimum proof strength (Table 8-9)
    # Ssy = .577*Sy
    d = 5/16
    At = 0.0524 #in^2
    Fi = 0.75*At*Sp
    C = kb/(kb+km)
    n = Sp*At/(C*P+Fi)
    print(n)

def Problem6():
    """Given the figure below, what is the maximum 
    tensile load in lbf that can be applied to the 
    joint to ensure a factor of safely of 1.5 against 
    bearing on the members? Assume the members to be 
    made of SAE 1020 CD steel, and that both bolts are 
    SAE grade 7, have no preload, and support the load 
    evenly."""
    n = 1.5
    Sy = 57 #Kpsi Table A-20
    Ab = 2*1/4*1/4 #in^2
    sigmaB = Sy/n
    F = sigmaB*Ab
    print(F)

def Problem7():
    """Given the figure below, what is the minimum UNC 
    bolt size that can be used to support the loading 
    shown with a factor of safety of 1.5 against shearing 
    across the threads? Assume the bolts are SAE grade 4."""

def Problem8():
    """Given the figure below, what is the maximum force F 
    in kip that will cause an allowable shear stress of 34 
    kpsi given the following dimensions?
    b = 3 in, d = 2 in, h = 0.3 in"""
    b = 3 #in
    d = 2 #in
    h = 0.3 #in
    A = 0.707*h*(2*b+d)
    tau = 34 #kpsi
    Kfs = 2.7 # Table 9-5
    F = tau*0.707*h*3
    print(F)

def Problem9():
    """Given the figure below, what is the maximum force F 
    in kip that will cause an allowable shear stress of 36 
    kpsi given the following dimensions?
    b = 3 in, c = 6 in, d = 1.7 in, h = 0.3 in"""
    b = 3 #in
    c = 6 #in
    d = 1.7 #in
    h = 0.3 #in
    tau = 36
    tau1 = 1/(1.414*h*b)
    Ju = b*(3*d**2 + b**2)/6
    J = 0.707*h*Ju
    r = c + b/2
    ry = b/2
    rx = d/2
    tauy = r*ry/J
    taux = r*rx/J
    taumax = np.sqrt(taux**2 + (tau1 + tauy)**2)
    F = tau/taumax
    print(F)

def Problem9Test():
    """Given the figure below, what is the maximum force F 
    in kip that will cause an allowable shear stress of 36 
    kpsi given the following dimensions?
    b = 3 in, c = 6 in, d = 1.7 in, h = 0.3 in"""
    b = 4 #in
    c = 6 #in
    d = 2 #in
    h = 5/16 #in
    tau = 25
    tau1 = 1/(1.414*h*b)
    Ju = b*(3*d**2 + b**2)/6
    J = 0.707*h*Ju
    r = c + b/2
    ry = b/2
    rx = d/2
    tauy = r*ry/J
    taux = r*rx/J
    taumax = np.sqrt(taux**2 + (tau1 + tauy)**2)
    F = tau/taumax
    print(F)

def Problem11():
    """"""

# Problem2()
# Problem3()
# Problem4()
# Problem5()
# Problem6()
# Problem7()
# Problem8()
Problem9()
# Problem11()