import math
import numpy as np
from scipy.interpolate import lagrange, interp1d, interp2d
import matplotlib.pyplot as plt
"""
Zach Preator
10/10 Complet Mastery
"""
def RawData():
    return np.array([[100, 200, 300, 400, 600, 800, 1000],[450, 82, 46, 32.4, 18.9, 13, 10.5]])

def findNearest(values, Temp, k):
    """ Returns the nearsest k x values"""
    difference = [abs(values[0][i] - Temp) 
                  for i in range(len(values[0]))]
    index = np.argsort(difference)
    indexes = index[0:k]

    x = [values[0][i] for i in indexes]
    y = [values[1][i] for i in indexes]
    newData = np.array([x, y])
    return newData

def GetFirstThroughFourthLists(data, xPoint):
    """ Returns the lists for the first through fourth approximations"""
    firstOrder = []
    length = len(data[0])
    for i in range(length-1):
        val = (data[1][i+1]-data[1][i])/(data[0][i+1]-data[0][i])
        firstOrder.append(val)
    
    secondOrder = []
    for i in range(len(firstOrder)-1):
        val = (firstOrder[i+1]-firstOrder[i])/(data[0][i+2]-data[0][i])
        secondOrder.append(val)

    thirdOrder = []
    for i in range(len(secondOrder)-1):
        val = (secondOrder[i+1]-secondOrder[i])/(data[0][i+3]-data[0][i])
        thirdOrder.append(val)

    fourthOrder = []
    for i in range(len(thirdOrder)-1):
        val = (thirdOrder[i+1]-thirdOrder[i])/(data[0][i+4]-data[0][i])
        fourthOrder.append(val)
    return [firstOrder, secondOrder, thirdOrder, fourthOrder]

def FirstOrderEquation(data, firstOrder, xPoint):
    """ Equation for first order approximation"""
    first = data[1][0] + (xPoint -data[0][0])*firstOrder[0]
    return first

def SecondOrderEquation(data, secondOrder, xPoint, first):
    """ Equation for second order approximation"""
    second = first+(xPoint-data[0][0])*(xPoint-data[0][1])*secondOrder[0]
    return second

def ThirdOrderEquation(data, thirdOrder, xPoint, second):
    """ Equation for third order approximation"""
    third = second + (xPoint-data[0][0])*(xPoint-data[0][1])*(xPoint-data[0][2])*thirdOrder[0]
    return third

def FourthOrderEquation(data, fourthOrder, xPoint, third):
    """ Equation for fourth order approximation"""
    fourth = third + (xPoint-data[0][0])*(xPoint-data[0][1])*(xPoint-data[0][2])*(xPoint-data[0][3])*fourthOrder[0]
    return fourth

def display(data, order, vals, xPoint):
    """ Displays the equations and point approximations"""
    x = np.arange(xPoint - 100, xPoint + 100,1) 
    plt.plot(x, FirstOrderEquation(data, order[0], x), 'g')
    plt.plot(xPoint, vals[0], 'g^')
    plt.plot(x, SecondOrderEquation(data, order[1], x, vals[0]), 'k')
    plt.plot(xPoint, vals[1], 'ko')
    plt.plot(x, ThirdOrderEquation(data, order[2], x, vals[1]), 'b')
    plt.plot(xPoint, vals[2], 'b^')
    plt.plot(x, FourthOrderEquation(data, order[3], x, vals[2]), 'r')
    plt.plot(xPoint, vals[3], 'ro')
    plt.legend(['First order','Point', 'Second order', 'Point','Third order', 'Point', 'Fourth order', 'Point'])
    plt.show()


def Echo(vals):
    """ Prints a table of approximations"""
    print('\nOrder      Thermal Conductivity (W/m^2K)')
    print('========================================')
    print('1          {0:7.4f}'.format(vals[0]))
    print('2          {0:7.4f}'.format(vals[1]))
    print('3          {0:7.4f}'.format(vals[2]))
    print('4          {0:7.4f}'.format(vals[3]))
    print('\n')

def main():
    """ Calls all the functions """
    xPoint = 351
    k = 5
    data = findNearest(RawData(), xPoint, k)
    order = GetFirstThroughFourthLists(data, xPoint)
    first = FirstOrderEquation(data, order[0], xPoint)
    second = SecondOrderEquation(data, order[1], xPoint, first)
    third = ThirdOrderEquation(data, order[2], xPoint, second)
    fourth = FourthOrderEquation(data, order[3], xPoint, third)
    display(data, order, [first, second, third, fourth], xPoint)
    Echo([first, second, third, fourth])

main()