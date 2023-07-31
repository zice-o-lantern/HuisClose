label prologue:
    
    # Black scene
    pause 1.

    Me "Honestly{w=.5}, I couldn’t believe seeing my father at the stepdoor."
    Me "Or could I? {w=.25}Maybe I shouldn’t believe it." 
    Me "But I do. {w=.25}I really do."
    Me "{sc=1}I really do."
    # TODO: Write an essay about boredom and apathy 

    pause 2.
    scene ruralRoad
    with Dissolve(.5)
    play sound 'audio/sounds/car_white_noise.ogg' loop fadein 1.0

    Me "A beatiful day of April rises at the zenith."
    Me "The cold wind lulls the warm aspalth to sleep."
    Me "A very peaceful day in the end."
    Me "This same glacial breeze brushes my whiskers. {w=.25}I sigh."
    Me "My hands tap on the steering wheel."

    play music 'audio/music/griff.mp3' loop fadein 2.0

    Me "I was a bit bored. I must admit, the road can be long sometimes."

    Me "Trying to fight the monotony, I crank up the car radio so that it can distract me."

    # TODO: maybe develop it more
    play music 'audio/music/Roadhouse Blues.ogg'

    Me "Now, that’s what I’m talking about!"
    Me "I start to bop my head to the rythm of the music"
    Me "The waves of the sound makes me wiggle so much that I bounc"

    # TODO: Interrupt the dialogue (maybe find a better metaphor)

    Ammon "Hey! Stop daydreaming! You’re driving."
    Me "That stirs me out of my euphoric trance and I turn at him"
    Gasperd "Ah! Oh my god, sorry!"
    Gasperd "Don’t shout like this. You’re really gonna send us flying into the ditch"
    Ammon "LOOK AT THE FORSAKEN ROAD YOU MORON. STOP LOOKING AT ME."
    Me "Realising what I am doing, I quickly lose focus of my friend and focus back on the road."
    Me "Well, fortunately, nothing happened or crossed the road during our argument."
    Me "Given I wasn’t really paying attention beforehand, we’re lucky a hedgehog didn’t cross the road or a rabbit didn’t hop on."
    Me "I breathe a sigh of a relief and let of all my muscles relax."
    Me "I still don’t lose sight of the route ; my cheeks start to get pretty red."
    Me "Seconds are passing by and soon minutes and it wont’t stop getting warmer."
    Me "My shoulders slowly and slowly swallow the top of my body ; I’m quickly reminded that I should focus on the road so my head quickly bounces back up to place."
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
    Ammon "Sorry.{w=.5}.{w=.125}.{w=.125} for yelling at you. Got carried away."
    Ammon "I am a bit on the nerves. I reacted too hard on you, it was…{w=.5} irresponsible of me."
    Gasperd "I apologise too…"
    Gasperd "I apologise for getting distracted that much. it was…"
    Me "The words stop in their tracks and I throw him a quick look, smirking."
    Gasperd "… irresponsible of me."
    Me "Ammon snickers."
    Ammon "Why are you repeating what I said?"
    Me "He opens the glove box and start rummaging."
    Me "I try to not pay attention to what he's doing."
    Gasperd "Why not? I think it's funny."
    Ammon "It's not. You're just making fun of me."
    Me "He starts searching frenetically in the box."
    Gasperd "Well, don't you like it?"
    Ammon "If I like it?"
    Me "Ammon stops searching though the box. He pauses."
    Ammon "Of course not! Would you like being run over by a car?"
    Gasperd "A car??? That's how you feel about me?"
    Me "I turn my head to shoot at him my most severe ironic glance."
    # Me "But Ammon shouts."
    Ammon "Eyes on the road, God damn it!!!"
    Gasperd "Oh please, could you say it more gently??{w=.5} What you’re doing is really counterproductive."
    Me "Both of us drop in silence. Then laughter erupts in the air."
    Me "It takes us a lot of time to calm ourselves."
    Ammon "Ahah… It’s been so long…"
    Gasperd "It’s been so long since what? Since you’ve laughed? A bit grim, don’t you think?"
    Ammon "No, no…{w=.5} Well maybe."
    Me "Slumped in his seat, he looks wishfully at the scenery"
    Ammon "Since…{w=.25} Since…{w=.25} {b}we{/b}’ve laughed like that."
    Gasperd "You mean… since what happened last week?"
    Ammon "Oh come on, you know very well you weren’t smiling a bunch even before."
    Me "No, I didn’t know, actually. What does that mean? Am I that much of a downer?"
    Gasperd "Are you telling me I don’t smile enough?"
    Ammon "I’m not saying that…"
    Me "His avoiding gaze says it."
    Me "Ammon gets back to look in the glove…{w=.5} Again."
    Me "The stuff inside it clashes into each other like he went to take a hike in a minefield and stepped on every possible mine."
    Gasperd "You know, you won’t get what you want after you’ve looked for the 59th time."
    Ammon "I known, I know!"
    Gasperd "What’re you’re looking for?"

    default both_options = 0

    while both_options < 2:
        menu the_missing_item:

            "Is it the map?":
                Ammon "No it isn’t."
                Ammon "I trust you know where we’re going for."
                Ammon "… Right?"
                Gasperd "Right…"
                
                $both_options += 1
            
            "Is it your crossword?":
                Ammon "I’m too broody to do any crosswords right now"
                Ammon "This trip has tired me."
                Gasperd "That much, huh…"
        
                $both_options += 1
    
    Ammon "Anyway, I’ve been looking for my book but I can’t find it."
    Gasperd "Your book? I remember seeing it in the trunk."
    Ammon "The trunk… Why did I put it in the trunk?"
    Gasperd "Don’t ask me."
    Me "Flustered as he continues to mess up my glove box, I catch a glimpse of a rest area sign."
    Me "Ammon can be pretty impatient sometimes so he won’t stop until he finds it."
    Gasperd "If you want it that much, we can make a stop."
    Ammon "You know what? Yeah. We both need a break."
    
    jump rest_area
    
