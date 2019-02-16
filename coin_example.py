import arcade
import random

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.AMAZON)
        self.set_mouse_visible(False)

    def setup(self):
        ''' Set up your game here '''
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite('bin/boehm.jpg', 0.4)
        self.player_sprite.center_x = WIDTH / 2
        self.player_sprite.center_y = HEIGHT / 2
        self.player_list.append(self.player_sprite)

        for i in range(20):
            coin = arcade.Sprite('bin/coin.jpg', 0.2)
            coin.center_x = random.randrange(WIDTH)
            coin.center_y = random.randrange(HEIGHT)
            self.coin_list.append(coin)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.player_list.draw()
        self.coin_list.draw()

        output = 'Score: {}'.format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dy, dx):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        for coin in  arcade.check_for_collision_with_list(self.player_sprite, self.coin_list):
            coin.kill()
            self.score += 1

def main():
    game = MyGame(WIDTH, HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
