import tkinter as tk

score = 0

class Snake():
    def gameStart(self):
        game_window = tk.Toplevel()
        game_window.title("Snake :)")
        label = tk.Label(game_window, text="Score: {}".format(score))
        label.pack(pady=10, side="top")
        
        back_button = tk.Button(game_window, text="Back to Menu", command=game_window.destroy)
        back_button.pack(pady=10)

        return game_window

