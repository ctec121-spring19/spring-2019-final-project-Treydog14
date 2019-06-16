# Model.py
#
# For TicTacToe

from View import *


class Model:

    def __init__(self):
        self.status = "X_Turn"
        self.view = View()
        self.cellList = [None, None, None, None, None, None, None, None, None]   
        self.win_location = None, None
        self.game_message = "X's Turn"

    def ControlX():
        click = v.Click()
        if click == 0:
            v.drawX(0)
        elif click == 1:
            v.drawX(1)
        elif click == 2:
            v.drawX(2)
        elif click == 3:
            v.drawX(3)
        elif click == 4:
            v.drawX(4)
        elif click == 5:
            v.drawX(5)
        elif click == 6:
            v.drawX(6)
        elif click == 7:
            v.drawX(7)
        elif click == 8:
            v.drawX(8)
        else:
            v.Message(3, "Please choose a valid cell.")
        return click
    def ControlO():
        click = v.Click()
        if click == 0:
            v.drawO(0)
        elif click == 1:
            v.drawO(1)
        elif click == 2:
            v.drawO(2)
        elif click == 3:
            v.drawO(3)
        elif click == 4:
            v.drawO(4)
        elif click == 5:
            v.drawO(5)
        elif click == 6:
            v.drawO(6)
        elif click == 7:
            v.drawO(7)
        elif click == 8:
            v.drawO(8)
        else:
            v.Message(3, "Please choose a valid cell.")
        return click
    choicesX = []
    choicesO = []

    playerOneTurn = True
    print(playerOneTurn)
    winner = False

def turns():
    while winner == False:
        v.Grid()
        print(choicesX)
        if playerOneTurn:
            v.eraseMessages()
            v.Message(1, "Player one's turn.")
            choiceX = v.Click()
        else:
            v.eraseMessages()
            v.Message(1, "Player two's turn.")
            choiceO = v.Click()


        if playerOneTurn:
            choiceX = ControlX()
            choicesX.append(choiceX)
        else:
            choiceO = ControlO()
            choicesO.append(choiceO)
        for i in choicesX:
            print(i)
            if int(i) == 0 and int(i) == 1 and int(i) == 2:
                print("Winner!")
        playerOneTurn = not playerOneTurn
        print(playerOneTurn)

def ModelTest():
    m = Model()
    v = View()

    if __name__ == "__main__":
        ModelTest()
