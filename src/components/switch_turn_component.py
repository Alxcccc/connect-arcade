from typing import Optional

import arcade
import arcade.gui
from arcade.types import Color

from src.logic.interfaces.board import BoardModel


PANEL_WIDTH = 340
PANEL_HEIGHT = 140


class SwitchTurnComponent(arcade.gui.UIAnchorLayout):
    def __init__(self, board: BoardModel, game_view: arcade.View):
        super().__init__()
        self.board = board
        self.game_view = game_view

        frame = self.add(arcade.gui.UIAnchorLayout(
            width=PANEL_WIDTH, height=PANEL_HEIGHT, size_hint=None
        ))
        frame.with_padding(all=20)
        frame.with_background(color=Color(0, 30, 70))

        player_name = "Red" if self.board.turn == "R" else "Yellow"
        player_color = (218, 41, 28) if self.board.turn == "R" else (255, 215, 0)

        label = arcade.gui.UITextArea(
            text=f"{player_name}'s Turn",
            font_name="Kenney Blocks",
            font_size=24,
            width=PANEL_WIDTH - 60,
            height=40,
            text_color=player_color,
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
            self.parent.remove(self)
            return True
        return super().on_event(event)
