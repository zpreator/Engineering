import numpy as np

def GetData():
    return np.array([[0, 2, 4], [7.82, 7.67, 8.36]])

def Trapezoid(x, y, I=None):
    integral = 0
    for i in range(len(x)-1):
        integral += (x[i+1]-x[i])*(y[i]+y[i+1])/2
    if I != None:
        e = abs(integral-I)/I
        return integral, e
    return integral

def Simpsons13(x, y, I=None):
    integral = 0
    for i in range(0, len(x) - 1, 2):
        integral += (x[i+2]-x[i])*(y[i]+4*y[i+1]+y[i+2])/6
    if I != None:
        e = abs(integral-I)/I
        return integral, e
    return integral

def main():
    data = GetData()
    integral = Trapezoid(data[0], data[1])
    integral2 = Simpsons13(data[0], data[1])
    print(integral, integral2)

main()