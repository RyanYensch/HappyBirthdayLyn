from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
DELAY = 75
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "purple"
FOOD_COLOUR = "red"
HEADER_COLOUR = "#ff809d"
BACKGROUND_COLOUR = "#FFD1DC"
XSTART = 0
YSTART = 0
REQUIRED_SCORE = 20

canvas = None
used_coords = []


class SnakeGame():

    class Snake():
        def __init__(self):
            self.bodySize = BODY_PARTS
            self.coordinates = []
            self.squares = []
            self.eyes = []

            for _ in range(0, self.bodySize):
                self.coordinates.append([XSTART, YSTART])

            global used_coords
            used_coords = self.coordinates

            for x, y in self.coordinates:
                square = canvas.create_rectangle(
                    x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
                self.squares.append(square)

    class Food():
        def __init__(self):
            occupied = True

            while occupied:
                occupied = False
                x = random.randint(0, (GAME_WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE
                y = random.randint(
                    0, (GAME_HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE

                for xcoord, ycoord in used_coords:
                    if x == xcoord and y == ycoord:
                        occupied = True

            self.coordinates = [x, y]

            image = PhotoImage(file="Images/orangeKitty.png")
            canvas.create_image(x, y, image=image, anchor="nw", tag="food")
            canvas.image = image

    def __init__(self) -> None:
        self.game_window = None
        self.score_frame = None
        self.label = None
        self.snake = None
        self.food = None
        self.score = 0
        self.direction = 'right'

    def got_required_score(self):
        if self.score >= REQUIRED_SCORE:
            return True
        return False

    def game_start(self):
        self.game_window = Toplevel()
        self.game_window.title("Snake :)")
        self.game_window["bg"] = HEADER_COLOUR
        self.game_window.resizable(False, False)

        self.score_frame = Frame(
            self.game_window, bg=HEADER_COLOUR, width=GAME_WIDTH)
        self.score_frame.pack(fill='x', expand=True)

        self.label = Label(self.score_frame, text=f"Score: {self.score}/{REQUIRED_SCORE}", font=("consolas", 20, "bold"), bg=HEADER_COLOUR)
        self.label.pack(side="left", pady=10, padx=10)

        back_button = Button(
            self.score_frame, text="Back to Menu", command=self.game_window.destroy)
        back_button.pack(side="right", pady=10, padx=10)

        global canvas
        canvas = Canvas(self.game_window, height=GAME_HEIGHT, width=GAME_WIDTH,
                        bg=BACKGROUND_COLOUR,
                        highlightbackground="black", highlightthickness=4)
        canvas.pack()

        self.game_window.update()

        window_height = self.game_window.winfo_height()
        window_width = self.game_window.winfo_width()
        screen_height = self.game_window.winfo_screenheight()
        screen_width = self.game_window.winfo_screenwidth()

        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))

        self.game_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.game_window.bind(
            '<Left>', lambda event: self.change_direction('left'))
        self.game_window.bind(
            '<Right>', lambda event: self.change_direction('right'))
        self.game_window.bind(
            '<Up>', lambda event: self.change_direction('up'))
        self.game_window.bind(
            '<Down>', lambda event: self.change_direction('down'))
        self.game_window.bind(
            '<a>', lambda event: self.change_direction('left'))
        self.game_window.bind(
            '<d>', lambda event: self.change_direction('right'))
        self.game_window.bind('<w>', lambda event: self.change_direction('up'))
        self.game_window.bind(
            '<s>', lambda event: self.change_direction('down'))

        self.snake = self.Snake()
        self.food = self.Food()

        self.next_turn(self.snake, self.food)

        return self.game_window

    def next_turn(self, snake, food):
        x, y = snake.coordinates[0]

        if self.direction == 'up':
            y -= SPACE_SIZE
        elif self.direction == 'down':
            y += SPACE_SIZE
        elif self.direction == 'left':
            x -= SPACE_SIZE
        elif self.direction == 'right':
            x += SPACE_SIZE

        snake.coordinates.insert(0, (x, y))
        canvas.delete("eyes")
        snake.eyes = []
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                         fill=SNAKE_COLOUR, tag="snake")
        snake.squares.insert(0, square)

        heart_emoji = "❤︎"
        heart_color = "pink"

        if self.direction == 'up':
            eye1 = canvas.create_text(x + int(SPACE_SIZE / 4), y + int(SPACE_SIZE / 4),
                                      text=heart_emoji, font=("Helvetica", 24), fill=heart_color,
                                      tag="eyes")
            eye2 = canvas.create_text(x + int(3 * SPACE_SIZE / 4), y + int(SPACE_SIZE / 4),
                                      text=heart_emoji, font=("Helvetica", 24), fill=heart_color,
                                      tag="eyes")
            snake.eyes.append([eye1, eye2])
        elif self.direction == 'down':
            eye1 = canvas.create_text(x + int(SPACE_SIZE / 4), y + int(3 * SPACE_SIZE / 4),
                                      text=heart_emoji, font=("Helvetica", 24), fill=heart_color,
                                      tag="eyes")
            eye2 = canvas.create_text(x + int(3 * SPACE_SIZE / 4), y + int(3 * SPACE_SIZE / 4),
                                      text=heart_emoji, font=("Helvetica", 24), fill=heart_color,
                                      tag="eyes")
            snake.eyes.append([eye1, eye2])
        elif self.direction == 'left':
            eye1 = canvas.create_text(x + int(SPACE_SIZE / 4), y + int(SPACE_SIZE / 4),
                                      text=heart_emoji, font=("Helvetica", 24), fill=heart_color,
                                      tag="eyes")
            eye2 = canvas.create_text(x + int(SPACE_SIZE / 4), y + int(3 * SPACE_SIZE / 4),
                                      text=heart_emoji, font=("Helvetica", 24), fill=heart_color,
                                      tag="eyes")
            snake.eyes.append([eye1, eye2])
        elif self.direction == 'right':
            eye1 = canvas.create_text(x + int(3 * SPACE_SIZE / 4), y + int(SPACE_SIZE / 4),
                                      text=heart_emoji, font=("Helvetica", 24), fill=heart_color,
                                      tag="eyes")
            eye2 = canvas.create_text(x + int(3 * SPACE_SIZE / 4), y + int(3 * SPACE_SIZE / 4),
                                      text=heart_emoji, font=("Helvetica", 24), fill=heart_color,
                                      tag="eyes")
            snake.eyes.append([eye1, eye2])

        if x == food.coordinates[0] and y == food.coordinates[1]:
            self.score += 1
            self.label.config(text=f"Score: {self.score}/{REQUIRED_SCORE}")
            if self.score == REQUIRED_SCORE:
                self.label.config(fg="green")
            canvas.delete("food")

            food = self.Food()
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        global used_coords
        used_coords = snake.coordinates

        if self.check_collision(self.snake):
            self.game_over()
        else:
            self.game_window.after(DELAY, self.next_turn, snake, food)

    def change_direction(self, new_direction) -> None:
        if new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction
        elif new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction

    def check_collision(self, snake) -> None:
        x, y = snake.coordinates[0]
        if x < 0 or x >= GAME_WIDTH:
            return True
        elif y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

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
