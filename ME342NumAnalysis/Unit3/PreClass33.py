from scipy.interpolate import lagrange
import numpy as np

def GetData():
    return np.array([[0, 0.4, 0.8, 1.2, 1.6],[0, 0.196, 0.3688, 0.4983, 0.5699]])

def Lagrange(data):
    xPoint = 0.6
    f_lagrange = lagrange(data[0], data[1])
    value = f_lagrange(xPoint)
    return value

def main():
    data = GetData()
    answer = Lagrange(data)
    print(answer)

main()