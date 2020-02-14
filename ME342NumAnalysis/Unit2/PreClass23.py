import math
import numpy as np
import matplotlib.pyplot as plt


def importText():
    file = np.loadtxt('velocityData.txt')
    return file

def findStuff(file):
    a = [i[1] for i in file]
    max = np.max(a)
    min = np.min(a)
    avg = np.average(a)
    range = np.ptp(a)
    std = np.std(a)
    b = [.5*10*i**2 for i in a]
    maxEn = np.max(b)
    print(max, min, avg, range, std, maxEn)
    return [max, min, avg, range, std, maxEn]

def plotStuff(stuff, file):
    t = list(file[:,0])
    v = list(file[:,1])
    a = [(j-i)/.1 for i, j in zip(v[:-1], v[1:])]
    a.append(-1)

    plt.plot(t, v,'r')
    plt.plot(t, a,'b')
    plt.show()
    plt.savefig('ZachPreator.pdf')

def main():
    file = importText()
    stuff = findStuff(file)
    plotStuff(stuff, file)

main()