from typing import Dict

import arcade
import arcade.gui

from src.views.game_view import GameView
from src.components.reset_score_component import ResetScoreComponent
from src.logic.interfaces.scoring import ScoreTracker
from src.logic.interfaces.board import Board
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


class MainView(arcade.View):
    def __init__(self, score_tracker: ScoreTracker, board: Board):
        super().__init__()
        self.score_tracker: ScoreTracker = score_tracker
        self.manager: arcade.gui.UIManager = arcade.gui.UIManager()

        self.score_color: tuple = arcade.color.WHITE
        self.score_font_size: int = 18
        self.button_width: int = 150
        self.button_height: int = 50

        self.red_score_text: arcade.Text = arcade.Text(
            "Score Red", 50, 570, self.score_color, self.score_font_size
        )
        self.blue_score_text: arcade.Text = arcade.Text(
            "Score Blue", 700, 570, self.score_color, self.score_font_size
        )

        self.play_button: arcade.gui.UIFlatButton = arcade.gui.UIFlatButton(
            text="Play", width=self.button_width
        )
        self.reset_score_button: arcade.gui.UIFlatButton = arcade.gui.UIFlatButton(
            text="Reset Score", width=self.button_width
        )
        self.exit_game_button: arcade.gui.UIFlatButton = arcade.gui.UIFlatButton(
            text="Exit", width=self.button_width
        )

        self.grid: arcade.gui.UIGridLayout = arcade.gui.UIGridLayout(
            column_count=1, row_count=4, horizontal_spacing=20, vertical_spacing=20
        )

        self.grid.add(self.play_button, column=0, row=0)
        self.grid.add(self.reset_score_button, column=0, row=1)
        self.grid.add(self.exit_game_button, column=0, row=2)

        self.anchor: arcade.gui.UIAnchorLayout = self.manager.add(
            arcade.gui.UIAnchorLayout()
        )

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.grid
        )

        self.game_view: GameView = GameView(board, score_tracker)
        self.reset_score_component: ResetScoreComponent = ResetScoreComponent(
            self.score_tracker
        )

        self._setup_events()

    def _setup_events(self) -> None:
        @self.play_button.event("on_click")
        def on_click_play(_event):
            self.window.show_view(self.game_view)

        @self.reset_score_button.event("on_click")
        def on_click_reset(_event):
            self.manager.add(self.reset_score_component)

        @self.exit_game_button.event("on_click")
        def on_click_exit(_event):
            arcade.exit()

    def on_show_view(self) -> None:
        arcade.set_background_color(arcade.color.DARK_GRAY)
        self.manager.enable()

    def on_hide_view(self) -> None:
        self.manager.disable()

    def on_draw(self) -> None:
        self.clear()
        score_texts: Dict[str, str] = self.score_tracker.show()

        self.red_score_text.text = score_texts["R"]
        self.blue_score_text.text = score_texts["B"]

        self.red_score_text.draw()
        self.blue_score_text.draw()
        self.manager.draw()
