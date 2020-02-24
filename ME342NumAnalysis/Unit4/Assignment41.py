import numpy as np

def Function(x):
    return -.1*x**4-.15*x**3-.5*x**2-.25*x+1.2

def Forward1(f, x, xPoint):
    F1 = []
    der = -.9125
    for i in range(len(x)-1):
        F1.append((f(x[i+1])-f(x[i]))/(x[i+1]-x[i]))
    F1.append(0)
    index = np.argwhere(x == xPoint)[0][0]
    e = abs(F1[index]-der)/F1[index]*100
    return f(x[index]), e

def Backward1(f, x, xPoint):
    B1 = [0]
    der = -.9125
    for i in range(len(x)-1):
        B1.append((f(x[i+1])-f(x[i]))/(x[i+1]-x[i]))
    index = np.argwhere(x==xPoint)[0][0]
    e = abs(B1[index]-der)/B1[index]*100
    return f(x[index]), e

def Central2(f, x, xPoint):
    C2 = [0]
    der = -.9125
    for i in range(1,len(x)-1):
        c = (f(x[i+1])-f(x[i-1]))/(x[i+1]-x[i-1])
        C2.append(c)
    index = np.argwhere(x==xPoint)[0][0]
    e = abs(C2[index]-der)/C2[index]*100
    return f(x[index]), e


# def Central2():

# def Forward2():

# def Backward2():

# def Central4():

def main():
    h = 0.25
    x = np.arange(0, 2, h)
    F1, F1Err = Forward1(Function, x, 0.5)
    B1, B1Err = Backward1(Function, x, 0.5)
    print(F1, F1Err)
    print(B1, B1Err)

main()