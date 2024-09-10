from tkinter import *

HEADER_COLOUR = "#ff809d"
BACKGROUND_COLOUR = "#FFD1DC"
GAME_WIDTH = 1000
GAME_HEIGHT = 700
BIRD_COLOUR = "orange"
PIPE_COLOUR = "green"
STARTX, STARTY = 200, 350
BIRD_WIDTH, BIRD_HEIGHT = 75, 50
FLAP_POWER = 30
GRAVITY_STRENGTH = 1
TICK_LENGTH = 50


canvas = None

class FlappyGame():
    class Bird():
        def __init__(self) -> None:
            self.coords = [STARTX, STARTY]
            self.height = BIRD_HEIGHT
            self.width = BIRD_WIDTH
            self.speed = 0
            
        def spawn_bird(self):
            self.body = canvas.create_rectangle(self.coords[0], self.coords[1], 
                                                self.coords[0] + self.width, self.coords[1] + self.height,
                                                fill = BIRD_COLOUR, tag="bird")
            
        def flap(self):
            canvas.delete(self.body)
            self.coords[1] -= FLAP_POWER
            if self.coords[1] < 0: self.coords = 0
            self.speed = 0
            self.spawn_bird()
            
        def fall(self):
            canvas.delete(self.body)
            self.speed += GRAVITY_STRENGTH
            self.coords[1] += self.speed
            self.spawn_bird() 
            
    
    
    def __init__(self) -> None:
        self.game_window = None
        self.has_beaten = False
        self.bird = self.Bird()
        
    def game_start(self):
        self.game_window = Toplevel()
        self.game_window.title("Flappy Bird :)")
        self.game_window["bg"] = HEADER_COLOUR
        self.game_window.resizable(False, False)
        back_button = Button(
            self.game_window, text="Back to Menu", command=self.game_window.destroy)
        back_button.pack()
        
        global canvas
        canvas = Canvas(self.game_window, height= GAME_HEIGHT, width= GAME_WIDTH,
                        bg = BACKGROUND_COLOUR, highlightbackground="black", highlightthickness=4)
        canvas.pack()

        self.bird.spawn_bird()
        self.game_window.update()

        window_height = self.game_window.winfo_height()
        window_width = self.game_window.winfo_width()
        screen_height = self.game_window.winfo_screenheight()
        screen_width = self.game_window.winfo_screenwidth()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        self.game_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.game_window.bind('<Up>', lambda event: self.flap())
        self.game_window.bind('<w>', lambda event: self.flap())
        self.game_window.bind('<space>', lambda event: self.flap())
        
        self.next_tick()

        return self.game_window
    
    def flap(self):
        self.bird.flap()

    def next_tick(self):
        self.bird.fall()
        self.game_window.after(TICK_LENGTH, self.next_tick)