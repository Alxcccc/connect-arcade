import arcade

from src.logic.interfaces.board import Board
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT


class SwitchTurnView(arcade.View):
    def __init__(self, board: Board, previous_view: arcade.View):
        super().__init__()
        self.previous_view: arcade.View = previous_view
        self.board: Board = board

    def on_show_view(self) -> None:
        self.window.background_color = arcade.color.BLACK

    def on_draw(self) -> None:
        self.clear()
        self.board.draw_board()
        player_name: str = "red" if self.board.turn == "R" else "blue"
        arcade.draw_text(
            f"Turn of {player_name} - click to advance",
            SCREEN_HEIGHT / 2,
            SCREEN_WIDTH / 2,
            arcade.color.DARK_GRAY,
            font_size=20,
            anchor_x="center",
            font_name="Kenney Blocks"
        )

    def on_mouse_press(self, _x: int, _y: int, _button: int, _modifiers: int) -> None:
        self.window.show_view(self.previous_view)
