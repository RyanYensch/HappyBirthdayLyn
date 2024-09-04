import tkinter as tk

GAME_WIDTH = 700
GAME_HEIGHT = 700
DELAY = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "black"
FOOD_COLOUR = "red"
BACKGROUN_COLOUR = "#FFD1DC"



class Snake():

    class Snake():
        pass

    class Food():
        pass

    def gameStart(self):
        self.game_window = tk.Toplevel()
        self.game_window.title("Snake :)")
        self.game_window.resizable(False, False)

        self.score = 0
        self.direction = 'right'


        label = tk.Label(self.game_window, text="Score: {}".format(self.score))
        label.pack(pady=10, side="top")
        
        back_button = tk.Button(self.game_window, text="Back to Menu", command=self.game_window.destroy)
        back_button.pack(pady=10)

        return self.game_window
    
    def nextTurn(self):
        pass

    def changeDirection(self, newDirection):
        pass

    def checkCollision(self):
        pass

    def gameOver(self):
        pass