label rest_area:
    
    stop music

    scene parkingLot with Dissolve(2.)
    
    Me "The car steers over on the parking lot."
    Me "I give a quick look through the window to see if there’s anyone there."
    Me "Nobody…"
    Me "I turn off the car and open the door as I put my hand into my pocket."
    Me "I move my hands inside the pocket but I couldn’t find any cigarettes."
    Me "So I decided to keep it in my pocket for some time."
    Me "The rest area breathes some tinges of loneliness."
    Me "Alone, I wander over the deserted road."
    Me "There’s some restroons and a phone booth around."
    Me "But that doesn’t matter for me."
    Me "As I stretch my arms, I can’t help but notice something in the grass."
    Me "I carefully approach it and here was a colony waiting for me"
    Me "The rattling of the ants fills up the space"
    Me "I crouch in the grass to take a closer look."
    Me "Their train of life continues without a worry in the world."
    Me "I wonder if they ever feel bored… Inside their little never-ending fetch quest."
    Me "Even though I am stranded in a desert place, the quietness of it all soothes my heart."
    Me "Ammon bursts through his door."
    Ammon "Stretching your legs, huh?"
    Gasperd "Yeah…"
    Me "I quickly get up."
    Me "As Ammon slams the door shut, he pulls out a box of cigarette out of his front pocket."
    Me "I observe him as he lights it, a bit envious."
    Me "He must have noticed my stare because he casts me a side look."
    Me "He’s never been keen to sharing so I could dream ever getting one from him."
    Ammon "Sorry, last one."
    Me "He pauses and then takes a long drag and puff it in the clean air."
    # TODO: Ammon’s description

    Me "Not enough determined, for the moment, to dig into his blatant lie, I’m reminded of the phone booth I’ve seen earlier."
    Me "I’m gonna "
    Ammon "Go on, I will wait here for you."
    Me "As soon as he finishes his phrase, I trot over the booth."
    # TODO: Change tranquil later
    Me "I didn’t notice before but I want some tranquility."
    Me "dealing with him is all but tranquil."
    Me "I briskly reach the phone and enter inside."
    Me "I seal the door fast and I take a breath."
    Me "Now I need to make this phone call."
    Me "I take another deep breath."
    Me "Breathing out, I promptly grab the phone."
    Me "The phone numbers print themselves at high-speed on the station monitor."
    Me "Once the number dialed-in, I don’t wait for a second thought and press call."
    Me "The phone rings once "
    #TODO: write conversation with girlfriend.

    return