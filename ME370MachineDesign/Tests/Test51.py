import numpy as np
from ZachsPackage import Screw

def Problem2():
    """ CORRECT
    What is the torque, in pound-inches, required 
    to raise a 7 kip load using a square thread power 
    screw with a major diameter of 1.5 inches and a 
    pitch of 0.2 inches, and a collar with mean diameter 
    of 2.8 inches? Assume the screw to be single threaded 
    and the friction on the thread and collar to be 0.14."""
    F = 7000 #kip
    dc = 2.8 #in
    d = 1.5 #in (Major diameter)
    p = 0.2 #in
    dm = d-p/2 # (Median diameter)
    ft = 0.14
    l = p #Single threaded
    ans = Screw.TorqueToRaiseWCollar(F, ft, ft, dm, dc, l)
    print(ans)

def Problem3():
    """WRONG
    Supposing that you need to clamp a 1.3" thick steel 
    plate with a 0.5" thick brass plate using a 1/4"-20 
    through-hole bolt and nut, what is the stiffness of the 
    members in Mlbf/in? Assume there isn't a need for a washer."""
    steel = 1.3 # in
    brass = 0.5 # in
    d = .25 # in
    D = 1.5*d 
    l =  steel + brass #in grip length
    ksteel = Screw.SpringRate(30, d, D, steel)
    kbrass = Screw.SpringRate(15.4, d, D, brass)
    k = 1/(1/ksteel + 1/kbrass)
    print(k)

def Problem3Test():
    """ Problem 8-33"""
    steel = 20 # mm
    brass = 20 # mm
    d = 12 # in
    D = 1.5*d 
    l =  steel + brass #in grip length
    ksteel = Screw.SpringRate(207, d, D, steel)
    kbrass = Screw.SpringRate(100, d, D, brass)
    k = 1/(1/ksteel + 1/kbrass)
    print(k)

def Problem4():
    """CORRECT
    Given a non-permanent bolted joint with a bolt stiffness 
    of 3 Mlbf/in and a member stiffness of 4 Mlbf/in that is 
    supporting a tensile load of 12 kip, what minimum SAE grade 
    bolt should be used to ensure a factor of safety against 
    exceeding the proof strength of at least 1.1 if 6, 5/16"-18 
    bolts are used?"""
    kbolt = 3000 #Klbf/in
    km = 4000 #Klbf/in
    F = 12/6 #kip
    At = 0.0524 #in^2
    Ps = 105 #kpsi change this value for the different SAE specs (7=105 proof strength)
    C = kbolt/(kbolt+km)
    Fi = 0.75*At*Ps
    n = Ps/((C*F+Fi)/At)
    print(n)
    
def Problem5():
    """WRONG
    Given a non-permanent bolted joint with a bolt stiffness 
    of 2.4 Mlbf/in and a member stiffness of 3.5 Mlbf/in that is 
    supporting a tensile load that fluctuates repeatedly between 
    0 and 2.1 kip, what is the factor of safety against fatigue 
    failure if one, 5/16”-18, SAE grade 8 bolt is used? Use Goodman 
    theory if needed."""
    kb = 2400 #klbf/in
    km = 3500 #klbf/in
    P = 2.1 #kip
    Sy = 130 #kpsi
    d = 5/16
    At = 0.0524 #in^2
    Fi = 0.75*At*Sy
    C = kb/(kb+km)
    sigmaI = Fi/At
    sigmaA = C*P/(2*At)
    sigmaM = sigmaA + sigmaI
    Sut = 150 #kpsi   Table 8-9
    Se = 23.2 #kpsi   Table 8-17
    n = Screw.Goodman(Se, Sut, sigmaI, sigmaA, sigmaM)
    print(n)

