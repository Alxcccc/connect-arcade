import arcade
from src.views.main_view import MainView
from src.logic.modules.punctuation import Connect4Punctuation
from src.logic.modules.board import Connect4Board


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Connect 4"

def main():
    board = Connect4Board()
    punctuation = Connect4Punctuation()
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)
    main_view = MainView(punctuation, board)
    window.show_view(main_view)
    arcade.run()

if __name__ == "__main__":
    main()