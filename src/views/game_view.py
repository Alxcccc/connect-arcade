from typing import Optional, Tuple

import arcade

from src.logic.interfaces.board import Board
from src.logic.interfaces.scoring import ScoreTracker
from src.logic.modules.win_checker import WinChecker
from src.views.switch_turn_view import SwitchTurnComponent
from src.components.game_over_component import GameOverComponent


class GameView(arcade.View):
    def __init__(self, board: Board, score_tracker: ScoreTracker):
        super().__init__()
        self.score_tracker: ScoreTracker = score_tracker
        self.board: Board = board
        self.manager: arcade.gui.UIManager = arcade.gui.UIManager()
        self.winner: Optional[str] = None
        self.background_color: tuple = (0, 81, 186)

    def on_draw(self) -> None:
        self.clear()
        self.board.draw_board()
        self.manager.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if self.manager.on_mouse_press(x, y, button, modifiers):
            return

        if self.winner is not None:
            return

        win_checker: WinChecker = WinChecker(self.board, self.score_tracker)

        if win_checker.is_board_full():
            self.board.turn = "R"
            self.board.clear_board()

        placement: Optional[Tuple[int, int]] = self.board.put_token(x, y)

        if placement is not None:
            row, col = placement
            self.winner = win_checker.check_win(row, col)

            if self.winner is None:
                self.manager.add(SwitchTurnComponent(self.board, self), layer=1)
            else:
                self.board.turn = "R"
                self.manager.add(
                    GameOverComponent(self.board, self.score_tracker, self.winner, self.window)
                )
