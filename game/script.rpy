 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ch = Character("Charles", color="#26222cff")

define am = Character("Ammon", color="#f0ee7b", callback=ammon_noise)

define narrator = Character(name=None, what_color="#39f7dc", what_font="gui/fonts/ApercuItalic.otf", callback=narrator_noise)
define az = Character(name="???", image="azzy", color="#714c8f", what_italic=True, who_italic=True, what_color = "#714c8f", what_font="gui/fonts/lydianbi.ttf", who_font="gui/fonts/lydianbi.ttf")

define ga = Character("Gaspard", color="#454b41", callback=gap_noise)

define mj = Character("Marie–Jil", color="#aa6aca")

# Declare images

image ruralRoad = At("bg/ruralRoad.webp")
image parkingLot = At("bg/bg restArea.jpg")

define dissolve = Dissolve(.5)
define fade = Fade(1., 1., 1.)


# The game starts here.

label start:
    stop music

    jump prologue
