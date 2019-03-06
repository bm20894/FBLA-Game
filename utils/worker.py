import arcade, random
from . import WIDTH, HEIGHT, questions, Button, dim, margin

class Worker(arcade.Sprite):
    coords = [(158, 95), (730, 515)]
    def __init__(self):
        imgs = [('bin/walk/walk1.png', 0.2), ('bin/worker3.png', 0.4)]
        image, scale = random.choice(imgs)

        super().__init__(image, scale)
        x_left, x_right = dim+10, WIDTH - dim+10
        y_bottom, y_top = dim, HEIGHT - dim

    def ask_question(self):
        q = random.choice(questions)

        buttons = []
        vals = [v for v in q.buttons]
        for i, v in enumerate(vals):
            s = 30 if len(vals) > 2 else 50
            b = Button(WIDTH/2*(i+1)/len(q.buttons) + s + i*75, 200, v)
            buttons.append(b)

        return buttons, q


    @classmethod
    def get_coords(cls, level_number):
        level_3 = cls.coords + [(558, 515), (641, 85), (358, 515), (542, 515), (158, 515)]
        cooler = level_3 + [(WIDTH/2 - 50, dim + 15)]
        c = cls.coords
        if level_number+1 == 3:
            c = level_3
        elif level_number+1 == 4:
            c = cooler
        return random.choice(c)
