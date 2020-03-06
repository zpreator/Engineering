import math
import Util

class MomentOfArea2:
    """ Shape: circle, rectangle, ring, Tbeam\n
    -circle: dim1 = diameter\n
    -rectangle: dim1 = base (short), dim2 = height (long)\n
    -ring: dim1 = outerDiameter, dim2 = innerDiameter\n
    -Tbeam: dim1 = web width, dim2 = web height, dim3 = flat width, dim4 = flat height\n
    -Ibeam: dim1 = Total height, dim2 = web height, dim3 = web width, dim4 = total beam width
    Units: metric = 0 (m), english = 1 (in)\n"""
    momentMetric = 0.0
    momentEnglish = 0.0
    def __init__(self, shape, units, dim1=None, dim2=None, dim3=None, dim4=None):
        self.shape = shape
        self.units = units
        if self.units == 1:
            self.dim1 = Util.InchToMeter(dim1)
            self.dim2 = Util.InchToMeter(dim2)
            self.dim3 = Util.InchToMeter(dim3)
            self.dim4 = Util.InchToMeter(dim4)
        elif self.units == 0:
            self.dim1 = dim1
            self.dim2 = dim2
            self.dim3 = dim3
            self.dim4 = dim4
        self.setMoments(shape)
    
    def setMoments(self, shape):        
        if shape == "circle":
            self.momentMetric = Util.momentCircle(self.dim1)
            self.momentEnglish = Util.Meter4ToInch4(self.momentMetric)
        elif shape == "rectangle":
            self.momentMetric = Util.momentRect(self.dim1, self.dim2)
            self.momentEnglish = Util.Meter4ToInch4(self.momentMetric)
        elif shape == "ring":
            self.momentMetric = Util.momentRing(self.dim1, self.dim2)
            self.momentEnglish = Util.Meter4ToInch4(self.momentMetric)
        elif shape == "ibeam":
            self.momentMetric = Util.momentIBeam(self.dim1, self.dim2, self.dim3, self.dim4)
            self.momentEnglish = Util.Meter4ToInch4(self.momentMetric)

