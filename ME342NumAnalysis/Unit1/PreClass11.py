import matplotlib.pyplot as plt
import numpy as np

def plot():
    x = np.arange(0.0, 10.0, 0.1)
    plt.plot((5*(x-1)-x**2)*(np.exp(-x)-1))
    plt.show()

plot()