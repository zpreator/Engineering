import numpy as np
import math

def GetData():
    """ Gets the data from the txt file"""
    data = np.loadtxt(u"/Repos/Engineering/ME342NumAnalysis/Unit3/PreClass32.txt", unpack=True)
    return data

