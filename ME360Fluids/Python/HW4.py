import numpy as np
from scipy.integrate import quad

def Problem2(L, w, V1, V2):
    a = V1
    c = (V2-a)/(L**2)
    rho = 1000
    Vavg = 1/(L*w)*w*(a*L+c/3*L**3)
    Vdot = Vavg*L*w
    print(Vdot)
    eq1 = lambda x: w*rho*(a+c*x**2)**2
    integral = quad(eq1, 0, L)
    print(integral)

def Problem3LossPipe(L, D, V):
    g = 9.81 # m/s^2
    return 0.02*L/D*V**2/(2*g)

def Problem3LossValve(K, V):
    g = 9.81 # m/s^2
    return K*V**2/(2*g)

def Problem3(D1, D2, h, D3, K, Ve):
    rho = 1000 # kg/m^3
    g = 9.81 # m/s^2
    # Calculating the areas
    A1 = np.pi/4*D1**2
    A2 = np.pi/4*D2**2
    A3 = np.pi/4*D3**2

    # Mdot
    mDot = A3 * Ve * rho

    # Using conservation of mass to calculate velocities
    V1 = Ve*A3/A1
    V2 = Ve*A3/A2
    V3 = Ve

    # Calculating losses
    pipeLoss = Problem3LossPipe(h, D2, V2)
    valveLoss = Problem3LossValve(K, V2)

    # Using engergy equation to compute Pressure
    P2 = rho*g*((V3**2-V2**2)/(2*g) - h + pipeLoss + valveLoss)
    P1 = P2+rho*(V2**2-V1**2)/2

    F = 4/5*P1*A1 + mDot*(4/5 * V1 - V3)
    print(F)
    

# Problem2(1.2, 0.005, 3, 7)
# Problem2(1.35, 0.0042, 2.4, 7.3)

# Problem3(0.12, 0.05, 5, 0.03, 10, 30)
Problem3(0.10, 0.045, 5.2, 0.03, 10, 28.7)

