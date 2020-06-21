import numpy as np
from ZachsPackage import Screw

def Problem2():
    """What is the torque, in pound-inches, 
    required to raise a 6 kip load using a 
    square thread power screw with a major 
    diameter of 2.3 inches and a pitch of 
    0.2 inches? Assume the screw to be single 
    threaded and the friction on the thread 
    to be 0.15. There is no collar."""
    F = 6000 #lb
    # dc = 2.8 #in
    d = 2.3 #in (Major diameter)
    p = 0.2 #in
    dm = d-p/2 # (Median diameter)
    ft = 0.14
    l = p #Single threaded
    ans = Screw.TorqueRaiseThread(F, dm, ft, l)
    print(ans)

def Problem3():
    """Supposing that you need to clamp a 0.4" 
    thick steel plate with a 0.4" thick brass 
    plate using a 1/4"-20 through-hole bolt and 
    nut, what is the stiffness of the members 
    in Mlbf/in? Assume there isn't a need for 
    a washer."""
    tan = 0.5773502692
    t1 = 0.4 #in
    t2 = 0.4 #in
    d = 0.25 #in
    D2 = 1.5*d
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

def Problem3Test():
    """Supposing that you need to clamp a 0.4" 
    thick steel plate with a 0.4" thick brass 
    plate using a 1/4"-20 through-hole bolt and 
    nut, what is the stiffness of the members 
    in Mlbf/in? Assume there isn't a need for 
    a washer."""
    tan = 0.5773502692
    t1 = 20 #in
    t2 = 20 #in
    d = 12 #in
    D2 = 1.5*d
    l = t1 + d/2
    D1 = D2 + l*tan
    a = t1 - l/2
    b = l - t1
    D3 = D1 - 2*a*0*tan
    k1 = Screw.SpringRate(207, d, D2, l/2)
    k2 = Screw.SpringRate(207, d, D3, a)
    k3 = Screw.SpringRate(100, d, D2, b)
    ans = 1/(1/k1 + 1/k2 + 1/k3)
    print(ans)

def Problem4():
    """What is the factor of safety against exceeding 
    the proof strength if 4, 3/8"-16, SAE grade 5 bolts, 
    each having a bolt stiffness of 3.5 Mlbf/in, are 
    used in a non-permanent bolted joint to clamp members 
    with a stiffness of 6.9 Mlbf/in, and is supporting a 
    total tensile load of 11 kip? """
    kbolt = 3500 #Klbf/in
    km = 6900 #Klbf/in
    F = 11/4 #kip
    At = 0.0775 #in^2
    Ps = 85 #kpsi change this value for the different SAE specs (7=105 proof strength)
    C = kbolt/(kbolt+km)
    Fi = 0.75*At*Ps
    n = Ps/((C*F+Fi)/At)
    print(n)

def Problem5():
    """ Given a non-permanent bolted joint with a bolt 
    stiffness of 2.5 Mlbf/in and a member stiffness of 3.7 
    Mlbf/in that is supporting a tensile load that fluctuates 
    repeatedly between 0 and 1.7 kip, what is the factor of 
    safety against yielding if one, 5/16”-18, SAE grade 8 
    bolt is used?"""
    kb = 2.5 #Mlbf/in
    km = 3.7 #Mlbf/in
    P = 1.7 #kip
    Sp = 120 #kpsi Because fatigue, we must use minimum proof strength (Table 8-9)
    # Ssy = .577*Sy
    d = 5/16
    At = 0.0524 #in^2
    Fi = 0.75*At*Sp
    C = kb/(kb+km)
    n = Sp*At/(C*P+Fi)
    print(n)

def Problem5Test():
    """Example 8-5"""
    kb = 6.78 #Mlbf/in
    km = 17.4 #Mlbf/in
    P = 5 #kip
    Sp = 85 #kpsi Because fatigue, we must use minimum proof strength (Table 8-9)
    # Ssy = .577*Sy
    d = 5/16
    At = 0.226 #in^2
    Fi = 0.75*At*Sp
    C = kb/(kb+km)
    n = Sp*At/(C*P+Fi)
    print(n)

def Problem6():
    """CORRECT
    Given the figure below, what is the maximum tensile load in 
    lbf that can be applied to the joint to ensure a factor of safely 
    of 1.3 against bearing on the members? Assume the members to be 
    made of SAE 1020 CD steel, and that both bolts are SAE grade 7, 
    have no preload, and support the load evenly."""
    n = 1.3
    Sut = 68 #Kpsi Table A-20
    Sy = 57 #Kpsi Table A-20
    Sutb = 133 #Kpsi Table 8-9
    Syb = 115 #Kpsi ""
    Spb = 105 #Kpsi ""
    Ab = 2*1/4*1/4
    sigmaB = Sy/n
    F = sigmaB*Ab
    print(F)

def Problem7():
    """
    Given the figure below, what is the minimum 
    UNC bolt size that can be used to support the 
    loading shown with a factor of safety of 1.5 
    against shearing across the threads? Assume the 
    bolts are SAE grade 4."""
    d = .25
    F = 250 #lbf
    M = 14.5*F
    F1 = M/3
    V = F/2
    Fa = F1 - V
    Fb = F1 + V
    As = np.pi/4*d**2
    tau = Fb/As
    n = 57700/tau
    print(n)

def Problem8():
    """
    Given the figure below, what is the 
    maximum force F in kip that will cause 
    an allowable shear stress of 34 kpsi 
    given the following dimensions?"""
    b = 1 #in
    d = 1 #in
    h = 0.4 #in
    A = 0.707*h*(2*b+d)
    tau = 34 #kpsi
    Kfs = 2.7 # Table 9-5
    F = tau*0.707*h*3
    print(F)

def Problem9():
    """Given the figure below, what is the 
    maximum force F in kip that will cause 
    an allowable shear stress of 28 kpsi 
    given the following dimensions?
    b = 2.3 in, c = 5 in, d = 1.5 in, h = 0.3 in"""
    b = 2.3
    c = 5
    d = 1.5
    h = 0.3
    tau = 25
    tau1 = 1/(1.414*h*(b+d))
    Ju = (b+d)**3/6
    J = 0.707*h*Ju
    r = c + b/2
    ry = d/2
    tau2 = r*ry/J
    taumax = np.sqrt(tau2**2 + (tau1 + tau2)**2)
    F = tau/taumax
    print(F)

def Problem9Test():
    """Problem 9-22"""
    b = 2
    c = 6
    d = 2
    h = 5/16
    tau = 25
    tau1 = 1/(1.414*h*(b+d))
    Ju = (b+d)**3/6
    J = 0.707*h*Ju
    r = c + b/2
    ry = d/2
    tau2 = r*ry/J
    taumax = np.sqrt(tau2**2 + (tau1 + tau2)**2)
    F = tau/taumax
    print(F)

def Problem11():
    """What is the maximum tensile load in pounds 
    that can be applied to a 1/4"-20 SAE grade 8 
    bolt before it acquires a permanent set or is 
    considered to have failed? """
    d = .25
    sy = 130
    At = 0.0318
    F = At*sy
    print(F)

# Problem2()
# Problem3()
# Problem4()
# Problem5()
# Problem6()
# Problem7()
# Problem8()
# Problem9()
Problem11()