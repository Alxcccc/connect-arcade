from typing import Optional

import arcade
import arcade.gui
from arcade.types import Color

from src.logic.interfaces.scoring import ScoreTracker
from src.logic.interfaces.board import Board


PANEL_WIDTH = 460
PANEL_HEIGHT = 200


class GameOverComponent(arcade.gui.UIAnchorLayout):
    def __init__(self, board: Board, score_tracker: ScoreTracker, winner: str,
                 window: arcade.Window):
        super().__init__()
        self.board = board
        self.score_tracker = score_tracker
        self.winner = winner
        self.window = window

        frame = self.add(arcade.gui.UIAnchorLayout(
            width=PANEL_WIDTH, height=PANEL_HEIGHT, size_hint=None
        ))
        frame.with_padding(all=20)
        frame.with_background(color=Color(0, 30, 70))

        winner_name = "Red" if self.winner == "R" else "Yellow"
        winner_color = (218, 41, 28) if self.winner == "R" else (255, 215, 0)

        label = arcade.gui.UITextArea(
            text=f"{winner_name} is the winner!",
            font_name="Kenney Blocks",
            font_size=18,
            width=PANEL_WIDTH - 60,
            height=50,
            text_color=winner_color,
        )

        hint = arcade.gui.UITextArea(
            text="Click to continue",
            font_name="Kenney Blocks",
            font_size=14,
            width=PANEL_WIDTH - 60,
            height=30,
            text_color=(180, 200, 230),
        )

        layout = arcade.gui.UIBoxLayout(align="center", space_between=10)
        layout.add(label)
        layout.add(hint)

        frame.add(child=layout, anchor_x="center_x", anchor_y="center_y")

    def on_event(self, event: arcade.gui.UIEvent) -> Optional[bool]:
        if isinstance(event, arcade.gui.UIMousePressEvent):
            self._go_to_menu()
            return True
        return super().on_event(event)

    def _go_to_menu(self) -> None:
        from src.views.main_view import MainView
        self.board.clear_board()
        menu_view = MainView(self.score_tracker, self.board)
        self.window.show_view(menu_view)
