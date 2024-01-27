style bottom:
    xalign .5
    yalign .98

screen restarea(screen_active=True):
    tag restarea

    on "show" action SetVariable("current_screen", "restarea")
    on "replace" action SetVariable("current_screen", "restarea")

    add 'parking' at zpos_bg

    imagebutton:
        pos (300, 400)
        anchor (.5, .5)

        idle 'ammon_pn'
        hover 'ammon_pn_hovered'
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
    
    if not got_stick:
        imagebutton:
            pos (900, 700)
            anchor (.5, .5)

            idle 'stick'
            hover 'stick_hovered'
            action Call("restarea_stick")
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
    
    play sound "audio/sounds/unlock.ogg"

    "Finally you open the padlock. Time to rummage through his stuff then."

    hide screen restarea_padlock with dissolve

    "You find some clothes, the usual cleaning hygiene stuff and an unusual amount of medicines of all kind and you think is his notebook?"
    "You notice another thing. A blue flask. You’ve already seen this flask."

    az "The notebook looks interesting. You should take it."
    az "Perhaps he writes his dirty secrets in it? Who knows."

    dk "Watch out for the medicines! Maybe he is telling you everything. Maybe he is dangerous and he can hurt you."

    $ picked_from_the_bag = ""

    menu:
        "Pick up the medicines":
            $ picked_from_the_bag = "medicine"
            "The medicine is what piqued your interest the most."
            "You grab one of them, and sure, it is a antipyretic. Nothing out of the ordinary. Nowadays it is used to treat mild pain."
            "You put it back. It still remains a lot of medicines you have to check out." 
            "Just the fact that he has so many different types medications is concerning."
            "Not everyone has a first aid kit available on them every second."
            "Then you stumble one very interesting. You recognize the brand."
            "You grab it and turn it in every direction in the case you were mistaken. You have already taken some."
            "It’s an antidepressant."
            hl "... What?"
            jump confront_him
        "Pick up the notebook":
            $ picked_from_the_bag = "notebook"
            "The notebook is what piqued your interest the most."
            "You grab it, rotate a little in every direction."
            "It doesn’t look young at all. Even it looks it has been around for ages. The worn—out leather of the cover presents a lot of cuts within it."
            "Some chunks of it are gone. The book is barely holding together. You dare not move it around too much, in fear of it crumpling down."
            "You look for some writing on the front or the back to know if there is any name or something that could indicate you the nature of the notebook."
            "Although, no such luck."
            "You decide to open the book. The inside is no better than the outside."
            "The pages have turned a slight yellow, some page are torn–up, lots of illegible writings, scratchings everywhere. Truly a mess."
            "In all of this you manage to decipher Ammon’s writing and you’re able to read some parts of it."
            "A particular page catches your eye. You start to read it."
            ###TODO:Maybe set it in nvl mode.
            "\"Saturday, 14th September 1975\""
            "\"Dear Diary,\""
            "\"{cps=50}Today Howl ki{nw}\""

            jump confront_him
        "Pick up the flask":
            $ picked_from_the_bag = "flask"
            "You can’t look away from the flask."
            "You cracked opened the bag for that after all."
            "You carefully turn it around, still not able to believe what you have in front of your eyes."
            "You struggle to remember where you have seen it. It itches in the back of your brain. It sets you uncomfortable. You can’t put it down anymore."
            "You have to find where it comes from."
            show eye_lid
            show expression "#000" with blink_reverse
            "So you take a deep breath, close your eyes and rub your temples. You should be able to remember, right?"
            "You clear your mind. You need every inch of your energy. You concentrate on the itching. A centipede crawls around your skull."
            "You breathe in slowly."
            "You breathe out."
            stop music fadeout 1.0
            "You are ready."
            "You plunge your hand deep into your ear and you hit the cage of your brain. You wiggle your claws around, randomly. It’s squishy." 
            "It’s more arduous than you thought. Although you’re more determined than that. It won’t be able to escape your grasp any longer."
            "Finally, you grab one of its legs and you pull without a warning. But it won’t give out easily. It scratches every surfaces it can cling onto. It is desperate."
            "The pain caused by it tore you down from the inside, it is similar to being opened in half and little by little, slowly, very slowly, disemboweled."
            "You writhe out your suffering but you won’t give up. You have to remember."
            "You extract the rampant from your ear and hold it still and keep it in your control. It convulses. You have to keep going."
            "You wrap your fingers around the insect. You want to throw it onto the ground. Its thousand legs wiggles under your skin so much that your stomach begins to churn."
            "But you hold still. You have to."
            "Then you crush it. It doesn’t move anymore. You’ve succeeded."
            "The before hot and squishy insides of the insect turns solid cold. You’re confused. You open your clutch."
            "A beautiful cocoon sits there. You admire it. The centipede morphed."
            "As you get closer of it, a ray of light beams in your eyes and you let it go, to hide your eyes of it."
            "When you reopen them, a beautiful firefly illuminates the your world. You can’t move, mouth agape."
            "And like that, the firefly gently lands."
            show eye_lid
            hide expression "#000" with blink_transition
            play music "audio/music/moment_orange.mp3" fadein 0.5
            hide eye_lid with dissolve
            "Wait. You remember now."
            "Why does Ammon have your Father’s flask."
            jump confront_him

