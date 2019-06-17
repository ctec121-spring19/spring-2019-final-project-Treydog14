# Controller.py
#
# For TicTacToe

from View import View
from Model import Model

class Controller:
    def __init__(self):
        self.Game = Model()
        self.Graphics = View()
        self.play_game()
    
    def clicked_board(self):
        mouseX, mouseY = Game.mouse.get_pos()  # Makes mouseX and mouseY equal to the coordinates of the mouse
        row, col = self.Game.find_cell(mouseX, mouseY) # board_position returns which row and column the user clicked in

        if self.Game.cell_occupied(col, row): # Checks to see if the space is full
            return # If it is, do nothing.
        else: # If it is
            self.Graphics.draw_move(self.Game.status, row, col, self.Game.CELL_DIMENSIONS) # Draw the Symbol onto the board
            self.Game.update_grid(row, col)
            self.Game.toggle_turn()

    def play_game(self):
        running = True
        while running:
            # Check to end the game
            if (self.Game.status == "X_Win") or (self.Game.status == "O_Win") or (self.Game.status == "Tie"):
                running = False

            self.check_for_event() # Checks to see if the window X button was pressed or if the user clicked
            self.Game.change_status() # Updates the status
            self.Game.choose_message()
            self.Graphics.draw_winning_line(self.Game.win_location) # Draws the winning line (if needed)
            self.Graphics.draw_status(self.Game.game_message) # Redraw the status with the new message
            self.Graphics.update_board() # Redraws the board

    def check_for_event(self):
        for event in event.get(): # Finds events that are currently queued up
            if event.type == Game.QUIT:  # If the window close button is pressed
                Game.quit()
                sys.exit()
            elif event.type == Game.MOUSEBUTTONDOWN: # If the mouse is clicked
                self.clicked_board() # Run clicked_board()

def ControllerTest():
    controller = Controller()
    controller.playgame()

if __name__ == "__main__":
    ControllerTest()
