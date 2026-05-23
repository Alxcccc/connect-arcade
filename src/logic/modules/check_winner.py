from src.logic.interfaces.board import Board
from src.logic.interfaces.punctuation import Punctuation


class CheckWinner():
    def __init__(self, board: Board, punctuation: Punctuation, turn: str):
        self.board = board.get_board()
        self.board_rows = board._ROW_COUNT
        self.board_cols = board._COLUMN_COUNT
        self.punctuation = punctuation
        self.turn = turn
        
    def check_enough(self):
        count = 0
        for column in range(len(self.board[0])):
            if self.board[self.board_rows-1][column] != " ":
                count +=1
        if count == 6:
            return True
        return False
        
    def check_win(self):
        if self.check_vertical() == "R" or self.check_horizontal() == "R" or self.check_diagonal_right() == "R" or self.check_diagonal_left() == "R":
            self.punctuation.increment_points(user="R")
            return "R"
        elif self.check_vertical() == "B" or self.check_horizontal() == "B" or self.check_diagonal_right() == "B" or self.check_diagonal_left() == "B":
            self.punctuation.increment_points(user="B")
            return "B"
        else:
            return None
        
    def check_vertical(self):
        for row in range(self.board_rows-1):
            for column in range(self.board_cols-1):
                if row+3 <= self.board_rows-1:
                    if self.board[row][column].strip():
                        if self.board[row][column] == "R" and self.board[row+1][column] == "R" and self.board[row+2][column] == "R" and self.board[row+3][column] == "R":
                            return "R"
                        elif self.board[row][column] == "B" and self.board[row+1][column] == "B" and self.board[row+2][column] == "B" and self.board[row+3][column] == "B":
                            return "B"

    def check_horizontal(self):
        for row in range(self.board_rows-1):
            for column in range(self.board_cols-1):
                if column+3 <= self.board_cols-1:
                    if self.board[row][column].strip():
                        if self.board[row][column] == "R" and self.board[row][column    +1] == "R" and self.board[row][column+2] == "R" and self.board[row][column+3] == "R":
                            return "R"
                        elif self.board[row][column] == "B" and self.board[row][column+1] == "B" and self.board[row][column+2] == "B" and self.board[row][column+3] == "B":
                            return "B"
        
    def check_diagonal_right(self):
        for row in range(self.board_rows-1):
            for column in range(self.board_cols-1):
                if row+3 <= self.board_rows-1 and column+3 <= self.board_cols-1:
                    if self.board[row][column].strip():
                        if self.board[row][column] == "R" and self.board[row+1][column+1] == "R" and self.board[row+2][column+2] == "R" and self.board[row+3][column+3] == "R":
                            return "R"
                        elif self.board[row][column] == "B" and self.board[row+1][column+1] == "B" and self.board[row+2][column+2] == "B" and self.board[row+3][column+3] == "B":
                            return "B"


    def check_diagonal_left(self):
        for row in range(self.board_rows-1):
            for column in range(self.board_cols-1, -1, -1):
                if row+4 <= self.board_rows-1 and column-3 >= 0:
                    if self.board[row][column].strip():
                        if self.board[row][column] == "R" and self.board[row+1][column-1] == "R" and self.board[row+2][column-2] == "R" and self.board[row+3][column-3] == "R":
                            return "R"
                        elif self.board[row][column] == "B" and self.board[row+1][column-1] == "B" and self.board[row+2][column-2] == "B" and self.board[row+3][column-3] == "B":
                            return "B"
            