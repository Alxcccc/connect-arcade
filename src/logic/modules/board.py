from typing import Optional, Tuple, List

import arcade

from src.logic.interfaces.board import Board
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT


CELL_SIZE = 72
CELL_SPACING = 10
FRAME_PADDING = 18
TOP_BAR_HEIGHT = 15

GRID_COLS = 7
GRID_ROWS = 6
GRID_WIDTH = GRID_COLS * CELL_SIZE + (GRID_COLS - 1) * CELL_SPACING
GRID_HEIGHT = GRID_ROWS * CELL_SIZE + (GRID_ROWS - 1) * CELL_SPACING
INNER_WIDTH = GRID_WIDTH
INNER_HEIGHT = GRID_HEIGHT
FRAME_WIDTH = INNER_WIDTH + 2 * FRAME_PADDING
FRAME_HEIGHT = INNER_HEIGHT + 2 * FRAME_PADDING + TOP_BAR_HEIGHT

FRAME_X = (SCREEN_WIDTH - FRAME_WIDTH) // 2
FRAME_Y = (SCREEN_HEIGHT - FRAME_HEIGHT) // 2

INNER_X = FRAME_X + FRAME_PADDING
INNER_Y = FRAME_Y + FRAME_PADDING + TOP_BAR_HEIGHT

FRAME_COLOR = (0, 50, 110)
INNER_COLOR = (240, 243, 248)
EMPTY_SLOT_COLOR = (160, 195, 230)
TOKEN_RADIUS = CELL_SIZE // 2 - 5


class Connect4Board(Board):
    def __init__(self):
        self._ROW_COUNT: int = GRID_ROWS
        self._COLUMN_COUNT: int = GRID_COLS
        self._grid: List[List[str]] = self.create_board()
        self.turn: str = "R"

    def create_board(self) -> List[List[str]]:
        return [[" " for _ in range(self._COLUMN_COUNT)] for _ in range(self._ROW_COUNT)]

    def get_board(self) -> List[List[str]]:
        return self._grid

    def draw_board(self) -> None:
        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                FRAME_X + FRAME_WIDTH / 2,
                FRAME_Y + FRAME_HEIGHT / 2,
                FRAME_WIDTH,
                FRAME_HEIGHT,
            ),
            FRAME_COLOR,
        )

        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                INNER_X + INNER_WIDTH / 2,
                INNER_Y + INNER_HEIGHT / 2,
                INNER_WIDTH,
                INNER_HEIGHT,
            ),
            INNER_COLOR,
        )

        for row in range(self._ROW_COUNT):
            for column in range(self._COLUMN_COUNT):
                cx = (
                    INNER_X
                    + column * (CELL_SIZE + CELL_SPACING)
                    + CELL_SIZE / 2
                )
                cy = (
                    INNER_Y
                    + row * (CELL_SIZE + CELL_SPACING)
                    + CELL_SIZE / 2
                )

                if self._grid[row][column] == "R":
                    color = (218, 41, 28)
                elif self._grid[row][column] == "B":
                    color = (255, 215, 0)
                else:
                    color = EMPTY_SLOT_COLOR

                arcade.draw_circle_filled(cx, cy, TOKEN_RADIUS, color)

    def clear_board(self) -> None:
        for i in range(self._ROW_COUNT):
            for j in range(self._COLUMN_COUNT):
                if self._grid[i][j] != " ":
                    self._grid[i][j] = " "

    def put_token(self, x: int, y: int) -> Optional[Tuple[int, int]]:
        col = int((x - INNER_X) // (CELL_SIZE + CELL_SPACING))

        if 0 <= col < self._COLUMN_COUNT:
            for current_row in range(self._ROW_COUNT):
                if self._grid[current_row][col] == " ":
                    self._grid[current_row][col] = self.turn
                    self.turn = "B" if self.turn == "R" else "R"
                    return current_row, col
        return None
