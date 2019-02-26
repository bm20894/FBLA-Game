import arcade
import random, math, sys, os
from utils import (FallingCoin, RisingCoin, BouncingCoin,
        WIDTH, HEIGHT, scale, dim, Worker, check_press, check_release)

MOVESPEED = 5

# constants holding game states
GAMERUN = 1
GAMEOVER = 2

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        super().__init__(width, height)
        arcade.set_background_color(arcade.color.AMAZON)
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
        else:
            self.make_walls()
            for i in range(num_coins):
                self.place_coin(coin_type)


    def place_coin(self, coin_type):
        while True:
            coin = coin_type('bin/gold/gold0.png', scale=0.3)
            coin.center_x = random.randrange(WIDTH)
            coin.center_y = random.randrange(HEIGHT)
            if isinstance(coin, BouncingCoin):
                coin.change_x = random.randrange(-3, 3)
                coin.change_y = random.randrange(-3, 3)
            # check for collisions
            wall_hits = arcade.check_for_collision_with_list(coin, self.wall_list)
            coin_hits = arcade.check_for_collision_with_list(coin, self.coin_list)

            if len(wall_hits) == len(coin_hits) == 0:
                break
        self.coin_list.append(coin)
        self.all_sprites.append(coin)

    def make_walls(self):
        for x in range(0, WIDTH, dim):
            wall_t = arcade.Sprite('bin/wall.jpg', scale)
            wall_b = arcade.Sprite('bin/wall.jpg', scale)
            wall_t.center_x, wall_t.center_y = x, 0
            wall_b.center_x, wall_b.center_y = x, HEIGHT
            self.wall_list.append(wall_t)
            self.wall_list.append(wall_b)

        for y in range(0, HEIGHT, dim):
            wall_l = arcade.Sprite('bin/wall.jpg', scale)
            wall_r = arcade.Sprite('bin/wall.jpg', scale)
            wall_l.center_x, wall_l.center_y = 0, y
            wall_r.center_x, wall_r.center_y = WIDTH, y
            self.wall_list.append(wall_l)
            self.wall_list.append(wall_r)

        for wall in self.wall_list:
            self.all_sprites.append(wall)


    def setup(self):
        ''' Set up your game here '''
        self.all_sprites = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.worker_list = arcade.SpriteList()
        self.button_list = []

        self.score = 0
        self.level_number = 0
        self.question_up = False

        self.player = arcade.AnimatedWalkingSprite()

        self.player.stand_right_textures = [arcade.load_texture('bin/boehm_walk/walk_boehm0.png', scale=0.75)]
        self.player.stand_left_textures = [arcade.load_texture('bin/boehm_walk/walk_boehm0.png', scale=0.75, mirrored=True)]
        self.player.walk_right_textures = [arcade.load_texture('bin/boehm_walk/walk_boehm{}.png'.format(i), scale=0.75) for i in range(6)]
        self.player.walk_left_textures = [arcade.load_texture('bin/boehm_walk/walk_boehm{}.png'.format(i), scale=0.75, mirrored=True) for i in range(6)]
        self.player.texture_change_distance = 20

        self.player.center_x = WIDTH / 2
        self.player.center_y = HEIGHT / 2
        self.player.scale = 0.8
        self.all_sprites.append(self.player)

        # make workers
        self.make_workers()

        # start a level
        self.level()
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.wall_list)

    def make_workers(self):
        # worker = arcade.Sprite('bin/walk/walk1.png', 0.2)
        worker = Worker('bin/walk/walk1.png', 0.2)
        worker.center_x = dim + 10
        worker.center_y = random.randrange(dim, HEIGHT - dim)
        self.worker_list.append(worker)
        self.all_sprites.append(worker)

    def check_worker_collisions(self):
        pass
        # for worker in self.worker_list:
            # if (self.player.left <= worker.right or self.player.right >= worker.left) \
                    # and (self.player.top >= worker.bottom \
                    # or self.player.bottom <= worker.top):
                # self.player.left = worker.right
    def draw_question(self):
        worker = self.worker_list[0]
        arcade.draw_rectangle_filled(worker.center_x - 10, worker.center_y + 20, 50, 20, arcade.color.WHITE)
        for b in worker.ask_question():
            b.draw()

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
            arcade.draw_text(output, WIDTH/4, 25 + dim, (r-15, g-15, b-15), 50, width=WIDTH/2, align='center')
            if self.question_up:
                self.draw_question()

        self.all_sprites.draw()
        output = 'Score: {}'.format(self.score)
        arcade.draw_text(output, 10, HEIGHT-20, arcade.color.WHITE, 14)
        output = 'Press [q] to quit'
        arcade.draw_text(output, WIDTH/2-50, HEIGHT-20, arcade.color.WHITE, 12)

        # draw buttons
        for button in self.button_list:
            button.draw()

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

        # TEST WORKER QUESTIONS
        if key == arcade.key.SPACE:
            self.question_up = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_mouse_press(self, x, y, button_num, modifiers):
        check_press(x, y, self.button_list)
        if not self.game_state:
            self.game_state = GAMERUN
        if self.game_state == GAMEOVER:
            self.game_state = GAMERUN
            self.setup()

    def on_mouse_release(self, x, y, button_num, modifiers):
        check_release(x, y, self.button_list)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        if self.game_state == GAMERUN:
            self.coin_list.update()
            self.wall_list.update()
            self.physics_engine.update()
            # self.all_sprites.update()
            self.all_sprites.update_animation()

            hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
            for coin in hit_list:
                coin.kill()
                self.score += 1

            # self.check_worker_collisions()

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
