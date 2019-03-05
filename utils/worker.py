import arcade, random
from . import WIDTH, HEIGHT, questions, Button, dim, margin

class Worker(arcade.Sprite):
    coords = [(158, 95), (70, 515)]
    def __init__(self):
        imgs = [('bin/walk/walk1.png', 0.2), ('bin/worker2.jpg', 0.1)]
        image, scale = random.choice(imgs)

        super().__init__(image, scale)
        x_left, x_right = dim+10, WIDTH - dim+10
        y_bottom, y_top = dim, HEIGHT - dim

    def ask_question(self):
        q = random.choice(questions)

        print(q.buttons)
        buttons = []
        vals = [v for v in q.buttons]
        for i, v in enumerate(vals):
            s = 30 if len(vals) > 2 else 50
            b = Button(WIDTH/2*(i+1)/len(q.buttons) + s + i*75, 200, v)
            buttons.append(b)

        return buttons, q


    @classmethod
    def get_coords(cls, level_number):
        right_side = cls.coords + [(728, 515), (641, 85)]
        cooler = right_side + [(WIDTH/2 - 50, dim + 15)]
        c = cls.coords
        print(level_number)
        if level_number == 2:
            c = right_side
        elif level_number == 3:
            c = cooler
        return random.choice(c)
