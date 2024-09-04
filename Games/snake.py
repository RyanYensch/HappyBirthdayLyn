from tkinter import *

GAME_WIDTH = 700
GAME_HEIGHT = 700
DELAY = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "black"
FOOD_COLOUR = "red"
HEADER_COLOUR = "#ff809d"
BACKGROUND_COLOUR = "#FFD1DC"



class Snake():

    class Snake():
        pass

    class Food():
        pass

    def gameStart(self):
        self.game_window = Toplevel()
        self.game_window.title("Snake :)")
        self.game_window["bg"] = HEADER_COLOUR
        self.game_window.resizable(False, False)

        self.score = 0
        self.direction = 'right'

        self.scoreFrame = Frame(self.game_window, bg=HEADER_COLOUR, width=GAME_WIDTH)
        self.scoreFrame.pack(fill='x', expand=True)

        label = Label(self.scoreFrame, text="Score: {}".format(self.score), font=("consolas", 20, "bold"), bg=HEADER_COLOUR)
        label.pack(side="left", pady=10, padx=10)
        
        back_button = Button(self.scoreFrame, text="Back to Menu", command=self.game_window.destroy)
        back_button.pack(side = "right", pady=10, padx=10)

        self.canvas = Canvas(self.game_window, height=GAME_HEIGHT, width=GAME_WIDTH, bg = BACKGROUND_COLOUR)
        self.canvas.pack()

        self.game_window.update()


        windowHeight = self.game_window.winfo_height()
        windowWidth = self.game_window.winfo_width()
        screenHeight = self.game_window.winfo_screenheight()
        screenWidth = self.game_window.winfo_screenwidth()

        x = int((screenWidth/2) - (windowWidth/2))
        y = int((screenHeight/2) - (windowHeight/2))

        self.game_window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")


        return self.game_window
    
    def nextTurn(self):
        pass

    def changeDirection(self, newDirection):
        pass

    def checkCollision(self):
        pass

    def gameOver(self):
        pass


