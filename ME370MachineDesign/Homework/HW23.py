import numpy as np
from Source import Fatigue
from Source import MomentOfArea
from sympy import *
from sympy.physics.continuum_mechanics.beam import Beam

def InClassStuff():
		""" W = Weight at each point, (Wi)
		y = Deflection at each point, (yi)
		
		Steps,
		1. get deflection using weight of shaft
		2. get omega of shaft using 7 - 23 or 7 - 22 or integrate
		3. get deflection from weight of loads
		4. get omega due to loads using 7 - 23 or integrate
		5. get omegaTotal using 7 - 32
		
		Integration:
			integrate accross length of shaft (similar to rayleighs or 7-23)
			omega = Sqrt(g*integral(wi yi, 0, l)/integral(wi yi^2, 0, l))"""
		# omega = Fatigue.CriticalSpeedShaft()

def Test():
	x, y, z = symbols('x y z')
	init_printing(use_unicode=True, wrap_line=False)
	
	E, I = symbols('E, I')
	b = Beam(9, E, I)

	#Apply loads
	# -point load of 12 kN downward at x = 9 and of the -1 order or,  -12<x-9>^-1
	b.apply_load(-12, 9, -1)

	# -Moment applied at x = 5 or,  5<x-5>^-2
	b.apply_load(50, 5, -2)

	# -Distributed load from x= 0 to x=5 and of -8, or  -8<x-0>^0  8<x-5>^0
	b.apply_load(-8, 0, 0, end=5)
	
	#Boundary conditions
	# -At 0,0 the deflection will be 0
	b.bc_deflection.append((0, 0))

	# -At 0, 0 the slope will be 0
	b.bc_slope.append((0, 0))

	R, M = symbols('R, M')
	b.apply_load(R, 0, -1)
	b.apply_load(M, 0, -2)
	b.solve_for_reaction_loads(R, M)
	# b.plot_shear_force()
	# b.plot_bending_moment()
	# b.plot_slope(subs={E: 20E9, I: 3.25E-6})
	# b.plot_deflection(subs={E: 20E9, I: 3.25E-6})
	# b.plot_loading_results(subs={E: 20E9, I: 3.25E-6})
	# var = b.bending_moment()
	# print(var)

def Problem4_7():
	x, y, z = symbols('x y z')

	
	A = lambda d: np.pi/4*d**2

	I1 = MomentOfArea.MomentOfArea2("circle", 1, 1).momentEnglish
	I2 = MomentOfArea.MomentOfArea2("circle", 1, 1.5).momentEnglish
	I3 = MomentOfArea.MomentOfArea2("circle", 1, 1.75).momentEnglish

	gamma = 0.282
	g = 32.2 * 12

	L1 = 0.5
	L2 = 8.0
	L3 = 11.0
	L4 = 0.5

	A1 = A(1)
	A2 = A(1.5)
	A3 = A(1.75)
	A4 = A(1)

	# E, I = symbols('E, I')

	E = 30E6
	init_printing(use_latex=True, wrap_line=False)
	b1 = Beam(L1, E, I1)
	b2 = Beam(L2, E, I2)
	b3 = Beam(L3, E, I3)
	b4 = Beam(L4, E, I1)
	ba = b1.join(b2, "fixed")
	bb = b2.join(ba, "fixed")
	bc = b3.join(bb, "fixed")
	b = b4.join(bc, "fixed")

	#Apply loads
	# -point load of 12 kN downward at x = 9 and of the -1 order or,  -12<x-9>^-1
	R1, R2 = symbols('R1, R2')
	# b.apply_load(R1, 0, -1)
	b.apply_load(-600, 8.5, -1)

	# -Moment
	

	# -Distributed load
	
	#Boundary conditions
	# -At 0,0 the deflection will be 0
	b.bc_deflection.append((0, 0))
	b.bc_deflection.append((0.5, 0))
	# print(b.load)

	# -At 0, 0 the slope will be 0
	# b.bc_slope.append((0, 0))

	# R, M = symbols('R, M')
	b.apply_load(R1, 0, -1)
	b.apply_load(R2, 20, -1)
	# b.apply_load(R, 0, -1)
	# b.apply_load(M, 0, -2)

	b.solve_for_reaction_loads(R1, R2)
	
	# b.plot_shear_force()
	# b.plot_bending_moment()
	# Y = lambdify(x, b.plot_deflection(subs={E: 30E6}), "sympy")
	expr = b.deflection()
	# print(expr)
	m = b.max_deflection()
	f = lambdify(x, expr, "sympy")

	ans = f(5)
	L1c = L1/2
	L2c = L1 + L2/2
	L3c = L1 + L2 + L3/2
	L4c = L1 + L2 + L3 + L4/2

	w1 = gamma*g*L1*A1
	w2 = gamma*g*L2*A2
	w3 = gamma*g*L3*A3
	w4 = gamma*g*L4*A4

	omega = Fatigue.RayleighsLumpedMasses([w1, w2, w3, w4], [f(L1c), f(L2c), f(L3c), f(L4c)])
	print(omega)

Problem4_7()
