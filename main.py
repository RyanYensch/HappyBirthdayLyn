from tkinter import *
from Games.snake import *

BACKGROUND_COLOUR = "#FFD1DC"

def start_snake():
    window.withdraw()
    game = SnakeGame()
    game_window = game.game_start()
    window.wait_window(game_window)
    window.deiconify()

def start_game2():
    pass


window = Tk()
window.title("FOR THE LOVE OF MY LIFE <3")
window.config(bg=BACKGROUND_COLOUR)

Title = Label(window, text="Select A Game To Earn Points", 
              bg=BACKGROUND_COLOUR, font=("Arial", 20, "bold"))
Title.pack(pady=20, side="top")

game_one_button = Button(window, text="Snake", command=start_snake)
game_one_button.pack(pady=10)



window.mainloop()