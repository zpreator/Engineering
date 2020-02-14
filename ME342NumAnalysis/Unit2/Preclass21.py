import numpy as np
import scipy

def MatricesNP():
		A = np.array([[2, -6, 1], [-.5, -3, 8],[5, 0, -2]])
		B = np.array([8, -12, 6])
		C = np.linalg.solve(A, B)
		print(C)
		
def MatricesSci():
		A = np.array([[2, -6, 1], [-.5, -3, 8],[5, 0, -2]])
		B = np.array([8, -12, 6])
		C = scipy.linalg.solve(A, B)
		print(C)		
		
MatricesSci()
