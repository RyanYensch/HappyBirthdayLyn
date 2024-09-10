from tkinter import *
import time

HEADER_COLOUR = "#ff809d"
BACKGROUND_COLOUR = "#FFD1DC"
REQUIRED_SCORE = 12
GRIDSIZE = 4
TILESIZE = 1


class SimonGame():
    def __init__(self) -> None:
        self.has_beaten = False
        self.buttons = []
        self.label = NONE
        self.game_window = None
        self.score = 0
        self.buttons = []
        self.score_frame = None
        self.label = None
        
    def game_start(self):
        self.game_window = Toplevel()
        self.game_window.title("Snake :)")
        self.game_window["bg"] = HEADER_COLOUR
        self.game_window.resizable(False, False)

        self.score_frame = Frame(
        self.game_window, bg=HEADER_COLOUR)
        self.score_frame = Frame(self.game_window, bg=HEADER_COLOUR)
        self.score_frame.grid(
            row=0, column=0, columnspan=GRIDSIZE, sticky="nsew")

        self.label = Label(self.score_frame, text=f"Score: {self.score}/{REQUIRED_SCORE}", font=(
            "consolas", 20, "bold"), bg=HEADER_COLOUR)
        self.label.grid(row=0, column=0, sticky="w", columnspan=GRIDSIZE-1)

        back_button = Button(
            self.score_frame, text="Back to Menu", command=self.game_window.destroy)
        back_button.grid(row=0, column=GRIDSIZE-1,
                         sticky="e", padx=(20*20*TILESIZE, 0))
        
        self.initialise_buttons()
        
        self.game_window.update()

        window_height = self.game_window.winfo_height()
        window_width = self.game_window.winfo_width()
        screen_height = self.game_window.winfo_screenheight()
        screen_width = self.game_window.winfo_screenwidth()

        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))

        self.game_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.flash_button(0,0)

        
        return self.game_window
    
    
    def initialise_buttons(self):
        for r in range(0, GRIDSIZE):
            row = []
            for c in range(0, GRIDSIZE):
                button = Button(self.game_window, text="", font=('Arial', 10, 'bold'),
                                width=1, height=8, fg="black",
                                bg=BACKGROUND_COLOUR, activebackground=BACKGROUND_COLOUR, bd=3,
                                highlightthickness=0, command=lambda r=r, c=c: self.button_clicked(r, c))
                row.append(button)
                button.grid(row=r+1, column=c, sticky="nsew")

            self.buttons.append(row)
            
    def button_clicked(self, row, col):
        pass
    
    def flash_button(self, row, col):
        self.buttons[row][col].config(bg=HEADER_COLOUR, activebackground=HEADER_COLOUR)
        self.game_window.update_idletasks()
        time.sleep(1)
        self.buttons[row][col].config(bg=BACKGROUND_COLOUR, activebackground=BACKGROUND_COLOUR)
