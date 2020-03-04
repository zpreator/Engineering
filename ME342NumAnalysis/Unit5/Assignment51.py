import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
"""
Zachary Preator
Mastery Level: 10
"""
def x1(t):
    return -np.exp((-2+np.sqrt(2))*t)

def x2(t):
    return -np.exp(-2*t)

def x3(t):
    return -np.exp(-2*t)*(np.cos(2*t)+np.sin(2*t))

def v1(t):
    return -(-2+np.sqrt(2))*np.exp((-2+np.sqrt(2))*t)

def v2(t):
    return 2*np.exp(-2*t)

def v3(t):
    return 4*np.exp(-2*t)*np.sin(2*t)

def display(f, lineType, label='', done = False, xLabel=None, yLabel=None, plotLabel=None):
    """ Displays the function parameter f"""
    t = np.arange(0, 10, 0.1)
    plt.plot(t, f(t), lineType, label=label)
    if (done):
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend(loc='best')
        plt.tight_layout()
        # plt.show()
        plt.savefig('{0}.pdf'.format(plotLabel))

def main():
    """ Calls the display function for each equation of the ODE"""
    # plt.figure must be outside of display to keep them on same plot
    plt.figure(figsize=(6, 4))
    plt.rc('font', family='serif', size=12)

    # Function x1(t) for  k = 10 N/m
    display(x1, '-.', label=r'm = 5, c = 20, k = 10 Over Damped')

    # Function x2(t) for  k = 20 N/m
    display(x2, '--', label=r'm = 5, c = 20, k = 20 Critically Damped')

    # Function x3(t) for  k = 40 N/m, done says to plot all previous if true
    display(x3, ':', label=r'm = 5, c = 20, k = 40 Under Damped',
            done=True,
            xLabel=r'Time (t)',
            yLabel=r'Displacement (x)',
            plotLabel='Displacement')

    plt.figure(figsize=(6, 4))

    # Function v1(t) for k = 10 N/m
    display(v1, '-.', r'm = 5, c = 20, k = 10 Over Damped')

    # Function v2(t) for  k = 20 N/m
    display(v2, '--', r'm = 5, c = 20, k = 20 Critically Damped')

    # Function v3(t) for  k = 40 N/m, done says to plot all previous if true
    display(v3, ':', r'm = 5, c = 20, k = 40 Under Damped', 
            done=True,
            xLabel=r'Time (t)',
            yLabel=r'Velocity (V)',
            plotLabel='Velocity')


main()