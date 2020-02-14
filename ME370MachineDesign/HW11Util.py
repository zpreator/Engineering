import scipy.integrate as i

def CastiglianoBending(l, E, I):
    f = lambda x: 35*x**3/12+150*x**2
    n = i.quad(f, 0, l)
    num = n[0]/(E*I)
    return num