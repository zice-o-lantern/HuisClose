style bottom:
    xalign .5
    yalign .98

screen restarea(screen_active=True):
    tag restarea

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
    if ammon_talked == 0:
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
    "Nice trunk"
    "Wish it had items"
    return

label restarea_wallet:
    $ renpy.show_screen(current_screen, _layer="master", screen_active=False)
    "Deez nuts"

    return

label restarea_bottle:
    $ renpy.show_screen(current_screen, _layer="master", screen_active=False)
    "Don’t mind me"

    return

label restarea_notebook:
    $ renpy.show_screen(current_screen, _layer="master", screen_active=False)
    "Cock"

    return