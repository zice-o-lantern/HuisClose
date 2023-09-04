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
        sensitive button_available(screen_active)
        
        at custom_zoom


screen restareatrunk(screen_active=True):
    tag restarea

    add 'trunkopen'

    on "show" action SetVariable("current_screen", "restareatrunk")
    on "replace" action SetVariable("current_screen", "restareatrunk")

    imagebutton:
        pos (350, 800)
        anchor (.5, .5)

        idle 'ammon_bag'
        hover 'ammon_bag_hover'
        action Call("restarea_bag")
        sensitive button_available(screen_active)
    
    if not got_water:
        imagebutton:
            pos (900, 700)
            anchor (.5, .5)

            idle 'bottle'
            hover 'bottle_hovered'
            action Call("restarea_bottle")
            sensitive button_available(screen_active)

    if not got_notebook:
        imagebutton:
            pos (1400, 800)
            anchor (.5, .5)
            idle 'notebook'
            hover 'notebook_hovered'
            action Call("restarea_notebook")
            sensitive button_available(screen_active)
            at custom_zoom
    
    if button_available(screen_active):
        imagebutton auto "backbutton_%s.png" action Show("restarea", _layer="master", transition=dissolve):
            style 'bottom'
            at custom_zoom

transform start_code:
    pos (1005, 520)

init python:
    def check_code():
        good_code = [1, 3, 0, 9]
        # nice_code = [6, 9, 6, 9]
        if padlock_code == good_code:
            renpy.jump("ammon_padlock_good_code")
        
        elif padlock_code == [6, 9, 6, 9]:
            renpy.jump("ammon_padlock_nice_code")
        
        elif padlock_code == [0, 0, 0, 0] or padlock_code == [1, 2, 3, 4]:
            renpy.jump("ammon_padlock_basic_code")



screen restarea_padlock(screen_active=True):
    add "padlock"
    vbox:
        at start_code
        spacing 45
        for i in range(4):
            hbox:
                xalign 0.5
                imagebutton auto "gui/padlock_leftbutton_%s.png" action [SetDict(padlock_code, i, (padlock_code[i] - 1) % 10), Function(check_code)]:
                    at c_zoom
                    sensitive button_available(screen_active)

                text str(padlock_code[i])

                imagebutton auto "gui/padlock_rightbutton_%s.png" action [SetDict(padlock_code, i, (padlock_code[i] + 1) % 10), Function(check_code)]:
                    at c_zoom
                    sensitive button_available(screen_active)

    if button_available(screen_active):
        imagebutton auto "backbutton_%s.png" action Return():
            style 'bottom'
            at custom_zoom


label ammon_padlock_good_code:
    show screen restarea_padlock(screen_active=False)
    "Congrats"
    return
label ammon_padlock_nice_code:
    show screen restarea_padlock(screen_active=False)
    "Nice code."
    "You would use it if this padlock belonged to you. You giggle like a six year–old, it is very funny indeed."

    am "What are you laughing for, Gap?"

    ga "H–Huh nothing! For nothing! Don’t worry!"

    "Ammon confused, doesn’t notice what you’re doing and goes back on sucking that smokey candy of his."
    "You’re reminded that it’s not your padlock. Maybe you should focus on the task at hand, don’t you think?"

    jump restarea_padlock_loop_local

label ammon_padlock_basic_code:
    show screen restarea_padlock(screen_active=False)
    "Despite inputing the first code come to mind, the padlock doesn’t submit."
    "Did you think that Ammon would be that basic? You are disappointed with yourself that you could think that Ammon was able to do that."
    "Well you should keep searching anyway."
    "And stop inputting basic codes that anyone would crack. Ammon is smarter that that. That should be something important to him."

    jump restarea_padlock_loop_local

transform custom_zoom:
    zoom 0.2
transform c_zoom:
    zoom 0.05


label restarea_ammon:
    $ renpy.show_screen(current_screen, _layer="master",screen_active=False)

    ga "Hi Gappy. What is it?"

    menu:
        "I want to talk about something with you":
            "What is it?"
        
        "I’ve got to something for you."

            am "What do you "

label restarea_trunk:
    $ renpy.show_screen("restareatrunk", _layer="master", screen_active=False)
    $ renpy.transition(dissolve)
    
    pause 0.5
    if not trunk_explored:
        "I open the little trunk in the back of the motorcycle."
        "It was so crammed that I was a bit surprised that we managed to fit everything in that much of a place."
        "Discouraged by this sight, I slump my shoulders——I will never find that water bottle "
        $ trunk_explored = True
    return
    
