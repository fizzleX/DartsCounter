from tkinter import *

class Player():
    points = 0 
    shotsFactor = 1 / 3
    
    def __init__(self):        
        self.average = 0.0
        self.averageLeg = 0.0
        self.shots = 0
        self.shotsLeg = 0
    
    def UpdateValues(self, points):
        self.points += points
        self.shots += self.shotsFactor
        self.shotsLeg += self.shotsFactor
        self.CalcAverageLeg()
        #CalcAverage(points)
    
    def CalcAverageLeg(self):
        self.averageLeg = self.points / self.shotsLeg
           
    def CalcAverage(self, points):        
        return
    
    def NewLeg(self):
        self.averageLeg = 0.0
        self.shotsLeg = 0
    
player1 = Player()
player1.UpdateValues(60)
print(player1.averageLeg)
player1.UpdateValues(60)
print(player1.averageLeg)
player1.UpdateValues(20)
print(player1.averageLeg)
player1.UpdateValues(21)
print(player1.averageLeg)
player1.UpdateValues(34)
print(player1.averageLeg)
player1.UpdateValues(27)
print(player1.averageLeg)