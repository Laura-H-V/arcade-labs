"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.WHITE)

# Get ready to draw
arcade.start_render()


# Cara
arcade.draw_circle_filled(390, 300, 280, arcade.color.BLEU_DE_FRANCE)
arcade.draw_circle_filled(390, 240, 230, arcade.color.WHITE)
arcade.draw_circle_outline(390, 240, 230, arcade.color.BLACK,5)

# Ojos
arcade.draw_ellipse_filled(330, 460, 110, 130,arcade.color.WHITE)
arcade.draw_ellipse_outline(330, 460, 110, 130,arcade.color.BLACK,5)
arcade.draw_ellipse_filled(440, 460, 110, 130,arcade.color.WHITE)
arcade.draw_ellipse_outline(440, 460, 110, 130,arcade.color.BLACK,5)

# Iris
arcade.draw_ellipse_filled(350, 460, 20, 40,arcade.color.BLACK)
arcade.draw_ellipse_filled(420, 460, 20, 40,arcade.color.BLACK)

# Pupila
arcade.draw_ellipse_filled(350, 460, 10, 20,arcade.color.WHITE)
arcade.draw_ellipse_filled(420, 460, 10, 20,arcade.color.WHITE)

# Boca
arcade.draw_arc_filled(390, 290, 280, 400, arcade.color.RED, 180, 360)
arcade.draw_arc_outline(390, 290, 280, 400, arcade.color.BLACK, 180, 360,5)
arcade.draw_line(250,290,530,290,arcade.color.BLACK,3)

# Lengua
arcade.draw_ellipse_filled(390, 152, 170, 120,arcade.color.PINK)


# Nariz
arcade.draw_circle_filled(385, 370, 50, arcade.color.RED)
arcade.draw_circle_outline(385, 370, 50, arcade.color.BLACK,5)

# Bigotes izq
arcade.draw_line(300,370,220,380,arcade.color.BLACK,3)
arcade.draw_line(300,350,220,350,arcade.color.BLACK,3)
arcade.draw_line(300,330,220,320,arcade.color.BLACK,3)

# Bigotes der
arcade.draw_line(550,380,470,370,arcade.color.BLACK,3)
arcade.draw_line(550,350,470,350,arcade.color.BLACK,3)
arcade.draw_line(550,320,470,330,arcade.color.BLACK,3)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

