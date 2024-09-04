import tkinter as tk
import sys
from Games.snake import *

BACKGROUND_COLOUR = "#FFD1DC"

def startSnake():
    window.withdraw()
    game = Snake()
    game_window = game.gameStart()
    window.wait_window(game_window)
    window.deiconify()

def startGame2():
    pass


window = tk.Tk()
window.title("FOR THE LOVE OF MY LIFE <3")
window.config(bg=BACKGROUND_COLOUR)

Title = tk.Label(window, text="Select A Game To Earn Points", bg=BACKGROUND_COLOUR, font=("Arial", 20, "bold"))
Title.pack(pady=20, side="top")

game_one_button = tk.Button(window, text="Snake", command=startSnake)
game_one_button.pack(pady=10)


window.mainloop()