import numpy as np
from ZachsPackage.Display import Display
import matplotlib.pyplot as plt

def GetData(file):
    data = np.loadtxt(u'C:/Repos/Engineering/ME360Fluids/Unit 6/{0}.csv'.format(file), unpack=True, delimiter=',')
    return data

def Main(): 
    CL = GetData('CopperLarge')
    CM = GetData('CopperMedium')
    CS = GetData('CopperSmall')
    PX = GetData('Pex')
    GS = GetData('Galvanized')
    # flowRates = np.arange(0, 3.75, 0.01)
    plt.figure(figsize=(5, 3))
    Display([CL[0], CL[2]], '.-' , label='Copper (Large)')
    Display([CM[0], CM[2]], 'o--', label='Copper (Medium)')
    Display([CS[0], CS[2]], '+-' , label='Copper (Small)')
    Display([PX[0], PX[2]], 'x-.', label='Pex')
    Display([GS[0], GS[2]], '^:' , label='Galvanized Steel', save=True, done=True, xLabel=r'Flow Rate $(L/s)$', yLabel=r'Pressure Drop $(psi)$', plotLabel='PressureVFlow')

    # plt.figure(figsize=(5, 3))
    Display([CL[5], CL[4]], 'b.-',  label=r'Copper (Large)  $f_{meas}$')
    Display([CL[5], CL[6]], 'b.:',  label=r'Copper (Large)  $f_{theo}$')
    Display([CM[5], CM[4]], 'go-',  label=r'Copper (Medium) $f_{meas}$')
    Display([CM[5], CM[6]], 'go:',  label=r'Copper (Medium) $f_{theo}$')
    Display([CS[5], CS[4]], 'r+-',  label=r'Copper (Small)  $f_{meas}$')
    Display([CS[5], CS[6]], 'r+:',  label=r'Copper (Small)  $f_{theo}$')
    Display([PX[5], PX[4]], 'cx-',  label=r'Pex $f_{meas}$')
    Display([PX[5], PX[6]], 'cx:',  label=r'Pex $f_{theo}$')
    Display([GS[5], GS[4]], 'm^-',  label=r'Galvanized Steel $f_{meas}$')
    Display([GS[5], GS[6]], 'm^:',  label=r'Galvanized Steel $f_{theo}$', save=False, done=True, xLabel=r'Flow Rate $(L/s)$', yLabel=r'Pressure Drop $(psi)$', plotLabel='sadf')

Main()