from tkinter import *
from Games.snake import SnakeGame
from Games.slide import SlideGame

BACKGROUND_COLOUR = "#FFD1DC"
TOTAL_GAMES = 2


games_beaten = set()
all_beaten = False
lines = []

def games_done():
    beaten_label.config(text=f"{len(games_beaten)} completed of {TOTAL_GAMES}")
    global all_beaten
    if all_beaten == False and len(games_beaten) == TOTAL_GAMES:
        all_beaten = True
        beaten_button = Button(window, text="YOU HAVE BEATEN ALL THE GAMES\nCLICK HERE TO GET YOUR REWARD!", font="wingdings", command=get_reward)
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

    label1 = Label(win_window, text=lines[0])
    label1.pack()
    label2 = Label(win_window, text=lines[1])
    label2.pack()


    win_window.mainloop()

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
        games_beaten.add("Slide")

    games_done()
    window.deiconify()

def read_first_two_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = [next(file) for _ in range(2)]
            return lines
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except StopIteration:
        print(f"The file {file_path} is empty or has fewer than two lines.")
        return None

file_path = 'Prize.txt'
lines = read_first_two_lines(file_path)



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