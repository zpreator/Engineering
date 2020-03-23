import numpy as np
import matplotlib.pyplot as plt
from ZachsPackage import Display as D
L = 0.15 # Fin length
Tb = 500 # Base temperature K
k = 16.0 # Thermal conductivity W/mK
Ac = 1.67e-4 # Cross sectional area m^2
P = 0.066 # Perimeter length m
Tf = 300 # Free stream temperature K
h = 25 # Heat transfer coefficient W/m^2
TL = 350 # Fixed tip temperature K
dx = 0.03 # Step size

"""
Zachary Preator
Mastery Level 10/10
"""
def dTdUdx(x, var):
    """ ODE represented as two first order ODEs"""
    T = var[0]
    U = var[1]
    dTdx = U
    dUdx = h*P/k/Ac*(T-Tf)
    return np.array([dTdx,dUdx])
    

def RK4(f,t0,y0,tf,h):
    """ Runge-Kutta method"""
    t = np.arange(t0,tf+h,h)
    n = len(t)
    m = len(y0)
    y = np.zeros([n,m])
    y[0] = y0
    
    for i in range(n-1):
        k1 = f(t[i],y[i])
        k2 = f(t[i]+.5*h,y[i]+k1*.5*h)
        k3 = f(t[i]+.5*h,y[i]+k2*.5*h) 
        k4 = f(t[i]+h,y[i]+k3*h)
        y[i+1] = y[i] + h/6*(k1 + 2*k2 + 2*k3 + k4)
        
    return t, y.transpose()

def FuncTempFixedT(x):
    """ Function for temperature with fixed temperature TL"""
    m = np.sqrt(h*P/(k*Ac))

    #Finding the constants thetaL an thetab
    thL = TL-Tf
    thb = Tb-Tf
    return thL*np.sinh(m*x)/np.sinh(m*L)+thb*np.sinh(m*(L-x))/np.sinh(m*L) + Tf

def FuncGradientFixedT(x):
    """ Function for temperature gradient"""
    m = np.sqrt(h*P/(k*Ac))
    thL = TL-Tf
    thb = Tb-Tf
    return m*k*Ac/np.sinh(m*L)*(thb*np.cosh(m*(L-x)) - thL*np.cosh(m*x))

def FuncTempAdiabatic(x):
    """ Function for tempearture with adiabatic tip temperature"""
    m = np.sqrt(h*P/(k*Ac))
    thb = Tb-Tf
    return thb*(np.cosh(m*(L-x))/(np.cosh(m*L)))+Tf

def FuncGradientAdiabatic(x):
    """ Function for temp gradient with adiabatic tip temperature"""
    m = np.sqrt(h*P/(k*Ac))
    thb = Tb-Tf
    return m*k*Ac*thb*np.sinh(m*(L-x))/np.cosh(m*L)

def HTR(U):
    """Calculates heat transfer rate given T' """
    return -k*Ac*U

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
            # row += str(data[i][j]) + ' & '             # Use this line for the raw input
            row += '{0:4.3E}'.format(data[i][j]) + ' & ' # Toggle this line to format numbers
        # row += str(data[i][-1])                        # Raw input
        row += '{0:4.3E}'.format(data[i][-1])            # Format numbers
        print('      ', row, '\\\\')

    # Ends the table schema
    print('      \\bottomrule')
    print('   \end{tabular}')
    label = '{' + label + '}'
    print('   \label{0}'.format(label))
    print('\end{table}')

def Display(data, lineType, label='', done = False, xLabel=None, yLabel=None, plotLabel=None, f=None, log=False):
    """ Displays data as [x, y]"""
    t = np.arange(0, 4, 0.01)
    
    plt.plot(data[0], data[1], lineType, label=label)
    if (done):
        if f != None:
            plt.plot(t, f(t, 1), 'k', label='Exact')
        if log:
            plt.xscale("log")
            plt.yscale("log")
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.legend(loc='best')
        plt.tight_layout()
        # plt.savefig('{0}.pdf'.format(plotLabel))
        plt.show()

