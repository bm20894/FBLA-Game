import arcade, random
from . import questions, YesButton, NoButton

class Worker(arcade.Sprite):

    def ask_question(self):
        q = random.choice(questions)
        text, value = q.value.values()

        # create buttons
        yes_button = YesButton(350, 500, lambda: foo())
        no_button = NoButton(500, 500, lambda: foo())
        return [yes_button, no_button]

def foo():
    arcade.draw_text('TESTING', 400, 300, font_size=20)
