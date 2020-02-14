import math

def mag(x, y):
    return math.sqrt(x**2 + y**2)

def angle(x, y):
    return math.atan2(y, x)

def r2d(theta):
    return 180/math.pi * theta

def rect2cyl(x, y):
    return mag(x,y), r2d(angle(x,y))

def main():
    x = input("enter the x coordinates \n")
    y = input("enter the y coordinates \n")

    r, theta = rect2cyl(float(x), float(y))
    print(r, theta)

main()