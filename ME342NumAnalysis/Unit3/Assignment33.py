import math
import numpy as np
from scipy.interpolate import lagrange

def data():
    return np.array([[100, 200, 300, 400, 600, 800, 1000],[450, 82, 46, 32.4, 18.9, 13, 10.5]])

def findNearest(values, Temp, k):
    difference = [abs(values[0][i] - Temp) for i in range(len(values[0]))]
    index = np.argsort(difference)
    indexes = index[0:k]

    x = [values[0][i] for i in indexes]
    y = [values[1][i] for i in indexes]
    newData = np.array([x, y])
    return newData

def Lagrange(data):
    xPoint = 351
    f_lagrange = lagrange(data[0], data[1])
    value = f_lagrange(xPoint)
    return value

def main():
    temps = findNearest(data(), 351, 4)
    print(Lagrange(temps))

main()