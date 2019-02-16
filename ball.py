import arcade

WIDTH, HEIGHT = 600, 600

RADIUS = 20
g = 0.3

BOUNCINESS = 0.9

def draw(delta_time):
    arcade.start_render()
    arcade.draw_circle_filled(draw.x, draw.y, RADIUS, arcade.color.BLACK)

    draw.x += draw.delta_x
    draw.y += draw.delta_y

    draw.delta_y -= g

    # collision detection
    if draw.x < RADIUS and draw.delta_x < 0 \
        or draw.x > WIDTH - RADIUS and draw.delta_x > 0:
        draw.delta_x *= -BOUNCINESS
        draw.bounces += 1

    if draw.y < RADIUS and draw.delta_y < 0:
        if draw.delta_y * -1 > g * 15:
            draw.delta_y *= -BOUNCINESS
        else:
            draw.delta_y *= -BOUNCINESS / 2
        # print('{:.2f}'.format(draw.delta_y))
        if draw.delta_y < 1:
            draw.delta_y = 0
            # draw.delta_x = 0
        draw.bounces += 1

    msg = 'Number of Bounces: {}'.format(draw.bounces)
    arcade.draw_text(msg, 10, HEIGHT-15, arcade.color.BLACK, 14)

draw.bounces = 0
draw.x = RADIUS
draw.y = HEIGHT - RADIUS
draw.delta_x, draw.delta_y = 2, 0


def main():
    arcade.open_window(WIDTH, HEIGHT, 'Bouncy Ball')
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(draw, 1/80)

    arcade.run()
    arcade.close_window()

if __name__ == '__main__':
    main()
