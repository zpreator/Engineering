import numpy as np
from scipy.integrate import trapz, simps

"""
Zachary Preator
10/10
"""
def GetData():
    data = np.loadtxt(u"/Repos/Engineering/ME342NumAnalysis/Unit4/InClassData.txt", unpack=True)
    return data

def Trapezoid(x, y, I):
    integral = 0
    for i in range(len(x)-1):
        integral += (x[i+1]-x[i])*(y[i]+y[i+1])/2
    e = abs(integral-I)/I
    return integral, e

def TrapScipy(x, y, I):
    integral = trapz(y, x)
    e = abs(integral-I)/I
    return integral, e

def Simpsons13(x, y, I):
    integral = 0
    for i in range(0, len(x) - 1, 2):
        integral += (x[i+2]-x[i])*(y[i]+4*y[i+1]+y[i+2])/6
    e = abs(integral-I)/I
    return integral, e

def Simpsons38(x, y, I):
    integral = 0
    for i in range(0, len(x) - 1, 3):
        integral += (x[i+3]-x[i])*(y[i]+3*y[i+1]+3*y[i+2]+y[i+3])/8
    e = abs(integral-I)/I
    return integral, e

def SimpsonsScipy(x, y, I):
    integral = simps(y, x)
    e = abs(integral-I)/I
    return integral, e

def main():
    I = -0.23061
    data = GetData()
    x = data[0]
    y = data[1]
    print('Integral estimations where the true integral is:', I)
    print('==============================================')
    print('Trapezoid:       {0:7.4f}  Error: {1:7.4f}'.format(*Trapezoid(x, y, I)))
    print('Trapezoid Scipy: {0:7.4f}  Error: {1:7.4f}'.format(*TrapScipy(x, y, I)))
    print('Simpsons 1/3:    {0:7.4f}  Error: {1:7.4f}'.format(*Simpsons13(x, y, I)))
    print('Simpsons 3/8:    {0:7.4f}  Error: {1:7.4f}'.format(*Simpsons38(x, y, I)))
    print('Simpsons Scipy:  {0:7.4f}  Error: {1:7.4f}'.format(*SimpsonsScipy(x, y, I)))

main()



