# View.py
# 
# For TicTacToe

from graphics import *

class View:

    def __init__(self):

        self.win = GraphWin("Tic-Tac-Toe", 600, 600)

    def Grid(self):
        # draw grid lines
        Line(Point(200,50),Point(200,550)).draw(self.win)
        Line(Point(400,50),Point(400,550)).draw(self.win)
        Line(Point(50,200),Point(550,200)).draw(self.win)
        Line(Point(50,400),Point(550,400)).draw(self.win)

        # Top text "tic tac toe"
        self.topText = Text(Point(300,25),"Tic Tac Toe")
        self.topText.setStyle("bold")
        self.topText.setSize(18)
        self.topText.draw(self.win)

        # Bottom text formatting and location 
        self.bottomText = Text(Point(300,575),"")
        self.bottomText.setStyle("bold")
        self.bottomText.setSize(18)
        self.bottomText.draw(self.win)   
    
    def startText(self, message):
        self.bottomText.setText('')


    def getClick(self):
        p1mouse = self.win.getMouse()
        p1x = p1mouse.getX()
        p1y = p1mouse.getY()

        if int(p1x) == 0 and int(p1y) == 0:
            return cell_0
        elif int(p1x) == 1 and int(p1y) == 0:
            return cell_1
        elif int(p1x) == 2 and int(p1y) == 0:
            return cell_2
        elif int(p1x) == 0 and int(p1y) == 1:
            return cell_3
        elif int(p1x) == 1 and int(p1y) == 1:
            return cell_4
        elif int(p1x) == 2 and int(p1y) == 1:
            return cell_5
        elif int(p1x) == 0 and int(p1y) == 2:
            return cell_6
        elif int(p1x) == 1 and int(p1y) == 2:
            return cell_7
        elif int(p1x) == 2 and int(p1y) == 2:
            return cell_8
    def player1(self):
        message = Text(Point(self.win.getWidth()/2, 480), "Player one's turn.")
        message.draw(self.win)
    def player2(self):
        message = Text(Point(self.win.getWidth()/2, 480), "Player two's turn.")
        message.draw(self.win)


def viewTest():
    v = View()
    v.Grid()
    print(v.getClick())
    input()

    
if __name__ == "__main__":
    viewTest()
