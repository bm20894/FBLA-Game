import arcade

class Button:
    def __init__(self, cx, cy, w, h, text, font_size=18,\
            font_face='Arial', face_color=arcade.color.LIGHT_GRAY):
        self.center_x = cx
        self.center_y = cy
        self.width = w
        self.height = h
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.face_color = face_color
        self.pressed = False
        self.shadow_color = arcade.color.GRAY
        self.highlight_color = arcade.color.WHITE
        self.button_height = 2

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y,\
                self.width, self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # bottom horizontal
        arcade.draw_line(self.center_x - self.width // 2,\
                self.center_y - self.height // 2,\
                self.center_x + self.width // 2,\
                self.center_y - self.height // 2, color, self.button_height)

        # right vertical
        arcade.draw_line(self.center_x + self.width // 2,\
                self.center_y - self.height // 2,\
                self.center_x + self.width // 2,\
                self.center_y + self.height // 2, color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # top horizontal
        arcade.draw_line(self.center_x - self.width // 2,\
                self.center_y + self.height // 2,\
                self.center_x + self.width // 2,\
                self.center_y + self.height // 2, color, self.button_height)

        # let vertical
        arcade.draw_line(self.center_x - self.width // 2,\
                self.center_y - self.height // 2,\
                self.center_x - self.width // 2,\
                self.center_y + self.height // 2, color, self.button_height)

        x, y = self.center_x, self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y, arcade.color.BLACK,\
                font_size=self.font_size, width=self.width,\
                align='center', anchor_x='center', anchor_y='center')

    def on_press(self):
        self.pressed = True
        arcade.draw_text('clicked', 300, 500, aracade.color.BLACK)

    def on_release(self):
        self.pressed = False

def check_press(x, y, button_list):
    for button in button_list:
        if x > button.center_x + button.width // 2\
            or x < button.center_x - button.width // 2\
            or y > button.center_y + button.height // 2\
            or y < button.center_y - button.height // 2:
            continue
        print('button pressed')
        button.on_press()

def check_release(x, y, button_list):
    for button in button_list:
        if button.pressed:
            button.on_release()

class YesButton(Button):
    def __init__(self, cx, cy, action):
        super().__init__(cx, cy, 100, 40, 'Yes')
        self.action = action

    def on_release(self):
        super().on_release()
        self.action()

class NoButton(Button):
    def __init__(self, cx, cy, action):
        super().__init__(cx, cy, 100, 40, 'No')
        self.action = action

    def on_release(self):
        super().on_release()
        self.action()

