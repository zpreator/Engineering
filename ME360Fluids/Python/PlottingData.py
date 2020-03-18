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

def Theoretical(vDot, Dn, theta):
    vDot /= 60000 # m^3/s
    Dn /= 1000 
    rho = 998 # kg/m^3
    # theta = theta/360*(2*np.pi) #Degrees to radians
    theta = np.deg2rad(theta)
    return rho*vDot**2*4/(Dn**2*np.pi)*(1-np.cos(theta))

def ProduceLatexTable(columnHeadings, data, title='', label=''):
    """ Prints latex table"""
    # Adds a catption and begins table
    caption = '{' + title + '}'
    print('\\begin{table}')
    print('   \centering')
    print('   \caption{0}'.format(caption))

    # Sets the columns in \begin{tabular} (cccc...)
    cols = ''
    for i in range(len(data[0])):
        cols += 'c'
    print('   \\begin{tabular}{@{}', cols, '@{}}\\toprule')

    # Sets the column headings
    line = ''
    for i in range(len(columnHeadings)-1):
        line += columnHeadings[i] + ' & '
    line += columnHeadings[-1]
    print('      ', line, '\\\\ \midrule')

    # Prints the rows with the data provided
    for i in range(len(data)):
        row = ''
        for j in range(len(columnHeadings)-1):
            row += str(data[i][j]) + ' & '
            # row += '{0:6.4G}'.format(data[i][j]) + ' & '
        row += str(data[i][-1])
        # row += '{0:5.4G}'.format(data[i][-1])
        print('      ', row, '\\\\')

    # Ends the table schema
    print('      \\bottomrule')
    print('   \end{tabular}')
    label = '{' + label + '}'
    print('   \label{0}'.format(label))
    print('\end{table}')

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
        # plt.savefig('MattIsCool.pdf')
        # plt.show()
        j += 1
    plt.show()

# def Display2():

def main():
    data = GetData()
    # All lists should correspond indeces (VolumeFlowRate[0] goes with Force25[0])
    VolumeFlowRate = data[0] # List of all volume flow rates
    nozzles = [2.83, 3.28, 5.25, 6.35]
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
    # shapes = ['^', 'o', 's', 'P']
    plt.figure(figsize=(5,3))
    plt.rc('font', family='serif', size=10)

    plt.plot()


    # # This will produce 4 graphs, 1 for each nozzle size
    # xLabels = ['Label1', 'Label2', 'Label3', 'Label4']
    # yLabels = ['yLabel1', 'yLabel2', 'yLabel3', 'yLabel4']
    # Display(Force74, VolumeFlowRate, xLabel=xLabels, yLabel=yLabels, powerCurve=True)
    
    
    
    # anglesFloat = [25, 30.5, 47.7, 65, 74, 90, 105, 120, 150, 180]
    # anglesString = [r'${0}$\dgr'.format(i) for i in anglesFloat]
    # lineTypes = ['-', '--', '-.', ':', '-', '--', '-.', ':', '-', '--']
    # g = 0
    # table = []
    # for i in range(1, len(data[0])-1, 2):
    #     # for j in range(4):
    #     F = [data[i][3], data[i][7], data[i][11], data[i][15]]            
    #     plt.plot(nozzles, F, lineTypes[g], label=anglesString[g])
    #     row = [anglesString[g]] + F
    #     table.append(row)
    #     g += 1
    # plt.legend(loc='best', ncol=2)
    # plt.xlabel(r'Nozzle size $(mm)$')
    # plt.ylabel(r'Force $(N)$')
    # plt.tight_layout()
    # # plt.savefig('AllAngles.pdf')
    # # plt.show()
    # nozzles2 = [r'Target angle',
    #            r'$(2.83mm)$',
    #            r'$(3.28mm)$',
    #            r'$(5.25mm)$',
    #            r'$(6.35mm)$',]
    # ProduceLatexTable(nozzles2, table)

main()