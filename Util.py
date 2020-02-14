import math

def InchToMeter(dim):
    return dim/39.37

def Meter4ToInch4(dim):
    return dim*2402509.61

def momentCircle(dim):
    return (math.pi*dim**4)/64

def momentRect(dim1, dim2):
    return (dim1*dim2**3)/12

def momentRing(dim1, dim2):
    r1 = dim1
    r2 = dim2
    return (math.pi*(r1**4-r2**4))/4

def momentIBeam(H, h, a, b):
    """ Calculating I for I beam with
    H = height of cross section
    h = height of web
    a = thickness of web
    b = width of beam """
    return (a*h**3/12)+(b/12)*(H**3-h**3)

def momentTBeam(dim1, dim2, dim3, dim4):
    """ Oriented like a T and starting from bottom\n
    dim1 = width, dim2 = height, dim3 = width, dim4 = height"""
    return 1