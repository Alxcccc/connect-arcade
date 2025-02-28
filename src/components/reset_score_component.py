import arcade
import arcade.gui

from src.logic.interfaces.punctuation import Punctuation

arcade.resources.load_kenney_fonts()

class ResetScoreComponent(arcade.gui.UIMouseFilterMixin, arcade.gui.UIAnchorLayout):
    
    def __init__(self, punctuation: Punctuation):
        super().__init__()
        self.punctuation = punctuation
        frame = self.add(arcade.gui.UIAnchorLayout(width=300, height=400, size_hint=None))
        frame.with_padding(all=20)
        
        frame.with_background(
            texture=arcade.gui.NinePatchTexture(
                left=7,
                right=7,
                bottom=7,
                top=7,
                texture=arcade.load_texture(
                    ":resources:gui_basic_assets/window/dark_blue_gray_panel.png"
                )
            )
        )
        question = arcade.gui.UITextArea(text="Do you wanna reset score?", font_name="Kenney Blocks", width=250,  # Ajusta el ancho para que quepa el texto
    height=50)
        yes_button = arcade.gui.UIFlatButton(text="Yes", width=100)
        no_button = arcade.gui.UIFlatButton(text="No", width=100)
        yes_button.on_click = self.on_click_yes_button
        no_button.on_click = self.on_click_back_button
        
        self.grid = arcade.gui.UIGridLayout(
            column_count=1, row_count=3, horizontal_spacing=20, vertical_spacing=20
        )
        
        self.grid.add(question, column=0, row=0)
        self.grid.add(yes_button, column=0, row=1)
        self.grid.add(no_button, column=0, row=2)
        
        
        widget_layout = arcade.gui.UIBoxLayout(align="left", space_between=10)
        
        widget_layout.add(self.grid)
        
        frame.add(child=widget_layout, anchor_x="center_x", anchor_y="top")
        
    def on_click_yes_button(self, event):
        self.punctuation.reset_point()
        self.parent.remove(self)
    
    def on_click_back_button(self, event):
        self.parent.remove(self)
        
        
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_GRAY)
        
        self.manager.enable()
        
    def on_hide_view(self):
        self.manager.disable()
        
    def on_draw(self):
        self.clear()
        
        self.manager.draw()