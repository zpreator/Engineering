import math
import sys
import numpy as np
from time import perf_counter as time
"""
Zachary Preator
Functionality - 20.0
Style and Efficiency - 5.0
Documentation - 5.0
"""
def Friction(constants, variables):
    """ Friction equation"""
    P1, P2, z1, z2, L, hp, Km, epsilon, rho, nu, g, boo = constants
    f, D, Vdot, Re = variables 
    return -2*np.log10((epsilon/D)/3.7+2.51/(Re*np.sqrt(f)))-1/np.sqrt(f)
    

def ReynoldsNum(constants, variables):
    """ Reynolds number"""
    P1, P2, z1, z2, L, hp, Km, epsilon, rho, nu, g, boo = constants
    f, D, Vdot, Re = variables
    return 4*Vdot/(math.pi*nu*D)
    

def EnergyVdot(constants, variables):
    """ Energy equation to return Vdot"""
    P1, P2, z1, z2, L, hp, Km, epsilon, rho, nu, g, boo = constants
    f, D, Vdot, Re = variables 
    return math.sqrt((P1/(rho*g)+z1+hp-P2/(rho*g)-z2)/(f*L/D+Km)*(math.pi**2*g*D**4)/8)

def EnergyDia(constants, variables):
    """ Energy equation for root finding with D """
    P1, P2, z1, z2, L, hp, Km, epsilon, rho, nu, g, boo = constants
    f, D, Vdot, Re = variables 
    return P1/(rho*g)+z1+hp-P2/(rho*g)-z2-(f*L/D+Km)*8*Vdot**2/(math.pi**2*g*D**4)

def secant(f, guess0, guess1, c, errorMax = 1E-6):
    """ Taks a function reference and any two lists of guesses
        where one variable is a guess and the rest are constant 
        i is the index of the guess in the lists"""
    i = c[11] 
    e = 1
    while e > errorMax:
        gnew = list(guess0)
        gnew[i] = guess1[i] - (f(c, guess1)*(guess0[i]-guess1[i]))/(f(c, guess0)-f(c, guess1))
        guess0 = list(guess1)
        guess1[i] = gnew[i]
        e = abs(gnew[i] - guess0[i])/gnew[i]
    return gnew[i]

def pipeFlow(P1, P2, z1, z2, L, hp, Km, epsilon, rho, nu, g, f, D, Vdot, Vdot_D):
    """ Gets the pipe flow volume flow rate or diameter with inputs:
        P1 = Kpa (pressure 1) 0
        P2 = Kpa (pressure 2) 1
        z1 = m (elevation 1) 2
        z2 = m (elevation 2) 3
        L = m (Length of pipe) 4
        hp = J/N (m) (Pump head) 5
        Km = unitless (Sum of minor losses) 6
        epsilon = mm (Pipe Roughness) 7
        rho = kg/m^3 (Density) 8
        nu = kkg/m^3 (Kinematic viscosity) 9
        g = m/s^2 (Accel. of gravity) 10
        f = 0.01-0.06 (friction guess) 0
        D = cm (diameter) 1
        Vdot = m^3/s (Flow rate) 2"""
    
    # Assigning to lists of constants and variables
    constants = [P1, P2, z1, z2, L, hp, Km, epsilon, rho, nu, g, 0]
    # note
    # constants = {"P1":P1, "P2":P2, "z1":z1, "z2":z2, "L":L, "hp":hp, "Km":Km, "epsilon":epsilon, "rho":rho, "nu":nu, "g":g, "Secant Index":0}
    # This ^ would be way easier to read later, but I already have these stupid lists. 10/10 would recommend doing this instead
    # As a dictionary you could keep everything and reference it by the string. For example constants["P1"] would give you the value
    # for P1 and the dictionary could be 1 argument instead of 100000000000 arguments

    # Assigning variables with an empty slot for Reynolds boi
    variables = [f, D, Vdot, 0]
    
    # Conversions
    constants[0] = constants[0]*1000 #Kpa to pa
    constants[1] = constants[1]*1000 #Kpa to pa
    constants[7] = constants[7]/1000 #mm to m
    variables[1] = variables[1]/100 #cm to m

    # Fake variables list for second guesses in secant function
    variables2 = list(variables) 

    # For whale loooooop
    e, errorMax = 1, 1E-6
    
    # Just gotta not randomly guess the first number.. 100 seems good
    old = 100

    # Whale looooooop
    while e > errorMax:
        if Vdot_D == 'Vdot':
            # Case where volume flow rate is wanted #2 slot in variables is for Vdot
            variables[2] = EnergyVdot(constants, variables)
        elif Vdot_D == 'D':
            constants[11] = 1 # This will tell our secant function to look at #1 index in the variables list which is Diameter
            variables2[1] = variables[1]+0.01 # Using our dummy list, slot 2 will contain a different num for secant method guess
            variables[1] = secant(EnergyDia, variables, variables2, constants) # Send two lists to secant funct along with all the constants
        else:
            sys.exit()

        # Getting reynolds number given the new variables
        variables[3] = ReynoldsNum(constants, variables) 
        
        variables2[3] = variables[3] # Don't remember exactly what this was for..

        variables2[0] = variables[0]+0.01 # same deal as before, just getting a second different guess
        constants[11] = 0 # Telling our secant function to use index 0 or friction
        variables[0] = secant(Friction, variables, variables2, constants)
        
        # Calculates error based on 'old' which will be like crazy big the first iteration haha
        if Vdot_D == 'Vdot':
            e = abs(variables[2] - old)/variables[2] 
            old = variables[2]
        elif Vdot_D == 'D':
            e = abs(variables[1] - old)/variables[1]
            old = variables[1]

    # Returns the desired output
    if Vdot_D == 'Vdot':
        return variables[2]
    elif Vdot_D == 'D':
        return variables[1]*100 # converting back to cm from m
    

def main():
    t1 = time()
    vdot = pipeFlow(350, 425, 0, 12, 225, 56, 16.2, 0.045, 998, 1.004E-6, 9.81, 0.01, 5.25, 0.05, 'Vdot')
    print(vdot)
    t2 = time()
    t = t2-t1
    print(t)
    D = pipeFlow(350, 425, 0, 12, 225, 56, 16.2, 0.045, 998, 1.004E-6, 9.81, 0.01, 5.25, 0.05, 'D')
    print(D)

main()