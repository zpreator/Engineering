import math
import numpy as np
import matplotlib.pyplot as plt
"""
Zachary Preator
Mastery Level: 10
2/13/2020
"""
def GetData():
    """ Gets the data from the txt file"""
    data = np.loadtxt(u"/Repos/Engineering/ME342NumAnalysis/Unit3/PreClass32.txt", unpack=True)
    return data

def CalculateB(data):
    """ Calculates the b value given a 2D numpy array of x and y values"""
    squared = [i**2 for i in data[0]]
    product = [i*j for i, j in zip(data[0], data[1])]
    b=(len(data[0])*np.sum(product)-np.sum(data[0])*np.sum(data[1]))/(len(data[0])*np.sum(squared)-np.sum(data[0])**2)
    return b

def PowerLawData(data):
    newData = [[np.log(i) for i in data[0]], [np.log(j) for j in data[1]]]
    return newData

def PowerLawB(data):
    squared = [np.log(i)**2 for i in data[0]]
    product = [np.log(i)*np.log(j) for i, j in zip(data[0], data[1])]
    n = len(data[0])
    x = list(data[0])
    y = list(data[1])
    b = (n*np.sum(product)-np.sum(np.log(x))*np.sum(np.log(y)))/(n*np.sum(squared)-(np.sum(np.log(x)))**2)
    return b

def PowerLawA(data, b):
    return (np.sum(np.log(data[1]))-b*np.sum(np.log(data[0])))/len(data[0])

def CalculateA(data, b):
    """ Calculates the a value given a 2D numpy array of x and y values """
    a = np.average(data[1])-b*np.average(data[0])
    return a

def CoeffDeterm(data, a, b):
    """ Calulates the coeffecient of determination given A and B values
    and a numpy 2D array of x and y values"""
    squared = [i**2 for i in data[1]]
    product = [i*j for i, j in zip(data[0], data[1])]
    return (a*np.sum(data[0])+b*np.sum(product)-1/len(data[0])*(np.sum(data[1]))**2)/(np.sum(squared)-1/len(data[0])*(np.sum(data[0]))**2)

def Equation(x, a, b):
    """ Returns the bx + a"""
    return b*x+a

def Equation2(x, a, b):
    return a*x**b

def Display(f, data, a, b):
    """ Displays the discrete data along with the trendline"""
    plt.plot(data[0], data[1], 'b.')
    plt.plot(data[0], [f(i, a, b) for i in data[0]], 'r')
    plt.show()

def LinearRegression():
    data = GetData()
    b = CalculateB(data)
    a = CalculateA(data, b)
    rs = CoeffDeterm(data, a, b)
    print("A value: ", a, "\nB value: ", b, "\nR squared: ", rs)
    Display(Equation, data, a, b)

def PowerLaw():
    data = GetData()
    # newData = PowerLawData(data)
    # b = CalculateB(newData)
    # a = CalculateA(newData, b)
    b = PowerLawB(data)
    a = PowerLawA(data, b)
    rs = CoeffDeterm(data, a, b)
    print("A value: ", a, "\nB value: ", b, "\nR squared: ", rs)
    Display(Equation2, data, a, b)
    
PowerLaw()