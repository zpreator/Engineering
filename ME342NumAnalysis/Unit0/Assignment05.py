import numpy as np
import math
import matplotlib.pyplot as plt

E = 30 #Modulus of Elasticity
v = 0.3 #Poisons Ratio

def getFileData(fileName):
    """ Gets the data from the file"""
    newData = np.loadtxt(fileName)
    # foo = newData[:2, 1:3]
    return newData

def getPrincipleStrains(e1, e2, e3):
    """ Calculates and returns the principle strains from 
    the three measured strain values"""
    ep = (e1 + e2)/2 + math.sqrt((e1-e2)**2+(2*e3-e1-e2)**2)/2
    eq = (e1 + e2)/2 - math.sqrt((e1-e2)**2+(2*e3-e1-e2)**2)/2
    return ep, eq

def getPrincipleStresses(ep, eq):
    """ Calculates and returns the pinciple stresses from the principle
    strains, modulus of elasticity, and poison's ratio"""
    global E
    global v
    sigmap = (E*(ep+v*eq))/(1-v**2)
    sigmaq = (E*(eq+v*ep))/(1-v**2)
    return sigmap, sigmaq

def getEquivalentStress(sigmap, sigmaq):
    """ Calculates and returns the equivalent stress 
    from the principle stresses"""
    return math.sqrt(sigmap**2-sigmap*sigmaq+sigmaq**2)

def calculateEquivalentStress(e1, e2, e3):
    """ Calls all the functions to return just the equivalent
    stress from the input of the three strain values"""
    ep, eq = getPrincipleStrains(e1, e2, e3)
    sigmap, sigmaq = getPrincipleStresses(ep, eq)
    return getEquivalentStress(sigmap, sigmaq)

def displayData(data, col):
    """ Displays the data from the specified column"""
    times = [i[0] for i in data]
    values = [calculateEquivalentStress(i[1 + col], i[2 + col], i[3 + col]) for i in data]
    maximum = np.max(np.array(values))
    time = times[np.argmax(values)]
    print('The maximum is:', maximum, 'psi at time:', time, 's and the factor of safety is:', 50000/maximum)
    plt.plot(times, values)
    plt.legend(['Equivalent Stress Over Time'])
    plt.xlabel('Time elapsed (s)')
    plt.ylabel('Equivalent stress (psi)')
    plt.show()
    
    
        
def main():
    """ Gets the file text and passes it to the display function """
    data = getFileData('StrainData.txt')
    # for col use 0 for first, 3 for second, 6 for the third
    # and 9 for the fourth column
    displayData(data, 0)
    


main()
