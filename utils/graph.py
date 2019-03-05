'''
Graph Module
display a graph on screen with multiple points
'''
import arcade
from . import WIDTH, HEIGHT, margin

def graph(points, game):
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    cx, cy = WIDTH/2, HEIGHT/2
    w, h = WIDTH - margin, HEIGHT - margin
    arcade.draw_rectangle_filled(cx, cy, w, h, arcade.color.WHITE)

    # title
    arcade.draw_text('Quarterly Report', cx, HEIGHT-25,
            arcade.color.BLACK, font_size=18, width=500,
            align='center', anchor_x='center', anchor_y='center')


    # translate origin
    origin = margin/2, margin/2

    # axis
    arcade.draw_line(origin[0], origin[1], margin/2, h+margin/2,
        arcade.color.BLACK, 5)
    arcade.draw_line(origin[0], origin[1], w+margin/2, margin/2,
        arcade.color.BLACK, 5)

    xspc, yspc = int(w/5), int(h/5)
    xbin, ybin = 1, 100

    # ticks
    n = 1
    for i in range(int(origin[0]) + xspc, int(w+margin/2), xspc):
        arcade.draw_line(i, origin[1]-10, i, origin[1]+10,
            arcade.color.BLACK, 3)
        msg = 'Q{}'.format(xbin * n)
        arcade.draw_text(msg, i, origin[1]-20,
                arcade.color.BLACK, font_size=10, width=20,
                align='center', anchor_x='center', anchor_y='center')
        n += 1

    n = 1
    for j in range(int(origin[1]) + yspc, int(h+margin/2), yspc):
        arcade.draw_line(origin[0]-10, j, origin[0]+10, j,
            arcade.color.BLACK, 3)
        msg = '${}'.format(ybin * n)
        arcade.draw_text(msg, origin[0]-30, j,
                arcade.color.BLACK, font_size=10, width=20,
                align='center', anchor_x='center', anchor_y='center')
        n += 1

    # draw point
    coords = [(origin[0], origin[1])]
    for x, p in enumerate(points):
        x += 1
        y = p / 100
        x = x * xspc
        y = y * yspc
        x += origin[0]
        y += origin[1]
        arcade.draw_point(x, y, arcade.color.RED, 10)
        s = '${}'.format(p)
        arcade.draw_text(s, x - 3, y + 15,
                arcade.color.RED, font_size=10, width=20,
                align='center', anchor_x='center', anchor_y='center')
        coords.append((x, y))

    # coords.insert(0, (0, 0))
    for i, point in enumerate(coords[1:]):
        old = coords[i]
        arcade.draw_line(point[0], point[1], old[0], old[1], arcade.color.RED, 5)

    return len(points) == 4
