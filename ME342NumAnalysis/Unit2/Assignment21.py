import numpy as np
import scipy
import math

def MatricesSolve(A, B):
	""" Solves a set of matrices A, B """
	A = np.array(A)
	B = np.array(B)
	C = np.linalg.solve(A, B)
	print(C)
	return C
		

def Problem1():
	""" Solves the problem given in Unit 2.1 """
	g = 9.81
	m1 = 40
	m2 = 10
	m3 = 50
	ang1 = math.radians(30)
	ang2 = math.radians(60)
	mu1 = 0.2
	mu2 = 0.5
	mu3 = 0.3
	#Equation 1
	#E1 = m1*math.sin(30)*g+40*math.cos(30)*g*mu1-T1-40*a
	
	V1 = m1*math.sin(ang1)*g+m1*math.cos(ang1)*g*mu1
	#Equation 2
	#E2 = T1 + 10*math.sin(30)*g+10*math.cos(30)*g*mu2-T2-10*a
	V2 = m2*math.sin(ang1)*g+m2*math.cos(ang1)*g*mu2
	#Equation 3
	# E3 = T2 - 50*math.sin(60)*g+50*math.cos(60)*g*mu3-50*a
	V3 = -m3*math.sin(ang2)*g+m3*math.cos(ang2)*g*mu3
	A = np.array([[-1, 0, -40], [1, -1, -10],[0, 1, -50]])
	B = np.array([-V1, -V2, -V3])
	C = MatricesSolve(A, B)
	

Problem1()