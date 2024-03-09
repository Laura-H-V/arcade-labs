import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Muneco_nieve:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def nariz(self):
        nose_length = self.radius // 3
        nose_offset_y = self.radius // 4
        arcade.draw_triangle_filled(self.position_x, self.position_y + nose_offset_y,
                                    self.position_x - nose_length, self.position_y - nose_length + nose_offset_y,
                                    self.position_x + nose_length, self.position_y - nose_length + nose_offset_y,
                                    arcade.color.ORANGE)

    def ojos(self):
        eye_radius = self.radius // 6
        eye_offset_x = self.radius // 3
        eye_offset_y = self.radius // 3
        arcade.draw_circle_filled(self.position_x - eye_offset_x, self.position_y + eye_offset_y, eye_radius, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x + eye_offset_x, self.position_y + eye_offset_y, eye_radius, arcade.color.BLACK)

    def update(self):
        self.position_y += self.change_y
        if self.position_y < self.radius:
            self.position_y = self.radius
            self.change_y *= -1
        elif self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            self.change_y *= -1

        self.position_x += self.change_x
        if self.position_x < self.radius or self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLUE)
        self.bola_nieve1 = Muneco_nieve(320, 150, 3, 3, 30, arcade.color.WHITE)
        self.bola_nieve2 = Muneco_nieve(320, 180, 3, 3, 30, arcade.color.WHITE)  # Tamaño ajustado
        self.bola_nieve3 = Muneco_nieve(320, 220, 3, 3, 30, arcade.color.WHITE)  # Tamaño ajustado

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.bola_nieve1.draw()
        self.bola_nieve2.draw()
        self.bola_nieve3.draw()

        # Draw a carrot nose and eyes on the top snowman ball
        self.bola_nieve3.nariz()
        self.bola_nieve3.ojos()

    def update(self, delta_time):
        self.bola_nieve1.update()
        self.bola_nieve2.update()
        self.bola_nieve3.update()

        self.bola_nieve2.set_position(self.bola_nieve1.position_x, self.bola_nieve1.position_y + 30)
        self.bola_nieve3.set_position(self.bola_nieve2.position_x, self.bola_nieve2.position_y + 30)  # Ajuste de posición

        if self.bola_nieve3.position_y + self.bola_nieve3.radius > SCREEN_HEIGHT:
            self.bola_nieve3.position_y = SCREEN_HEIGHT - self.bola_nieve3.radius




def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Snowman Example")
    arcade.run()

if __name__ == "__main__":
    main()