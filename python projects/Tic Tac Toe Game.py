import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [" "]*9
        self.create_board()

    def create_board(self):
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text=" ", font=("Arial", 30), height=3, width=6, command=lambda j=i: self.make_move(j))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_win():
                self.game_over(self.current_player + " wins!")
            elif self.check_draw():
                self.game_over("Draw!")
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True

        return False

    def check_draw(self):
        return " " not in self.board

    def game_over(self, message):
        for button in self.buttons:
            button.config(state="disabled")
        game_over_label = tk.Label(self.master, text=message, font=("Arial", 20))
        game_over_label.grid(row=3, column=0, columnspan=3)

if __name__ == '__main__':
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()