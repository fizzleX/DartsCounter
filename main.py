from tkinter import *

class Player():
    points = 0 
    def __init__(self):        
        self.average = 0.0
        self.averageLeg = 0.0
        self.shots = 0
        self.shotsLeg = 0
    
    def CalcAverageLeg(self, points):
        if self.averageLeg != 0.0:
            self.averageLeg = (self.averageLeg + points) / 2
        else:
            self.averageLeg += points
        return
    
    def CalcAverage(self, points):
        return
    
player1 = Player()
player1.CalcAverageLeg(100)
print(player1.averageLeg)
player1.CalcAverageLeg(50)
print(player1.averageLeg)