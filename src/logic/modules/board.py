from typing import Optional, Tuple, List

import arcade

from src.logic.interfaces.board import Board
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT


class Connect4Board(Board):
    def __init__(self, row_count: int = 6, column_count: int = 7,
                 cell_width: int = 30, cell_height: int = 30, margin: int = 5):
        self._ROW_COUNT: int = row_count
        self._COLUMN_COUNT: int = column_count
        self._WIDTH: int = cell_width
        self._HEIGHT: int = cell_height
        self._MARGIN: int = margin
        self._WINDOW_WIDTH: int = (self._WIDTH + self._MARGIN) * self._COLUMN_COUNT + self._MARGIN
        self._WINDOW_HEIGHT: int = (self._HEIGHT + self._MARGIN) * self._ROW_COUNT + self._MARGIN
        self._grid: List[List[str]] = self.create_board()
        self.turn: str = "R"

    def create_board(self) -> List[List[str]]:
        return [[" " for _ in range(self._COLUMN_COUNT)] for _ in range(self._ROW_COUNT)]

    def get_board(self) -> List[List[str]]:
        return self._grid

    def draw_board(self) -> None:
        for row in range(self._ROW_COUNT):
            for column in range(self._COLUMN_COUNT):
                if self._grid[row][column] == "R":
                    color = arcade.color.RED
                elif self._grid[row][column] == "B":
                    color = arcade.color.BLUE
                else:
                    color = arcade.color.DARK_GRAY

                x = (self._MARGIN + self._WIDTH) * column + self._MARGIN + self._WIDTH // 2
                y = (self._MARGIN + self._HEIGHT) * row + self._MARGIN + self._HEIGHT // 2

                arcade.draw_circle_filled(center_x=x, center_y=y, radius=17, color=color)

    def clear_board(self) -> None:
        for i in range(self._ROW_COUNT):
            for j in range(self._COLUMN_COUNT):
                if self._grid[i][j] != " ":
                    self._grid[i][j] = " "

    def put_token(self, x: int, y: int) -> Optional[Tuple[int, int]]:
        column = int(x // (self._WIDTH + self._MARGIN))
        row = int(y // (self._HEIGHT + self._MARGIN))
        if row < self._ROW_COUNT and column < self._COLUMN_COUNT:
            for current_row in range(self._ROW_COUNT):
                if self._grid[current_row][column] == " ":
                    self._grid[current_row][column] = self.turn
                    self.turn = "B" if self.turn == "R" else "R"
                    return current_row, column
        return None
