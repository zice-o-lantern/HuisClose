 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")

define ch = Character("Charles")

define Carl = Character("Carl")

define Me = Character(name=None, what_italic=True)

define Gasperd = Character("Gasperd")


# The game starts here.

label start:

    # Black scene

    Me "Honestly{w=.5}, I couldn’t believe seeing my father at the stepdoor."
    Me "Or could I? {w=.25}Maybe I shouldn’t believe it." 
    Me "But I do. {w=.25}I really do."
    Me "{sc=1}I don’t really know anymore..."

    pause 2.
    scene bg rural_road
    with Dissolve(.5)
    play music "audio/music/griff.mp3" loop fadein 2.0

    Me "A beatiful day of April rises at the zenith."
    Me "The cold wind lulls the warm aspalth to sleep."
    Me "A very peaceful day in the end."
    Me "This same glacial breeze brushes my whiskers. {w=.25}I sigh."
    Me "My hands tap on the steering wheel."


    Me "I was a bit bored. I must admit, the road can be long sometimes."
    Me "Trying to fight the monotony, I crank up the car radio to distract me."
    # TODO: Find a song that goes well here and maybe develop it more
    Me "I really like this music."
    Me "I start to bop my head to the rythm of the music"
    Me "The waves of the sound makes me wiggle so much that I bounc"

    # TODO: Interrupt the dialogue (maybe find a better metaphor)

    Carl "Hey! Stop daydreaming! You’re driving."
    Me "That stirs me out of my euphoric trance and I turn at him"
    Gasperd "Ah! Oh my god, sorry!"
    Gasperd "Don’t shout like this. You’re really gonna send us flying into the ditch"
    Carl "LOOK AT THE FORSAKEN ROAD YOU MORON. STOP LOOKING AT ME."
    Me "Realising what I am doing, I quickly lose focus of my friend and focus back on the road."
    Me "Well, fortunately, nothing happened or crossed the road during our argument."
    Me "Given I wasn’t really paying attention beforehand, we’re lucky a hedgehog didn’t cross the road or a rabbit didn’t hop on."
    Me "I breathe a sigh of a relief and let of all my muscles relax."
    Me "I still don’t lose sight of the route ; my cheeks start to get pretty red."
    Me "Seconds are passing by and soon minutes and it wont’t stop getting redder."
    Me "My shoulders slowly and slowly swallow the top of my body ; I’m quickly reminded that I should focus on the road so my head quickly bounces back up."
    Me "That was careless of me but Carl’s intervention distracted me even more…"
    Me "… Speaking of him, he hasn’t talked since the altercation."
    Me "I can see him on the corner of my eyes that he’s crossed his arms and got slouched on the seat."
    Me "He’s on the point of resting his legs on the driveboard, but he knows he can’t because I would instantly scold him."
    Me "The silence between us grows thicker and starts to create a sultry space void."
    Me "And the car radio music does not help fill the blank…"
    Me "It starts to really unsettle me so I think up of a thing to say."
    Me "I take a breath and open my mouth."
    # TODO: Once again, interrupt dialogue.
    Gasperd "I huh apolog"
    Carl "Sorry.{w=.5}.{w=.125}.{w=.125} for yelling at you. Got carried away."
    Carl "I am a bit on the nerves. I reacted too hard on you, it was…{w=.5} irresponsible of me."
    Gasperd "I apologise too…"
    Gasperd "I apologise for getting distracted that much. it was…"
    Me "The words stop in their tracks and I throw him a quick look, smirking."
    Gasperd "… irresponsible of me."
    Me "Carl snickers."
    Carl "Why are you repeating what I said?"
    Me "He opens the glove box and start rummaging."
    Me "I try to not pay attention to what he's doing."
    Gasperd "Why not? I think it's funny."
    Carl "It's not. You're just making fun of me."
    Me "He starts searching frenetically in the box."
    Gasperd "Well, don't you like it?"
    Carl "If I like it?"
    Me "Carl stops searching though the box. He pauses."
    Carl "Of course not! Would you like being run over by a car?"
    Gasperd "A car??? That's how you feel about my company?"
    Me "I turn my head to shoot at my most severe ironic glance."
    # Me "But Carl shouts."
    Carl "Eyes on the road, God damn it!!!"
    Gasperd "Oh please, could you say it more gently??{w=.5} What you’re doing is really counterproductive."
    Me "Both of us drop in silence. Then laughter erupts in the air."
    Me "It takes us a lot of time to calm ourselves."
    Carl "Ahah… It’s been so long…"
    Gasperd "It’s been so long since what? Since you’ve laughed? A bit grim, don’t you think?"
    Carl "No, no…{w=.5} Well maybe."
    Me "Slumped in his seat, he looks wishfully at the scenery"
    Carl "Since…{w=.25} Since…{w=.25} we’ve laughed like that."
    Gasperd "You mean… since what happened"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    
    Me "I live at the outskirts"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
