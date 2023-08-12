 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ch = Character("Charles", color="#26222cff")

define am = Character("Ammon", color="#f0ee7b")

define n1 = Character(name=None, what_italic=True)

define ga = Character("Gasperd", color="#454b41")

define ju = Character("Julie", color="#aa6aca")

# Declare images

image ruralRoad = At("bg/ruralRoad.jpg")
image parkingLot = At("bg/bg restArea.jpg")


# The game starts here.

label start:
    stop music

    jump test_room
