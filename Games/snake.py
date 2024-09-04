from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
DELAY = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "black"
FOOD_COLOUR = "red"
HEADER_COLOUR = "#ff809d"
BACKGROUND_COLOUR = "#FFD1DC"
XSTART = 0
YSTART = 0



class SnakeGame():

    class Snake():
        def __init__(self):
            self.bodySize = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for _ in range(0, BODY_PARTS):
                self.coordinates.append([XSTART, YSTART])

            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
                self.squares.append(square)


    class Food():
        def __init__(self):
            x = random.randint(0, (GAME_WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE

            self.coordinates = [x,y]
            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag="food")
            

    def gameStart(self):
        self.game_window = Toplevel()
        self.game_window.title("Snake :)")
        self.game_window["bg"] = HEADER_COLOUR
        self.game_window.resizable(False, False)

        self.score = 0
        self.direction = 'right'

        self.scoreFrame = Frame(self.game_window, bg=HEADER_COLOUR, width=GAME_WIDTH)
        self.scoreFrame.pack(fill='x', expand=True)

        self.label = Label(self.scoreFrame, text="Score: {}".format(self.score), font=("consolas", 20, "bold"), bg=HEADER_COLOUR)
        self.label.pack(side="left", pady=10, padx=10)
        
        back_button = Button(self.scoreFrame, text="Back to Menu", command=self.game_window.destroy)
        back_button.pack(side = "right", pady=10, padx=10)

        global canvas
        canvas = Canvas(self.game_window, height=GAME_HEIGHT, width=GAME_WIDTH, bg = BACKGROUND_COLOUR, highlightbackground="black", highlightthickness=4)
        canvas.pack()

        self.game_window.update()


        windowHeight = self.game_window.winfo_height()
        windowWidth = self.game_window.winfo_width()
        screenHeight = self.game_window.winfo_screenheight()
        screenWidth = self.game_window.winfo_screenwidth()

        x = int((screenWidth/2) - (windowWidth/2))
        y = int((screenHeight/2) - (windowHeight/2))

        self.game_window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

        self.game_window.bind('<Left>', lambda event: self.changeDirection('left'))
        self.game_window.bind('<Right>', lambda event: self.changeDirection('right'))
        self.game_window.bind('<Up>', lambda event: self.changeDirection('up'))
        self.game_window.bind('<Down>', lambda event: self.changeDirection('down'))
        self.game_window.bind('<a>', lambda event: self.changeDirection('left'))
        self.game_window.bind('<d>', lambda event: self.changeDirection('right'))
        self.game_window.bind('<w>', lambda event: self.changeDirection('up'))
        self.game_window.bind('<s>', lambda event: self.changeDirection('down'))

        self.snake = self.Snake()
        self.food = self.Food()

        self.nextTurn(self.snake, self.food)

        return self.game_window
    
    def nextTurn(self, snake, food):
        x,y = snake.coordinates[0]

        if self.direction == 'up':
            y -= SPACE_SIZE
        elif self.direction == 'down':
            y += SPACE_SIZE
        elif self.direction == 'left':
            x -= SPACE_SIZE
        elif self.direction == 'right':
            x += SPACE_SIZE


        snake.coordinates.insert(0, (x, y))
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
        snake.squares.insert(0,square)

        
        if x == food.coordinates[0] and y == food.coordinates[1]:
            self.score += 1
            self.label.config(text= "Score: {}".format(self.score))
            canvas.delete("food")

            food = self.Food()
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]


        if self.checkCollision(self.snake):
            self.gameOver()
        else:
            self.game_window.after(DELAY, self.nextTurn, snake, food)

    def changeDirection(self, newDirection):
        if newDirection == 'left' and self.direction != 'right':
            self.direction = newDirection
        elif newDirection == 'right' and self.direction != 'left':
            self.direction = newDirection
        elif newDirection == 'up' and self.direction != 'down':
            self.direction = newDirection
        elif newDirection == 'down' and self.direction != 'up':
            self.direction = newDirection

    def checkCollision(self, snake):
        x, y = snake.coordinates[0]
        if x < 0 or x >= GAME_WIDTH:
            return True
        elif y < 0 or y >= GAME_HEIGHT:
            return True
        
        for bodyPart in snake.coordinates[1:]:
            if x == bodyPart[0] and y == bodyPart[1]:
                return True
            
        return False

    def gameOver(self):
        pass


