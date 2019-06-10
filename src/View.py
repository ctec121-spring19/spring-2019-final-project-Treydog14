# View.py
# 
# For TicTacToe

from graphics import *

class View:

    def __init__(self):
        self.win = GraphWin("Tic-Tac-Toe Grid", 600, 600)
        self.win.setCoords(0, 0, 3, 3)
    
        Line(Point(1, 0), Point(1, 3)).draw(self.win)
        Line(Point(2, 0), Point(2, 3)).draw(self.win)

        Line(Point(0, 1), Point(3, 1)).draw(self.win)
        Line(Point(0, 2), Point(3, 2)).draw(self.win)

    
    def drawO(self, cellNum):
        self.circ = Circle()
        self.circ.draw(self.win)

    def method(self):
        self.drawO(self.win)


def ViewTest():

    viewLot = View()
    input()

    
if __name__ == "__main__":
    ViewTest()
