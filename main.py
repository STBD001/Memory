import tkinter as tk
import random
from tkinter import messagebox

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        self.buttons = []
        self.first_choice = None
        self.second_choice = None
        self.cards = list("AABBCCDDEEFFGGHH")
        random.shuffle(self.cards)
        self.create_board()

    def create_board(self):
        for i in range(4):
            row = []
            for j in range(4):
                button = tk.Button(self.root, text=" ", width=8, height=4,
                                   command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def on_click(self, i, j):
        # If a button is already disabled, ignore the click
        if self.buttons[i][j].cget("state") == "disabled":
            return

        if self.first_choice and self.second_choice:
            return

        button = self.buttons[i][j]
        card = self.cards[i * 4 + j]
        button.config(text=card)

        if not self.first_choice:
            self.first_choice = (i, j)
        else:
            self.second_choice = (i, j)
            self.root.after(1000, self.check_match)

    def check_match(self):
        i1, j1 = self.first_choice
        i2, j2 = self.second_choice

        if self.cards[i1 * 4 + j1] == self.cards[i2 * 4 + j2]:
            self.buttons[i1][j1].config(state="disabled")
            self.buttons[i2][j2].config(state="disabled")
        else:
            self.buttons[i1][j1].config(text=" ")
            self.buttons[i2][j2].config(text=" ")

        self.first_choice = None
        self.second_choice = None

        # Check if all buttons are disabled (i.e., all matches have been found)
        if all(button.cget("state") == "disabled" for row in self.buttons for button in row):
            messagebox.showinfo("Memory Game", "You win!")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
