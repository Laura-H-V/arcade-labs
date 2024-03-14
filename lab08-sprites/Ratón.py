import arcade
import random

SPRITE_SCALING = 0.5
SPRITE_QUES0 = 0.3
QUESO_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = ""
SOUND_COLECTAR_QUESO = arcade.load_sound("raton.mp3")
MUSIC_FONDO = arcade.load_sound("gta-san-andreas.mp3")

MOVEMENT_SPEED = 5

class Mouse(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.player_list = None
        self.queso_list = None

        self.player_sprite = None
        self.score = 0
        self.score_text = f"Score: {self.score}"
        self.sound_colectar_queso = SOUND_COLECTAR_QUESO
        self.music_fondo = MUSIC_FONDO
        arcade.play_sound(self.music_fondo, volume=0.5)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.queso_list = arcade.SpriteList()

        self.player_sprite = Mouse("mouse.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(QUESO_COUNT):
            queso = arcade.Sprite("queso.png", SPRITE_QUES0)
            queso.center_x = random.randrange(SCREEN_WIDTH)
            queso.center_y = random.randrange(SCREEN_HEIGHT)
            self.queso_list.append(queso)

    def on_draw(self):

        arcade.start_render()
        self.clear()

        self.player_list.draw()
        self.queso_list.draw()
        arcade.draw_text(self.score_text, 10, 10, arcade.color.WHITE, 14)

    def on_update(self, delta_time):

        self.player_list.update()
        self.queso_list.update()

        queso_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.queso_list)

        for queso in queso_hit_list:
            queso.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.sound_colectar_queso)

        self.score_text = f"Score: {self.score}"


    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            arcade.play_sound(self.music_fondo, volume=5)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()