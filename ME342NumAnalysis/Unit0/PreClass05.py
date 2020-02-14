import numpy as np
import matplotlib.pyplot as plt

def getFileData(fileName):
    """ Gets the data from the file"""
    newData = np.loadtxt(fileName)
    return newData

def display(x, y):
    """ Displays the given lists of x and y with 
    a legend and labeled axes""" 
    plt.plot(x, y, 'b:', x, y, 'ro')
    plt.legend(['Dotted Line','Points of Interest'])
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.show()

def sumData(x, y):
    """ Sums and prints data """
    print(sum(x))
    print(sum(y))

def main():
    """ Calls all the functions and splits fileData
    into x and y lists"""
    fileData = getFileData('data_test.txt')
    x = fileData[:,0]
    y = fileData[:,1]
    sumData(x, y)
    display(x, y)

main()