def Problem6():
    """CORRECT
    Given the figure below, what is the maximum tensile load in 
    lbf that can be applied to the joint to ensure a factor of safely 
    of 1.3 against bearing on the members? Assume the members to be 
    made of SAE 1020 CD steel, and that both bolts are SAE grade 8, 
    have no preload, and support the load evenly."""
    n = 1.3
    Sut = 68 #Kpsi Table A-20
    Sy = 57 #Kpsi Table A-20
    Sutb = 150 #Kpsi Table 8-9
    Syb = 130 #Kpsi ""
    Spb = 120 #Kpsi ""
    Ab = 2*1/4*1/4
    sigmaB = Sy/n
    F = sigmaB*Ab
    print(F)

def Problem6Test():
    """Problem 8-70 
    plugging in known factor of safety, n, to get
    original load"""
    n = 2.68
    Sut = 68 #Kpsi Table A-20
    Sy = 57 #Kpsi Table A-20
    Sutb = 150 #Kpsi Table 8-9
    Syb = 130 #Kpsi ""
    Spb = 120 #Kpsi ""
    Ab = 3*1/4*5/16
    sigmaB = Sy/n
    F = sigmaB*Ab
    print(F)

def Problem7():
    """WRONG
    Given the figure below, what is the minimum 
    UNC bolt size that can be used to support the 
    loading shown with a factor of safety of 1.5 
    against shearing across the threads? Assume the 
    bolts are SAE grade 4."""
    n = 1.5
    Sut = 115
    Sy = 100000
    Ssy = .577*Sy
    V = 250 #lbf
    #primary shear
    F1 = V/2
    M = V*14.5
    r = 1.5 #in
    F2 = M*r/(2*r**2)
    Fmax = F1+F2
    A = n*Fmax/(Ssy)
    d = np.sqrt(4*A/np.pi)
    print(d)

def Problem8():
    """CORRECT
    Given the figure below, what is the maximum 
    allowable force F in kip that can be applied if 
    the horizontal bar and vertical support are both 
    made of AISI 1020 CD steel and an E60xx electrode 
    is used, given the following dimensions?
    b = 1 in, d = 1 in, h = 0.4 in"""
    b = 1 #in
    d = 1 #in
    h = 0.4 #in
    A = 0.707*h*(2*b+d)
    x = b**2/(2*b+d)
    y = d/2
    tau = 18
    f = 12.73*h
    F = f*3
    print(F)
    Sut = 55
    Sy = 30
    print(0.3*Sut)
    print(0.4*Sy)
    F = 0.4*Sy*A
    print(F)

def Problem9():
    """WRONG
    Given the figure below, what is the maximum 
    force F in kip that will cause an allowable shear 
    stress of 30 kpsi given the following dimensions?
    b = 2.9 in, c = 5 in, d = 1.8 in, h = 0.4 in"""
    b = 2.9
    c = 5
    d = 1.8
    h = 0.4
    tauAllow = 30
    Marm = c+b/2
    r = d/2
    A = 1.414*(h*b)
    Ju = d*(3*b**2+d**2)/6
    J = 0.707*h*Ju
    tau1 = 1/A
    tau2 = Marm*r/J
    tauMax = np.sqrt(tau2**2+(tau1+tau2)**2)
    F = tauAllow/tauMax
    print(F)

def Problem9Test():
    """ Problem 9-18"""
    b = 2
    c = 6
    d = 2
    h = 5/16
    tauAllow = 25
    Marm = c+b/2
    r = d/2
    A = 1.414*(h*b)
    Ju = d*(3*b**2+d**2)/6
    J = 0.707*h*Ju
    tau1 = 1/A
    tau2 = Marm*r/J
    tauMax = np.sqrt(tau2**2+(tau1+tau2)**2)
    F = tauAllow/tauMax
    print(F)

def Problem11():
    """CORRECT
    What is the tensile stress in psi on a 1/4"-20 SAE 
    grade 8 bolt if it undergoes a load of 203 lbs? """
    d = 1/4
    At = 0.0318
    F = 203
    tau = F/At
    print(tau)

# Problem2()
# Problem3()
# Problem4()
# Problem5()
# Problem6()
# Problem7()
# Problem8()
# Problem9()
Problem11()