import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import least_squares, curve_fit
"""
Zachary Preator
10/10
"""
data = None
def GetDataFromFile():
    """ Gets data from a file"""
    global data
    data = np.loadtxt(u"/Repos/Engineering/ME342NumAnalysis/Unit3/data.txt", unpack=True)

def Sutherlands(T, a, b):
    """ Returns the sutherlands equation"""
    return a*np.sqrt(T)/(1+b/T)

def GetLogData():
    """ Returns the natural logs and natural log squared
    of x and y for easier use in computing a and b"""
    global data
    lnx = [np.log(i) for i in data[0]]
    lny = [np.log(i) for i in data[1]]
    lnxlny = [i*j for i, j in zip(lnx, lny)]
    lnxsq = [i**2 for i in lnx]
    lnysq = [i**2 for i in lny]
    # lnyerr = 0.2*data[1]/data
    return [lnx, lny, lnxlny, lnxsq, lnysq, ]

def PowerCurveFitA(data, b):
    """ Computes A for the power curve"""
    n = len(data[0])
    lnx = data[0]
    lny = data[1]
    sumlny = np.sum(lny)
    sumlnx = np.sum(lnx)
    a = np.exp(1/n*sumlny-b*sumlnx/n)
    return a

def PowerCurveFitB(data):
    """ Computes B for the power curve"""
    n = len(data[0])
    lnx = data[0]
    lny = data[1]
    lnxlny= data[2]
    lnxsq = data[3]
    # lnysq = data[4]
    sumlny = np.sum(lny)
    sumlnx = np.sum(lnx)
    sumlnxlny = np.sum(lnxlny)
    sumlnxsq = np.sum(lnxsq)
    # sumlnysq = np.sum(lnysq)
    b = (sumlnxlny-1/n*sumlnx*sumlny)/(sumlnxsq-1/n*sumlnx**2)
    return b

def PowerCurveFitRSq(data):
    """ Computes the coefficient of determination"""
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
    rsq = (sumlnxlny-1/n*sumlnx*sumlny)**2
          /(sumlnxsq-sumlnx**2/n)/(sumlnysq-sumlny**2/n)
    return rsq

def PowerCurveFit(data):
    """ packages up the a, b, 
    and rsq into a list for later"""
    b = PowerCurveFitB(data)
    a = PowerCurveFitA(data, b)
    rsq = PowerCurveFitRSq(data)
    return [a,b, rsq]

def PowerCurve(x, a, b):
    """ Is used for the curve_fit 
    function in 'PowerCurveFitScipy'"""
    return a*x**b

def PowerCurveFitScipy():
    """ Computes the power law curve fit for the data"""
    global data
    popt, pcov = curve_fit(PowerCurve, data[0], data[1])
    residuals = data[1]-PowerCurve(data[0], popt[0], popt[1])
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((data[1]-np.mean(data[1]))**2)
    r_squared = 1 - (ss_res / ss_tot)
    return [popt[0], popt[1], r_squared]

def SutherlandsCurveFit(a0, b0):
    """ Computes the sutherland curve 
    fit for the data taking two initial guesses"""
    global data
    fitfunc = lambda T, a, b: a*np.sqrt(T)/(1+b/T)
    popt, pcov = curve_fit(fitfunc, data[0], data[1], p0=[a0, b0])
    residuals = data[1]-fitfunc(data[0], popt[0], popt[1])
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((data[1]-np.mean(data[1]))**2)
    r_squared = 1 - (ss_res / ss_tot)
    return [popt[0], popt[1], r_squared]

def display(PC, PCS, S):
    """ Displays the data input in list format"""
    global data
    x = np.linspace(100, 1600)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(data[0], data[1], 'ko', label=r'$\mu$ (data)')
    ax.plot(x, PC[0]*x**PC[1], 'g', label=r'Power Law Curve $r^2={0:7.4f}$'.format(PC[2]))
    ax.plot(x, PCS[0]*x**PCS[1], 'r', label=r'Power Law Curve (Scipy) $r^2={0:7.4f}$'.format(PCS[2]))
    ax.plot(x, Sutherlands(x, S[0], S[1]), 'b', label=r'Sutherlands Curve $r^2={0:7.4f}$'.format(S[2]))
    ax.legend()
    plt.show()

def main():
    # Gets the data and sets the global variable
    GetDataFromFile()

    # Gets the log data which is lists of lnx, lny etc. 
    logData = GetLogData()

    # Gets the power law data from my calculations
    PC = PowerCurveFit(logData)

    # Gets the power law data from scipy
    PCS = PowerCurveFitScipy()

    # Gets the sutherlands curve fit data
    S = SutherlandsCurveFit(0.1, 100.0)

    # Displays everthing
    display(PC, PCS, S)

main()