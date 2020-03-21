import numpy as np




q = 5400
L = 75
EI = (30e6)*120
dx = 1

MaxError = 1e-6

y0 = 0
yL = 0

x = np.arange(0,L+dx,dx)
y = np.zeros(np.size(x)) #(q*x*(L-x))/(2*EI)


error = 1
y[0] = y0 #the boundary value at the left end
y[-1] = yL #the boundary value at the right end
while error>MaxError: #continue iterating until the solution error is acceptable
    yOld = np.copy(y)
    for i in range(1,np.size(x)-1): #Gauss-Seidel loop
        y[i] = (y[i-1] + y[i+1])/2 - (x[i]*(L-x[i])*q*dx**2)/(4*EI)
    error = np.max(abs((y[1:L]-yOld[1:L])/y[1:L]))

print (y)
print (np.min(y))