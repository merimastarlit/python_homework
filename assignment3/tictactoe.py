# Task 6

# first class using the parent exception class
class TicTacToeException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)

# second class as per the homework instructions that creates the game board and later will use the exception class above
class Board:
    # initializing the board and sets the first turn to X
    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    valid_moves = ["upper left", "upper center", "upper right", "middle left",
                   "center", "middle right", "lower left", "lower center", "lower right"]
    # string representation of the board
    def __str__(self):
        lines = []
        lines.append(
            f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(
            f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(
            f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)
    # method to make a move
    def move(self, move_string):
        if not move_string in Board.valid_moves:
            raise TicTacToeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3  # row
        column = move_index % 3  # column
        if self.board_array[row][column] != " ":
            raise TicTacToeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    # method to check the game status
    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                else:
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's Game.")
        win = False
        for i in range(3):  # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3):  # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ":  # check diagonals
                if self.board_array[0][0] == self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] == self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if not win:
            if self.turn == "X":
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")

# running the game
instance1 = Board()
print(instance1)

# game loop with handling exceptions
while True:
    try:
        move_input = input(f"{instance1.turn}'s move: ")
        instance1.move(move_input)
        print(instance1)
        game_over, message = instance1.whats_next()
        print(message)
        if game_over:
            break
    except TicTacToeException as e:
        print(e.message)
