import matplotlib.pyplot as plt

class Display:
    """The ultimate display class"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def Plot(self):
        plt.plot(self.x, self.y)
        