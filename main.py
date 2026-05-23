import arcade

from src.views.main_view import MainView
from src.logic.modules.board import Connect4Board
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


def main() -> None:
    board: Connect4Board = Connect4Board()
    window: arcade.Window = arcade.Window(
        SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False
    )
    main_view: MainView = MainView(board)
    window.show_view(main_view)
    arcade.run()


if __name__ == "__main__":
    main()
