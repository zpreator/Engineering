import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares, curve_fit

data = None
def GetDataFromFile():
    global data
    data = np.loadtxt(u"/Repos/Engineering/ME342NumAnalysis/Unit3/data.txt", unpack=True)

def Sutherlands(T, a, b):
    return a*np.sqrt(T)/(1+b/T)

def GetDataPowerCurve():
    global data
    # data = np.array([[10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35],[0.95,1.05,1.25,1.41,1.73,2,2.53,2.98,3.85,4.59,6.02]])
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
    # a = np.exp(1/n*np.sum(lny)-b*np.sum(lnx)/n)
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
    # b = (np.sum(lnx*lny)-1/n*np.sum(lnx)*np.sum(lny))/(np.sum(lnx**2)-1/n*np.sum(lnx)**2)
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
    # rsq = (np.sum(lnx*lny)-1/n*np.sum(lnx)*np.sum(lny))**2/((np.sum(lnx**2)-np.sum(lnx)**2/n)*(np.sum(lny**2)-np.sum(lny)**2/n))
    rsq = (sumlnxlny-1/n*sumlnx*sumlny)**2/(sumlnxsq-sumlnx**2/n)/(sumlnysq-sumlny**2/n)
    return rsq

def PowerCurveFit(data):
    b = PowerCurveFitB(data)
    a = PowerCurveFitA(data, b)
    rsq = PowerCurveFitRSq(data)
    return [a,b, rsq]

def PowerCurveFitScipy(logData, a0, b0):
    fitfunc = lambda x, a, b: a+b*x
    out = curve_fit(fitfunc, logData[0], logData[1], p0=[a0, b0])
    return out

def PowerCurveFitScipy2(logData):
    fitfunc = lambda p, x, y: p[0] + p[1] * x
    out = least_squares(fitfunc, [2, -2],args=(np.array(logData[0]), np.array(logData[1])))
    return out

def SutherlandsSolver(x):
    global data
    FIModel = [x[0]*0.000001*np.sqrt(i)/(1+x[1]/i) for i in data[0]]
    si2 = [(i-j)**2 for i, j in zip(data[1], FIModel)]
    return np.sum(si2)*1E12

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
    # plt.plot(x, (np.exp(PCS[0]))*x**PCS[1], 'r', label='Power Law Curve (Scipy)')
    plt.plot(x, Sutherlands(x, S[0][0], S[0][1]), 'b', label='Sutherlands Curve')
    plt.legend(loc='best')
    plt.show()

def main():
    GetDataFromFile()
    logData = GetDataPowerCurve()
    PC = PowerCurveFit(logData)
    PCS = PowerCurveFitScipy2(logData).x
    S = SutherlandsCurveFit(0.0000015, 150.0)
    display(PC, PCS, S)

main()
