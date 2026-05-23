from typing import Optional, Tuple

import arcade

from src.logic.interfaces.board import BoardModel
from src.logic.modules.board_renderer import BoardRenderer
from src.logic.modules.win_checker import WinChecker
from src.logic.enums import Token
from src.components.switch_turn_component import SwitchTurnComponent
from src.components.game_over_component import GameOverComponent


class GameView(arcade.View):
    def __init__(self, board: BoardModel):
        super().__init__()
        self.board: BoardModel = board
        self.renderer: BoardRenderer = BoardRenderer(board)
        self.manager: arcade.gui.UIManager = arcade.gui.UIManager()
        self.winner: Optional[str] = None
        self.background_color: tuple = (0, 81, 186)

    def on_draw(self) -> None:
        self.clear()
        self.renderer.draw_board()
        self.manager.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if self.manager.on_mouse_press(x, y, button, modifiers):
            return

        if self.winner is not None:
            return

        win_checker: WinChecker = WinChecker(self.board)

        if win_checker.is_board_full():
            self.board.turn = Token.RED
            self.board.clear_board()

        col: int = BoardRenderer.pixel_to_column(x)
        placement: Optional[Tuple[int, int]] = self.board.put_token(col)

        if placement is not None:
            row, col = placement
            self.winner = win_checker.check_win(row, col)

            if self.winner is None:
                self.manager.add(SwitchTurnComponent(self.board, self), layer=1)
            else:
                self.board.turn = Token.RED
                self.manager.add(
                    GameOverComponent(self.board, self.winner, self.window)
                )
