import numpy as np
from Source import Fatigue

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
		omega = Fatigue.CriticalSpeedShaft()
