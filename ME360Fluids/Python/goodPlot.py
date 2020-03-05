import numpy as np
import matplotlib.pylab as plt

def getData():
	data1 = np.array([0.047, 0.05, 0.049, 0.048, 0.045, 0.03, 0.02, 0.018, 0.015, 0.028, 0.045, 0.048, 0.05, 0.05, 0.05])
	data2 = np.array([0.3, 0.29, 0.29, 0.29, 0.27, 0.2, 0.12, 0.11, 0.14, 0.27, 0.3, 0.31, 0.32, 0.32, 0.32])
	data3 = np.array([0.8,0.8,0.78,0.75,0.65,0.4,0.38,0.35,0.4,0.65,0.75,0.8,0.85,0.82,0.82])
	data4 = np.array([1.4,1.45,1.35,1.25,1.2,0.8,0.75,0.7,0.65,0.9,1,1.3,1.5,1.5,1.5])
	data5 = np.array([2.62,2.6,2.52,2.25,1.5,1.08,0.85,0.9,1.11,1.59,2.25,2.45,2.55,2.6,2.61])
	return [data1, data2, data3, data4, data5]
	
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

def display(delPs, velocities, Cps, normalized):	
	for i, j in zip(delPs, np.array(['b', 'g', 'r', 'y', 'k' ])):
		plt.plot(np.arange(-3.5, 4.0, .5), i, j)
		plt.legend([r'$0.05\ in\ H_2O$', r'$0.3\ in\ H_2O$', r'$0.8\ in\ H_2O$', r'$1.4\ in\ H_2O$',r'$2.6\ in\ H_2O$' ])
	plt.xlabel(r'Position ($in$)')
	plt.ylabel(r'Manometer Setting ($in\ H_2O$)')
	plt.show()

	for i, j in zip(velocities, np.array(['b', 'g', 'r', 'y', 'k' ])):
		plt.plot(np.arange(-3.5, 4.0, .5), i, j)
		plt.legend([r'$0.05\ in\ H_20$', r'$0.3\ in\ H_20$', r'$0.8\ in\ H_20$', r'$1.4\ in\ H_20$',r'$2.6\ in\ H_20$' ])
	plt.xlabel(r'Position ($in$)')
	plt.ylabel(r'Velocity ($m/s$)')
	plt.show()

	for i, j in zip(Cps, np.array(['b', 'g', 'r', 'y', 'k' ])):
		plt.plot(np.arange(-3.5, 4.0, .5), i, j)
		plt.legend([r'$0.05\ in\ H_20$', r'$0.3\ in\ H_20$', r'$0.8\ in\ H_20$', r'$1.4\ in\ H_20$',r'$2.6\ in\ H_20$' ])
	plt.xlabel(r'Position ($in$)')
	plt.ylabel(r'Pressure Coefficient')
	plt.show()

	for i, j in zip(normalized, np.array(['b', 'g', 'r', 'y', 'k' ])):
		plt.plot(np.arange(-3.5, 4.0, .5), i, j)
		plt.legend([r'$0.05\ in\ H_20$', r'$0.3\ in\ H_20$', r'$0.8\ in\ H_20$', r'$1.4\ in\ H_20$',r'$2.6\ in\ H_20$' ])
	plt.xlabel(r'Position ($in$)')
	plt.ylabel(r'Normalized Velocity ($m/s)')
	plt.show()

def main():
	delPs = getData()
	velocities = []
	Cps = []
	normalized = []
	for j in range(len(delPs)):
		velocities.append([getVelocity(i, getRho()) for i in delPs[j]])
		Cps.append([getCp(i, getRho(), velocities[j][0]) for i in delPs[j]])
		normalized.append([normalize(i, velocities[j][0]) for i in velocities[j]])
	display(delPs, velocities, Cps, normalized)
	
main()
# # Change plt font family and text size
# plt.rc('font', family='serif', size=10)

# # Example data
# #t = np.linspace(0,1,num=100,endpoint=True)
# #s = np.cos(4 * np.pi * t) + 2

# # Example descreate data
# tData = np.arange(-3.5, 4.0, .5)
# sData = delPs

# #tData = np.linspace(0,1,num=20,endpoint=True)
# #sData = np.cos(4 * np.pi * tData) + 2+np.random.random(len(tData))/10
# #uData = np.random.random(len(tData))/10

# # Make the plot
# #plt.figure(figsize=(5,3)) #set the figuer size (width,height)(inches)
# #plt.plot(t,s,'-.',label='Modeled values')
# plt.errorbar(tData,sData,fmt='o',capsize=5,label='Mesured Values')

# plt.xlabel('Time (s)')
# plt.ylabel('Voltage (mV)')
# #plt.xlabel(r'Time ($s$)') #the r'...' alows for LaTeX math input
# # plt.ylabel(r'Voltage ($mV$)')
# plt.legend(loc='lower right')
# #plt.grid()
# plt.tight_layout()
# #plt.show()
# #plt.savefig('goodPlot.pdf') # save the image as a vecortized pdf
# plt.show()








