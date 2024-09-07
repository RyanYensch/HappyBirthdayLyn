from tkinter import *
import random
import sys

sys.setrecursionlimit(2000)


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
            self.flagged = False

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
        self.flag_frame.grid(
            row=0, column=0, columnspan=GRIDSIZE, sticky="nsew")

        self.label = Label(self.flag_frame, text=f"Flags Left: {self.flags}", font=(
            "consolas", 20, "bold"), bg=HEADER_COLOUR)
        self.label.grid(row=0, column=0, sticky="w", columnspan=GRIDSIZE-1)

        back_button = Button(
            self.flag_frame, text="Back to Menu", command=self.game_window.destroy)
        back_button.grid(row=0, column=GRIDSIZE-1,
                         sticky="e", padx=(20*20*TILESIZE, 0))

        self.initialise_buttons()
        self.initialise_bombdata()
        self.calculate_surroundings()

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
                                width=1, height=1, fg="black",
                                bg=colour, activebackground=colour, bd=0,
                                highlightthickness=0, command=lambda r=r, c=c: self.tile_clicked(r, c))
                button.bind("<Button-3>", lambda event, r=r,
                            c=c: self.tile_right_clicked(r, c))
                bombrow.append(self.Tile())
                row.append(button)
                button.grid(row=r+1, column=c, sticky="nsew")

            self.buttons.append(row)
            self.tiles.append(bombrow)

    def initialise_bombdata(self):
        bombset = set()
        while len(bombset) < MINES:
            bombset.add((random.randint(0, GRIDSIZE-1),
                        random.randint(0, GRIDSIZE-1)))

        for row, col in bombset:
            self.tiles[row][col].is_bomb = True

    def reveal_bombs(self):
        for r in range(0, GRIDSIZE):
            for c in range(0, GRIDSIZE):
                if self.tiles[r][c].is_bomb:
                    self.buttons[r][c].config(bg="red", activebackground="red")

    def is_bomb(self, row, col):
        if self.tiles[row][col].is_bomb:
            return 1
        return 0

    def calculate_surroundings(self):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for r in range(0, GRIDSIZE):
            for c in range(0, GRIDSIZE):
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if 0 <= new_r < GRIDSIZE and 0 <= new_c < GRIDSIZE:
                        self.tiles[r][c].surrounding += self.is_bomb(
                            new_r, new_c)

    def reveal_surroundings(self, r, c):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc

            if 0 <= new_r < GRIDSIZE and 0 <= new_c < GRIDSIZE and self.tiles[new_r][new_c].revealed == False:
                self.tile_clicked(new_r, new_c)

    def disable_all_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def game_over(self):
        self.reveal_bombs()
        self.disable_all_buttons()

    def tiles_left(self):
        count = 0
        for r in range(0, GRIDSIZE):
            for c in range(0, GRIDSIZE):
                if self.tiles[r][c].revealed == False and self.is_bomb(r, c) == False:
                    count += 1
        return count

    def check_win(self):
        if self.tiles_left() == 0:
            if self.has_beaten == False:
                win_popup = Toplevel(self.game_window)
                win_popup.title("Congratulations!")
                win_popup.geometry("300x100")
                win_popup.configure(bg=HEADER_COLOUR)
                label = Label(win_popup, text="YAYY NICE BABY!", font=(
                    "Arial", 20, "bold"), bg=HEADER_COLOUR, fg="black")
                label.pack(expand=True, fill=BOTH)

                button = Button(win_popup, text="YIPPEEE",
                                command=win_popup.destroy)
                button.pack(pady=10)

                win_popup.update_idletasks()
                popup_width = win_popup.winfo_width()
                popup_height = win_popup.winfo_height()
                screen_width = win_popup.winfo_screenwidth()
                screen_height = win_popup.winfo_screenheight()
                x = int((screen_width / 2) - (popup_width / 2))
                y = int((screen_height / 2) - (popup_height / 2))
                win_popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

            self.has_beaten = True

    def tile_clicked(self, row, col):
        can_click = self.tiles[row][col].revealed == False and self.tiles[row][col].flagged == False
        if self.tiles[row][col].is_bomb and can_click:
            self.game_over()
        elif can_click:
            colour = "#d2b99a" if (row+col) % 2 == 0 else "#dfc4a0"
            number = self.tiles[row][col].surrounding if self.tiles[row][col].surrounding != 0 else ""
            self.buttons[row][col].config(
                bg=colour, activebackground=colour, text=number, fg="black", activeforeground="black")
            self.tiles[row][col].revealed = True
            if number == "":
                self.reveal_surroundings(row, col)

        self.check_win()

    def tile_right_clicked(self, row, col):
        if self.tiles[row][col].flagged == False and self.tiles[row][col].revealed == False and self.flags > 0:
            self.tiles[row][col].flagged = True
            self.flags -= 1
            self.buttons[row][col].config(
                text="❤", fg="red", activeforeground="red")
            self.label.config(text=f"Flags Left: {self.flags}")
        elif self.tiles[row][col].flagged == True and self.tiles[row][col].revealed == False:
            self.tiles[row][col].flagged = False
            self.flags += 1
            self.buttons[row][col].config(text="")
            self.label.config(text=f"Flags Left: {self.flags}")
