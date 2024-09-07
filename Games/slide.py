from tkinter import *
import random

HEADER_COLOUR = "#ff809d"
BACKGROUND_COLOUR = "#FFD1DC"
TILESPERROW = 5
PIXELSPERTILEROW = 100
GAME_WIDTH = GAME_HEIGHT = TILESPERROW * PIXELSPERTILEROW
REMOVEDROW = 0
REMOVEDCOL = 4

class SlideGame():
    def __init__(self):
        self.game_window = None
        self.has_beaten = False
        self.tiles = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]
        self.correct_coords = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]
        self.blanktilecoords = []
        self.images = []


    def game_start(self):
        self.game_window = Toplevel()
        self.game_window.title("Sliding Tiles :)")
        self.game_window["bg"] = HEADER_COLOUR
        self.game_window.resizable(False, False)
        back_button = Button(self.game_window, text="Back to Menu", command=self.game_window.destroy)
        back_button.pack()

        global canvas
        canvas = Canvas(self.game_window, height=GAME_HEIGHT, width=GAME_WIDTH,
                        bg = BACKGROUND_COLOUR,
                        highlightbackground="black", highlightthickness=4)
        canvas.pack()

        self.inititalise_tiles()
        self.game_window.update()

        window_height = self.game_window.winfo_height()
        window_width = self.game_window.winfo_width()
        screen_height = self.game_window.winfo_screenheight()
        screen_width = self.game_window.winfo_screenwidth()
        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))

        self.game_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.play_game()
        
        return self.game_window
    
    
    def play_game(self):
        self.remove_tile(REMOVEDROW, REMOVEDCOL)
        self.shuffle_board()

    def inititalise_tiles(self):
        for y in range(0,5):
            row = []
            for x in range(0,5):
                num = 25-(y*5 + x)
                row.append(PhotoImage(file= f"Images/SlideGameImages/{num}.png"))
                self.tiles[y][x] = (canvas.create_image(x*PIXELSPERTILEROW,y*PIXELSPERTILEROW, image=row[x], anchor="nw"))
                canvas.tag_bind(self.tiles[y][x], '<Button-1>', lambda event, id=self.tiles[y][x]: self.on_image_click(id))
                self.correct_coords[y][x] = (x*PIXELSPERTILEROW,y*PIXELSPERTILEROW)
                canvas.create_rectangle(x*PIXELSPERTILEROW,y*PIXELSPERTILEROW,x*PIXELSPERTILEROW+PIXELSPERTILEROW,y*PIXELSPERTILEROW+PIXELSPERTILEROW)
                canvas.image = row[x]
            self.images.append(row)

    def remove_tile(self, row, col):
        self.blanktilecoords = canvas.coords(self.tiles[row][col])
        canvas.delete(self.tiles[row][col])

    def swap_tiles(self, row, col, image_id):
        if abs(self.blanktilecoords[0]/PIXELSPERTILEROW - col) + abs(self.blanktilecoords[1]/PIXELSPERTILEROW - row) == 1:
            coords = canvas.coords(image_id)
            canvas.coords(image_id, self.blanktilecoords[0], self.blanktilecoords[1])
            self.blanktilecoords = coords
        else:
            print("invalid")
            print(self.blanktilecoords[0]/PIXELSPERTILEROW, " ", row)
            print(self.blanktilecoords[1]/PIXELSPERTILEROW, " ", col)

    def on_image_click(self, image_id):
        coords = canvas.coords(image_id)
        self.swap_tiles(coords[1]/PIXELSPERTILEROW, coords[0]/PIXELSPERTILEROW, image_id)
        self.check_for_win()


    def check_for_win(self):
        for row in range (0,5):
            for col in range(0,5):
                if row == REMOVEDROW and col == REMOVEDCOL:
                    continue
                corr_coords = self.correct_coords[row][col]
                act_coords = canvas.coords(self.tiles[row][col])
                if (corr_coords[0] != act_coords[0]) or (corr_coords[1] != act_coords[1]):
                    return False
        
        self.game_won()
        
    def game_won(self):
        self.has_beaten = True
        for row in range (0,5):
            for col in range(0,5):
                if row == REMOVEDROW and col == REMOVEDCOL:
                    continue
                self.remove_tile(row, col)

        img = PhotoImage(file= "Images/SlideGameImages/FullPicture.png")
        canvas.create_image(0,0, image=img, anchor="nw")
        canvas.image = img

    def shuffle_board(self):
        y = self.blanktilecoords[1]/PIXELSPERTILEROW
        x = self.blanktilecoords[0]/PIXELSPERTILEROW
        choices = []
        print(x, "-", y)

        if y > 0:
            choices.append((x, y-1))
        if y < 4:
            choices.append((x, y+1))
        if x > 0:
            choices.append((x-1, y))
        if x < 4:
            choices.append((x+1, y))

        swapper = random.choice(choices)
        col = int(swapper[0])
        row = int(swapper[1])
        print(col, ", ", row)
        img_id = self.tiles[row][col]
        print(self.blanktilecoords)
        print(canvas.coords(img_id))
        self.swap_tiles(row,col, img_id)