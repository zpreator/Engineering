import numpy as np
import math

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
