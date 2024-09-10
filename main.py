from tkinter import *
from Games.snake import SnakeGame
from Games.slide import SlideGame
from Games.mines import MineGame
from Games.flappy import FlappyGame

BACKGROUND_COLOUR = "#FFD1DC"
TOTAL_GAMES = 4


games_beaten = set()
all_beaten = False
lines = []


def games_done():
    beaten_label.config(text=f"{len(games_beaten)} completed of {TOTAL_GAMES}")
    global all_beaten
    if all_beaten == False and len(games_beaten) == TOTAL_GAMES:
        all_beaten = True
        beaten_button = Button(
            window, text="YOU HAVE BEATEN ALL THE GAMES\nCLICK HERE TO GET YOUR REWARD!", font="wingdings", command=get_reward)
        beaten_button.pack(pady=20)

    return len(games_beaten)


def get_reward():
    window.destroy()
    win_window = Tk()
    win_window.title("YOU DID IT BABY")
    win_window.title("FOR THE LOVE OF MY LIFE <3")
    win_window.config(bg=BACKGROUND_COLOUR)

    win_title = Label(win_window, text="OMG YOU DID IT HERES YOUR PRIZE!",
                      bg=BACKGROUND_COLOUR, font=("Arial", 30, "bold"))
    win_title.pack(pady=10, side="top")

    label1 = Label(win_window, text=lines[0], font=("Arial", 20, "bold"))
    label1.pack()
    label2 = Label(win_window, text=lines[1], font=("Arial", 20))
    label2.pack()

    win_window.mainloop()


def start_snake():
    window.withdraw()
    game = SnakeGame()
    game_window = game.game_start()
    window.wait_window(game_window)

    if game.got_required_score():
        games_beaten.add("Snake")
        snake_button.config(fg="green", activeforeground="green")

    games_done()
    window.deiconify()


def start_slide():
    window.withdraw()
    game = SlideGame()
    game_window = game.game_start()
    window.wait_window(game_window)

    if game.has_beaten:
        games_beaten.add("Slide")
        slide_button.config(fg="green", activeforeground="green")


    games_done()
    window.deiconify()


def start_mines():
    window.withdraw()
    game = MineGame()
    game_window = game.game_start()
    window.wait_window(game_window)

    if game.has_beaten:
        games_beaten.add("Mines")
        mine_button.config(fg="green", activeforeground="green")


    games_done()
    window.deiconify()
    

def start_flappy():
    window.withdraw()
    game = FlappyGame()
    game_window = game.game_start()
    window.wait_window(game_window)

    if game.has_beaten:
        games_beaten.add("flappy")
        flap_button.config(fg="green", activeforeground="green")


    games_done()
    window.deiconify()


def read_first_two_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            filelines = [next(file) for _ in range(2)]
            return filelines
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except StopIteration:
        print(f"The file {file_path} is empty or has fewer than two lines.")
        return None


FILE_PATH = 'Prize.txt'
lines = read_first_two_lines(FILE_PATH)


window = Tk()
window.title("FOR THE LOVE OF MY LIFE <3")
window.config(bg=BACKGROUND_COLOUR)

Title = Label(window, text="Select A Game To Earn Points",
              bg=BACKGROUND_COLOUR, font=("Arial", 30, "bold"))
Title.pack(pady=10, side="top")

beaten_label = Label(window, text=f"0 completed of {TOTAL_GAMES}",
                     bg=BACKGROUND_COLOUR, font=("Arial", 20, "bold"))
beaten_label.pack(pady=(0, 20), side="top")


snake_button = Button(window, text="Snake", command=start_snake)
snake_button.pack(pady=10)

slide_button = Button(window, text="Sliding Tiles", command=start_slide)
slide_button.pack(pady=10)

mine_button = Button(window, text="Minesweeper", command=start_mines)
mine_button.pack(pady=10)

flap_button = Button(window, text="Flappy Bird", command=start_flappy)
flap_button.pack(pady=10)


window.mainloop()
