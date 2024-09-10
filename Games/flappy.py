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
REQUIRED_SCORE = 20


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
        self.score = 0
        self.score_frame = None
        self.label = None
        self.Done = False
        
    def game_start(self):
        self.game_window = Toplevel()
        self.game_window.title("Flappy Bird :)")
        self.game_window["bg"] = HEADER_COLOUR
        self.game_window.resizable(False, False)
        
        self.score_frame = Frame(
            self.game_window, bg=HEADER_COLOUR, width=GAME_WIDTH)
        self.score_frame.pack(fill='x', expand=True)
        back_button = Button(
            self.score_frame, text="Back to Menu", command=self.game_window.destroy)
        back_button.pack(side= "right")
        self.label = Label(self.score_frame, text="Score: {}".format(
            self.score), font=("consolas", 20, "bold"), bg=HEADER_COLOUR)
        self.label.pack(side="left", pady=10, padx=10)
        
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
        if not self.done:
            self.bird.flap()

    def next_tick(self):
        self.bird.fall()
        if self.check_floor_collision() or self.check_pipe_collision():
            self.game_over()
            self.done = True
        else:
            self.game_window.after(TICK_LENGTH, self.next_tick)
        
    def check_floor_collision(self):
        return self.bird.coords[1] + self.bird.height >= GAME_HEIGHT
    
    def check_pipe_collision(self):
        return False
        
    def game_over(self) -> None:
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                           font=('consolas', 70, "bold"),
                           text="GAME OVER", fill="red", tag="game over")
        if self.score >= REQUIRED_SCORE:
            canvas.create_text(canvas.winfo_width()/2, 2*canvas.winfo_height()/3,
                               font=('consolas', 25),
                               text="YOU MET THE REQUIRED SCORE\nCONGRATS", fill="red", tag="done")