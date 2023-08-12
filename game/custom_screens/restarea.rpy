screen restarea(screen_active=True):
    tag restarea

    add 'parking'

    imagebutton:
        xpos 100
        ypos 200
        idle 'ammon'
        hover 'ammon_hovered'
        action Call("restarea_ammon")
        sensitive screen_active
        at custom_zoom
    
    imagebutton:
        xpos 1000
        ypos 500

        idle 'trunk'
        hover 'trunk_hovered'
        action [Call("restarea_trunk")]
        sensitive screen_active
        at custom_zoom


screen restareatrunk(screen_active=True):
    tag restarea
    add 'trunkopen'

transform custom_zoom:
    zoom 0.5


label restarea_ammon:
    $ renpy.show_screen("restarea", _layer="master",screen_active=False)
    if ammon_talked == 0:
        $ ammon_talked += 1
        n1 "He’s still sucking on that cigarette. I hope he will choke on it, you asshole."
        am "What are you looking at me for like that? Get over it."
        ga "{cps=3}...{/cps}"
        am "Standing in silence won’t help you, you know? Just go take a hike, I wan’t to finish it in peace."
        am "And that means without your daggering glance on me."
        n1 "He’s right, I won’t get anywhere by just looking at him"
    else:
        n1 "Please choke on it."
    return 

label restarea_trunk:
    $ renpy.show_screen("restareatrunk", _layer="master",screen_active=False)
    "Nice trunk"
    
    return