 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ch = Character("Charles", color="#26222cff")

##TODO: Change the name
define cl = Character("Clair", what_font = "gui/fonts/lydianbi.ttf",  image="clair", callback=clair_noise)

define am = Character("Ammon", color="#f0ee7b", callback=ammon_noise, image="ammon")

define narrator = Character(name=None, what_color="#39f7dc", what_font="gui/fonts/ApercuItalic.otf", callback=narrator_noise)
define az = Character(name="Aimé", image="azzy", color="#714c8f", what_italic=True, who_italic=True, what_color = "#714c8f", what_font="gui/fonts/lydianbi.ttf")
define dk = Character(name="Prudence", image="derek", color="#4c6f8f", what_italic=True, who_italic=True, what_color = "#4c6f8f", what_font="gui/fonts/lydianbi.ttf")

define hl = Character("Howl", color="#454b41", callback=gap_noise)
define hl1 = Character("Hurles", color="#454b41", callback=gap_noise)

define mj = Character("Marie–Jil", color="#aa6aca")


# The game starts here.

label start:
    stop music

    jump prologue
