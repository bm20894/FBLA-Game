import arcade
import random

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.AMAZON)
        # self.set_mouse_visible(False)

    def setup(self):
        ''' Set up your game here '''
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite('bin/boehm.jpg', 0.4)
        self.player_sprite.center_x = WIDTH / 2
        self.player_sprite.center_y = HEIGHT / 2
        self.player_list.append(self.player_sprite)

        # set up walls
        for i in range(0, WIDTH, 50):
            wall = arcade.Sprite('bin/wall.jpg', 0.1)
            wall.center_x, wall.center_y = i, 200
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_key_press(self, key, modifiers):
        SPEED = 5

        if key == arcade.key.UP:
            self.player_sprite.change_y = SPEED
        if key == arcade.key.DOWN:
            self.player_sprite.change_y = -SPEED
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -SPEED
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.player_list.draw()
        self.wall_list.draw()

        output = 'Score: {}'.format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.physics_engine.update()

def main():
    game = MyGame(WIDTH, HEIGHT)
    game.setup()
    arcade.run()

if __name__ == '__main__':
    main()
