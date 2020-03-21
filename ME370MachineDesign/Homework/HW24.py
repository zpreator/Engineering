from ZachsPackage import Screw

def Problem8_1():
    d = 25 #mm
    pitch = 5 #mm
    threadDepth = pitch/2
    threadWidth = pitch/2
    dm = d - pitch/2
    dr = d - pitch
    l = pitch
    print(threadDepth, threadWidth, dm, dr, l)

    threadWidth = 0.3707*pitch
    print(threadDepth, threadWidth, dm, dr, l)

def Problem8_4():
    d = 25 #mm
    p = 5 #mm
    F = 5 #Kn
    fc = 0.06
    ft = 0.09
    dc = 45 #mm
    dm = d - p/2
    l = p * 1 # Single threaded, n = 1
    Tr = Screw.TorqueToRaiseWCollar(F, ft, fc, dm, dc, l) 
    Tl = Screw.TorqueToLowerWCollar(F, ft, fc, dm, dc, l)
    e = Screw.Efficiency(F, l, Tr)
    print(Tr, Tl, e)

def Problem8_8():
    d = 0.75 #in
    ft = 0.15
    fc = ft
    p = 1/6
    dc = 1 #in
    F = 8 #lbf
    r = 3.5 #in
    T = F * r
    dm = d - p/2
    l = p
    F = Screw.ForceFromTorqueRaiseCollar(T, dm, dc, ft, fc, l)
    print(F)

Problem8_1()
Problem8_4()
Problem8_8()
