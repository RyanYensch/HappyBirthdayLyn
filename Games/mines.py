from tkinter import *
import random

HEADER_COLOUR = "#ff809d"
BACKGROUND_COLOUR = "#FFD1DC"
TILESIZE = 1
GRIDSIZE = 24
GAME_WIDTH = GRIDSIZE*TILESIZE
MINES = 99

class MineGame():
    class Tile():
        def __init__(self) -> None:
            self.is_bomb = False
            self.surrounding = 0
            self.revealed = False


    def __init__(self) -> None:
        self.has_beaten = False
        self.buttons = []
        self.tiles = []
        self.flags = MINES
        self.flag_frame = NONE
        self.label = NONE
        self.game_window = None

    def game_start(self):
        self.game_window = Toplevel()
        self.game_window.title("Minesweeper :)")
        self.game_window["bg"] = HEADER_COLOUR
        self.game_window.resizable(False, False)

        self.flag_frame = Frame(self.game_window, bg=HEADER_COLOUR)
        self.flag_frame.grid(row=0, column=0, columnspan=GRIDSIZE, sticky="nsew")

        self.label = Label(self.flag_frame, text=f"Flags Left: {self.flags}", font=("consolas", 20, "bold"), bg=HEADER_COLOUR)
        self.label.grid(row=0, column=0, sticky="w", columnspan=GRIDSIZE-1)

        back_button = Button(self.flag_frame, text="Back to Menu", command=self.game_window.destroy)
        back_button.grid(row=0, column=GRIDSIZE-1, sticky="e", padx=(20*20*TILESIZE, 0))

        self.initialise_buttons()
        self.initialise_bombdata()

        self.game_window.update()

        window_height = self.game_window.winfo_height()
        window_width = self.game_window.winfo_width()
        screen_height = self.game_window.winfo_screenheight()
        screen_width = self.game_window.winfo_screenwidth()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        self.game_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.play_game()

        return self.game_window
    
    def play_game(self):
        pass

    def initialise_buttons(self):
        for r in range(0, GRIDSIZE):
            row = []
            bombrow = []
            for c in range(0, GRIDSIZE):
                colour = "#abd052" if (r+c) % 2 == 0 else "#b3d659"
                button = Button(self.game_window, text="", font=('Arial', 10, 'bold'),
                                width=1, height=1, fg= "black",
                                bg=colour, activebackground= colour,bd=0,
                                highlightthickness=0, command=lambda r=r, c=c: self.tile_clicked(r, c))
                button.bind("<Button-3>", lambda event, r=r, c=c: self.tile_right_clicked(r, c))
                bombrow.append(self.Tile())
                row.append(button)
                button.grid(row=r+1, column=c, sticky="nsew")

            self.buttons.append(row)
            self.tiles.append(bombrow)

    def initialise_bombdata(self):
        bombset = set()
        while len(bombset) < 99:
            bombset.add((random.randint(0,GRIDSIZE-1), random.randint(0,GRIDSIZE-1)))

        for row, col in bombset:
            self.tiles[row][col].is_bomb = True

    def reveal_bombs(self):
        for r in range(0, GRIDSIZE):
            for c in range(0, GRIDSIZE):
                if self.tiles[r][c].is_bomb:
                    self.buttons[r][c].config(bg="red", activebackground= "red")

    def disable_all_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def game_over(self):
        self.reveal_bombs()
        self.disable_all_buttons()

                
    def tile_clicked(self, row, col):
        print(f"clicked row {row} and column {col}")
        if self.tiles[row][col].is_bomb :
            self.game_over()
        else:
            colour = "#d2b99a" if (row+col) % 2 == 0 else "#dfc4a0"
            number = self.tiles[row][col].surrounding if self.tiles[row][col].surrounding != 0 else ""
            self.buttons[row][col].config(bg=colour, activebackground= colour, text=number)
            self.tiles[row][col].revealed = True

    def tile_right_clicked(self, row, col):
        print(f"Right clicked row {row} and column {col}")