import numpy as np
import matplotlib.pylab as plt

def getData():
	data = np.array([0.05, 0.05, 0.05, 0.048, 0.045, 0.03, 0.02, 0.018, 0.015, 0.028, 0.045, 0.048, 0.05, 0.05, 0.05])
	return data
	
def getRho():
	R=0.287 #KJ/kgk
	Patm=85.2 #kPa
	T=20.5+273 #K
	rho = Patm/(R*T)
	return rho
	
def getVelocity(delP, rho):
	
	delP=delP*3.387/13.6*1000 #Pa

	return np.sqrt(2*delP/rho)
	
def getCp(delP, rho, U):
	return delP/(.5*rho*U**2)

def normalize(velocity, U):
	return velocity/U
rho = getRho()

delPs = getData()
velocities = [getVelocity(i, rho) for i in delPs]	
Cps=[getCp(i, rho, velocities[0]) for i in delPs]
normalized = [normalize(i, velocities[0]) for i in velocities]
	
# Change plt font family and text size
plt.rc('font', family='serif', size=10)

# Example data
#t = np.linspace(0,1,num=100,endpoint=True)
#s = np.cos(4 * np.pi * t) + 2

# Example descreate data
tData = np.arange(-3.5, 4.0, .5)
sData = delPs

)#tData = np.linspace(0,1,num=20,endpoint=True)
#sData = np.cos(4 * np.pi * tData) + 2+np.random.random(len(tData))/10
#uData = np.random.random(len(tData))/10

# Make the plot
#plt.figure(figsize=(5,3)) #set the figuer size (width,height)(inches)
#plt.plot(t,s,'-.',label='Modeled values')
plt.errorbar(tData,sData,fmt='o',capsize=5,label='Mesured Values')

plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
#plt.xlabel(r'Time ($s$)') #the r'...' alows for LaTeX math input
#plt.ylabel(r'Voltage ($mV$)')
plt.legend(loc='lower right')
#plt.grid()
plt.tight_layout()
#plt.show()
#plt.savefig('goodPlot.pdf') # save the image as a vecortized pdf
plt.show()








