from scipy.interpolate import lagrange
import numpy as np

def GetData():
    return np.array([[0, 0.4, 0.8, 1.2, 1.6],[0, 0.196, 0.3688, 0.4983, 0.5699]])

def Lagrange(data):
    xPoint = 0.6
    f_lagrange = lagrange(data[0], data[1])
    value = f_lagrange(xPoint)
    return value

def FourthOrder(data, xPoint):
    firstOrder = []
    length = len(data[0])
    for i in range(length-1):
        val = (data[1][i+1]-data[1][i])/(data[0][i+1]-data[0][i])
        firstOrder.append(val)
    
    secondOrder = []
    for i in range(len(firstOrder)-1):
        val = (firstOrder[i+1]-firstOrder[i])/(data[0][i+2]-data[0][i])
        secondOrder.append(val)

    thirdOrder = []
    for i in range(len(secondOrder)-1):
        val = (secondOrder[i+1]-secondOrder[i])/(data[0][i+3]-data[0][i])
        thirdOrder.append(val)

    fourthOrder = []
    for i in range(len(thirdOrder)-1):
        val = (thirdOrder[i+1]-thirdOrder[i])/(data[0][i+4]-data[0][i])
        fourthOrder.append(val)

    first = data[1][0] + (xPoint -data[0][0])*firstOrder[0]
    second = first+(xPoint-data[0][0])*(xPoint-data[0][1])*secondOrder[0]
    third = second + (xPoint-data[0][0])*(xPoint-data[0][1])*(xPoint-data[0][2])*thirdOrder[0]
    fourth = third + (xPoint-data[0][0])*(xPoint-data[0][1])*(xPoint-data[0][2])*(xPoint-data[0][3])*fourthOrder[0]
    return fourth

def main():
    data = GetData()
    answer = Lagrange(data)
    FourthOrder(data, 0.6)
    print(answer)

main()

# def Lagrange(data, xPoint):
#     f_lagrange = lagrange(data[0], data[1])
#     value = f_lagrange(xPoint)
#     return value

# def FirstOrder(data, xPoint):
#     x = data[0]
#     y = data[1]
#     linearSpline = interp1d(x, y, kind='linear')
#     return linearSpline(xPoint)


# def SecondOrder(data, xPoint):
#     x = data[0]
#     y = data[1]
#     quadraticSpline = interp1d(x, y, kind='quadratic')
#     return quadraticSpline(xPoint)

# def ThirdOrder(data, xPoint):
#     x = data[0]
#     y = data[1]
#     cubicSpline = interp1d(x, y, kind='cubic')
#     return cubicSpline(xPoint)