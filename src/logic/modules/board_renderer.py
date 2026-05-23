import arcade

from src.logic.interfaces.board import BoardModel
from src.logic.enums import Token
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

RED_COLOR = (218, 41, 28)
YELLOW_COLOR = (255, 215, 0)


class BoardRenderer:
    def __init__(self, board: BoardModel):
        self._board = board

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

        grid = self._board.get_board()
        for row in range(self._board.row_count):
            for column in range(self._board.col_count):
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

                if grid[row][column] == Token.RED:
                    color = RED_COLOR
                elif grid[row][column] == Token.YELLOW:
                    color = YELLOW_COLOR
                else:
                    color = EMPTY_SLOT_COLOR

                arcade.draw_circle_filled(cx, cy, TOKEN_RADIUS, color)

    @staticmethod
    def pixel_to_column(x: int) -> int:
        return int((x - INNER_X) // (CELL_SIZE + CELL_SPACING))
