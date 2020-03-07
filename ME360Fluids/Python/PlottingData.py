import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def GetData():
    # Enter the path to the data text file here
    data = np.loadtxt(u"C:/Repos/Engineering/ME360Fluids/Data/MomentumData.txt", unpack=True)
    return data

def RemoveNanValues(x, y):
    for i in range(len(x)):
        val = y[i]
        if np.isnan(y[i]):
            x[i] = 'nan'
        elif x[i] == 'nan':
            y[i] = 'nan'
    x = x[np.logical_not(np.isnan(x))]
    y = y[np.logical_not(np.isnan(y))]
    return x, y

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

def Display(x, y, lineType='.', done = False, xLabel=None, yLabel=None, powerCurve=False):

    # This removes the zeros from the lists (zeros will mess up the data)
    # Matplotlib reads 'nan' and ignores it
    x = [float('nan') if i==0 else i for i in x]
    y = [float('nan') if x==0 else x for x in y]

    # Our data is split up in batches of 5 with 0s for no data
    # so we will run this for loop for each batch of 5
    j = 0 # used for lists of stuff for 4 different plots (Should go from 0 to 3)
    for i in range(0, len(x), 5):
        xBatch = x[i:i+5]
        yBatch = y[i:i+5]

        if powerCurve:
            x1, y1 = RemoveNanValues(np.array(xBatch),np.array(yBatch))
            a, b = PowerCurveFitScipy(x1, y1)
            t = np.arange(min(x), max(x), 0.001)
            plt.plot(t, PowerCurve(t, a, b), label='PowerCurve')
        
        plt.plot(xBatch, yBatch, lineType)
        plt.xlabel(xLabel[j])
        plt.ylabel(yLabel[j])
        plt.tight_layout()
        plt.show()
        j += 1

def main():
    data = GetData()
    # All lists should correspond indeces (VolumeFlowRate[0] goes with Force25[0])
    VolumeFlowRate = data[0] # List of all volume flow rates
    Force25 = data[1] # List of all force values
    Std25 = data[2] # List of all std deviations
    Force305 = data[3]
    Std305 = data[4]
    Force477 = data[5]
    Std477 = data[6]
    Force65 = data[7]
    Std65 = data[8]
    Force74 = data[9]
    Std74 = data[10]
    Force90 = data[11]
    Std90 = data[12]
    Force105 = data[13]
    Std105 = data[14]
    Force120 = data[15]
    Std120 = data[16]
    Force150 = data[17]
    Std150 = data[18]
    Force180 = data[19]
    Std180 = data[20]

    #Begin Plotting
    shapes = ['^', 'o', 's', 'P']
    plt.rc('font', family='serif', size=10)

    # This will produce 4 graphs, 1 for each nozzle size
    xLabels = ['Label1', 'Label2', 'Label3', 'Label4']
    yLabels = ['yLabel1', 'yLabel2', 'yLabel3', 'yLabel4']

    Display(Force74, Std74, xLabel=xLabels, yLabel=yLabels, powerCurve=True)
    
    
main()