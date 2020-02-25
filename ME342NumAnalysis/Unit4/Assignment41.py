import numpy as np

""" 
Zachary Preator
10/10
"""
def Function(x):
    """ The starting function"""
    return -.1*x**4-.15*x**3-.5*x**2-.25*x+1.2

def Forward1(f, x, xPoints):
    """ Computes the first order forward first derivative """
    L = []
    for i in range(len(x)-1):
        L.append((f(x[i+1])-f(x[i]))/(x[i+1]-x[i]))
    L.append(0)
    indexes = [np.argwhere(x == i)[0][0] for i in xPoints]
    # e = -(F1[index]-der)/der*100
    derivs = [L[i] for i in indexes]
    return derivs

def Backward1(f, x, xPoints):
    """ Computes the first order backward first derivative """
    L = [0]
    for i in range(len(x)-1):
        L.append((f(x[i+1])-f(x[i]))/(x[i+1]-x[i]))
    indexes = [np.argwhere(x == i)[0][0] for i in xPoints]
    derivs = [L[i] for i in indexes]
    return derivs

def Central2(f, x, xPoints):
    """ Computes the second order central first derivative """
    L = [0]
    for i in range(1,len(x)-1):
        c = (f(x[i+1])-f(x[i-1]))/(x[i+1]-x[i-1])
        L.append(c)
    indexes = [np.argwhere(x == i)[0][0] for i in xPoints]
    derivs = [L[i] for i in indexes]
    return derivs

def Forward2(f, x, xPoints):
    """ Computes the second order forward first derivative """
    L = []
    for i in range(len(x)-2):
        c = (-f(x[i+2])+4*f(x[i+1])-3*f(x[i]))/(x[i+2]-x[i])
        L.append(c)
    indexes = [np.argwhere(x == i)[0][0] for i in xPoints]
    L.append(L[-1])
    derivs = [L[i] for i in indexes]
    return derivs

def Backward2(f, x, xPoints):
    """ Computes the second order backward first derivative """
    L = [0, 0]
    for i in range(2, len(x)):
        c = (3*f(x[i])-4*f(x[i-1])+f(x[i-2]))/(x[i]-x[i-2])
        L.append(c)
    indexes = [np.argwhere(x == i)[0][0] for i in xPoints]
    derivs = [L[i] for i in indexes]
    return derivs

def Central4(f, x, xPoints):
    """ Computes the fourth order central first derivative """
    L = [0,0]
    for i in range(2, len(x)-2):
        c = (-f(x[i+2])+8*f(x[i+1])-8*f(x[i-1])+f(x[i-2]))/(12*(x[i+1]-x[i]))
        L.append(c)
    indexes = [np.argwhere(x == i)[0][0] for i in xPoints]
    L.append(L[-1])
    derivs = [L[i] for i in indexes]
    return derivs

def Error(val, true):
    """ returns the error using the true value"""
    return -(val-true)/(true)*100

def TrueDer(x):
    """ This is the symbolic derivative which will return
    the actual for error checking"""
    return -4*0.1*x**3-3*0.15*x**2-2*0.5*x-0.25

def GetErrors(sortedDer, xPoints):
    """ Takes the sorted table and replaces the derivatives
    with their respective errors, don't ask why I did it 
    this way"""
    col = []
    for i in range(len(sortedDer)):
        row = []
        for j in sortedDer[i]:
            row.append(Error(j, TrueDer(xPoints[i])))
        col.append(row)
    return col

def Display(dontCare):
    """ Displays the dontcare item"""
    text = [r'$0.5$', r'$1.0$', r'$1.5$']
    j = 0
    print(    'Value | Forward 1 | Backward 1| Central 2 | Forward 2 | Backward 2| Central 4 |')
    print(    '===============================================================================')
    for i in dontCare:
        print(text[j], '|{0:11.2f}|{1:11.2f}|{2:11.2f}|{3:11.2f}|{4:11.2f}|{5:11.2f}|'.format(*i))
        j += 1

def main():
    """ calls all the functions to create the table of errors"""
    h = 0.25
    x = np.arange(0, 2, h)
    points = [0.5, 1.0, 1.5]
    F1 = Forward1(Function, x, points)
    B1 = Backward1(Function, x, points)
    C2 = Central2(Function, x, points)
    F2 = Forward2(Function, x, points)
    B2 = Backward2(Function, x, points)
    C4 = Central4(Function, x, points)
    sortedDer = np.array([F1, B1, C2, F2, B2, C4]).T.tolist()
    Errors = GetErrors(sortedDer, points)
    Display(Errors)


main()