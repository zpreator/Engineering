import numpy as np

def PowerLawFit(xdata,ydata):
        #linearize the data
        xdata = np.log(xdata)
        ydata = np.log(ydata)

        #least-squares regression
        a,b,r2 = LinearLeastSquaresRegression(xdata,ydata)

        #de-linearize the coefficents
        a = np.exp(a)
        b = b
        
        print('\nPower Law Model')
        print('y = {:1.6f}x**{:1.6f} '.format(a,b))
        print('r**2 = ',r2)

        return a,b,r2

def LinearFit(xdata,ydata):
        #least-squares regression
        a,b,r2 = LinearLeastSquaresRegression(xdata,ydata)
        
        print('Linear Model')
        print('y = {:1.6f} + {:1.6f} x'.format(a,b))
        print('r**2 = ',r2)
        
        return a,b,r2

def LinearLeastSquaresRegression(xdata,ydata):
	n = xdata.size
	sumx = xdata.sum()
	sumx2 = (xdata*xdata).sum()
	sumy = ydata.sum()
	sumy2 = (ydata*ydata).sum()
	sumxy = (xdata*ydata).sum()

	Rx = np.array([[n,sumx],[sumx,sumx2]])
	Ry = np.array([sumy,sumxy])
	a,b = np.linalg.solve(Rx,Ry)
	r2 = (a*sumy + b*sumxy - sumy**2/n)/(sumy2 - sumy**2/n)

	return a,b,r2

##### Example ######
import matplotlib.pyplot as plt

#training data
x = np.linspace(0.01,3,7)
y = 2.3*x**1.4
plt.plot(x,y,'o')

#ploting data for the fit function
xx = np.linspace(x.min(),x.max(),100)

#curve-fits
a,b,r = LinearFit(x,y)
plt.plot(xx,a+b*xx,label='Linear')

a,b,r = PowerLawFit(x,y)
plt.plot(xx,a*xx**b,label='Power-Law')

plt.legend()
plt.show()
