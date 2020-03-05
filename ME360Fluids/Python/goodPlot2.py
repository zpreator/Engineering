import numpy as np
import matplotlib.pylab as plt

# Change plt font family and text size
plt.rc('font', family='serif', size=10)
#plt.rc('text', usetex=True)  #render text output with LaTeX

# Example data
t = np.linspace(0,1,num=100,endpoint=True)
s = np.cos(4 * np.pi * t) + 2

# Example descrete data
tData = np.linspace(0,1,num=20,endpoint=True)
sData = np.cos(4 * np.pi * tData) + 2+np.random.random(len(tData))/10
uData =np.random.random(len(tData))/10

# Make the plot
plt.figure(figsize=(5,3)) #set the figure size (width,height)(inches)
plt.plot(t,s,'-.',label='Modeled values')
plt.errorbar(tData,sData,yerr=uData,fmt='o',capsize=5,label='Mesured Values')

plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
#plt.xlabel(r'Time ($s$)')
#plt.ylabel(r'Voltage ($mV$)')
plt.legend(loc='lower right')
#plt.grid()
plt.tight_layout()
#plt.subplots_adjust(bottom=0.16, top=0.95, left=0.12, right=0.96) #for manual control of plot area
#plt.show()
plt.savefig('goodPlot.pdf',format='pdf')








