from utilites.Raylock import *
# from SandboxLibrary.Raylock import *

class App:

    def __init__(self):

        StartAppUtility(self)
        AddInput(self, 'Axial Force')
        AddInput(self, 'Cross Sectional Area', units='inches^2')
        AddOutput(self, 'Normal Stress')
        # AddTable(self, 'My table', [['First Header', 'Second Header'],['Item 1', 'Item 2']])

        # add inputs
        # add outputs
        # add drawings
        # add plots
        # add tables


    def solve(self):
        F = GetInput(self, 'Axial Force')
        A = GetInput(self, 'Cross Sectional Area')
        
        NormalStress = F/A
        SetOutput(self, 'Normal Stress', NormalStress)
        
        # retrieve inputs
        # perform calculations
        # set outputs


