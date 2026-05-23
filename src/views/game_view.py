from typing import Optional, Tuple

import arcade

from src.logic.interfaces.board import Board
from src.logic.interfaces.scoring import ScoreTracker
from src.logic.modules.win_checker import WinChecker
from src.views.switch_turn_view import SwitchTurnView
from src.views.game_over_view import GameOverView


class GameView(arcade.View):
    def __init__(self, board: Board, score_tracker: ScoreTracker):
        super().__init__()
        self.score_tracker: ScoreTracker = score_tracker
        self.board: Board = board
        self.manager: arcade.gui.UIManager = arcade.gui.UIManager()
        self.winner: Optional[str] = None
        self.background_color: tuple = arcade.color.BLACK

    def on_draw(self) -> None:
        self.clear()
        self.board.draw_board()
        self.manager.draw()

    def on_key_press(self, key: int, modifiers: int) -> None:
        if key == arcade.key.ESCAPE:
            from src.views.main_view import MainView
            menu_view = MainView(self.score_tracker, self.board)
            self.window.show_view(menu_view)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if self.winner is None:
            win_checker: WinChecker = WinChecker(self.board, self.score_tracker)

            if win_checker.is_board_full():
                self.board.turn = "R"
                self.board.clear_board()

            placement: Optional[Tuple[int, int]] = self.board.put_token(x, y)

            if placement is not None:
                row, col = placement
                self.winner = win_checker.check_win(row, col)

                if self.winner is None:
                    switch_turn_view = SwitchTurnView(self.board, self)
                    self.window.show_view(switch_turn_view)
                else:
                    self.board.turn = "R"
        else:
            self.board.clear_board()
            game_over_view: GameOverView = GameOverView(
                self.board, self.score_tracker, self.winner
            )
            self.winner = None
            self.window.show_view(game_over_view)
