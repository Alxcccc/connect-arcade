import arcade
from src.logic.interfaces.board import Board

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

arcade.resources.load_kenney_fonts()

class SwitchTurnView(arcade.View):
    def __init__(self, board: Board, view):
        super().__init__()
        self.view = view
        self.board = board

    def on_show_view(self):
        self.window.background_color = arcade.color.BLACK
    def on_draw(self):
        self.clear()
        self.board.show_matrix()
        arcade.draw_text(f"Turn of {"red" if self.board.turn == "R" else "blue"} - click to advance", SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2,
                         arcade.color.DARK_GRAY, font_size=20, anchor_x="center", font_name="Kenney Blocks")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.show_view(self.view)