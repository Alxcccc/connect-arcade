from typing import Dict

import arcade
import arcade.gui
from arcade.gui.widgets.buttons import UIFlatButtonStyle

from src.views.game_view import GameView
from src.logic.interfaces.scoring import ScoreTracker
from src.logic.interfaces.board import Board
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT


YELLOW_NORMAL = (255, 215, 0)
YELLOW_HOVER = (220, 185, 0)
YELLOW_PRESS = (180, 150, 0)
RED_NORMAL = (218, 41, 28)
RED_HOVER = (180, 30, 18)
RED_PRESS = (140, 20, 10)


class MainView(arcade.View):
    def __init__(self, score_tracker: ScoreTracker, board: Board):
        super().__init__()
        self.score_tracker: ScoreTracker = score_tracker
        self.manager: arcade.gui.UIManager = arcade.gui.UIManager()

        self.score_font_size: int = 18
        self.button_width: int = 180

        play_style = {
            "normal": UIFlatButtonStyle(bg=YELLOW_NORMAL, font_color=(0, 0, 0)),
            "hover": UIFlatButtonStyle(bg=YELLOW_HOVER, font_color=(0, 0, 0), border=(255, 255, 255), border_width=2),
            "press": UIFlatButtonStyle(bg=YELLOW_PRESS, font_color=(0, 0, 0), border=(255, 255, 255), border_width=2),
            "disabled": UIFlatButtonStyle(bg=(128, 128, 128)),
        }

        exit_style = {
            "normal": UIFlatButtonStyle(bg=RED_NORMAL, font_color=(0, 0, 0)),
            "hover": UIFlatButtonStyle(bg=RED_HOVER, font_color=(0, 0, 0), border=(255, 255, 255), border_width=2),
            "press": UIFlatButtonStyle(bg=RED_PRESS, font_color=(0, 0, 0), border=(255, 255, 255), border_width=2),
            "disabled": UIFlatButtonStyle(bg=(128, 128, 128)),
        }

        self.title_text = arcade.Text(
            "CONNECT 4",
            SCREEN_WIDTH / 2,
            530,
            arcade.color.WHITE,
            font_size=52,
            anchor_x="center",
            font_name="Kenney Blocks",
        )

        self.subtitle_text = arcade.Text(
            "Two-Player Game",
            SCREEN_WIDTH / 2,
            490,
            (180, 200, 230),
            font_size=16,
            anchor_x="center",
            font_name="Kenney Blocks",
        )

        self.play_button: arcade.gui.UIFlatButton = arcade.gui.UIFlatButton(
            text="Play", width=self.button_width, style=play_style
        )
        self.exit_game_button: arcade.gui.UIFlatButton = arcade.gui.UIFlatButton(
            text="Exit", width=self.button_width, style=exit_style
        )

        self.grid: arcade.gui.UIGridLayout = arcade.gui.UIGridLayout(
            column_count=1, row_count=4, horizontal_spacing=20, vertical_spacing=20
        )

        self.grid.add(self.play_button, column=0, row=0)
        self.grid.add(self.exit_game_button, column=0, row=1)

        self.anchor: arcade.gui.UIAnchorLayout = self.manager.add(
            arcade.gui.UIAnchorLayout()
        )

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.grid
        )

        self.game_view: GameView = GameView(board, score_tracker)

        self._setup_events()

    def _setup_events(self) -> None:
        @self.play_button.event("on_click")
        def on_click_play(_event):
            self.window.show_view(self.game_view)

        @self.exit_game_button.event("on_click")
        def on_click_exit(_event):
            arcade.exit()

    def on_show_view(self) -> None:
        arcade.set_background_color((0, 30, 70))
        self.manager.enable()

    def on_hide_view(self) -> None:
        self.manager.disable()

    def on_draw(self) -> None:
        self.clear()

        self.title_text.draw()
        self.subtitle_text.draw()

        arcade.draw_circle_filled(SCREEN_WIDTH / 2 - 130, 520, 15, (218, 41, 28))
        arcade.draw_circle_filled(SCREEN_WIDTH / 2 + 130, 520, 15, (255, 215, 0))

        self.manager.draw()
