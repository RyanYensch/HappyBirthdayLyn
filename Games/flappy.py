from tkinter import *

HEADER_COLOUR = "#ff809d"
BACKGROUND_COLOUR = "#FFD1DC"


class FlappyGame():
    def __init__(self) -> None:
        self.game_window = None
        self.has_beaten = False

    def game_start(self):
        self.game_window = Toplevel()
        self.game_window.title("Flappy Bird :)")
        self.game_window["bg"] = HEADER_COLOUR
        self.game_window.resizable(False, False)
        back_button = Button(
            self.game_window, text="Back to Menu", command=self.game_window.destroy)
        back_button.pack()

        self.game_window.update()

        window_height = self.game_window.winfo_height()
        window_width = self.game_window.winfo_width()
        screen_height = self.game_window.winfo_screenheight()
        screen_width = self.game_window.winfo_screenwidth()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        self.game_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        return self.game_window
