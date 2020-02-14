import math
import numpy as np
import sys
"""
Zachary Preator
10/10
program works well and correct answers are obtained
"""
def f1(var):
    """ Inputs a list of 3 variables
        x
        y
        z """
    x,y,z = var
    return np.cos(y+x**2) + z

def sign(x):
    """ Returns -1 if x is negative
        and 1 if x is positive """
    if x < 0:
        return -1
    else:
        return 1

def bisectionMD(f, guess1, guess2, maxError = 1E-6):
    """ Takes a function reference and two lists of guesses
        and computes the root by bisectin method.
        *Guesses must straddle root sign(f(x1)) != sign(f(x2))"""
    for j in range(len(guess1)):
        if guess1[j] != guess2[j]:
            i = j
            break
    
    if (f(guess1) > 0 and f(guess2) > 0) or (f(guess1) < 0 and  f(guess2) < 0):
        sys.exit()

    gnew = list(guess1)
    e = 1
    while e > maxError:
        gnew[i] = (guess1[i] + guess2[i])/2
        if sign(f(gnew)) == sign(f(guess1)):
            old = list(guess1)
            guess1 = list(gnew)
        else:
            old = list(guess2)
            guess2 = list(gnew)
        e = abs(gnew[i] - old[i])/gnew[i]

    return gnew
        
def secantMD(f, guess0, guess1, errorMax = 1E-6):
    """ Taks a function reference and any two lists of guesses
        where one variable is a guess and the rest are constant """
    for j in range(len(guess1)):
        if guess0[j] != guess1[j]:
            i = j
            break
    e = 1
    while e > errorMax:
        gnew = list(guess0)
        gnew[i] = guess1[i] - (f(guess1)*(guess0[i]-guess1[i]))/(f(guess0)-f(guess1))
        guess0 = list(guess1)
        guess1[i] = gnew[i]
        e = abs(gnew[i] - guess0[i])/gnew[i]
    return gnew

def main():
    """ Calls the bisection and secant methods"""
    bis1 = bisectionMD(f1, [1, 2.5, 0.2], [2, 2.5, 0.2])
    bis2 = bisectionMD(f1, [1.4, 2, 0.2], [1.4, 3, 0.2])
    sec1 = secantMD(f1, [1, 2.5, 0.2], [2, 2.5, 0.2])
    sec2 = secantMD(f1, [1.4, 2, 0.2], [1.4, 3, 0.2])
    print(bis1, bis2, sec1, sec2)

main()