import arcade
import arcade.gui

from src.views.game_view import GameView
from src.components.reset_score_component import ResetScoreComponent
from src.logic.interfaces.punctuation import Punctuation
from src.logic.interfaces.board import Board

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Connect 4"

arcade.resources.load_kenney_fonts()

class MainView(arcade.View):
    def __init__(self, punctuation: Punctuation, board: Board):
        super().__init__()
        self.punctuation = punctuation
        self.manager = arcade.gui.UIManager()
        
        self.score_color = arcade.color.WHITE
        self.score_font_size = 18
        self.button_width = 150
        self.button_height = 50
        
        self.score_red = arcade.Text("Score Red", 50, 570, self.score_color, self.score_font_size)
        self.score_blue = arcade.Text("Score Blue", 700, 570, self.score_color, self.score_font_size)
        
        self.play_button = arcade.gui.UIFlatButton(text="Play", width=self.button_width)
        self.reset_score_button = arcade.gui.UIFlatButton(text="Reset Score", width=self.button_width)
        self.exit_game_button = arcade.gui.UIFlatButton(text="Exit", width=self.button_width)
        
        self.grid = arcade.gui.UIGridLayout(
            column_count=1, row_count=4, horizontal_spacing=20, vertical_spacing=20
        )
        
        self.grid.add(self.play_button, column=0, row=0)
        self.grid.add(self.reset_score_button, column=0, row=1)
        self.grid.add(self.exit_game_button, column=0, row=2)
        
        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())
        
        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.grid
        )
        
        # Vistas adicionales
        self.game_view = GameView(board, punctuation)
        self.reset_score_view = ResetScoreComponent(self.punctuation)
        
        # Eventos
        self.setup_events()
        
    def setup_events(self):
        @self.play_button.event("on_click")
        def on_click_play_button(event):
            self.window.show_view(self.game_view)
        
        @self.reset_score_button.event("on_click")
        def on_click_reset_button(event):
            self.manager.add(self.reset_score_view)
            
        @self.exit_game_button.event("on_click")
        def on_click_exit_game_button(event):
            arcade.exit()
        
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_GRAY)
        self.manager.enable()
        
    def on_hide_view(self):
        self.manager.disable()
        
    def on_draw(self):
        self.clear()
        punctuation_texts = self.punctuation.show()
    
        self.score_red.text = punctuation_texts["R"]
        self.score_blue.text = punctuation_texts["B"]
        
        self.score_red.draw()
        self.score_blue.draw()
        self.manager.draw()
