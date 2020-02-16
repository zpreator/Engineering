from winreg import *
from os import path
from math import *
from SandboxLibrary.RaylockDialogs import *
from SandboxLibrary.RaylockDrawing import *
from SandboxLibrary.RaylockPlot import *
from SandboxLibrary.RaylockWidgets import *
from SandboxLibrary.AppUtility import *
from SandboxLibrary.RaylockShortcuts import *
from SandboxLibrary.RaylockDoc import *

def GetCSVfile(filename):

    data = []

    with open(filename, "r") as file:

        lines = file.readlines()

        for line in lines:

            entry = line.split(",")
            data.append(entry)

    return data











    


    

    
    
    

    
    
    
    
    
    
    


