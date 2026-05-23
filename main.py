import arcade

from src.views.main_view import MainView
from src.logic.modules.board_model import Connect4BoardModel
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, load_resources


def main() -> None:
    load_resources()
    board: Connect4BoardModel = Connect4BoardModel()
    window: arcade.Window = arcade.Window(
        SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False
    )
    main_view: MainView = MainView(board)
    window.show_view(main_view)
    arcade.run()


if __name__ == "__main__":
    main()
