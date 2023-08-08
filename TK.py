import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = []
        for row in range(3):
            row_buttons = []
            for col in range(3):
                button = tk.Button(root, text="", font=("Helvetica", 24), width=8, height=3,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_win(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self, player):
        for row in self.board:
            if all([cell == player for cell in row]):
                return True

        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True

        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2 - i] == player for i in range(3)]):
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def reset_board(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()