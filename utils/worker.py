import arcade, random
from . import WIDTH, HEIGHT, questions, YesButton, NoButton, dim

class Worker(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        x_left, x_right = dim+10, WIDTH - dim+10
        y_bottom, y_top = dim, HEIGHT - dim

        self.center_x = random.randrange(x_left, x_right)
        self.center_y = random.randrange(y_bottom, y_top)

    def ask_question(self):
        q = random.choice(questions)
        value = q.value
        text = q.text

        # create buttons
        margin = 100
        yes_button = YesButton(313, 300 - margin)#, foo)
        no_button = NoButton(488, 300 - margin)#, foo)
        return [yes_button, no_button], q
