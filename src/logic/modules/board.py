import arcade
from src.logic.interfaces.board import Board

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Connect4Board(Board):
    
    def __init__(self, ROW_COUNT = 6, COLUMN_COUNT = 7, WIDTH = 30, HEIGHT = 30, MARGIN = 5):
        self._ROW_COUNT = ROW_COUNT
        self._COLUMN_COUNT = COLUMN_COUNT
        self._WIDTH = WIDTH
        self._HEIGHT = HEIGHT
        self._MARGIN = MARGIN
        self._WINDOW_WIDTH = (self._WIDTH + self._MARGIN) * self._COLUMN_COUNT + self._MARGIN
        self._WINDOW_HEIGHT = (self._HEIGHT + self._MARGIN) * self._ROW_COUNT + self._MARGIN
        self._matrix = self.create_board()
        self.turn = "R"
        
    def create_board(self):
        return [[" " for _ in range(self._COLUMN_COUNT)] for _ in range(self._ROW_COUNT)]
    
    def get_board(self):
        return self._matrix
        
    def show_matrix(self):
        for row in range(self._ROW_COUNT):
            for column in range(self._COLUMN_COUNT):
                
                if self._matrix[row][column] == "R":
                    color = arcade.color.RED
                elif self._matrix[row][column] == "B":
                    color = arcade.color.BLUE
                else:
                    color = arcade.color.DARK_GRAY
                    
                x = (self._MARGIN + self._WIDTH) * column + self._MARGIN + self._WIDTH // 2
                y = (self._MARGIN + self._HEIGHT) * row + self._MARGIN + self._HEIGHT // 2

                arcade.draw_circle_filled(center_x=x, center_y=y, radius=17, color=color)
    
    def reset_matrix(self):
        for i in range(self._ROW_COUNT):
            for j in range(self._COLUMN_COUNT):
                if self._matrix[i][j] != " ":
                    self._matrix[i][j] = " "
                else:
                    continue
                
    def put_token(self, x, y):  
        column = int(x // (self._WIDTH + self._MARGIN))
        row = int(y // (self._HEIGHT + self._MARGIN))
        if row < self._ROW_COUNT and column < self._COLUMN_COUNT:
            for row_grid in range(0, 6):
                if self._matrix[row_grid][column] == " ":
                    self._matrix[row_grid][column] = self.turn
                    self.turn = "B" if self.turn == "R" else "R"
                    return True