label ammon_padlock_nice_code:
    show screen restarea_padlock(screen_active=False)
    "Nice code."
    "You would use it if this padlock belonged to you. You giggle like a six year–old, it is very funny indeed."

    az "That is very funny actually."

    dk "Don’t listen to them.{w} Just keep looking."

    jump restarea_padlock_loop_local

label ammon_padlock_basic_code:
    show screen restarea_padlock(screen_active=False)
    "Despite inputing the first code come to mind, the padlock doesn’t submit."
    "Did you think that Ammon would be that basic? You are disappointed with yourself that you could think that he was able to do that."
    "Well you should keep searching anyway."
    "And stop inputting basic codes that anyone would crack. He’s smarter that that. That should be something important to him."

    jump restarea_padlock_loop_local

transform custom_zoom:
    zoom 0.2
transform c_zoom:
    zoom 0.05


label restarea_ammon:
    $ renpy.show_screen(current_screen, _layer="master",screen_active=False)

    show ammon at american_shot
    with dissolve

    am "Hi Howly. Do you need anything?"
    am "Have you found what you want?   "

    if checked_padlock >= 1:
        "You notice he has his wallet in his pants on his back pockets."
        "You’re sure it has valuable information about the padlock code. Like his ID with his birthday on it."
        "If you’re willing to steal his wallet..."

    menu:
        "I want to talk about something with you":
            am "What is it?"

            menu ammon_questions:

                "Are you sure you don’t have any water?":
                    hl "I’m thirsty."

                    am "Yes I am sure."

                    hl "Not any tiney bitey one for me?"

                    am "No Howl, no matter how much you ask, the answer will stay the same."
                    am e_disgusted "Do you want me to shake the deep bottom of my bag so you can see I’m not lying?"

                    hl "No..."

                    am e_neutral "So stop asking."

                    "He’s really acting weird. You need to get at the bottom of this."

                "What’s your favourite number" if checked_padlock >= 1:
                    hl "Hey Ammon, do you have a favourite number?"

                    am e_disgusted "... What do you mean?"

                    hl "Like a 4 digits number, you know like 4562? 6512? 2313? Those are cool numbers! Really cool numbers..."

                    am j_noway "Hum no? Why would I have a favourite 4 digits number? This is just stupid?"

                    show ammon j_neutral

                    hl "I don’t know, I do have a favourite 5 digits number! So why not 4 digits?"

                    am "... Which it is..?"

                    hl "Huuuuuh, {cps=5}6... 8...{cps=2} 83.. 1"

                    am right e_smug j_disgusted "Greaaaaaat...."

                    hl "But I also have a favourite 2 digits number!"

                    am j_noway "Yeah I know this one. You don’t have to tell me."

                    az "But it’s so funny..."

                    dk "Stop it."

                    hl "Oh ok..."

                "When’s your birthday?" if checked_padlock >= 1:
                    "What are you doing???"

                    az "Sounds like someone wants to get beaten by Ammon"
                    az "That’s exciting."

                    dk "... Could you not do that?"

                    "Anyway, you won’t say that."
                

                "Hand me your wallet" if checked_padlock >= 1:

                    am e_disgusted j_disgusted "{cps=3}...{/cps}"
                    show ammon j_noway
                    extend " What?"

                    hl "You know, the square thing you have in your back pocket?"
                    hl "It can be used for storing money, cards, id–"

                    am e_neutral "I know what a wallet is."
                    am e_neutral j_neutral "What’s bothering me is why you’re \"asking\" me my wallet."
                    am "You have no use for my wallet."

                    hl "It’s because you didn’t think hard enough."

                    am e_disgusted "..."
                    am "I’m going to ignore what you just said if that’s fine by you."

        
        "I’ve got to something for you." if ga_inventory != []:

            am "What you got?"

            label ammon_item_present:
                $ evidence_needed = True
                call screen inventory
                
                if selected_item.name == "Notebook":

                    hl "Heeeeeeey, Ammmo"

                    "Ammon sighs. He sees what you got in your hands."

                    am "Is it your notebook. It’s true that you like drawing on your part time."
                    am right "Why are you showing me this? I’ve already seen it."

                    hl "Yes I am aware... I feel like you can give me some advice on one of my sketches."

                    am "You don’t need my advice, you are already fine on your own."

                    hl "I don’t know "

                    am "Fiiiiine but this is the last time you’re showing it to me ok?"

                    hl "Ok!"

                    show ammon front e_neutral j_neutral

                    "You hand him the notebook and he opens it, grumpily, slogging through the pages."
                    "You stick to him on his side to better appreciate your little sketches. You’re proud of your silly drawings. You hope him too."
                    "From times to times, you point out some sketch reminding you some memories. Some you made at college. Some made at MJ’s. Some at Ammon’s, etc"
                    show ammon pupils_down j_happy
                    "Despite Ammon’s initial reservations, you see a big grin drawn on his illuminated face."
                    
                    am "Honestly I don’t even know why you’re asking me this, all of these are great."
                    if checked_padlock >= 1:
                        "Meanwhile, you lean into him, trying to grab the wallet in his pocket."
                        "The thing is you’re not really sneaky, discreet or anything."
                        "So you just end up gluing your body onto his, creating a pretty embarrassing situation."
                        show ammon j_disgusted e_disgusted pupils
                        "Ammon raises an eyebrow."

                        
                        am "Um, what are you doing? Is there something wrong?"

                        hl "No– No! I just wanted to get a better look at it that’s all. It was hard to see from where I was."

                        am j_noway "Hum okay?"

                        show ammon j_neutral

                        "You quickly retrieve your hand from his back. No need to make it more awkward."

                        az "You should try to steal more often."
                        dk "Do not encourage him."
                        
                    
                    show ammon right e_neutral j_neutral
                    "Ammon closes the notebook and hands it back to you."
                    am "Happy?"

                    hl "Yes, great thank you!"

                    am front "Well I’m happy than I was able to help."

                elif selected_item.name == "Stick":
                    hl "I have something for you, Ammon!"

                    am e_disgusted "... What?"

                    hl "Quick, go fetch, good dog!"

                    "You throw the stick in the grass behind him. Confused he turns his back to you."
                    "You take the opportunity to slip your hand into his back pocket. You manage to grab onto it."
                    "You quickly retrieve your hand with the wallet."
                    ## TODO: Show item gettings
                    "(You should examine the wallet in your inventory.)"
                    $ ga_inventory.append(ammon_wallet)

                    "After some time, Ammon faces you again even more confused."

                    am "What was that about? What were you expecting me to do?"

                    hl "... Go fetch it?"

                    am e_neutral j_disgusted "... I’m going to politely ignore this."
                
                elif selected_item.name == "Ammon’s Wallet":
                    "Wait!!!!! Don’t do that!!"
                    "Are you a total moron? Put that back."
                
                else:
                    "Nice."
    hide ammon with dissolve
    return

