from typing import Optional, List, Tuple

from src.logic.interfaces.board import BoardModel


class WinChecker:
    def __init__(self, board: BoardModel):
        self._grid: List[List[str]] = board.get_board()
        self._row_count: int = board.row_count
        self._col_count: int = board.col_count

    def is_board_full(self) -> bool:
        count = 0
        for column in range(self._col_count):
            if self._grid[self._row_count - 1][column] != " ":
                count += 1
        return count == self._col_count

    def check_win(self, row: int, col: int) -> Optional[str]:
        player_color: str = self._grid[row][col]
        if player_color == " ":
            return None

        directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for dr, dc in directions:
            consecutive_count: int = 1

            r, c = row + dr, col + dc
            while (0 <= r < self._row_count and 0 <= c < self._col_count
                   and self._grid[r][c] == player_color):
                consecutive_count += 1
                r += dr
                c += dc

            r, c = row - dr, col - dc
            while (0 <= r < self._row_count and 0 <= c < self._col_count
                   and self._grid[r][c] == player_color):
                consecutive_count += 1
                r -= dr
                c -= dc

            if consecutive_count >= 4:
                return player_color

        return None
