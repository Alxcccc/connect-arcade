import arcade

from src.logic.interfaces.board import Board
from src.logic.interfaces.punctuation import Punctuation

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Connect 4"

class GameOverView(arcade.View):
    def __init__(self, board: Board, punctuation: Punctuation, winner: str):
        super().__init__()
        self.board = board
        self.punctuation = punctuation
        self.winner = winner
        
    def on_show_view(self):
        self.window.background_color = arcade.color.BLACK

    def on_draw(self):
        self.clear()
        arcade.draw_text(f"{"Red" if self.winner == "R" else "Blue"} is the winner - press any key to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.DARK_GRAY, 30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the main menu view """
        from views.main_view import MainView
        menu_view = MainView(self.punctuation, self.board)
        self.window.show_view(menu_view)
