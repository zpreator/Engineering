from utilities.Raylock import *

class App:

    def __init__(self):

        StartAppUtility(self)
        AddInput(self, 'Axial Force')
        AddInput(self, 'Cross Sectional Area', units='inches^2')
        AddOutput(self, 'Normal Stress')
        

        # add inputs
        # add outputs
        # add drawings
        # add plots
        # add tables


    def solve(self):

        AxialForce = GetInput('Axial Force')
        CrossSectionalArea = GetInput('Cross Sectional Area')
        
        NormalStress = AxialForce/CrossSectionalArea
        SetOutput(self, 'Normal Stress', NormalStress)
        
        # retrieve inputs
        # perform calculations
        # set outputs


