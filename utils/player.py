import arcade
from . import WIDTH, HEIGHT, dim

dim = dim // 2

class Player(arcade.AnimatedWalkingSprite):
    def __init__(self, images):
        super().__init__()
        self.stand_right_textures = images[0]
        self.stand_left_textures = images[1]
        self.walk_right_textures = images[2]
        self.walk_left_textures = images[3]
        self.texture_change_distance = 20

        self.center_x = WIDTH / 2
        self.center_y = HEIGHT / 2
        self.scale = 0.8

    def update_animation(self):
        super().update_animation()

        if self.left <= dim:
            self.left = dim
        if self.right >= WIDTH - dim:
            self.right = WIDTH - dim
        if self.bottom <= dim:
            self.bottom = dim
        if self.top >= HEIGHT - dim:
            self.top = HEIGHT - dim
