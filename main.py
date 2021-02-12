from tkinter import *

class Player():
    shotsFactor = 1 / 3
    
    def __init__(self):    
        self.points = 0 
        self.pointsLeg = 0
        self.pointsLeft = 0    
        self.average = 0.0
        self.averageLeg = 0.0
        self.shots = 0
        self.shotsLeg = 0        
    
    # Updates the values after new points given
    def UpdateValues(self, points):
        self.pointsLeft -= points
        self.points += points
        self.pointsLeg += points
        self.shots += self.shotsFactor
        self.shotsLeg += self.shotsFactor
        self.CalcAverageLeg()
        self.CalcAverage()
    
    # calculates the average of the leg
    def CalcAverageLeg(self):
        self.averageLeg = self.pointsLeg / self.shotsLeg
    
    # calculates the average of the total match       
    def CalcAverage(self):
        self.average = self.points / self.shots                
    
    # starts a new leg
    def NewLeg(self, points):
        self.pointsLeft = points
        self.pointsLeg = 0
        self.averageLeg = 0.0
        self.shotsLeg = 0
    
player1 = Player()
player2 = Player()    

