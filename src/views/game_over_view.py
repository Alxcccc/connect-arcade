import arcade

from src.logic.interfaces.board import Board
from src.logic.interfaces.scoring import ScoreTracker
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


class GameOverView(arcade.View):
    def __init__(self, board: Board, score_tracker: ScoreTracker, winner: str):
        super().__init__()
        self.board: Board = board
        self.score_tracker: ScoreTracker = score_tracker
        self.winner: str = winner

    def on_show_view(self) -> None:
        self.window.background_color = arcade.color.BLACK

    def on_draw(self) -> None:
        self.clear()
        winner_name: str = "Red" if self.winner == "R" else "Blue"
        arcade.draw_text(
            f"{winner_name} is the winner - press any key to advance",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            arcade.color.DARK_GRAY,
            30,
            anchor_x="center"
        )

    def on_key_press(self, key: int, _modifiers: int) -> None:
        from src.views.main_view import MainView
        menu_view = MainView(self.score_tracker, self.board)
        self.window.show_view(menu_view)
