from scipy.interpolate import interp1d
import numpy as np

x = np.array([0, 0.4, 0.8, 1.2, 1.6])
y = np.array([0, 0.196, 0.3688, 0.4983, 0.5699])
xTest = 0.6
linearSpline = interp1d(x, y, kind='linear')
linearValue = linearSpline(xTest)

quadraticSpline = interp1d(x, y, kind='quadratic')
quadraticValue = quadraticSpline(xTest)

cubicSpline = interp1d(x, y, kind='cubic')
cubicValue = cubicSpline(xTest)

print(linearValue, quadraticValue, cubicValue)