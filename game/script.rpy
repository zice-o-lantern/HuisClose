 ﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")

define ch = Character("Charles")

define ca = Character("Carl")

define me = Character(name=None, what_italic=True)

define ga = Character("Gasperd")


# The game starts here.

label start:

    # Black scene

    me "Honestly, I couldn’t believe seeing my father at the stepdoor."
    me "Or could I? {w=.25}Maybe I shouldn’t believe it." 
    me "But I do. {w=.25}I really do."
    me "{sc=1}I don’t really know anymore..."

    scene bg rural road
    with Dissolve(2)
    play music "audio/music/griff.mp3" loop fadein 2.0

    me "A beatiful day of April rises at the zenith."
    me "The cold wind lulls the warm aspalth to sleep."
    me "A very peaceful day in the end."
    me "This same glacial breeze brushes my whiskers. {w=.25}I sigh."
    me "My hands tap on the steering wheel."
    me "I was a bit bored. I must admit, the road can be long sometimes."
    me "Trying to fight the monotony, I crank up the car radio to distract me."
    me "I really like this music."
    me "I start to bop my head to the rythm of the music"
    me "The waves of the sound makes me wiggle so much that"

    # TODO: Interrupt the dialogue (maybe find a better metaphor)

    ca "Hey! Stop daydreaming! You’re driving."
    ga "Ah! Don’t shout like this. You’re really gonna send us flying into the ditch"
 
    # Blank
    # Gasperd desc
    me "I am someone you could find at every corner of the street."
    me "Well maybe not. Some people wouldn’t say that."
    me "\"Oh my god, you should smile more.\" \"Are you ever happy?\" \"Why are you brooding again?\""
    me "That really annoys me. I can smile if I want. It’s just I’m tired you know."
    me "Mom once told me \"You are the smiliest boy I’ve ever seen. Never drop that smile, you hear me?\""
    me "I wasn’t really listening but that caught me off guard."
    me "Mrs. Cranberry once told me \"Of all my pupils, you’re one of the brightest and warmest boy I’ve had.\""
    me "I still wasn’t really listening but it didn’t caught me off guard."
    me "At the end of the day, I’m still lost. Do I smile enough?"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    
    me "I live at the outskirts"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
