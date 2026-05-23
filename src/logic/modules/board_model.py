from typing import Optional, Tuple, List

from src.logic.interfaces.board import BoardModel
from src.logic.enums import Token


GRID_ROWS = 6
GRID_COLS = 7


class Connect4BoardModel(BoardModel):
    def __init__(self):
        self._row_count: int = GRID_ROWS
        self._col_count: int = GRID_COLS
        self._grid: List[List[str]] = self.create_board()
        self._turn: Token = Token.RED

    @property
    def row_count(self) -> int:
        return self._row_count

    @property
    def col_count(self) -> int:
        return self._col_count

    @property
    def turn(self) -> Token:
        return self._turn

    @turn.setter
    def turn(self, value: Token) -> None:
        self._turn = value

    def create_board(self) -> List[List[str]]:
        return [[Token.EMPTY for _ in range(self._col_count)] for _ in range(self._row_count)]

    def get_board(self) -> List[List[str]]:
        return self._grid

    def clear_board(self) -> None:
        for i in range(self._row_count):
            for j in range(self._col_count):
                if self._grid[i][j] != Token.EMPTY:
                    self._grid[i][j] = Token.EMPTY

    def put_token(self, col: int) -> Optional[Tuple[int, int]]:
        if 0 <= col < self._col_count:
            for current_row in range(self._row_count):
                if self._grid[current_row][col] == Token.EMPTY:
                    self._grid[current_row][col] = self._turn
                    self._turn = Token.YELLOW if self._turn == Token.RED else Token.RED
                    return current_row, col
        return None
