from tkinter import *
import time
import random

HEADER_COLOUR = "#ff809d"
BACKGROUND_COLOUR = "#FFD1DC"
REQUIRED_SCORE = 10
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
        self.turn_count = 1
        self.pattern = []
        self.input_pattern = []
        
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
        
        self.start_turn()
        self.game_window.update_idletasks()
        
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
        self.input_pattern.append((row, col))
        
        for i in range(len(self.input_pattern)):
            if self.input_pattern[i] != self.pattern[i]:
                self.game_over()
                return None
        
        if len(self.input_pattern) == len(self.pattern):
            self.score += 1
            self.label.config(text=f"Score: {self.score}/{REQUIRED_SCORE}")
            if self.score == REQUIRED_SCORE:
                self.label.config(fg= "green")
                self.has_beaten = True
            self.set_buttons_state(False)
            self.start_turn()

    def flash_button(self, row, col):
        self.buttons[row][col].config(bg=HEADER_COLOUR, activebackground=HEADER_COLOUR)
        self.game_window.update_idletasks()
        time.sleep(1)
        self.buttons[row][col].config(bg=BACKGROUND_COLOUR, activebackground=BACKGROUND_COLOUR)
        self.game_window.update_idletasks()
        time.sleep(0.2)
        
    def game_over(self):
        self.set_buttons_state(False)
        label = Label(self.game_window, text=f"Game Over", font=(
            "consolas", 20, "bold"), bg=HEADER_COLOUR)
        label.grid(row=GRIDSIZE+1, column=0, columnspan=GRIDSIZE)
        self.all_buttons_colour("red")
        
    def set_buttons_state(self, enable):
        for row in self.buttons:
            for button in row:
                if enable:
                    button.config(state='normal')
                else:
                    button.config(state='disabled')
    
    def all_buttons_colour(self, colour):
        for row in self.buttons:
            for button in row:
                button.config(bg = colour)
    
    def show_pattern(self):
        for r, c in self.pattern:
            self.flash_button(r, c)

    def start_turn(self):
        self.pattern.append((random.randint(0,GRIDSIZE-1), random.randint(0,GRIDSIZE-1)))
        self.input_pattern = []
        self.set_buttons_state(False)
        self.show_pattern()
        self.set_buttons_state(True)
        