def ShootingMethod(guess1, guess2, desiredVal, der):
    """ Performs the shooting method with runge-kutta.
    desiredVal = value to shoot for
    der = order of the dependent variable sought
    FOR EXAMPLE: To find what input guess for T' will
    give a value of T = TL, then my input would be:
    ShootingMethod(guess1, guess2, TL, 1). If I wanted
    to get the value of T' = 0 then: ShootingMethod(.., 0, 2)"""
    i = der - 1
    x1, var1 = RK4(dTdUdx, 0, [Tb,guess1], L, dx)
    x2, var2 = RK4(dTdUdx, 0, [Tb,guess2], L, dx)
    guess3 = (desiredVal-var1[i,-1])/(var2[i,-1]-var1[i,-1])*(guess2-guess1) + guess1
    x3, var3 = RK4(dTdUdx, 0, [Tb, guess3], L, dx)
    return x3, var3, guess3

def main():
    """ Calls all other methods"""
    tFixedT, valFixedT, guessFixedT = ShootingMethod(0, -1000, TL, 1) # We want the Temperature to be TL @ L
    tAdiabatic, valAdiabatic, guessAdiabatic = ShootingMethod(0, -1000, 0, 2) # We want the derivative to be 0 @ L
    print('2.')
    print('  (a) @ x = 0, T\' = {0:5.4f} @ x = {1:4.2f}, T = {2:5.4f}'.format(guessFixedT, L, valFixedT[0][-1]))
    print('  (b) @ x = 0, T\' = {0:5.4f} @ x = {1:4.2f}, T\' = {2:5.4f}'.format(guessAdiabatic, L, valAdiabatic[1][-1]))

    x = np.arange(0,L,0.0001)
    q = FuncGradientFixedT(x)
    T = FuncTempFixedT(x)
    qa = FuncGradientAdiabatic(x)
    Ta = FuncTempAdiabatic(x)
    # Display(x, qa, Ta, x3, var3)

    test = np.rot90(valFixedT)
    # Plot of temperature using fixed temperature guess
    plt.figure(figsize=(5, 3))
    Display([x, T], '-', label='Analytical') 
    Display([tFixedT, valFixedT[0]], '--', label='Numerical', done=True, xLabel='Position', yLabel='Temperature', plotLabel='Temperature(x)')

    # Plot of temp gradient using fixed temperature guess
    plt.figure(figsize=(5, 3))
    Display([x, q], '-', label='Analytical')
    Display([tFixedT,  HTR(valFixedT[1])], '--', label='Numerical', done=True, xLabel='Position', yLabel='Temperature', plotLabel='Temp Gradient(x)')

    # Plot of temperature using adiabatic guess
    plt.figure(figsize=(5, 3))
    Display([x, Ta], '-', label='Analytical') 
    Display([tAdiabatic, valAdiabatic[0]], '--', label='Numerical', done=True, xLabel='Position', yLabel='Temperature', plotLabel='TemperatureA(x)')

    # Plot of temp gradient using adiabatic guess
    plt.figure(figsize=(5, 3))
    Display([x, qa], '-', label='Analytical') 
    Display([tAdiabatic, HTR(valAdiabatic[1])], '--', label='Numerical', done=True, xLabel='Position', yLabel='Temperature', plotLabel='Temp GradientA(x)')

    # Creating lists of all errors
    TerrFixed = [abs((valFixedT[0][i] - FuncTempFixedT(tFixedT[i]))/FuncTempFixedT(tFixedT[i])) for i in range(len(tFixedT))]
    qerrFixed = [abs((HTR(valFixedT[1][i]) - FuncGradientFixedT(tFixedT[i]))/FuncGradientFixedT(tFixedT[i])) for i in range(len(tFixedT))]
    TerrAdiabatic = [abs((valAdiabatic[0][i] - FuncTempAdiabatic(tAdiabatic[i]))/FuncTempAdiabatic(tAdiabatic[i])) for i in range(len(tAdiabatic))]
    qerrAdiabatic = [abs((HTR(valAdiabatic[1][i]) - FuncGradientAdiabatic(tAdiabatic[i]))/FuncGradientAdiabatic(tAdiabatic[i])) for i in range(len(tAdiabatic))]

    # Putting the error data into a latex table
    table = []
    [table.append([TerrFixed[i], qerrFixed[i], TerrAdiabatic[i], qerrAdiabatic[i]]) for i in range(len(tFixedT))]
    ProduceLatexTable([r'$e_T$', r'$e_q$', r'$e_T$', r'$e_q$'], table)

main()