label restarea_trunk:
    $ renpy.show_screen("restareatrunk", _layer="master", screen_active=False)
    $ renpy.transition(dissolve)
    
    pause 0.5
    if not trunk_explored:
        "I open the little trunk in the back of the motorcycle."
        "It was so crammed that I was a bit surprised that we managed to fit everything in that much of a place."
        "Discouraged by this sight, I slump my shoulders——I will never find that water stick "
        $ trunk_explored = True
    return
    
label restarea_bag:
    $ renpy.show_screen(current_screen, _layer="master", screen_active=False)

    if checked_padlock == 0:
        
        "You sneakily get at a close distance of your friend’s bag and you try to open it. You cast some quick looks at Ammon while doing your little crime but he seems distracted, elsewhere."
        "Being discreet, you can’t force the bag to open, so you notice something that preventing you from going any further without making a fuss."

        $ renpy.show_screen("restarea_padlock", screen_active=False)
        $ renpy.transition(dissolve)

        pause 1.0

        "You remember that Ammon is a pretty cautious guy so obviously, he has set a code padlock on his trip belongings. Taking a peek in it will demonstrate harder that you thought."
        "You check the bag if it has a hole or any openings, making you able to bypass his security." 
        "Unfortunately no such luck. No tearing, no manufacturing defects, no hole, nothing." 
        "You shake the bag.{w} It’s filled to the brim."
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
        "{cps=3}...{/cps} Wait. Did you really forget, Ammon’s birthday? You’re utterly ashamed. What a great friend you are. Forgetting his birthday. Great job."
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

label restarea_stick:
    $ renpy.show_screen(current_screen, _layer="master", screen_active=False)
    "Oh a stick."
    "You wonder how it got there."
    "Well might as well take it then. Maybe you could use it with Ammon."
    
    $ got_stick = True
    $ empty_inventory = False
    $ ga_inventory.append(stick)

    return

label restarea_notebook:
    $ renpy.show_screen(current_screen, _layer="master", screen_active=False)
    "Oh here is your beloved notebook you bring with you everywhere."
    "Studies can be really exhausting. If you dedicated all your life, you’d already jumped over a window."
    "So you got a hobby of yours to distract you. When you’re bored at classes in the amphitheater, you take out your notebook and start sketching in them."
    "Over the years, you estimate you got really good at it. You can’t resist showing it to your friends. Julie loves your drawings. She encourages you into an artist career."
    "You also show it a lot to Ammon. He likes what you do but at this point, he’s got fed up that you show it to him every minute."
    "You should show it to him again. You could also keep sketching in it. Bring it with you."
    
    $ ga_inventory.append(notebook)
    # $ check_inventory_empty()
    $ empty_inventory = False
    $ got_notebook = True

    return