 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Charles = Character("Charles")

define Ammon   = Character("Ammon")

define Me      = Character(name=None, what_italic=True)

define Gasperd = Character("Gasperd")

# Declare images

image ruralRoad = At("images/bg/ruralRoad.jpg")
image parkingLot = At("images/bg/bg restArea.jpg")


# The game starts here.

label start:
    stop music

    jump prologue
