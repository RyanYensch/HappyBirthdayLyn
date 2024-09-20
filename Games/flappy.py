from tkinter import *
import random
import math

HEADER_COLOUR = "#ff809d"
BACKGROUND_COLOUR = "#FFD1DC"
GAME_WIDTH = 1000
GAME_HEIGHT = 700
BIRD_COLOUR = "orange"
PIPE_COLOUR = "green"
STARTX, STARTY = 200, 350
BIRD_WIDTH, BIRD_HEIGHT = 58, 50
FLAP_POWER = 30
GRAVITY_STRENGTH = 1
TICK_LENGTH = 50
REQUIRED_SCORE = 20
PIPE_WIDTH = BIRD_WIDTH
PIPE_GAP = math.floor(BIRD_HEIGHT * 2.5)
FLIGHT_SPEED = math.floor(TICK_LENGTH/10)


canvas = None

class FlappyGame():
    class Pipes():
        def __init__(self) -> None:
            self.all_coords = []
            self.shapes = []
            self.width = PIPE_WIDTH
            self.gap = PIPE_GAP
            self.active_pipes = 0
        
        def generate_pipe(self):
            self.active_pipes += 1
            coords = [GAME_WIDTH, 0]
            length = random.randint(self.width, GAME_HEIGHT - self.width - self.gap)
            coords.append(coords[0] + self.width)
            coords.append(coords[1] + length)
            self.all_coords.append(coords)
            self.shapes.append(canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill=PIPE_COLOUR))
            
            coords = [GAME_WIDTH, length + self.gap]
            coords.append(coords[0] + self.width)
            coords.append(coords[1] + (GAME_HEIGHT - length - self.gap))
            self.all_coords.append(coords)
            self.shapes.append(canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill=PIPE_COLOUR))

        
        def move_pipes(self):
            index = 0
            remove_first = False
            for x, y, rightx, bottomy in self.all_coords:
                new_coords = [x-FLIGHT_SPEED, y, rightx-FLIGHT_SPEED, bottomy]
                self.all_coords[index] = new_coords
                canvas.delete(self.shapes[index])
                if new_coords[2] > 0:
                    self.shapes[index] = canvas.create_rectangle(new_coords[0], new_coords[1], new_coords[2], new_coords[3], fill=PIPE_COLOUR)
                else:
                    remove_first = True
                index+=1
            
                            
            if remove_first:
                self.all_coords = self.all_coords[2:]
                self.shapes = self.shapes[2:]
                self.generate_pipe()
        
        
    class Bird():
        def __init__(self) -> None:
            self.coords = [STARTX, STARTY]
            self.height = BIRD_HEIGHT
            self.width = BIRD_WIDTH
            self.speed = 0
            self.image = PhotoImage(file="Images/yippee_cat.png")
            
        def spawn_bird(self):
            self.body = canvas.create_image(self.coords[0], self.coords[1], image=self.image, anchor="nw", tag="bird")
            
        def flap(self, flaps = 2):
            canvas.delete(self.body)
            self.coords[1] -= FLAP_POWER/5
            if self.coords[1] < 0: self.coords[1] = 0
            self.speed = -3
            self.spawn_bird()
            if flaps > 0:
                self.flap(flaps-1)

            
        def fall(self):
            canvas.delete(self.body)
            self.speed += GRAVITY_STRENGTH
            self.coords[1] += self.speed
            self.spawn_bird() 
            
    
    
    def __init__(self) -> None:
        self.game_window = None
        self.has_beaten = False
        self.bird = self.Bird()
        self.pipes = self.Pipes()
        self.score = 0
        self.score_frame = None
        self.label = None
        self.done = False
        self.total_ticks = 0
        
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
        self.label = Label(self.score_frame, text=f"Score: {self.score}/{REQUIRED_SCORE}", font=("consolas", 20, "bold"), bg=HEADER_COLOUR)
        self.label.pack(side="left", pady=10, padx=10)
        
        global canvas
        canvas = Canvas(self.game_window, height= GAME_HEIGHT, width= GAME_WIDTH,
                        bg = BACKGROUND_COLOUR, highlightbackground="black", highlightthickness=4)
        canvas.pack()

        self.bird.spawn_bird()
        self.pipes.generate_pipe()
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
        self.total_ticks += 1
        if self.total_ticks * FLIGHT_SPEED >= (math.floor(GAME_WIDTH+PIPE_WIDTH)/3) and self.pipes.active_pipes < 2:
            self.pipes.generate_pipe()
        elif self.total_ticks * FLIGHT_SPEED >= (math.floor(2*(GAME_WIDTH+ PIPE_WIDTH)/3)) and self.pipes.active_pipes < 3:
            self.pipes.generate_pipe()
            
        if self.check_floor_collision() or self.check_pipe_collision():
            self.game_over()
            self.done = True
        else:
            self.bird.fall()
            self.pipes.move_pipes()
            self.game_window.after(TICK_LENGTH, self.next_tick)
        
    def check_floor_collision(self):
        return self.bird.coords[1] + self.bird.height >= GAME_HEIGHT
    
    def check_pipe_collision(self):
        for x,y, rightx, boty in self.pipes.all_coords:
            if self.bird.coords[0] <= rightx and (self.bird.coords[0] + self.bird.width) >= x:
                if y != 0 and (self.bird.coords[1] + self.bird.height) >= y:
                    return True
                elif y == 0 and self.bird.coords[1] <= boty:
                    return True
                else:
                    if x == self.bird.coords[0]:
                        self.score += 0.5
                        self.label.config(text=f"Score: {int(self.score)}/{REQUIRED_SCORE}")
                        if self.score == REQUIRED_SCORE:
                            self.label.config(fg="green")
        return False
    
                    
            
    def game_over(self) -> None:
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                           font=('consolas', 70, "bold"),
                           text="GAME OVER", fill="red", tag="game over")
        if self.score >= REQUIRED_SCORE:
            self.has_beaten = True
            canvas.create_text(canvas.winfo_width()/2, 2*canvas.winfo_height()/3,
                               font=('consolas', 25),
                               text="YOU MET THE REQUIRED SCORE\nCONGRATS", fill="red", tag="done")