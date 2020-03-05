import numpy as np
import matplotlib.pyplot as plt
"""
Zachary Preator
Mastery Level: 10
"""
def K1(f, t, y, h):
    """ Returns the k1 calculations"""
    return f(t, y)

def K2(f, t, y, h, K1):
    """ Returns the k2 calculations"""
    a = t + .5*h
    b = y + .5*h*K1
    return f(a, b)

def K3(f, t, y, h, K2):
    """ Returns the k3 calculations"""
    a = t + .5*h
    b = y + .5*h*K2
    return f(a, b)

def K4(f, t, y, h, K3):
    """ Returns the k4 calculations"""
    a = t + h
    b = y + h*K3
    return f(a, b)

function1 = lambda t, y: y*(np.sin(t))**3

function2 = lambda t, y: 4*np.exp(0.8*t)-0.5*y

function3 = lambda t, y: -2 * t ** 3 + 12 * t ** 2 - 20 * t + 8.5

function4 = lambda t, y: 9.81 - 12.5 / 68.1 * y

def RK4(f, t, y, h):
    """ Calls the k functions and calculates the
    next y (y+1) and returns that y for an ODE f"""
    k1 = K1(f, t, y, h)
    k2 = K2(f, t, y, h, k1)
    k3 = K3(f, t, y, h, k2)
    k4 = K4(f, t, y, h, k3)
    y1 = y + 1/6*(k1 + 2*k2 + 2*k3 + k4)*h
    return y1

def Eulers(f, t, y, h):
    """ Returns the Euler's method for the ODE f"""
    return y + f(t, y)*h

def Display(data, plot):
    """ Displays the two plots for each Case"""
    plotType = ['Runge-Kutta method', 'Euler\'s Method']
    for i in range(len(data[0])):
        plt.plot(data[i][0], data[i][1], label=plotType[i])
        
    plt.legend(loc='best')
    plt.savefig('{0}.pdf'.format(plot))
    plt.show()
    
def GetStuff(f, y0, desiredY, h):
    """ Gets the y values incrementally from
    the Runge-Kutta method and Euler method 
    and sends them to the display function"""
    g = desiredY
    y = y0

    # Runge-kutta
    RKy = []
    RKt = []
    
    for i in np.arange(0, g, h):
        RKt.append(i)
        y = RK4(f, i, y, h)
        RKy.append(y)
    RK = [RKt, RKy]

    y1 = y0
    # Eulers
    # Euler = [[j for j in np.arange(0, g, h)], [Eulers(f, i, y1, h) for i in np.arange(0, g, h)]]
    Ey = []
    Et = []
    for i in np.arange(0, g, h):
        Et.append(i)
        y1 = Eulers(f, i, y1, h)
        Ey.append(y1)
    E = [Et, Ey]

    return [RK, E]

def main():
    Display(GetStuff(function1, 1, 6, 1), 'Case1')
    Display(GetStuff(function2, 2, 4, 1), 'Case2')
    Display(GetStuff(function3, 1, 4, 0.5), 'Case3')
    Display(GetStuff(function4, 0, 20, 2), 'Case4')

main()