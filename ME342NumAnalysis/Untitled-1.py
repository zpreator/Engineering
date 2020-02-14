import math

def fToC(f):
    c = (f-32)*(5/9)
    return c, c + 273 

def twoReturn():
    return 1, 2

def main():
    # print(twoReturn())
    f = input('Enter Temperature in Fahrenheit \n')
    print(fToC(float(f)))
    
    

main()