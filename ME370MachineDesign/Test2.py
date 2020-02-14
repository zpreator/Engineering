import math

def question3():
    d = 0.468 #in
    I = math.pi/64*d**4 #in^4
    E = 29E6 #psi
    m = E*I/120 #10ft to in
    print(m)

def question4():
    E = 1.5E6 #psi
    Lab = 32 #in
    Lbc = 103 #in
    b = 14 #in
    h = 1.6 #in
    I = b*h**3/12 #in^4
    

question3()