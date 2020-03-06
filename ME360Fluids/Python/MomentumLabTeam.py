import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def GetData():
    # data = np.loadtxt(u"C:/Repos/Engineering/ME360Fluids/MomentumData.txt", unpack=True)
    data = np.array([[2.83, 3.28, 5.25, 6.35], [0.34, 0.2425, 0.09, 0.06], [0.012, 0.00695, 0.006, 0.013]])
    # diameters = np.array([2.83, 3.28, 5.25, 6.35])
    # forces = data[7]
    # stdDev = data[8]
    # flowRates = data[0]
    # return [flowRates, forces, diameters, stdDev]
    return data

def PowerCurveFitScipy(x, y):
    """ Computes the power law curve fit for the data"""
    popt, pcov = curve_fit(PowerCurve, x, y)
    residuals = y-PowerCurve(x, popt[0], popt[1])
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((x-np.mean(x))**2)
    r_squared = 1 - (ss_res / ss_tot)
    # return [popt[0], popt[1], r_squared]
    return popt[0], popt[1]

def PowerCurve(x, a, b):
    """ Is used for the curve_fit function in 'PowerCurveFitScipy'"""
    return a*x**b

def main():
    data = GetData()
    shapes = ['^', 'o', 's', 'P']
    plt.rc('font', family='serif', size=10)
    j = 0
    # for i in range(0, 20, 5):
    for i in range(1):
        # Example data
        #t = np.linspace(0,1,num=100,endpoint=True)
        #s = np.cos(4 * np.pi * t) + 2

        # Example descreate data
        # tData = data[0][i:i+5]
        # sData = data[1][i:i+5]
        # uData = data[3][i:i+5]

        #tData = np.linspace(0,1,num=20,endpoint=True)
        #sData = np.cos(4 * np.pi * tData) + 2+np.random.random(len(tData))/10
        #uData = np.random.random(len(tData))/10

        tData = data[0]
        sData = data[1]
        uData = data[2]


        # tData = np.array([float('nan') if x==0 else x for x in tData])
        # sData = np.array([float('nan') if x==0 else x for x in sData])
        # Make the plot
        #plt.figure(figsize=(5,3)) #set the figuer size (width,height)(inches)
        # plt.plot(tData, sData)
        # plt.errorbar(tData,sData,yerr=uData ,fmt=shapes[j],capsize=5,label='{0} mm Nozzle Diameter'.format(str(data[2][j])))

        t = np.arange(min(tData), max(tData), 0.01)
        # tDat, sDat = RemoveNanValues(tData, sData)
        a, b = PowerCurveFitScipy(tData, sData)
        s = PowerCurve(t, a, b)
        plt.plot(t,s,'-.', label='Power Law Curve Fit')

        plt.errorbar(tData,sData,yerr=uData ,fmt='o',capsize=5, label='Force Measured')
        plt.xlabel(r'Nozzle Diameter $(mm)$')


        # plt.xlabel(r'Flow Rate $(L/min)$')
        plt.ylabel(r'Force $(N)$')
        #plt.xlabel(r'Time ($s$)') #the r'...' alows for LaTeX math input
        # plt.ylabel(r'Voltage ($mV$)')
        j += 1
    plt.legend(loc='best')
    #plt.grid()
    plt.tight_layout()
    #plt.show()
    plt.savefig('PowerLaw.pdf') # save the image as a vecortized pdf
    plt.show()
    
main()