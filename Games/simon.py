from tkinter import *

HEADER_COLOUR = "#ff809d"
BACKGROUND_COLOUR = "#FFD1DC"
REQUIRED_SCORE = 15


class SimonGame():
    def __init__(self) -> None:
        self.has_beaten = False
        self.buttons = []
        self.label = NONE
        self.game_window = None
        self.score = 0
        
    def game_start(self):
        self.game_window = Toplevel()
        self.game_window.title("Snake :)")
        self.game_window["bg"] = HEADER_COLOUR
        self.game_window.resizable(False, False)

        self.score_frame = Frame(
        self.game_window, bg=HEADER_COLOUR)
        self.score_frame.pack(fill='x', expand=True)

        self.label = Label(self.score_frame, text=f"Score: {self.score}/{REQUIRED_SCORE}", font=("consolas", 20, "bold"), bg=HEADER_COLOUR)
        self.label.pack(side="left", pady=10, padx=10)

        back_button = Button(
            self.score_frame, text="Back to Menu", command=self.game_window.destroy)
        back_button.pack(side="right", pady=10, padx=10)
        
        
        self.game_window.update()

        window_height = self.game_window.winfo_height()
        window_width = self.game_window.winfo_width()
        screen_height = self.game_window.winfo_screenheight()
        screen_width = self.game_window.winfo_screenwidth()

        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))

        self.game_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        return self.game_window