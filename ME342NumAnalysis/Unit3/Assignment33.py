import math
import numpy as np
from scipy.interpolate import lagrange

def data():
    return np.array([[100, 200, 300, 400, 600, 800, 1000],[450, 82, 46, 32.4, 18.9, 13, 10.5]])

def findNearest(values, Temp, k):
    difference = [abs(values[i] - Temp) for i in range(len(values[0]))]
    index = np.argsort(difference)
    return index[0:k]

def main():
    temps = findNearest(data(), 351, 4)
