import arcade

class TextButton:
    def __init__(self, cx, cy, width, height, text, font_size=18, font_face='Arial'):
        self.center_x = cx
        self.center_y = cy
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = arcade.color.LIGHT_GRAY
        self.highlight_color = arcade.color.WHITE
        self.shadow_color = arcade.color.GRAY
        self.button_height = 2

        self.clicked = False

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y,\
                self.width, self.height, self.face_color)
        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x, y = self.center_x, self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                arcade.color.BLACK, font_size=self.font_size,
                width=self.width, align='center',
                anchor_x='center', anchor_y='center')

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False

def check_press(x, y, button_list):
    pressed = False
    for b in button_list:
        if x > b.center_x + b.width / 2\
        or x < b.center_x - b.width / 2\
        or y > b.center_y + b.height / 2\
        or y < b.center_y - b.height / 2:
            continue
        b.on_press()
        pressed = True
    return pressed

def check_release(x, y, button_list):
    for b in button_list:
        if b.pressed:
            b.on_release()
            return b

class Button(TextButton):
    def __init__(self, cx, cy, lbl):
        super().__init__(cx, cy, 100, 40, lbl)
        self.lbl = lbl

    def on_release(self):
        super().on_release()

    def __repr__(self):
        return '<Button "{}">'.format(self.lbl)
