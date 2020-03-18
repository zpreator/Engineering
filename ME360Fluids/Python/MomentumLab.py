import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def GetData():
    data = np.loadtxt(u"C:/Repos/Engineering/ME360Fluids/MomentumData.txt", unpack=True)
    return data
  
def Theoretical(vDot, Dn, theta):
    vDot /= 60000 # m^3/s
    Dn /= 1000 
    rho = 998 # kg/m^3
    # theta = theta/360*(2*np.pi) #Degrees to radians
    theta = np.deg2rad(theta)
    return rho*vDot**2*4/(Dn**2*np.pi)*(1-np.cos(theta))

def Uncertainty(std):
    u = [np.sqrt(0.01**2+(2*i)**2) for i in std]
    return u

def PowerCurve(x, a, b):
    """ Is used for the curve_fit function in 'PowerCurveFitScipy'"""
    return a*x**b

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

def display2(datas):
    # Volumetric flow rate
    vFlow = datas[0]
    anglesFloat = [25, 30.5, 47.7, 65, 74, 90, 105, 120, 150, 180]
    anglesString = [r'${0}$ degrees'.format(i) for i in anglesFloat]
    nozzlesFloat = [2.83, 3.28, 5.25, 6.35]
    nozzles = [r'Nozzle 1 $(2.83mm)$',
               r'Nozzle 2 $(3.28mm)$',
               r'Nozzle 3 $(5.25mm)$',
               r'Nozzle 4 $(6.35mm)$',]
    lineTypes = ['-', '--', '-.', ':']
    shapes = ['^', 'o', 's', 'P']
    colors = ['r', 'g', 'k', 'y']
    z = 0
    for i in range(1, 20, 2):
        plt.figure(figsize=(5,3.75)) #set the figure size (width,height)(inches)
        
        g = 0 
        for j in range(0,len(datas[0]),5):
            plt.tight_layout()
            plt.rc('font', family='serif', size=10)
            # plt.rc('text', usetex=True)  #render text output with LaTeX

            # # Force detected
            tData = vFlow[j:j+5]
            sData = datas[i][j:j+5]
            tData = np.array([float('nan') if x==0 else x for x in tData])
            sData = np.array([float('nan') if x==0 else x for x in sData])
            uData = Uncertainty(datas[i+1][j:j+5])
            
            #Concatenate color with line or marker type
            lineType = colors[g] + lineTypes[g]
            markerType = colors[g] + shapes[g]

            # Power Curve
            t = np.arange(min(tData), max(tData), 0.01)
            tDat, sDat = RemoveNanValues(tData, sData)
            a, b = PowerCurveFitScipy(tDat, sDat)
            s = PowerCurve(t, a, b)
            plt.plot(t,s,lineType,label=nozzles[g])
            print(nozzles[g], anglesFloat[z], b)
            
            
            # Theoretical curve
            theoY = [Theoretical(i, nozzlesFloat[g], anglesFloat[z]) for i in t]
            plt.plot(t, theoY, lineType)


            #Plots the errorbars with uData (standard deviation data)
            plt.errorbar(tData,sData,yerr=uData,fmt=markerType,capsize=5)
            plt.xlabel(r'Flow Rate $(L/min)$')
            plt.ylabel(r'Force $(N)$')
            g += 1

        plt.legend(loc='best')
        # plt.show()
        st = 'plotFinal' + str(anglesFloat[z]) + '.pdf'
        plt.savefig(st)
        z += 1

def main():
    datas = GetData()
    display2(datas)

main()