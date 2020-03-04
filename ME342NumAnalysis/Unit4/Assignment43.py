"""
Zachary Preator
10/10
The mean value differs from the average value because for
the average value, the points in between the discrete data
were taken into account
"""

def trapezoidal(x,y):
    """Trapezoidal integral of discrete data"""
    integral = 0
    for i in range(len(x)-1):
        integral += (y[i+1]+y[i])/2*(x[i+1]-x[i])
    return integral

def simpsons13(x,y):
    """Simpson's 1/3 rule of integration"""
    n = len(x) // 2
    integral = 0
    for i in range(n):
        integral += 2*(x[2*i+1]-x[2*i])*(y[2*i]+4*y[2*i+1]+y[2*i+2])/6
    return integral

def simpsons38(x,y):
    """Simpson's 3/8 rule of integration"""
    n = len(x) // 3
    integral = 0
    for i in range(n):
        integral += (x[3*i+3]-x[3*i])*(y[3*i]+3*y[3*i+1]+3*y[3*i+2]+y[3*i+3])/8
    return integral

def main():
    """Main function to call all other functions"""
    x = [0,4,8,12]
    y = [0,2,4]
    fxy = [[-2,-1,4,10],[-4,-3,1,7],[-8,-8,-6,4]]
    Area = x[-1]*y[-1]
    
    
    #Trapezoidal Integral
    inttrapz = []
    for i in range(len(y)):
        inttrapz.append(trapezoidal(x,fxy[i]))
    favgtrapz = trapezoidal(y,inttrapz)/Area
    print('Trapezoidal:')
    print(favgtrapz)
    
    #Simpsons Integral
    intsimp = []
    for i in range(len(y)):
        intsimp.append(simpsons38(x,fxy[i]))
    bartSimpsonIntegral = simpsons13(y,intsimp)/Area
    print('Simpsons Method:')
    print(bartSimpsonIntegral)
    
    #Find Arithmetic Mean
    total = 0
    for i in fxy:
        total += sum(i)
    mean = total/12
    print('Arithmetic Mean:')
    print(mean)
    
main()