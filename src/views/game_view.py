import arcade

from src.logic.interfaces.board import Board
from src.logic.interfaces.punctuation import Punctuation
from src.logic.modules.check_winner import CheckWinner
from src.views.switch_turn_view import SwitchTurnView
from src.views.winner_view import GameOverView


class GameView(arcade.View):

    def __init__(self, board: Board, punctuation: Punctuation):
        super().__init__()
        self.punctuation = punctuation
        self.board = board
        self.manager = arcade.gui.UIManager()
        self.winner = None

        self.background_color = arcade.color.BLACK
        

    def on_draw(self):
        self.clear()
        self.board.show_matrix()
        self.manager.draw()
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            from views.main_view import MainView
            menu_view = MainView(self.punctuation, self.board)
            self.window.show_view(menu_view)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.winner is None:
            check_winner = CheckWinner(self.board, self.punctuation, self.board.turn)
            if check_winner.check_enough() == True:
                self.board.turn = "R"
                self.board.reset_matrix()
            result = self.board.put_token(x, y)
            if result is True:
                self.winner = check_winner.check_win()
                if self.winner is None:
                    switch_turn_view = SwitchTurnView(self.board, self)
                    self.window.show_view(switch_turn_view)
                else:
                    self.board.turn = "R"
        else:
            self.board.reset_matrix()
            game_over_view = GameOverView(self.board, self.punctuation, self.winner)
            self.winner = None
            self.window.show_view(game_over_view)
        
                