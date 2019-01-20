from graphics import *
from button import Button 
class Quizans:
    def __init__(self, win):
        self.win = win
        self.aButton = Button(win, Point(56, 55), 25, 10, "A") 
        self.aButton.activate() 
        self.bButton = Button(win, Point(144, 55), 25, 10, "B")
        self.bButton.activate()
        self.nextButton = Button(win, Point(186.5, 45), 13, 8, "NEXT")
        self.nextButton.activate()

    def answer(self):
        
        # Event loop 
        pt = self.win.getMouse() 
        if self.aButton.clicked(pt): 
            return "A"
        if self.bButton.clicked(pt):
            return "B"
        pt = self.win.getMouse()
        
    def next(self):
        pt = self.win.getMouse() 
        if self.nextButton.clicked(pt): 
             return True
        pt = self.win.getMouse() 