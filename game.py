import arcade
import random, math, sys

WIDTH = 800
HEIGHT = 600
MOVESPEED = 5
ANGLESPEED = 5

# constants holding game states
GAMERUN = 1
GAMEOVER = 2

class FallingCoin(arcade.Sprite):
    def update(self):
        self.center_y -= 2
        if self.top < 0:
            self.bottom = HEIGHT
            self.center_x = random.randrange(WIDTH)

class RisingCoin(arcade.Sprite):
    def update(self):
        self.center_y += 2
        if self.bottom > HEIGHT:
            self.top = 0
            self.center_x = random.randrange(WIDTH)
class BouncingCoin(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.center_x < 0 or self.center_x > WIDTH:
            self.change_x *= -1
        if self.center_y < 0 or self.center_y > HEIGHT:
            self.change_y *= -1

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.AMAZON)
        # self.set_mouse_visible(False)
        self.game_state = 0

    def level(self):
        levels = [
            (arcade.Sprite, 30),
            (FallingCoin, 30),
            (RisingCoin, 20),
            (BouncingCoin, 20)
        ]
        try:
            coin_type, num_coins = levels[self.level_number]
        except IndexError:
            self.game_state = GAMEOVER
            return
        for i in range(num_coins):
            coin = coin_type('bin/gold/gold0.png', scale=0.3)
            coin.center_x = random.randrange(WIDTH)
            coin.center_y = random.randrange(HEIGHT)
            if isinstance(coin, BouncingCoin):
                coin.change_x = random.randrange(-3, 3)
                coin.change_y = random.randrange(-3, 3)
            self.coin_list.append(coin)
            self.all_sprites.append(coin)

    def setup(self):
        ''' Set up your game here '''
        self.all_sprites = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0
        self.level_number = 0

        # self.fullscreen = False

        self.player = arcade.AnimatedWalkingSprite()
        self.player.stand_right_textures = [arcade.load_texture('bin/walk/walking0.png', scale=0.75)]
        self.player.stand_left_textures = [arcade.load_texture('bin/walk/walking0.png', scale=0.75, mirrored=True)]
        self.player.walk_right_textures = [arcade.load_texture('bin/walk/walking{}.png'.format(i), scale=0.75) for i in range(6)]
        self.player.walk_left_textures = [arcade.load_texture('bin/walk/walking{}.png'.format(i), scale=0.75, mirrored=True) for i in range(6)]
        self.player.texture_change_distance = 20

        self.player.center_x = WIDTH / 2
        self.player.center_y = HEIGHT / 2
        self.player.scale = 0.8
        self.all_sprites.append(self.player)

        # start a level
        self.level()

    def draw_title(self):
        tex = arcade.load_texture('bin/title.png')
        arcade.draw_texture_rectangle(WIDTH//2, HEIGHT//2, tex.width, tex.height, tex, 0)

    def draw_game_over(self):
        w = WIDTH/4
        arcade.draw_text('Game Over', w, 400, arcade.color.WHITE, 50, width=w*2, align='center')
        arcade.draw_text('Click to Restart', w, 350, arcade.color.WHITE, 24, width=w*2, align='center')

    def draw_game(self):
        if self.game_state == GAMERUN:
            r, g, b = arcade.color.AMAZON
            output = 'Level {}'.format(self.level_number + 1)
            arcade.draw_text(output, WIDTH/4, 25, (r-15, g-15, b-15), 50, width=WIDTH/2, align='center')
        self.all_sprites.draw()
        output = 'Score: {}'.format(self.score)
        arcade.draw_text(output, 10, HEIGHT-20, arcade.color.WHITE, 14)
        output = 'Press [q] to quit'
        arcade.draw_text(output, WIDTH/2-50, HEIGHT-20, arcade.color.WHITE, 12)

        arcade.draw_text('State: {}'.format(self.game_state), 700, HEIGHT-20, arcade.color.WHITE, 14)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        if not self.game_state:
            self.draw_title()
        if self.game_state == GAMERUN:
            self.draw_game()
        if self.game_state == GAMEOVER:
            self.draw_game()
            self.draw_game_over()

    def on_key_press(self, key, modifiers):
        SPEED = 5
        if key == arcade.key.Q:
            sys.exit(0)

        if key == arcade.key.UP:
            self.player.change_y = SPEED
        if key == arcade.key.DOWN:
            self.player.change_y = -SPEED
        if key == arcade.key.LEFT:
            self.player.change_x = -SPEED
        if key == arcade.key.RIGHT:
            self.player.change_x = SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.game_state:
            self.game_state = GAMERUN
        if self.game_state == GAMEOVER:
            self.game_state = GAMERUN
            self.setup()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        if self.game_state == GAMERUN:
            self.all_sprites.update()
            self.all_sprites.update_animation()

            hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
            for coin in hit_list:
                coin.kill()
                self.score += 1

            # check for level change
            if len(self.coin_list) == 0:
                self.level_number += 1
                self.level()

def main():
    game = MyGame(WIDTH, HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
