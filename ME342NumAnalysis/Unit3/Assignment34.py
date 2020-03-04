import math
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

""" 
Zachary Preator
10/10
"""
def GetData():
    """ Returns the data from the problem x = depths of water, y = temperature"""
    return np.array([[0.0, 2.3, 4.9, 9.1, 13.7, 18.3, 22.9, 27.2],[22.8, 22.8, 22.8, 20.6, 13.9, 11.7, 11.1, 11.1]])

def CubicInter(data):
    """ Returns the cubic spline"""
    return CubicSpline(data[0], data[1])
    
def Display(CS, depth):
    """ Displays the cubic spline and the depth"""
    x = np.arange(0, 27.2, 0.1)
    plt.plot(x, CS(x), 'r',label='Temperature')
    plt.plot(x, CS(x, 1), 'b', label='Gradient')
    plt.plot(x, CS(x, 2), 'g', label='Second Derivative')
    plt.plot(depth, CS(depth), 'ko', label=r'Depth {0:4.1f} $m$, {1:4.2f} $C$'.format(depth, CS(depth)))
    plt.legend(loc='upper right')
    plt.xlabel(r'Depth $m$')
    plt.ylabel(r'Temperature $C$')
    plt.show()

def FindDepth(CS):
    """ Finds the maximum of the first derivative and returns the height"""
    x = np.arange(0, 27.2, 0.1)
    index = np.argmax([abs(CS(i, 1)) for i in x])
    return x[index]

def main():
    """ Calls the cubicInter(), FindDepth(), and Display() functions""" 
    data = GetData()
    CS = CubicInter(data)
    depth = FindDepth(CS)
    Display(CS, depth)
    print(CS(2.3, 1))
    
def CubicInterpolate(data):
    """ Returns the y values for the range of 
    x values"""
    x = np.arange(0, 27.2, 0.1)
    CS = CubicSpline(data[0], data[1])
    zeroth = CS(x)
    first = CS(x, 1)
    second = CS(x, 2)

main()