import arcade

WIDTH, HEIGHT = 800, 600
MOVESPEED = 5

class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > WIDTH - 1:
            self.right = WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > HEIGHT - 1:
            self.top = HEIGHT - 1

class MyGame(arcade.Window):
    def __init__(self, width, height, title=None):
        super().__init__(width, height, title)

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = Player('bin/boehm.jpg', 0.4)
        self.player_sprite.center_x, self.player_sprite.center_y = 50, 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    def update(self, delta_time):
        self.player_sprite.change_x, self.player_sprite.change_y = 0, 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVESPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVESPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVESPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVESPEED

        self.player_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = True
        if key == arcade.key.DOWN:
            self.down_pressed = True
        if key == arcade.key.LEFT:
            self.left_pressed = True
        if key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = False
        if key == arcade.key.DOWN:
            self.down_pressed = False
        if key == arcade.key.LEFT:
            self.left_pressed = False
        if key == arcade.key.RIGHT:
            self.right_pressed = False

def main():
    window = MyGame(WIDTH, HEIGHT, 'Better Movement')
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