label restarea_bag:
    $ renpy.show_screen(current_screen, _layer="master", screen_active=False)

    if checked_padlock == 0:
        
        "Doubting Ammon’s sayings veracity, you sneakily get at a close distance of your friend’s bag and you try to open it. You cast some quick looks at Ammon while doing your little crime but he seems distracted smoking."
        "Being discreet, you can’t force the bag to open, so you notice something that will prevent you from going any further without making a fuss."

        $ renpy.show_screen("restarea_padlock", screen_active=False)
        $ renpy.transition(dissolve)

        pause 1.0

        "You remember that Ammon is a pretty cautious guy so obviously, he has set a code padlock on his trip belongings. Taking a peek in it will demonstrate harder that you thought."
        "You check the bag if it has a hole or any openings, making you able to bypass his security. Unfortunately no such luck. No tearings, no manifacturing defects, no hole, nothing. You shake the bag. It’s filled to the brim."
        "You mull about a time, it shouldn’t hurt to try some combinations before giving up"
    
    elif checked_padlock == 1:

        "You figure you haven’t tried enough and that you should keep on guessing. You’ll surely find it someday. With enough determination, you’ll crack it don’t worry!"
        "But don’t forget that he has surely input a date dear to him, like you’d guess, his birthday, alright?"
    
    else:

        "Might give it another try."
    
    label restarea_padlock_loop_local:
    # window hide
        call screen restarea_padlock(screen_active=True)
    
    if checked_padlock == 0:

        "Well what were you thinking anyway? Do you really ponder he’d put a random number into his padlock? No that can’t be it. Ammon surely set a code like a date dear to him or something."
        "Perhaps his birthday. Should be easy enough. You just have to put his birthday into the padlock and you’ll be able to unlock, right? Go on, do it. You are{cps=3}...{/cps} able to do{cps=3}...{/cps} it..."
        "{cps=3}...{/cps} Wait. Did you really forget, Ammon’s birthday? You’re utterly ashamed. What a great friend you are. Forgetting the birthday of you are. Great job."
        "Alright, let’s go on. You know what to do. You should look for his birthday. But don’t ask him directly. He {b}will{/b} get mad. It’d be better if you could find it in secret."
        
        $ checked_padlock += 1
    
    elif checked_padlock == 1:
        
        $ checked_padlock += 1 
        "Ok, it really looks like you won’t go anywhere with what you are doing. There are smarter ways to go about it."
        "Just look for the code, ok?"
    else:
        "Ok you should just get back to your search."
    # $ ga_inventory.append(wallet)

    return

label restarea_bottle:
    $ renpy.show_screen(current_screen, _layer="master", screen_active=False)
    "You finally find the water bottles in the clutter of this forsaken top–box. They were hidden under a pile of rubbage. If not determined to make the pain away you’d have given up."
    "You grab one and you swallow it down your throat. With every gulp, contrary as you have expected, the throbbing pain in your head intensifies along as the vice around you forehead compressing it."
    "You suffocate of the heated cluttered mess in your head, and deduce that that water won’t be a short–term cure to your problem."
    if checked_padlock == 0: 
        "You put it down, disappointed. Then something catches your attention in the corner of your eyes. Just in the left–part of the box, in the middle of the mess, rises your hound friend’s bag."
        "You can’t help yourself but be attracted to it. Be mesmesrised by its mysteries. You remember. Ammon was acting weird earlier. Maybe he hides something to you."
        "You should check his bag for any suspicious issues he may have concealed. You can’t deal with Ammon acting shady so you have to get to the bottom of it."
    
    else:
        "You put it down, disappointed, when the padlock on the bag comes back to your mind. You still don’t know what’s inside of it. The contents and what may awaits you still make you intrigued."
        "You are mesmerised with this damn bag, side effect of your headache. Even considering your situation and the context, Ammon was still acting weird earlier, not his usual self."
        "You’ve decided to get back on searching for the code so you can stop fixating on this bag."
    
    "Talking about Ammon, you take out a second bottle for him. He said earlier he wanted some water. You hope that will make him relax and get him a bit more into his usual self."
    
    $ got_water = True
    $ empty_inventory = False
    $ ga_inventory.append(water_bottle)

    return

label restarea_notebook:
    $ renpy.show_screen(current_screen, _layer="master", screen_active=False)
    "Oh here is your beloved notebook you bring with you everywhere."
    
    $ ga_inventory.append(notebook)
    # $ check_inventory_empty()
    $ empty_inventory = False
    $ got_notebook = True

    return