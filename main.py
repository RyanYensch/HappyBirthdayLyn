from tkinter import *
from Games.snake import SnakeGame
from Games.slide import SlideGame

BACKGROUND_COLOUR = "#FFD1DC"
TOTAL_GAMES = 2

games_beaten = set()

def games_done():
    beaten_label.config(text=f"{len(games_beaten)} completed of {TOTAL_GAMES}")
    return len(games_beaten)

def start_snake():
    window.withdraw()
    game = SnakeGame()
    game_window = game.game_start()
    window.wait_window(game_window)

    if game.got_required_score():
        games_beaten.add("Snake")

    games_done()
    window.deiconify()

def start_slide():
    window.withdraw()
    game = SlideGame()
    game_window = game.game_start()
    window.wait_window(game_window)

    if game.has_beaten:
        games_beaten.add("Snake")

    games_done()
    window.deiconify()


window = Tk()
window.title("FOR THE LOVE OF MY LIFE <3")
window.config(bg=BACKGROUND_COLOUR)

Title = Label(window, text="Select A Game To Earn Points", 
              bg=BACKGROUND_COLOUR, font=("Arial", 30, "bold"))
Title.pack(pady=10, side="top")

beaten_label = Label(window, text = f"0 completed of {TOTAL_GAMES}",
                     bg=BACKGROUND_COLOUR, font=("Arial", 20, "bold"))
beaten_label.pack(pady=(0,20), side="top")


game_one_button = Button(window, text="Snake", command=start_snake)
game_one_button.pack(pady=10)

game_one_button = Button(window, text="Sliding Tiles", command=start_slide)
game_one_button.pack(pady=10)



window.mainloop()