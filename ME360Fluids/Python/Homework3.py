import numpy as np

coeff = np.array([32.174, -(13.3**2/2+32.174*2.9), 0, .5*13.3**2*1.8**2])
print(np.roots(coeff))

v1 = 13.3*1.8/5.33616776
v2 = 13.3*1.8/1.45776593
print(v1, v2)