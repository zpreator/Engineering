import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares, curve_fit

data = None
def GetDataFromFile():
    global data
    data = np.loadtxt(u"/Repos/Engineering/ME342NumAnalysis/Unit3/data.txt", unpack=True)

def Sutherlands(T, a, b):
    return a*np.sqrt(T)/(1+b/T)

def GetLogData():
    global data
    lnx = [np.log(i) for i in data[0]]
    lny = [np.log(i) for i in data[1]]
    lnxlny = [i*j for i, j in zip(lnx, lny)]
    lnxsq = [i**2 for i in lnx]
    lnysq = [i**2 for i in lny]
    lnyerr = 0.2*data[1]/data
    return [lnx, lny, lnxlny, lnxsq, lnysq, ]

def PowerCurveFitA(data, b):
    n = len(data[0])
    lnx = data[0]
    lny = data[1]
    sumlny = np.sum(lny)
    sumlnx = np.sum(lnx)
    a = np.exp(1/n*sumlny-b*sumlnx/n)
    return a

def PowerCurveFitB(data):
    n = len(data[0])
    lnx = data[0]
    lny = data[1]
    lnxlny= data[2]
    lnxsq = data[3]
    lnysq = data[4]
    sumlny = np.sum(lny)
    sumlnx = np.sum(lnx)
    sumlnxlny = np.sum(lnxlny)
    sumlnxsq = np.sum(lnxsq)
    sumlnysq = np.sum(lnysq)
    b = (sumlnxlny-1/n*sumlnx*sumlny)/(sumlnxsq-1/n*sumlnx**2)
    return b

def PowerCurveFitRSq(data):
    n = len(data[0])
    lnx = data[0]
    lny = data[1]
    lnxlny= data[2]
    lnxsq = data[3]
    lnysq = data[4]
    sumlny = np.sum(lny)
    sumlnx = np.sum(lnx)
    sumlnxlny = np.sum(lnxlny)
    sumlnxsq = np.sum(lnxsq)
    sumlnysq = np.sum(lnysq)
    rsq = (sumlnxlny-1/n*sumlnx*sumlny)**2/(sumlnxsq-sumlnx**2/n)/(sumlnysq-sumlny**2/n)
    return rsq

def PowerCurveFit(data):
    b = PowerCurveFitB(data)
    a = PowerCurveFitA(data, b)
    rsq = PowerCurveFitRSq(data)
    return [a,b, rsq]

def PowerCurve(x, a, b):
    return a*x**b

def PowerCurveFitScipy():
    global data
    out = curve_fit(PowerCurve, data[0], data[1])
    return out[0]

def SutherlandsCurveFit(a0, b0):
    global data
    fitfunc = lambda T, a, b: a*np.sqrt(T)/(1+b/T)
    out = curve_fit(fitfunc, data[0], data[1], p0=[a0, b0])
    return out

def display(PC, PCS, S):
    global data
    x = np.linspace(100, 1600)
    plt.plot(data[0], data[1], 'ko', label=r'$\mu$ (data)')
    plt.plot(x, PC[0]*x**PC[1], 'g', label='Power Law Curve')
    plt.plot(x, PCS[0]*x**PCS[1], 'r', label='Power Law Curve (Scipy)')
    plt.plot(x, Sutherlands(x, S[0][0], S[0][1]), 'b', label='Sutherlands Curve')
    plt.legend(loc='best')
    plt.show()

def main():
    GetDataFromFile()
    logData = GetLogData()
    PC = PowerCurveFit(logData)
    PCS = PowerCurveFitScipy()
    S = SutherlandsCurveFit(0.1, 100.0)
    display(PC, PCS, S)

main()