style bottom:
    xalign .5
    yalign .98

screen restarea(screen_active=True):
    tag restarea

    on "show" action SetVariable("current_screen", "restarea")
    on "replace" action SetVariable("current_screen", "restarea")

    add 'parking'

    imagebutton:
        pos (100, 200)
        anchor (.5, .5)

        idle 'ammon'
        hover 'ammon_hovered'
        action Call("restarea_ammon")
        sensitive screen_active

        at custom_zoom
    
    imagebutton:
        pos (1000, 500)
        anchor (.5, .5)

        idle 'trunk'
        hover 'trunk_hovered'
        action Call("restarea_trunk")
        sensitive screen_active
        
        at custom_zoom


screen restareatrunk(screen_active=True):
    tag restarea

    add 'trunkopen'

    on "show" action SetVariable("current_screen", "restareatrunk")
    on "replace" action SetVariable("current_screen", "restareatrunk")

    imagebutton:
        pos (350, 800)
        anchor (.5, .5)

        idle 'portefeuille_clark'
        hover 'portefeuille_clark_hovered'
        action Call("restarea_wallet")
        sensitive screen_active

        at custom_zoom
    
    imagebutton:
        pos (900, 700)
        anchor (.5, .5)

        idle 'bottle'
        hover 'bottle_hovered'
        action Call("restarea_bottle")
        sensitive screen_active
    
    imagebutton:
        pos (1400, 800)
        anchor (.5, .5)
        idle 'notebook'
        hover 'notebook_hovered'
        action Call("restarea_notebook")
        sensitive screen_active
        at custom_zoom
    
    if screen_active:
        imagebutton auto "backbutton_%s.png" action Show("restarea", _layer="master", transition=dissolve):
            style 'bottom'
            at custom_zoom

transform custom_zoom:
    zoom 0.2


label restarea_ammon:
    $ renpy.show_screen(current_screen, _layer="master",screen_active=False)
    python:
        for i in ga_inventory:
            if i.name == "Cigarette":
                renpy.jump("confront_him")
    if ammon_talked == 0:
        $ ammon_talked += 1
        ga "Hey Ammon."
        
        am "What."

        ga "Are you sure you don’t have a cigarette?"

        am "No."

        n1 "What a cheerfulness."

        ga "So…{w} what were you doing in the box?"

        am "None of your business, Gaspard."
        am "Haven’t you told you were thirsty? I don’t have anything for you right now so go get one."

        n1 "What’s gotten into him."
        n1 "I just wanted a smoke…"
    elif ammon_talked == 1:
        $ ammon_talked += 1
        n1 "He’s still sucking on that cigarette. I hope he will choke on it."

        am "What are you looking at me for like that? Get over it."

        ga "{cps=3}...{/cps}"
        
        am "Standing in silence won’t help you, you know? Just go take a hike, I want to finish it in peace."
        am "And that means without your daggering glaze on me."
        n1 "He’s right, I won’t get anywhere by just looking at him"
    else:
        n1 "Please choke on it."
    return 

label restarea_trunk:
    $ renpy.show_screen("restareatrunk", _layer="master", screen_active=False)
    $ renpy.transition(dissolve)
    pause 0.5
    if not trunk_explored:
        n1 "I open the little trunk in the back of the motorcycle."
        n1 "It was so crammed that I was a bit surprised that we managed to fit everything in that much of a place."
        n1 "Discouraged by this sight, I slump my shoulders——I will never find that water bottle "
        $ trunk_explored = True
    return

label restarea_wallet:
    $ renpy.show_screen(current_screen, _layer="master", screen_active=False)
    n1 "Ammon's wallet was sitting there, accessible to anyone's eyes, unaware of what it may happen."
    n1 "It has been previously opened by, I guess, the annoying dog smoking over there."
    n1 "Curious of its content, I peek over to see if he's distracted and assured he is, reach for it."
    n1 "Feeling no guilt, determined to get at the bottom of this, I grab it and open it."
    n1 "Maybe he hid some smokes in it. I run through all of his papers and documents he keeps in it but no such luck."
    ## TODO: Rewrite later
    n1 "Maybe "
    n1 "Interested by the photos I take them but I notice a box of cigarettes under the photos."
    n1 "Ahah knew he was lying."

    $ ga_inventory.append(cigarette)
    # $ ga_inventory.append(wallet)

    "(You can go see Ammon now)"

    return

label restarea_bottle:
    $ renpy.show_screen(current_screen, _layer="master", screen_active=False)
    "Don’t mind me"

    return

label restarea_notebook:
    $ renpy.show_screen(current_screen, _layer="master", screen_active=False)
    "Cock"

    return