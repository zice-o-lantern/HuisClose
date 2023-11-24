label prologue:
    
    # Black scene
    scene black
    pause 1.0
    cl "Honestly{w=0.5}, I cant’t believe you can strangle him that hard."
    cl "Or maybe it’s not that complicated. Maybe I’m just too weak. Perhaps you’re just used to it." 
    cl "You’re lucky. To be able to feel his beating heart. His cold carapace heating up with your hands."
    cl "I know I couldn’t{cps=3}...{/cps} {w=1.0}I think."
    cl "God, why do I feel like this. {w}Why, when, for once, I feel alive, must it be so grim? It makes me sick.{w}\nI’m sick of it.{w} I’m a monster."
    cl "Stuck in a never-ending cycle of boredom, regrets and suffering where Death isn’t an escape to your macabre plays. {w}Did you have to be so hard with me?"
    cl "I hope that, one day, when I’ll come upon the wicked and wretched god that bestowed me of this condition..."
    cl "I’ll be able to writhe him out every strands of life he ever had."
    cl "That I’ll be able to choke you harder than you ever could."
    
    pause 1.

    show clearing with dissolve

    # play music "audio/music/griff.mp3" fadein 1.0 loop
    play audio "sounds/cold_wind.mp3" fadein 2.0 loop
    cl "{w=1.0}At the frontiers of the forest, in the clearing of my misery, I lay there, overwhelmed, breathless. I breathe as much as I can but the hot air burns my throat."
    cl "Then I feel your reassuring presence, I’m reminded that I’m not alone. That you are here with me.{w} So I take deep breaths and finally my thumping torso lowers down to a steady pace."
    cl "Between two relieved exhalations, I look around in search for you and my eyes meet with him, someone I know really well, someone I’ll never forget, someone I wish to forget, a heartless monster."
    cl "I stare deep through him but the glimmering shines in his eyes disappeared long ago{w}, if there ever were any."
    cl "Sometimes I wonder if my life could have gone differently, what I should have done to not end up in a forest, in the middle of the night, beaten up, with this worthless being."
    cl "Had he smiled more at me, had he spoken more to me, had he taken me more in his arms, had he cared more, had he done all of that, perhaps, just perhaps, I would have felt pity."
    cl "Pity when you made him seethe though his teeth, guffing, gurgling, retching."
    cl "Regret when he was pleading to remember all the good times."
    cl "Remorse when he was imploring to you let him go, that he won’t talk what happened tonight."
    cl "But I wouldn’t.{w} I wouldn’t have felt anything for him."
    cl "During those lasting moments, where, with his last string of energy, he clenched my arm, {w=.5}there was nothing."
    cl "No sadness, no pleading, no torment, no anger, no rage, no wrath, no nothing.{w}\nWhile I stood there, I craved for any kind of sign that he was a warm conscious being. Something, just anything"
    cl "No. Just dead eyes. No matter how hard I look, I still see those same dead eyes. Looking at me."
    cl "I wished those weren’t the same eyes. I wish I could say a chill run through me, that sorrow overflown me when all of this unwinded."
    cl "No just dead eyes, for the past years and now forever.{w} Or at least I failed to perceive it. Like a lot of things in my life."
    cl "Every retching, I wished he had cared for me." 
    cl "That he had taken me in his arms, he’d spoken to me more than a dozens of words in my entire life."
    cl "I wish he could smile at me right now."
    cl "Except he can’t. He’ll keep that dead expression."
    cl "All these wishes, answers, aspirations, wishful thinking, buried with him."
    cl "I guess I’ll never know."

    pause 1.0

    cl"The cooling breeze strokes down my long ears , the surnatural howling of the wind cools me down but my throat still burns."
    cl "I try to make it go away but the thousands of needles stuffed down protest.{w}\nI need water."
    cl "So I difficultly make my way towards him and I search for something to soothe my thirst."
    cl "I am able to find some flask. I uncork it and stuff it down my dirty throat so the lukewarm water can flow."
    cl "With every gulp, it wash down a bit more."
    cl "That mucus obstruating my throat."
    cl "That warm hot itch that resided there."
    cl "That distress that had built up over the years."
    cl "Those regrets that I didn’t do good enough for him."
    cl "That guiltiness that I failed him, that I am not worthy."
    cl "That shame that I wasn’t good enough for him."
    cl "The only thing remaining is the overbearing numbness of my life."
    cl "I need more water."

    pause 0.5

    cl "I look, in the surroundings and not far from me, there stands a pond five meters away from me."
    cl "I crawled desesperately to it and chug down the water."
    cl "But even my filthy soul can’t take this foul water and I regurgitate everything in the pond."
    cl "Drool hanging from my muzzle, Tears streaming down my face, I collapse in the grass, drained of all my energy."
    cl "My vision stays stuck on the middle of this pond."
    cl "A little hill with a hundred of fireflies projects over me, offering me a spectacle that I’d never forget. Something I thought I would never see."
    cl "A beacon of longing light in the all–surrounding crushing darkness of the night that gets me alive."
    cl "It would almost make me forget the towering tree at the top of the hill, projecting its shadow over me, watching me. {w} Judging me."
    cl "Wait{w=0.5}, that’s not the tree who’s judging me..."
    
    pause 1.0
    
    cl "Hey I have a question."
    cl "The one watching me. The one judging me."
    cl "Yes. You.{w} Don't pretend You're not concerned."
    cl "Has that satisfied You? Did You like what you just did?"

    menu:
        "I did":
            jump i_did
        "I did not":
            jump i_did
    label i_did:
        cl "That doesn’t surprise me. I sure did.\n{w}I’ll do it again any day."

    pause 2.0

    cl "Hey I have another question.{w} Well it's more complex that that."
    cl "Do You think Apathy is a crime? Do you think my Boredom would turn into a tragedy?"
    cl "Do You think that the numbness I feel everyday in my life could cause problems for the people that I love and love me?"
    cl "Do You think that my inactivity, my tendency to not act, to endure, to stay where I am, where I should be could lead me to hurt the people around me?"

    menu:
        "Yes":
            jump dont_answer
        "No":
            jump dont_answer
    
    label dont_answer:
        cl "Wait, don’t say anything."
        cl "I think I already know the answer."

    pause 1.0
    show clearing:
        alpha 1.0
        ease 30 alpha 0.05

    play music "audio/music/build_up.mp3" fadein 30 loop

    cl "Hey You know what? Perhaps he loved me. Perhaps he never did. But he won’t be an issue anymore. He can’t hurt us anymore."
    cl "Perhaps You’re responsible for what happened but I am just as guilty as You."
    cl "Let’s just put all that behind us."

    show eyes:
        alpha 0.0
        xalign 0.5
        yalign 0.5
        easein 30 alpha 1.0
    
    cl "The time where he brought me to the fun fair and that he got me that sweet lollipop."
    cl "He would often crack a smile when he crossed a word on his daily newspapers."
    cl "He’d laugh anytime I grimaced."
    cl "{w=1.0}{cps=35}The time where he left me."
    cl "Let’s forget all of that."
    cl "Perhaps he truly loved me. but I don’t care."
    cl "Maybe I am a monster. Maybe I shouldn’t feel like that. Maybe I am like that because of you{w}, but I couldn’t care any less."
    cl "In the end I liked it. {w}In the end, I enjoyed it with every inch of my being. And also..."
    cl "Because You love the way I am, You love who I am. You love me"
    cl "And I love You."

    pause 1.0

    cl "Perhaps, more than I thought"
    stop music
    stop sound
    extend ", I need You."
    scene black
    scene ruralRoad with Fade(0.5, 4.0, .5)
    # play sound 'audio/sounds/car_white_noise.ogg' loop
    jump little_road

label little_road:
    play music "audio/music/The Beatles - Here Comes The Sun (2019 Mix).mp3" fadein 5.0 loop


    "You wake up from your reverie at the cold hands of someone grabbing your shoulder."
    hl "Aaaaaah!"

    show ammon with dissolve
    
    am "Hey were you sleeping?"
    
    hl "Huh—whuu?"
    
    am "Yes you were. Sorry I had to stop and wake you."
    am right "I was starting to feel your head on top of my back and you wouldn’t budge and that didn’t help me drive."

    hl "Oh... Sorry Ammon I didn’t mean to."

    am e_smug j_noway "No worries Howl. I think I’ll stop next stop, I’m starting to get weary too."
    # "You wake up at the hum of the radio, a bit shaken up, with drool staining your helmet visor — Fortunately there’s not enough to hide your vision."
    
    hide ammon
    with dissolve
    
    "You rub your eyes as Ammon restarts the bike and goes on its way."
    "Well you would rub your eyes if it weren't for the fact that you're wearing an helmet."
    "So you opt to blink your eyes until the numbing grain salts flow out of your eyelids."
    "Although, as much as you want, the sleepiness is still quite there. At the shores, coming in waves."
    "You might be sleepy but the rock song blasting out of the radio."
    "You find it..."

    $ radio_on = True

    menu:
        "Annoying":
            az "Turn that off."
            
            "Compelled by your inner self, you lean to Ammon and tap him on the shoulder; you don't know if he will listen to you but you might still ask it."
            
            show ammon right
            
            "Ammon begrudgingly turns his head toward you, visibly annoyed. Perhaps not the better idea."
            
            dk "It was expected."
            
            hl "Hey could you turn the radio off?"
            
            am "... why?"
            
            menu:
                "It gives me an headache.":
                    am "Well it didnt gave me one."
                    
                    "You grip your tighs. Is he that inconsiderate?"
                    
                    hl "Please, pretty please... Traveling for me is already hard enough as it is."
                    
                    "You lock eyes with Ammon. In spite of you, he is already probing inside you with those yellow eyes."
                    "It's a tendency of his so you maintain the contact as always."
                    "At some point he releases you, sighs and leans to the radio."
                    
                    am "Hmpf, you're right, I'll turn the radio off."
                    
                    hl "Thanks Ammon."
                    
                    am "Don't thank me."
                    
                    hide ammon
                    
                    "He grumbles, turns the radio off and sets back to look at the horizon."
                    "Relieved, your muscles relax and you let the hum of the bike fills your ears. You didn't have a headache, but it might as well give you if that kept going on."
                    
                    az "Good job"
                    
                    $ radio_on = False
                    $ azzy_score += 1
                
                "I don't like it.":
                    
                    "Ammon stares at you in disbelief. His furrowed eyebrows lets you know that it doesn't really bother him."
                    
                    am "So what? I like it."
                    
                    hl "Oh come on ! Can't you make an effort?"
                    
                    am "For what? It's my bike so it's my radio."
                    am "I get to pick the song I want. Deal with it."
                    
                    "He cuts short to the discussion and sets back to driving and looking at the horizon."
                    
                    dk "What a prick."
                    
                    $ derek_score += 1

                    "You grumble back to a slouched posture. Nothing you can do about it, he's the one driving after all." 
                   
                   
        "Incredible":
            "You lay down on the bike as the loud drums fill your world."
            "Your bang your head up and down to the rythm. With it, your finger taps on the frame."
            "As the trees run up to you, you watch them scale down behind you, toward the horizon."
            "The dying light of the sun highlights the silhouette of the dog with a helmet in front of you. He projects a shadow over you."
            "You don't mind. You like the cold and you want to be bitten by the glacial air."
            "The cold, the music and the roaring of the engine make your eyelids more and more heavy."
            "Maybe you can try to fall asleep without Ammon noticing?"
            
            menu:
                "Try to sleep":
                    "You decide that it's the best moment to take a nap. Surely he won't notice."
                    
                    ## TODO: Replace with eyelids animation
                    show black 
                    with dissolve
                    
                    "You let your tired eyelids be pulled by the unforgiving gravity and you doze off."
                    "And little by little your mind ascends to Wonderland."
                    "Away from the cold, away from the shadows, away from your ennui...{w} Away from everything"
                
                "Stay awake":
                    "You decide that it's better to stay awake. You don't know but it could be really dangerous to fall asleep on a bike."
                    "A wrong move and you fall head first on the asphalt at full speed."
                    "The thought of it strangely infuses life into you and you find the idea of sleeping not so appealing anymore."

                    am "Still dozing off?."

                    hl "Hmm? um, yeah ahah."

                    am "Ok..."

                    "An uncomfortable silence follows. Ammon looks for something to say but is lost for words."
                    "More the time passes, more the threat of falling off the bike doesn't bother you anymore. You have to sleep."

    am "Hey Howl? Don't you think it's nice around here?"
    
    hide black with dissolve
    show ammon
    

    "Ammon, interrupting to your train of thought, gestures his head towards the scenery, that, funny enough, you've been looking at for some time."
    
    menu:
        "I do think so":
            hl "I haven't had the opportunity to look at them lately."
            
            am "... Because of your studies?"
            
            hl "Pretty much."
            
            "You sigh. You rub your eyes. This subject flashes those long nights where you roll your head on exasperating papers."
            "You wish you could do otherwise and throw all of your lessons in the trash bin."
            
            dk "But you can't."
            
            am "You should get out of your house sometime..."
            
        "It isn't new":
            hl "I mean, I could see the same landscapes from my bedroom at home. I would often observe them as a child."
            
            ## TODO: Redo smug front expression
            am right e_smug "Didn't you have anything better to do?"
            
            "You lower your head meekly and consider carefully the question."
            "The thing is you can't remember you had anything better to do and that concerns you."
            "Ammon, picking up your long silence as an answer, scoffs and roll his eyes before smiling bitterly."
            
            ## TODO: Add happy jaw right
            am "You really are a dork."
            
            "You are suprised by his reaction and prepare yourself to argue back but..."
            
            dk "You are."
    
    hl "Wait a minute, I thought you weren't the type of guy that enjoys sceneries!" 
    hl "You just looked at me, confused, whenever I'd stop for looking landscapes."
    
    am right e_smug j_disgusted "This is because that would happen anywhere, anytime, this was annoying at some point."
    am "If I could have, I would have put you on leash and drag your ass around so you could stop fanwning on everything."
    
    hl "Well you couldn't."

    show ammon front e_neutral

    "Ammon hears your tone of defiance and even from behind his terrifying aura oozes from his shoulders, shivering. Might have struck a nerve."

    am "If I were you, I wouldn't push my luck."

    az "You absolutely should."
    
    "He looks down, melancholically, at his hands, surely reminescing our little outings together some time ago."
    
    az "You really enjoyed them{w}, Hehe."

    dk "Such a shame it had come to an end."
    
    am j_neutral "But yeah you are right, I don't really care. I was just trying to make you stay awake, you know."
    
    hl "Really?"
    
    am "Yeah pretty much. I don't want you to drool all over onto my new jacket."

    hl "But I wear an helmet."
    
    am "Then I don't want you to drown in your own drool."

    "A bit crude, he's always been like that ; you aren't fazed by his harshness though you aren't used to it anymore."
    "Even in your own usual moodiness, he would find ways to even lower it. A true pain in the neck."
    
    if azzy_score >= 1:
        az "But you like it."
    
    "However with all those years spent with him, you've come to understand his language, what he means behind his unpleasant comments, his bitter venom."
    "He doesn't want you to fall off the bike."
    "In the end, he bears a wall of bitterness and acerbity but he's kind of heart."
    "At least that's what you think."
    "It helps you teasing him."

    hl "Well I guess I'll just remove my helmet so I won't drown then. And stain a bit your jacket but I'm sure you don't mind it."

    am right "Urgh stop it. That's disgusting. And keep your helmet that's not the point."

    hl "What's the point then?"

    ## TODO: Fix an issue with this expression below
    #am front e_angry j_growl "Just stay awake !"
    am front e_neutral j_neutral "Just stay awake !"

    hl "Alright, alright, don't get mad, jeez."
    hl "... But I'm still sleepy."

    am "Do what you want but I don't want to feel your head on my back, it's cold."

    "Your sleepiness starts to invade your senses and they start to numb. If you don't do something quick, you'll succumb to nothingness."

    az "Don't try to fight it. Think of his big bulky back as a softy pillow. Ignore Ammon's threats, that's what you want anyway."
    
    dk "Noooooo don't! {w}If you do that you'll only anger him more."

    az "That's what's been said. You want that anyway."

    dk "Ask him to continue to talk to you, to keep you awake. Also, maybe you'll be able to catch up what you missed with him and the old good times."

    menu:
        "Sleep on his back":
            jump sleep_on_his_back
        "Ask him about what he's been doing":
            jump talk_with_ammon

label talk_with_ammon:
    $ derek_score += 1
    hl "Alright if you want me to keep awake, I'll stay awake."
    
    am "Great, then"
    
    hl "So, um Ammon..."

    "He turns his head inquisitively."

    am "Hum yes?"
    
    hl "How's life recently? Been able to scape up by?"

    "For a reason unknown to you, Ammon giggles under his helmet."

    hl "What's so funny about what I said?"

    am "Hmpf, nothing in particular."
    
    "He looks in front of him, reminiscing about what you said."

    am "So do you want since High School or since I left?"

    "You ponder the question. Yes that is true that he stayed at your village for some years before leaving."
    "Yet you have no recollection of this moment in your life. It worries you a bit as this is the first time you notice this blank in your memories."
    
    "The dog with the helmet takes your silence as an answer and sighs."

    am "No worries, I figured you wouldn't want me to talk about after High School."
    
    "The sentence he just said disturbs you."
    "Why can't you remember what happened back then after High School."
    "You can't pinpoint an event that could lead this sort of amnesia."
    "But you're not amnesiac, right? At this point, you thought you remembered everything pretty much, but your mind begins to crumble the more you think about it."
    dk "Let's just forget."

    menu:
        "Ask him after High School":
            hl "Um, actually couid you start since high school?"
            
            am "Alright if you want to".
            am "It's actually easier for me, but don't worry, I will go over it the fastest I can."
        "Stay silent":
            $ derek_score += 1
            "You don't want to find out about this anymore."
            "Some things are better left forgotten."
            am "Well it's easier to tell what happened since High School."
            am "But don't worry I will go over it the fastest I can."

    am "Alright, when we graduated, we had to choose a work career and the studies for it."
    am "You know, I acted big and tough then, I was not that sure about it."
    am "Nothing was really fitting me so I just took the subject I had the best grades at."
    am "I guess at the time I was very good at Physics. So I went to a Technical College. It was the one the nearer to our village."
    am "The thing is{cps=3}...{/cps}{w} I hated it. It was one thing to be good at Physics but making it my career. I really couldn't bear it."
    am "... So I dropped out of College. For some months, almost a year, I brooded a lot. What was I good at?"
    am "I wanted to tell you that back then. But..."
    
    "Ammon looks up the sky."
    
    am "You were a bit out there. I couldn't get a hold onto you..."

    "You fidget yourself. You try again to unravel this moment of your life. No dice."

    am "Anyway, I was a bit lost. But then..."
    am "But then, I remembered that I always had a thing for History and Ancient History at that."
    am "I was average at best at school so I couldn't think I could study it."
    am "But I passed the test at La Sorbonnes and got in it."
    am "So yeah, I moved out to Paris for some time. I needed it."
    am "It could sound like I am justifying myself but you asked so here it is. That's why you haven't seen me for long I guess."

    hl "I see. Well I never blamed you for leaving. The village is a bit of a shithole."

    "You giggle softly. Sure it was a \"shithole\" but you had some good time, nonetheless"

    am "By the way, do you remember the time where we got lost in the forest? It was frightening at first."
    am "We decided to trek yet again in the forest near the village. Only this time you asked me that we go beyond further the usual path."
    am "I was bored at the time, I didn't see the issue. Thinking back to it, it was not really a good idea." 
    am "Even more in our case, it was a pretty fucking shitty idea."
    am "But you wanted so much to go astray from your usual life, I guess at the time."
    am "Well the night came fast and we were stranded in the forest without any direction or signs."
    am "I was relying on your night vision but you couldn't really find the way back even with your ability. You were really lost that day."
    am "But I don't really blame you. It's hard to locate yourself when you're surrounded by trees."
    am "You know this is the night where we find our favorite spot."
    am "Honestly, it came out of nowhere. We never thought this could be so close to us."
    am "We loved this clearing, I don't even know how you found it. For once, I can thank your night vision."
    am "We'd always lay down under the tree on the hill. Somtimes we'd take some snacks and all. We even brought MJ times to times."
    am "It became our usual hangout, you know."
    
    hl "{cps=3}...{/cps} Yeah I remember now."

    am "Do you remember what happened at the hill? Under the tree?"

    "Ammon looks at you expectantly, as if he's trying to jog up a memory for you. You can feel his stare through the helmet."
    "Unfortunately, you don't understand what he's trying to refer to."
    
    hl "Hum no sorry I only have bits here and there about. Nothing in particular."

    am "Oh alright, well don't worry about it, it's nothing important."

    hl "Really?"

    am "Yeah it's just... There I could say and do everything with both of you."
    am "I just wanted to laugh at the goofy stuff I've done there... ahah."

    if azzy_score >= 1:
        az "He's lying. He wanted you to remember something you've done with him."
        az "Such a shame you've forgotten."
    else if derek_score >= 1:
        dk "He looks so sad."
        dk "I think you have disappointed him."
        dk "Such a shame you can't remember what happened at the tree."
    
    am "Hey by the way, good job for staying awake! I didn't have to wake you up again... yet."

    hl "Huh thanks..."

    am "Looks like we're on the point of getting to the rest area."

    hl "Oh right."

    am "Ready to take a break, you sleepyhead?"

    hl "Alright..."

    "Thus, the motorbike takes the next exit for your next stop..."


    stop music
    stop sound

    scene parkingLot
    with fade
    play sound "audio/sounds/bird_chirping.ogg" loop
    
    "The moto steers over on the parking lot. The wind has taken his liking over his liking over a blade of grass and a can of soda."
    # "With a lazy eye, you follow those lost souls. I hope for them that they'll find a place to rest. The trash passes in front of some restrooms, deserted of all life and not very well maintained." 
    # "The leaves fly, of trees that has seen more you could ever account for them into the breeze then onto the vast lands of grass."
    "You clumsily stumble out of motorcycle and try to get rid of my helmet in vain. Your ears are stuck in it and the motivation to get them ebb away to the shores of your mind."

    jump rest_area_1


label sleep_on_his_back:
    $ azzy_score += 1

    scene black with dissolve

    "You can't resist anymore."
    "You can't help but let your head fall first into the soft pilloz in front of you."
    "Loud screams and whining fill your ears but it doesnt bother you a bit. You are dragged into the abbyss of your sleep."
    "The overwhelming void of your mind lulls you up and fragments of your life flashes through you; You don't care, you're too frail to care"
    "You just wish to be alone and the comforting void invites you to."
    ## TODO: Add an impact sound
    "However the smell of lavander gets hold of your nose and you tempted to open again your eyes."
    "The odor becomes overbearring but you want to be left alone."
    "So you fight and ponder for a long time. You ought to discover where this comes from, it reminds you of the past, something you have forgotten."
    "This perfume reminds you of some of your most treasured memories and is almost divine to you."
    "At last, you give in and, entranced by this divine smell; you open your eyes slowly and the sun light gently penetrates your eyes."
    "Blinded at first, you take some time to get used to the sudden change of luminosity. How is it possible?"
    "It was only dusk one minute ago, it couldn't be so bright."
    "A large patch of grass expands in front of you. The trees swings to the wind. The birds chirp happily. You notice that you are on a hill."
    "You lay down under a big tree. You should be hot with the burning sun but fortunately you are covered by the tree's shadow."
    "You look down the hill and you can see some water surrounding it. You can only think it's surely a pond. No flowers in sight."
    "Wait, where's comming the smell of lavender from then?"

    am "Oh you're awake Hurle?"

    "You take a pause and notice Ammon. But it doesn't last long"
    "You still search for the smell. It drives you mad."
    "You crawl toward Ammon and then you finally understand."
    
    am "So I take you like my new perfume?"
    
    "On four legs over Ammon's torso sniffing, you sit back to your spot."

    am "Alright..."
    
    "Ammon scratches his head."
    
    am "So how's school recently? Been able to scrape up by?"

    "You nod your head silently. You're not feeling much like talking right now. The smell is all that you can think of."

    am "Hmpf, why am I even asking this? You're kind of a genius, aren't you?"

    "At this statement, you feel compelled to retort back, not let him say that."
    "Sure you have some aptitudes in the logical-mathematical intellingence."
    "But that doesn't mean that you got easy in life. You know it more than anybody."
    "So you won't let him say that."
    "However, your muzzle opened, no sound leaves off of it."
    "You raise your hand to your throat. Weird. As long as your mouth is opened, your throat tightens."
    "You start to hyperventilate, or you try, but you can't even have that. You heave as much as you can but no air comes out. Nothing."
    "Meanwhile, Ammon looks at you with a compassionate smile."
    "He snickers."

    am "Ahah. You're so silly, Hurle"

    "You reach out your hand toward him, imploring to help you, the panic rising into your eyes."
    "But he continues to gently smile at you."

    am "Don't you think it's ironic? {w}For a boy named Hurle, you're not even able to howl."
    am "Go on, tell me what you want to say, don't be afraid, tell me what's on your mind."
    am "Howl me what's in your heart."

    "As much as you want to comply with what is saying Ammon, you still can't breathe."
    "Your world starts to fill with black as the lack of air starts to be felt. You're choking right now, aren't you ?"
    "While your mind wander elsewehre, your last sight is the one of the smiing box watching you suffer."
    "And Lavender."

    show black with dissolve

    scene black

    show parkingLot
    with dissolve

    "You wake up at the smell of Lavender."
    
    show ammon
    with dissolve
    
    "You don't need to search for long the culprit as he is above you"
    "Laid on the grass, Ammon blocks the light from reaching, presenting as a imposing silhouette"
    
    am "Wake up, dummy"

    "Laid on the grass, you grumble, just out from your stupor and you sit difficultly."

    hl "Uuuurgh, what happened?"

    am "You can't remember??"

    "Ammon sighs out of exasperation."

    am "You fell asleep on the bike."
    am "And I could scream and wiggle all I want, you wouldn't budge."
    am "So I drove off to the next rest area I could find, in order to get you off of me."
    
    "Well that doesn't explain why you're laid in the grass."

    hl "Then why am I not on the bike? Did I magically appear here when you turned off the engine?"

    am "Well not quite..."

    "You stare at him with doubt. With every word he says, you begin having issues trusting his version of the events."

    am "When I went up to you to wake you up, I have maybe shaked you too much and that made you fell out of the bike..."
    am "... In the grass."

    hl "Okay, understood. Just help me up please?"

    "You reach out your hand to him."
    "With unease, he grabs your hand and put you on your two paws."

    "Drool all over your face; Sleeping with a helmet isn't a good idea."
    "Clumsily you try to take off the helmet."

    jump rest_area_1


    
label rest_area_1:
    # "Eventually, Ammon, who had stripped away his helmet since a long time ago, notices you."

    am "Do you want some help? You look like you're having a hard time."

    menu let_ammon_help_you:
        "Please, yes, can you help?":
            $ ammon_score += 1 
            "Usually, it would’ve been the time where you deflect any sort of assistance and where after some trepident events, you would either succed the task or yield into submission. So you lower your head and present it to Ammon."
            hl "Alright, go on."
            "You didn’t have the strength to struggle nor protest like the proud man you are so you give in to Ammon. His bulky hands grab the base of your helmet and his nails brush the tip of your neck hair, surprising you, not liking being touched."
            "But him being the one doing it doesn't mind you interestingly. Nonetheless, he gets troubles too to rid your feline head of the helmet. He pulls harder and harder on you and the pain gradually increases and you don't see the end of it."
            hl "Oh my god, Ammon, be softer!! Less harder! You're going to hurt me!"
            
            am "If you weren't so such tight!"
            
            hl "What did you say?!"

            am "I said, if you didn't have a such tight helmet... And such a big head!"
            
            hl "You can talk with your long big snout!"
            
            am "If you don't stop talking right now, I'll pull your helmet off in any way possible, with or without your head."
            
            hl "Stop talking with your long snout and just do what you just said, we'll both be better off!"
            
            "For a moment Ammon still struggles to remove your helmet. The pain is really insufferable and you both pull like idiots trying to pull out Excalibur." 
            "You yell and he apologises hoarsely."
            "At some point, you feel with your united combined effort, the helmet is ready to give in. Suddenly there's a pop and you fly out of the helmet on the grass rolling for a considerate amount of time."
            "When your frenetic charge comes to stop, you cough out the dirt and the blades of grasses caught in your mouth." 
            "You shake up your head so your blood flows back in it. When you come back to your senses, you are met with a laughing dog unable to stop."
            "His piercing laughter overwhelm your space and you get red of embarrassement irresistibly, despite you. You clutch the grass."
            menu:
                "Throw some grass at him.":
                    "You pluck out some grass and you throw some at him to make him shut its long snout trap that serves him as a mouth."
                    hl "Fucking moron !! I told you you shouldn't pull that hard! I'm all scratched and dirty now. I hate you, you hear me??"
            
                    "Ammon wipes out his tears of laughter and approches, triumphing, over you. His wicked smile pierces his helmet as he hands you your helmet and reach a hand to you."
        
                    am "Okay you crykitten, keep whining all you want. But if you stay on the ground, you won't get anywhere, will you?"
                
                "Stay calm": 
                    "You clutch the grass harder and harder. You want to unleash your rage on him, to throw grass and dirt at him."
                    "But you can't. You're too weak for that. He'd only laugh at you harder. {w}You hate him."
            
            
      
            "You grit your teeth as you clutch his hand. He carries you off the ground that you find yourself levitating. You often forget his undog force and that comforts as you can trust your dear friend."
        
        "I can do it on my own, no thanks":
            "You don't need the help of that prick."
            hl "I don't need your help. I can deal with it on my own."
            
            am "Alright... Suit yourself."
            
            "You don't wait for his signal."
            "However something's wrong: It really is stuck. No matter how much you pull or the angle you use, your ears won't budge so it won't come off."
            "As you panic, you wiggle out in every directions possible, almost rushing in the motorcycle or Ammon."
     
            am "Are you sure you don't need any help? you sure look like so."

            hl "I'm fine! I don't need your help or anyone's help!"
            
            am "Um, ok... I guess?"

            "In your wrestle against the helmet, you keep spinning around until you get nauseated from the all over experience."
            "By a thread of luck or misfortune, you manage to get rid of your helmet. However with all your dances and twirling, you lost sense of directions and you lose balance making you fall into the grass."
            "When your frenetic charge comes to stop, you cough out the dirt and the blades of grasses caught in your mouth. When you come back to your senses, you are met with a laughing dog unable to stop."
        
            am "Deserved it, jackass."
      
            hl "What did you say?"
 
            am "You heard. Just get up. You won't get anywhere like this."
            
            "You get up. You rub your head out of pain and you can feel a nasty bump on your head. Maybe you should've asked for Ammon."

    "You scramble out of the grass and rush toward the rear mirror of the motorcycle to watch your face and check any scratches."
    ## TODO: Illustration of gap looking in the mirror
    "As you look into it, you behold a scrawny cat in his twenties, with a medium stature, not delighted and grumpy." 
    "You sigh. You wouldn't be friend with him."
    dk "Never forget, it's you and will always be you."
    "Unfortunately you were not so lucky and your usual pure white–crystal hair face is tainted by some dirt and injuries." 
    "You lament yourself on your state. Other than your scratches, you don't look so good either."
    "Your tired eyes look like you haven't slept for a week—and you might not have—as the dark rings under your eyes draw themselves on a too much big surface." 
    "You scrub them, however they remain unchanged and any try to make it go make clear that they won't go away."
    "You check your red eye, swollen by the fatigue, you prod the inferior eyelid at it." 
    "The capillaries running through your green jade eyes sclera pulse a like a living entity."
    
    "You are annoyed at them and even more you are scared of them."
    "The next moment, they disappear and you are then alone with your no better thoughts, still uncomfortable that someone might be watching you." 
    cl "Just a wrong step and you're done for. Don't ever misstep, you hear me? Not ever. {w}You are a deviant and you know it."

    am "Hum Gap, what are you looking at? You've been staring for quite some time now."
   
    "Ammon tilts his head from the other side of the motorcycle to look at your reflection in the mirror"

    am "You've got to stop looking at yourself like that. You look like you are on the brink of murdering someone."

    "With this disturbing statement, Ammon goes on to get rid of his helmet." 
    "Realising he has got some points, you cut off your sight from your other you and you look at him inquisitively, wondering where he might have had this idea."
    "You weren't that unhinged, were you?"
    
    hl "Do you need help with your helmet, Ammon? You may use some given.. your head shape..."
    
    am "It's alright, pal. I can deal with it on my own. I'm used to."

    "The cocky dog removes his helmet elegantly without any issues nor events whatsoever." 
    "He wiggles his head finally free from his protective plastic jail." 
    "What a show–off. But a good show–off."
    "The thing to catch your attention within him is his eyes. His priceless golden eyes shining more than any sun you've seen." 
    "You find yourself mesmerising in these luxurious jewels." 
    "These piercing cruel eyes look through your soul and you are read like a dirty open book." 
    "At any time, if he feels like so, he can pick an excerpt from it and study it attentively to your expense" 
    dk "He can guess who you are from it alone."
    "He is objectively better than you in every domain possible."
    "He is handsome, he is charming, he is charismatic, he has a sense a sense of style you try to copy but you have ultimately not." 
    "You may want to say that to him but he’d say that you’re being too emotional so you always shut yourself."
    "He often wears biker suits because that fits his life style he told you." 
    "He also wears golden face piercing. It really amplifies his rebel attitude."
    "You wish you could be as extravagant as him and take crazy risks" 
    "You are not as bold as him so you keep to your little classic shirt with your tie."
    "You hope, one day, you’ll break the ties that roots you to your plain life and take the chance to be as free, as liveful as liberated as him."
    
    "Despite your fixation on Ammon, you come to notice the deserted rest area you just stop in." 
    "Dead leaves piled up on the border of the roads, signaling the fall has come and taken his toll on Nature." 
    "The brownish orangey landscape contrasted with the bright green of Summer." 
    "The mourning trees stand there, waiting for better times"
    "Sooner or later, even their melancholic colours will be replaced by scarcerd branches and the glacial white tucking them to their warm sleep." 
    "Tall grasses remain nonetheless undefeated by the time passing. Some sunflowers still resist, searching for their lead."
    "The usual restrooms stick out of the surrounding nature. They are not at all well–maintained..."
    "A tall metallic structure stand out with all this misery, a shine, a beacon of what lies ahead. You have seen them a handful of times. A phone booth." 
    "You rarely see phone boothes out in city so to find one in a rest area is even more incredible. Technology goes fast, you think, nowadays."

    hl "Hey look, Ammon! They have a phone booth around here. Isn’t that wonderful?"

    am "Huh? Oh yeah... sure."

    "Ammon doesn’t seem very interested in these incredible structure. You lower your gaze and notice his hand pressing his crotch, clutching his fist at a gradually faster pace." 
    "This explains his lack of interest, you guess."

    am "So you’re going to use it, right? Who you gonna call?"

    "You mull over the question, even though you don’t know a lot of people who owns a phone at home. Only two persons comes to mind."

    am "Is it gonna be you mom?.. Or... MJ?"

    "He says the last word with a lot of emphasis as it was only obvious from both of them you’re going to pick." 
    "A annoyed tone comes with and that disturbs you, as Ammon being genuinely annoyed is rare."

    hl "Yes I’m going to call her."

    am "Ok, suit yourself."
    am "I’m going to pee. Wait for me and don’t go far ok?"

    "Ammon quicly deflects the topic of discussion and comes back to the pressing matter at hand." 
    "You watch him waddling in place, jumping like a late hare and you find yourself hard to not comply with his request."

    hl "Ok, don’t lose yourself on the way!"

    am "Don’t worry! See ya!"

    "As soon as he finishes his sentence, you see him sprint towards the forsaken restroom and you chuckle." 
    "As he disappears from your vision, you are now alone... Not quite... There's the phone booth. It attracts, implore you to come."
    "So you stare at it longingly. For a moment, you can only stand there, in front of the cubicle, as your eyes runs through it, intrigued."


    
    jump phone_booth

label phone_booth: 
    stop music fadeout 0.5
    scene phone_booth with fade

    play music "audio/music/night_sky.mp3" fadein 1.0 loop

    "You jog towards the deserted phone booth. You hurry yourself to talk to her, to get it done." 
    "Dragging yourself the door, you grab with a grand difficulty the handle, not being able to find the motivation to penetrate into the dark cubicle."
    "You turn an inconsiderate amount of times the handle, at last, the dore opens when you shove into it." 
    "You mustn’t be in the right mindset to not notice that pulling a thousand times a door will not work on the 1001th time."
    "But you couldn’t give more than a care, your gloominess crashing down at its lowest as you finally set paw in the somber void, pierced by rays of declining sunlight."
    "Blind, by the low current luminosity of the place, you put some time to even find the phone."
    "On the phone box, on a little sign at the bottom of it, it is written \"10 francs for 10 minutes!\" You think the sign bargains a fair deal to you."
    "You get a coin from your pocket and you slid it into the coin slot. Soon after, the phone screen lits up awaiting your input." 
    "You observe carefully as some featuers disturb you: they never had a screen before."
    "With slothness, you press the phone number on the keypad, with petite–size buttons but you manage to input it on your first try."
    "You pick up the phone and wait for the ringing to come and let it resonate in the booth soothing the emptiness of the place. You liked the music tone and you daydream a bit of time."
    "You’ve wandered in your head for a undefinite span of time, the ringing going on and on, the sound receding away in the dark void."
    "You wonder why she puts this much amount of time to respond. Must it be the hour? Or is she’s not home right now? Maybe she has got an extended work shift and wasn’t still able to come this evening."
    "Whatever the reason, it has to be a valid one. You mull over it a bit. She wouldn’t ignore you, would she? Perhaps she is ignoring you and is looking at the phone ringing right now."
    "Suddenly a click travels from the other side of the line as to prove you wrong. You hear an inquisitve, quite sly, feminine voice answering the call."
    
    "???" "... Hello, who is it?"
    
    hl "Marie–Jil, it’s me, Hurle!"
    
    mj "Howly! It’s really you! I’ve waited for your call all day long, you know that?."

    "A deep sigh escapes of her long mouth, relieved to hear your voice."

    mj "Have you reached the hotel, yet?"

    hl "No, not yet."

    mj "You’re still on the road? How did you do to contact me then?"

    hl "Well apparently, they started to install phone booths on rest areas over the roads. Isn’t it amazing?" 
    hl "Some day, I’ll be able to find phone booths everywhere and to call you anytime I want!"
    hl "Imagine all of the possibilities! One day, maybe, we’ll truly never be apart. This is really wonderful! Technology is going so fast! Everything is going so fast!"
    
    "For a very enigmatic reason, your passion for latest high-tech overhauled your usual gloominess." 
    "You find yourself very eager to indulge yourself in this pit of wonders, dreaming for the future of all living beings."

    hl "Imagine for a second, how the americans reached the moon, {cps=120.0}how we will in the future be able to travel to space {cps=150.0}and also how we will be able to even eat without opening the mouth."
    hl "{cps=200}don’tyouthinkit’sfantasticsometimesyouthinkwowtechnolgyandallh\nowrapiditwillreachveryhighstandads??it’sreallywonderfulwhenyouthinkaboutitIwanttoneverdietowitnessthis{nw}"

    "You couldn’t hold my excitation anymore. The words leaving from your mouth were forming before your brain could even process the information you were spilling out at her. Your speaking functions were not functioning anymore."

    mj "Howl, Calm down! Calm down, for god's sake. You’re going to choke on your own words. Take a breath ok? Breathe with me, alright? At the count of three you’ll breathe out, ok?"

    "You follow Marie—Jil’s instructions and soon enough, you manage to calm yourself down and in the end you are able to talk at steady pace."
    "Once calmed down, your lungs stops contorting and burning the air within is able to bring you tranquility to you. Her voice helps you catch back and stand on your two paws."
    "You’re finally able to talk normally now."

    hl "Ahah, sorry, MJ. It’s been so long that I haven’t talked to you! It’s been like what? a week?"

    mj "You’ve talked to me this morning, Honey. But I don’t mind, I love it when you get all worked up over me, my little kitten."
    mj "I didn’t think that you’ll be missing me so much. You’ll only stay 3 day over there and you’re already panting your insides out"
    mj "You didn't even reach the hotel."
    mj "You’re lucky that I was the one answering the phone." 
    mj "Had it been Dad or Mom, they would have teased the heck out of you. Don’t thank me huh? I almost didn’t answer given the hour."

    hl "It’s not that late..."

    mj "It’s like fifty to 8, at least it’s starting to get late, don’t you think? I don’t think I’ll answer later in the evening. Or my parents will. I don’t think you want to talk to them that late, huh?"

    "She’s got a point. As much as you like her parents, the situation you would find yourself, head–to–head with them, not knowing what to say would be very akward."
    "So you agree with her, not very much a lot you can do more to talk to her later."

    hl "Yeah you are right..."
    hl "Hey, you should’ve come too, to the trip with us! I really miss you!"

    mj "Me? You’re doing great without me, don’t worry. And I wanted to come but you know I can’t, I’ve got to work tomorrow. Have to help out Mom with her restaurant."
    
    hl "You could’ve explained the situation to her. I’m sure she would have let you come."

    mj "It’s not like that, Howl. She just opened her restaurant. I can’t let her down like that. She really needs me, I don’t have the time to travel to a luxuous hotel unfortunately."

    hl "Alright... but next time, you gotta come!"

    "She softly chuckles at your liveliness."

    mj "You know, your attidude earlier reminded me of the time where we fisrt–{nw}"

    az "There she goes. On her rant like always."
    
    dk "Well it'd be rude to interrupt her don't you think?"
     
    az "Then don't"
    az "Think of something else."

    menu:
        "Listen to her":
            $ derek_score += 1
            mj "-we first went to the beach?"

            hl "Yes I do."

            mj 

        "Think of something else":
            $ azzy_score += 1
            "You really liked her, she’s a wonderful girl and you wonder everyday how your life would have played out, had she not been in your life at all." 
            "But you chase that thought rapidly as it always sets you in a desesperate state."
            "You are childhood friends and you were stuck together like hand in glove and never you has been seperated from her." 
            "She lived in your birth village, so you used to play together every day."
            "For some reason, she could stand your presence, contrary to most of your peers of your age. That made her a precious friend." 
            "She was always fond of your fantaisies and your games, you had a lot of them when you were young."
            "You would read a book about a boy in a green tunic going for adventures and you would pretend that you are this same boy reenacting the events of the book." 
            "Most kids would take you for a social case and most have."
            "But not Marie–Jil. Marie–Jil played with you in your little pretend games." 

            mj "So um Gaspard, Gaspard, are you listening?"

            "You wake up from your daydreaming, all of these memories have had left you groggy"

            hl "Yeah, MJ, you were saying?"

            mj "... I was saying, do you remember when we first got together? Your enthusiasm didn't die down since. It's warming to the heart to witness it."
    
    show canteen with dissolve
    "When you first got together, huh? Yes you do remember, how could you not? It was a very special day after all."
    "You weren't expecting it. One day, you were eating at the cafeteria of your high school." 
    "The usual crowd of the cafeteria flew away for an event you surely were not interested in so there were not a lot of people left here."
    "You tapped weakly at the food in front of you, not really hungry." 
    "The unusual quietness, although, helped you focus and take some bites into your plate, but no matter how much you tried, your plate remained, for the most part, untouched."
    "At your left, Ammon was laying on his chair, his tummy hurting him. He defied you earlier to an eating contest." 
    "You had accepted meekly, by principle, you’d never refuse any challenge thrown at you by your favorite troublemaker."
    "But you didn’t have the heart—nor the stomach—to follow him up on the challenge." 
    "You had been surprised at his dedication, this day we had been fed hachis parmentier and we both had taken double rations so it weighed a lot on his stomach."
    "He was so full, his shirt couln’t hold his belly any more, so you could admire his belly button and the lump the food had formed in his insides." 
    "Trying to cheer him up, you rubbed his abdomen and you were met with a pleasant squishiness."
    "You couldn’t stop so you kept on rubbing, hoping to appease him. To your disbelief, Ammon didn’t mind and he even let out some squeak of laughter and satisfaction."

    hl "Heheh, what do you think it’s gonna be?"

    "Confusion roses on Ammon’s face, still contorted by pain mixed with sootheness."

    am "I–I thiiiink it’s go– gonna be what?"

    "I look at his tummy."

    hl "A boy or a girl?"

    am "A–A gir– *Buuuurrurp* oh shut u–up man."

    "Ammon continued to burp uncontrollably so you remove your hand off of him, all disgusted by the show he had put on." 
    "You were less eager than before to finish your food so you mulled on the table, leaned on it, disturbed."
    "It started to worry you: Marie–Jil still had not come to the cafeteria, today. You three alaways ate together for lunch so you wondered where she could be." 
    "Usually, she was never late, so her absence left you concerned about her whereabouts."
    "Perhaps, she went to the match happening during lunch but she wasn’t really into the high school sports and she would have told you, if she were." 
    "Then her class might take longer than expected. But again, you didn’t think that was it."

    hl "I wonder where she is..."
    "Said out loud, you were expecting that Ammon was going to help you, or at least say where she was, but no response as Ammon laid now seemingly unconscious on his chair."
    "All of the sudden, Marie–Jil approached you, bringing in no food but an tense air on her way. It stressed you as she got closer to you."
    "Marie–Jil stood shut fast on the floor, very anxious, not knowing where to place herself. Her tail coulnd’t stop shaking; the nervosity of the situation got to me making your tail moving out of your own."
    ## TODO: add Marie–Jil sprite?
    mj "Hi Gap..."

    hl "Hi MJ... Why are you late, what’s going on? Do you want to tell me something?"

    "Marie–Jil raised her head, shocked, like she had been unmasked, as the end grew nearer with every second passing."

    mj "Huh, what do you mean?"

    hl "You’re all nervous. I never saw you like that. Did you break my stuff?"

    mj "No I did not!! {w}Oh hi Ammon..."
    mj "Ammon could you leave Gap and I alo–"

    "She finally noticed Ammon and his thick tummy. Hopeless at the scenery she was beholding, she ignored him and retuned her attention te me."

    mj "Please let me finish, Gap."

    "Sensing the seriousness of the situation, you laid down your tableware and looked at her in the eyes. You estimated that she needed your full attention, given the rarity of all this"
    "The disheartened deer clasped her hands together, breathing in, trying to gather all the courage needed for the tremendous act she was about to do." 
    "She lingers here for a time wether she had made the right choice." 
    "Not able to help her at this moment, you let her be. She had a lot on her mind and you see strands of doubt, confusion and determination twitching at the corner of her long snout."
    "She rubs her eyelids one last time and Resolve rosed in her eyes, determined to get done with it."
    
    mj "You know, how we have been friend for a very long time, now, Gappy?"

    hl "Yes I do?"

    mj "Well I am really happy with our friendship right now, how you always have been there for me."

    hl "And you always have been there for me! No need to sweat it o–"

    mj "Just a second please...{w} What I meant to say is that you are a wonderful person and I enjoy every moment I spend with you."

    "Ammon slowly raises from the dead, lending an interested ear to where the discussion was leading. In your heart, you knew where it was going and he knew too. You gaze at Marie–Jil."

    mj "But lately, I have felt a change inside me. I want to spend more time with you, I want to be closer to you. Closer than our current bond."
    mj "Those last years, I’ve come to long for a more intimate relatinoship with you, something Friendship can’t offer. Those last months, I’ve been pondering the question."
    mj "Is it really right? Do I need a closer relationship than what we have right now. Then I realised."

    "While she pronounced all of that, she teared her dress down nervously, helping her to stay calm, at the gravity of what she showed to you. But her composure broke once her eyes met yours."
    "Her face began to turn pinkish so she turned around, breaking the eye contact with you, making you unable to observe her facial features anymore." 
    "Your pierceful gaze caused her to get embarassed and she turned to prevent your gaze to reach her."
    "Ammon at this point, was fully alert, listeninn on her every words, every sounds leaving her mouth, every finger movement, every anxious tics."
    "You must have had put too much pressure on her because she yellep the next sentence."

    mj "Stop staring at me!! You’re making me anxious. Fine! What I mean is..."
    mj "I can’t go like this any longer. I need to know. I’m sure if I don’t have the response I want, I’m sure we will be able to go back at how things were."
    mj "So... I wanted to know, if those feelings are reprocical and if you want to explore and figure out those feelings with me then I’d be really happy... What I really mean is:–"

    "She clenched her dress hard, not wanting to let go her only last support with her. Ammon and you were both suspended at her lips waiting for her next actions. Is it really what you think it is?"

    mj "... Will you be my boyfriend..?"

    am "WHAAAAT?"

    "Ammon couldn’t stay still and get up from his chair from shock, his jaw hanging open. After his interjection, he stood silent, unable to say more."
    "In this point of time, something clicked within you. All of your relatives didn’t stop repeating to to you that Marie–Jil and you would make such a great couple." 
    "You never thought much of it, she was your closest friend, not a lover."
    "But now that Marie–Jil thought so too, you pondered. How stupid of you to not have thought about it!" 
    "It’s only natural and logical you’d end up together. You are a boy and a girl and you are so close to each other. Of course it has to be"
    "Once the epiphany rushed through you head, you knew what to do." 
    "Marie–Jil is such a great person, she’s smart, she’s creative you want to be with her your entire life; and if being a couple meant that, then you’ll wholeheartedly agree to it."
    "You dash to her and take her in your arms, in a loving embrace that can only mean one thing, and only one answer possible but can’t help it but say it aloud."

    # scene phone_booth with dissolve
    hide canteen with dissolve

    mj "I’ll always remember what you said..."

    show canteen with dissolve

    "Gaspard + Marie–Jil" "Of course, I’ll be your boyfriend! Why did we not do that sooner!"

    am "I think I need to vomit..."

    "Ammon abruptly stood up and rushed to the toilets."

    # scene phone_booth with dissolve
    hide canteen with dissolve

    hl "I had to check up on him that day too... He shouldn’t have eaten that much."

    mj "Actually Gappounet... I am the one who went check up on him, I made you stay at the table to keep guard of our stuff."

    "A sense of discomfort and awkwardess emanates from Marie—Jil’s words like you were opening matryosshka dolls you were highly forbidden to. She had to witness him bathing in his vomit after all. You wouldn’t want to be the one that had go that day."
    
    mj "By the way, while we are talking about him, is everythin alright with Ammon?"

    hl "What do you mean by that?"

    mj "I know he can be exhausting, sometimes. You didn’t do anything reckless with him, did you?"
    
    "A concerned voice comes out out of the receiver. You always become bold with the jackass dog around, so her worries were founded and justified by earlier events and tricks he pulled on you…"

    hl "No, nothing of the sort, thankfully."

    "Silence fills the air as it reeks with your poor fabricated lie. Marie–Jil returns you an doubting laugh, with multiple layers of sarcasm, suspicion and reservation. She was, with a lack of better words, able to see right through you."

    mj "Sure Gappounet."
    mj "Anything worthy telling me about him?"
    
    menu what_do_you_think_of_ammon:

        "Nothing special":
            hl "I mean we just rode the road. Nothing really exciting."
            mj "You sure? Nothing with Ammon? Don't you say nothing special happened when you travel with THE Ammon?"
            "You pause."
            hl "{cps=3}...{/cps} No, I can't remember  anything special nor specific."
            mj "{cps=3}...{/cps} You can't remember..."
        "Ammon is a prick" if radio_on:
            hl "Ammon is an asshole."
            mj "What did he do again."
            hl "Well I was starting to get a headache because of his music. So I asked him to turn off the radio. He asked me why."
            mj "What did you answer then?"
            hl "That I didn't like the music, I wasn't feeling like telling him it was bothering me so I said that."
            mj "Well I figured. You should've just told him you had a headache he would have understood."

            "It's too late to fix it, don't bother with it."

            mj "Don't tell me you have forgotten how he could be stubborn about his preferences?"
            hl "Maybe I have."
            mj "You don't remember huh?"
           
    
    mj "Well anyway, I wanted to talk to you about something that was bothering me lately..."

    hl "Huh what is it? Have you had another argument with your parents?"

    mj "No it’s not that. It’s something that concerns you. Something going on lately."

    "She grasps more tightly on the phone than before. The matter had been clinging on her heart for a good time."

    hl "Huh, okay? What is it? What does this have to do with me?"

    mj "I–I wanted to talk about your behaviour lately."

    "Unsettled, she struggles to find words on her thoughts. Her overall attitude disturbs you. You haven’t seen her a lot like that."
    "She grows impatient. You let her explain herself."

    mj "Are you alright?"

    hl "What do you mean? You’re making me confused."

    mj "With you trip, were you able to think about your... moods, clean your thoughts, to reflect on what happened recently."

    "She sounds concerned. Irritated. Have you been that out of it lately? You must admit that you had your up and down like everyone but you don’t consider it a matter to be discussed." 
    "At most, you felt a bit tired from the pressure but that’s all."
    "She waits for your answer, expecting a thorough justification. You don’t have one. You’re utterly confused." 
    "You scratch the back of your head, hoping something will come out, but nothing. Only oblivion and the dark void."

    hl "I genuinely don’t know what you’re talking about. I don’t recall anything noteworthy that happened earlier. Everything’s fine, alr–"

    stop music
    play music "audio/music/anger.mp3" 

    mj "Oh my god, for Jesus Christ?!" 
    mj "Are you for real, Gap??? You’ve been rolling in your bed sheets all day long 13 days straight and you say to my face that everything’s fine?!! THAT YOU DON’T RECALL ANYTHING??"
    
    hl "Huh..."

    "Confusion roses into you."
    "A burst of voice surges through the phone and you almost drop it." 
    "You panic. What happened, for Jesus’ sake? You dig through you mind."
    "You’re in the void, your head absent, beholding a black box. You open it. Even more void. You’re afraid. You shouldn’t go deeper"
    "You hand’s wet. Every second, you are to the point of letting it slip." 
    "You sweat profusely. Your throat tightens."
    "You fall silent."

    mj "Gaspard! please answer to me, why are you like that?? I want to help you but I can’t do anything if you keep shutting me out!! Even, I say, shutting us out!!!" 
    mj "Your mom is dead sick’ worried for you, don’t you see??"
    mj "It's this bad hub? You really don't remember? You really want me to remind you what eveything that had been on pur mind lately? You do, don’t you? Maybe that’ll help refresh your damn mind!"
    mj "You are failing your PhD. You are failing your classes. You haven't been to any classes for a month." 
    mj "Whenever I go to college, teachers ask me \"Where is Gaspard?\" \"Where is he? Why ins't he coming anymore? He's such a brilliant student though...\"" 
    mj "Where were you, you wonder then? You were at home, in your bedroom, either sitting or laying down on your bed, vacant, empty eyes." 
    mj "Your mom couldn't stand to see you like that anymore so she called Ammon and I to cheer you up. We would prod at you, implore you, to respond to us, something, anything."
    mj "You'd rarely say one word or two, when you weren't too occupied at staring at the void, mumbling, muttering low and weak sentences that you and only you could understand."
    mj "Once I tried to listen to the thread of words leaving your mouth, carefully, afraid to let it slip out of my ears. Literal nonsense."
    mj "Just nonsense. Absolute nonsense. That's what you were this month: a lifeless puppet whose strings have been cut by his own dubious master." 
    mj "Quickly, I look in your eyes and I see a ocean of darkness, void, nothingness, emptiness, torpor, lethargy and... Apathy. Sometimes I get scared of you."
    mj "No, Gaspard, not everything's fine. It sure hasn't been lately. Everyone has been worried about you. It's not at random that Ammon picked you to go with him at Paris. He wants to help you go better." 
    mj "So please, help me, Gaspard... Please Gap, will you let me help you? Will you tell me what happened last month"
    
    hl "Last... Month?"
    
    "I asked confused. everything she says, you can't hear it. More Accurately, you can hear her perfectly but you refuse to hear it. The black box should never be opened and every attempt sends a throb trough your brain." 
    "You head hurts. You seethe. Please stop. Please stop, you can't take it anymore."
    
    hl "Please.... stop"

    mj " Ohoohoh I sure won't stop, Gaspard Danbois. I {w=1.0}AM {w}FED UP. I won't stop until I'm finished." 
    mj "You will answer to my questions, Gaspard and you won't be able to esacpe forever."
    mj "We covered for you, we never asked any questions, we didn't want to put pressure on you. We let you breathe, rest, mourn, or even hell, agonize." 
    mj "But one day or sooner, you'll have to tell us what happened and I'm sick of not knowing the truth."
    mj "So tell me Gaspard. What happened, last month, September Friday the 13th?"
    
    "You panic even more. Friday the 13th, it hits a bell, a nefarious bell, a bell from hell. You realise. The box tightens even more. What happened that day must remain secret at all cost." 
    "She mustn't go further in her crusade of questioning. You ought to make her shut her or you don't know what may become of you."
    "She represents a menace to your tranquility. Your Apathy."
    
    hl "I tell you and tell you, I don't know! How many times do I have to tell you?!! I don't know, I don't know and I still don't know! How that goes for you!"
    
    mj "I am sick of you with your \"I don't know\" \"I don't know\"! You lie to me as you breathe! You do know and I will get the truth about that day."

    "The deluge of your body flows down on your sweaty palms. Your shaky hands tremble like a sinner to Judgment day. Your god with a disembodied voice continues to yell at you for what you have done and won't forgive you."
    "The phone slips out out of your hands and falls down; thus, its thud echoes heavily in the booth. You pick it up hastily and shove it into your by fear to annoy the Bringer of your Retributions." 
    "You are scared of it, you are scared of your Judgment, you are scared of the Truth."
    
    mj "Don't you dare to try and slip away. If not today, I'll make you spill out on way or another, just wait for it. That could be today, but that could be tomorrow or after tomorrow or a week or a year, just wait for me."
    mj "I'll be more precise then, if you can't tell that much... Were you at home, this day? Just tell me please, it'll be faster that way."
    
    "Yes you were at home, you can tell that much, you were preparing for a party, what type of party, you'll have to prod a bit more." 
    "You remember what it was, it was a birthday party, although you don’t remember who it was for, it should’ve been of your relatives surely."

    hl "Yes I was at home I think... But I don’t know any more than that, I swear!"

    mj "Ok then let me ask you another question: Someone ringed at your doorbell. Your mom told me she was going for to answer it but you’ve been faster than her so she let you alone." 
    mj "When she wanted to ask who it was, you were gone of the house."
    mj "Gone, she said. Not went somewhere and come back. Not hidden out of her sight but gone!" 
    mj "She went looking everywhere for you and she even had to ask Ammon and me to help her. So I think we deserve an explanation."
    mj "Where were you that day? Who was it at the door step that make you go go missing? Don’t you think it’s really weird and out of place, Gaspard?"

    "The stepdoor, the stepdoor, who was on the stepdoor. Everything is so blurry, and you can help but look deeper whereas your inner sense of danger always warned you."
    "Crack. Something broke out within you. The box, it’s opened. You remember."

    hl "Shut up."
    
    "You can’t stand up anymore. A fiery fever takes over you. Your view blurs itself, and you trip." 
    "Hunched back on the phone booth, you can’t stop your accelerating breath. You have lost control of it. This is tot late. It’s coming."
    "The walls of the cubicle close on you, pressing you. The previous cold air in the place flee at the increasing pression. Breathing in here is pain all accross your lungs and the heat rises considerably." 
    "Steam roses of your red cheeks and you huff to no end, pleading the air to come back. But it never came."
    "The hot oven you are shut in heat up more and more, to your death. No matter how much you plead. No matter how much you apologise. No matter the value of your guiltiness, you’ll die in the fire of Hell and the Truth will come out."
    
    mj "Don't you tell me to shut up. Answer to me, Gaspard? Who was it?!"
    
    hl "Shut up, shut up!"
    
    mj "It was your father, wasn't it?"
    
    "The one at the stepdoor, yes it was. He went missing. He didn't even try to look after you. He left. He doesn't care about you. You doesn't care about him. You hate him."
    "You followed him on the pavement. Did you follow him further? You think so. It doesn't matter. He shouldn't have come. He had to shut it. She has to shut it now. Shut it, shut it, shut it"
    
    mj "Why when you meet up with him, we find him later around your house?"
    
    hl "Huh you found him?? You really found my father?"

    mj "What do you mean we found him?? Of course, we found him. Don’t try to fool me, Gaspard, this is serious. I mean, we found you with him, numb, unresponsive, away..." 
    "...After all, we found him ×××××××××××××××××××××××{nw}"
    
    hl "No... No... No ! No no no no no no no nononono"

    mj "What are you saying?!"

    hl "No... No, shut up shut up, shut up, shut up, shut up, shut up"

    mj "Gaspard?.. Are you alright? Maybe I pushed you too f–"

    hl "Shut up. Shut it. Shut up, shut it, shut up, shut it, shut up shut it shut it shut up shut up shut up"
    hl "{size=60}SHUT THE FUCK UP{/size}"

    "A loud crash echoes and resonates within the phone booth. Slumped down, you don’t move anymore. Your head’s empty but a shrill and piercing white noise in your ears. You’re clawed to the ground and won’t get anymore."
    "When your bloodied vision sets back into focus, you observe with a dead eye the destroyed–to—thousand—pieces receiver on the ground, you come to wonder what has guided you to this point." 
    "You rise your hands at eye–level vision to watch the blood spill out of your hands." 
    "What happened that has come to you to bloody them. {w} What happened Semptember Friday the 13th?"



    jump rest_area_2

label rest_area_2:
    stop music

    scene parkingLot 
    with fade

    "You rush back towards the bike in hope to flee the burning rising inside the glacial heart of yours you wish you could shut out." 
    "The more you run, The more the distance between you and the vehicle stretches to unreasonable length, the cicadas, witnessing this pitiful performance, coulnd’t hold back their laughter."
    "Heinous hyenas; that’s what they are. You could mistake them for buzzing, singing, drilling or cries, but I hear them very well: it was a loud sarcastic cackle."
    "Sweat drops blur my vision. Or maybe it was tears. Either way, the distorted landscapes didn’t come back once I’ve run through the kilometers to reach the bike."
    "The metallic frame as my only support, I huff and huff, grasping for air." 
    "The tie tightening my neck for a long time, decided it was time to choke me. Not able to bear it anymore, I start to get rid of my blazer that was imprisoning and suffocating me."

    am "Huh, Gaspard? Are you alright?"

    "A familar voice and the sound of a belt swinging around rise my ears like antenna and stops me dead in my tracks. I slowly turn around my head to be met with the concerned face of a dog with his belt unbuckled."
    "An embarrassing contest of glances followed and I coulnd’t break the glaze. He finally buckles it up but that expression mixed with fear and inquisitiveness doesn’t disappear at all."

    am "Were you...{w} undressing? Why do you sweat so much?"
    ## TODO: Make him joke about undressing (it’s not a contest)

    "He drowns me with questions."

    am "Who did you call? Was it Marie–Jil? What did she tell you?"

    hl "Your fly."

    am "My... what?"

    hl "Your fly’s opened."

    "Ammon looks down, confused, to notice that, indeed, his fly is opened. He zips it up and raises his head back with an unamused look."

    am "… Anyway, have you been running?"

    "You quickly search for an excuse and determine that his proposition is the best outcome."

    hl "Exactly... {w} I was making a little jog to make me stay awake."

    "Ammon approaches me, maintaning the gaze as if just looking away will break the link between us."
    "At close range, he lays down his hand on my shoulder. His claws soflty brush my jacket. I know it is a very arduous task for him to be that considerate."

    am "Do you want to talk about what just happened?"

    hl "No… I’m alright."

    "He helps me set back my sweater. It’s embarrassing coming from him that my cheeks get warm."

    am "Well if you need anything, tell me huh? I ’ll always be there."

    play music "audio/music/griff.mp3" loop fadein 2.0

    "All of the sudden, he takes you in his comforting embrace." 
    "You are pressed against his breathing chest and his periodic huffing and puffing lulls you head and you forget with every going and coming why you were in such distress earlier."
    "His chiseled–out arms go around, under your armpits so his warmth travel in every tinges of your skin and it soothes you, relaxed more and more by his reassuring heat. His embrace was comparable to a loving brooding hen."
    "He scratches you under the neck, your weak spot and you start purring. The low hum of your sound of sootheness resonates in his chest helps him uncontract his muscles making that you finally make one with him."
    "You breathe out a sigh of relief, happy that you are not alone in this world. If it was only you two right now, you’d still be satisfield."
    "Ammon breaks the silence with comforting words."

    am "Listen, Gaspard. I don’t know what happened with Marie–Jil but my guess is that she bothered you with the events reganding your father, right?"

    "Your heart sunkens when your hear that word. You really don’t want to talk about it."

    am "Don’t worry, I won’t prod at you about it... Just know that she has their reasons. What happenned that day really marked her. Please don’t hold that up against her."
    am "Just now, that I won’t be asking any questions. Until you are ready. Until then, you’ll always be safe around me. Please do not worry. Everything’s fine, see?"
    am "Remember also that if you want to tell me anything, I won’t judge you. I will even help you. You have nothing to fear with me ok?"
    am "I can feel you carry a very heavy burden. You shut everyone out because of that. You don’t want to bother us. Buc you don’t bother me. As grumpy, bratty you can be, you don’t bother me. I like my little grumpy cat, heheh."

    "Ammon laughs melancholicly. Everything he said sounds like a distand memory, very far away from him."

    am "So please, no matter what happens, don’t leave, ok?"

    "Deep down, a little voice whispers to me \"Just open up\" \"What are you waiting for\" \"He won’t be always there for you\" and my arms move on their own towards the reassuring friend."
    "A puddle of emotions rains down my throat and dwells deep in my stomach. Some butterflies care not to get close of it, fly away to not be seen again." 
    "All of a sudden, my limbs fall dead, the threads maintaining them alive and up, slashed through, unfairly."
    "Nothing remains in my throat but a fragile cry and I mutter it."

    hl "Ok."

    am "Great."

    "He releases you and turns away toward the bike top–box. You wish you stayed like that longer but you know better to not abuse his gentleness so you let him go."
    "You check your pulse. It came back to a normal pace. You’re relieved. You couldn’t bear any longer the throbbing pain in your chest but the horrible headache hits you like a lift and you rub your temples."
    "You need something to relax you even more. You look for an aspirin in your pockets but you can’t find any. With all the fatigue and the pain, you wonder how you’re going to take back the road. You look at Ammon."

    hl "Hey Ammon, do you have anything for headaches? It’s really hurting right now. I don’t even know I can stand."

    "He scratches his head hair and search his trousers for any medicine able to help me. Unfortunately nothing comes out of his search."

    am "Sorry Gap, I have nothing on me. I mighgt have a cigarette though. Smoking some helps me relaxing. Perhaps it could help with your headache? Do you want some?"
    
    "I consider his proposition. You doubt of Ammon’s statements veracity but you don’t have any better option and you, in your inner soul, crave for some cigarettes. Ammon had initiad to this early this year and you must addict it can be pretty addicting."

    hl "I do want some. I don’t have nothing better to do anyway..."

    am "Okay cool, let me check my bag, I think I have left some in it. It’ll be quick don’t worry ahah."

    "He grins at me with his biggest smile and opens the top box on the motorcycle you were driving earlier. As it was going to be quite a trip, you both crammed everything you could in such a tight space. You were proud of your space management."
    "The gentle hound rumbles around for his stuff and after some long seconds of noises of every kind, he finally finds it." 
    "A little padlock contained private the contents of his bag. Paris was a big city with all kinds of thieves and pickpockets so you’d never know."
    "You are tempted to peek into the code of his secrets but you don’t see the purpose of this action, he’s going to bring you what you want anyway. You decide to respect his privacy."
    "He fiddles with it not for a long time. A small click rings out and he removes it." 
    "He immediately grabs a box of cigarettes like his precious meal and pulls out his lighter in a swift motion. Once lighted, he shoves it into his mouth."
    "Then he cleans the inside of his bag and zip it shut. He takes back the defensor of his belongings on the opening. But for some reason, he puts a concerning amount of time locking it."
    "As you were about to ask him about the issue he was having, another click roses out of the padlock and he wears a satisfied smile. You sigh, relieved." 
    "He shuffles out the numbers and, as expected, he puts another span of time trying to fit back into the trunk. You think to when you’ll have to get out your bag and you gulp."
    "Ammon approaches you and when he sets his sight, his face goes from content to worried. That makes you concerned."

    hl "Sooo... Do you have one for me? My headache still really hurts."

    "He breathes through his teath."

    am "Shhh... Yeah about that."

    "He hands you an already empty box of cigarettes. You eye it, utterly disappointed. You raise you head back to Ammon and he can’t stand you sorry look."
    "He turns away his head, in a guilty motion, crossed arms, compressing his chest out of embarrassement. Every time you try to get his compassion, he flees away"

    am "I’m sorry, Gapgap. I really thought I had one for you. I should have thought I had pretty much smoked everything last time."

    "You observe his elusive face, unable to withstand you. He grimaces in embrassement and cast you some rare looks and looks away as soos as he sets an eye in you gaze."
    "Something is off. Ammon is not someone who’d forget his stock of cigarettes the day of your big trip. Usually, he has around 3 box of smokes ready for every occasion."
    "He’s also the type to own up to his mistakes and puff his chest, not afraid of the repercussions. His current states makes you think to a sorry puppy who has done a very bad mistake."
    "Is he lying? But you don’t see why he would be lying to you. After all, he wouldn’t prevent you to soothe you pain. He can be cruel but not that cruel." 
    "You find yourself disturbed and confused, not knowing if you should trust your guts or your friend."

    am "Anyway, I don’t think a cigarette would help you anyway. You should get some water. That should tone down your headache better in the end."
    
    hl "But I wanted to smoke with you..."
    
    am "Ahah maybe another day then. I have seen bottles in the bike trunk. Go get some ok?"

    "He pats me on the shoulder, making me understand it was time that I turn the page. Defeated, you cross over him and go towards the bike."

    am "Oh by the way, could you bring me a bottle too? I’m thirsty."

    hl "Sure Amm."

    label restarea_pointnclick_start:
        "Ok so you should start getting on your way"
        "Perhaps, he’s right. Perhaps drinking water will really make you head gets better."
        # "Even though I’m not that thirsty..."
        "You are curious to what he was doing with the top—box, anyway."
        python:
            ammon_talked = 0
            current_screen = "restarea"
            trunk_explored = False

            padlock_code = [6, 1, 5, 3]
            checked_padlock = 0 
            
            got_water = False
            got_notebook = False
            good_code = ""

        
        # show screen custom_quickbar
        stop music
        play music "audio/music/moment_orange.mp3" loop fadein 1.0
        jump pointnclick_interact_loop 


label confront_him:
    scene parkingLot
    python:
        del ammon_talked
        del trunk_explored
        del padlock_code
        del good_code
        del checked_padlock  
        del got_water

        current_screen = "" 
    hl "So Ammon, I have a question for you"

    stop music fadeout 1.5
    play music "audio/music/suspense.mp3" loop fadein 0.5
    "The daydreaming dog spins his head, intrigued. Your grave tone might have shaken him because concern and worriedness covered all over his face. You feel you are on the good track."

    hl "Are you sure you don’t have any cigarettes for me. I mean, you always bring more than one, don’t you."

    am "I am sure. It’s just this time... I forgot some at home and only brought one. Nothing more to that."

    "He scratches the back of his head. He doesn’t have anything more to say to you. You almost feel pity for him. If you had not discovered it, you would have trusted him. But you can’t anymore."

    hl "Are you really sure?"

    am "Yes, I am."

    hl "Are you really {b}really{/b} sure?!"

    am "Yes!!"

    hl "Ok then do you have an idea of what this is?"

    "You pocket out, the heart of your sorrows, the epicenter of your troubles, the one responsible for that all, the box of cigarette in the center of your palm so he could clearly see it."

    hl "Do you recognise this?"

    "As soon as Ammon sets his eyes on the object, he slumps his shoulders, his face distorted in an unpleasant expression."

    am "I recognise it, yeah... It’s the box of cigarettes that was in my bag."

    hl "Yes it is. Do you know what it means?"

    am "Yes."

    "He stands there, akwardly, arms dangling, waiting for your response carefully."

    hl "Then why did you purposefully hide it from me?"

    am "... I don’t know."

    hl "You don’t know? You don’t know?? More like you don’t want to tell me, you liar."

    am "I’m not a liar."

    hl "You’re not a liar, what do you mean you’re not a liar? Then what does that mean, these damn cigarettes!"

    "Ammon raises his head defiantly, biting his lip. You’re pissing him off and he’s going to make you understand that you should back off." 
    "But you don’t care, that he comes at you! You can take all of his charges"

    am "I never said I didn’t have another box of cigarettes, I just said that the one I showed you was empty. Nothing more. You never asked if there was any more."

    hl "Don’t play on the words, you trickster, you deceived while I was at my lowest."

    am "Don’t make it a fuss."

    hl "A fuss, a fuss?? I am the one making a fuss??!"

    am "Yes you are."

    hl "So you{size=50} should’ve had given me some, we wouldn’t be here then!"

    am "Jeez, calm down, it’s just cigarettes..."

    hl "IT’S NOT JUST CIGARTTES, IT’S CIGARETTES YOU’VE HIDDEN FROM ME."

    "You yell out at the top of your lungs in the exposed ears of the elusive dog. They shivers out of the loud sound."
    "Ammon takes a step back, startled by your outburst."
    if take_him_out:
        extend " \n Once again, his concerned eyes look in vain. Only a stranger stands in front of him."
    
    else:
        extend " \n His concerned eyes look for a black and white cat named Gaspard. However, only a stranger stands in front of him"

    $ del take_him_out
    "Ammon stays silent, boiling. He contains himself to retaliate, but it is a hard task for a loud proud barking dog. His fists are clenched."
    "You stick yourself to him, only centimeters away. You press his chest with you finger to bug him even more. You want to make him crack, he’s got to pay."

    hl "Give me your lighter."

    am "Give you my what?"

    hl "You’ve heard me. Give me your lighter. I wont repeat myself. I need it for smoking."

    "The cornered hound rolls his eye but eventually, reluctantly, reaches for his jacket breast pocket and takes it into hands. For some moments, his gaze lingers in the void."
    "Taking avandtage of his moment of distraction, you snatch it from his hands and wave it into his face. He shows an irritated expression."
    "He gnarls his teeth at me but, ultimately, decides to do nothing about your annoying behaviour."

    am "Go on if you want it that much..."

    "You follow his lead and you pull out a cigarette from your now–yours box and you attempt to light it with difficulty as you are not used it." 
    "There are snickers in your back but you can’t hear them, you’ve finally got what you wanted. After a few tries, you manage to light it."
    "You huff your smoke and let it whisk away in the air in a majestic small cloud of your worries."
    "You wait for the adrenaline and the pleasure to kick in but you find yourself empty, of any sensations—worse, you didn’t think you’d say that—but it intensifies the throbbing pain in your head."
    "Clutching your head for salvation, you hear a taunting and provocative voice just behind you."

    am "Hey, have you ever thought that I planned, of you, that you’d do that?"

    "You turn your head, caught short by his intervention."

    hl "planned... that I’d do what?"

    am "Exactly what you just did. Snoop around my stuff because you can’t trust me when I tell you something."
    am "I mean, I couldn’t believe my eyes. As soon as I turn my back, I find you rummaging through my stuff and toying with my padlock."

    hl "I did not–"

    am "Why are you trying to deny it?! Those cigarettes didn’t end up in your hands by coincidence, did they?"

    "You shut yourself. He was right. You did snoop around his stuff. In retrospective, you went overboard with what you did." 
    "No good friend would just put his nose in private stuff just for a cigarette. But the urge was stronger than you, you couldn’t help it. Your cheeks get red and you boil out of shame."

    am "Well that’s not like that was the first time you did that. You always loooooooved snoop around my stuff anyway. I’m not really surprised."
    am "I just wanted to see if you really trusted today. After the last month where I wasn’t able to see you at all, because you’d shut yourself inside, I was confused about the state of our friendship."
    am "So I made a test, a little game of mine... and you failed miserably, congratulations"

    "He claps his hands, slowly, sarcastically with an apathetic face, bored of your antics. You couldn’t believe yourself. How were you able to be such a fool to fall into his trick that easily."

    am "Anyway, I still want to play our game, so I can give you a second chance."

    "Confused, you tilt your head at him. You had no intentions to partake one more time into his game. But still, a second chance for what?"

    am "So here it is: Can you guess why did I change the padlock code?"
    
    hl "You.. you’ve changed the code?"

    am "Why yes! you don’t think that the code to my belongings would be that easy, do you?  Did you think that I would set a code that much easy to crack??"

    "He sets his piercing gaze in mind, with an a expectant smirk up his ears on his face. You gulp. That doesn’t sound good."

    am "Well not anybody could crack it. Only a few people, those people being intimate relatives, that only they would know about me. I don’t know, my closest friend for example?"
    am "So tell me, Gaspard, why did I change the code?"

    menu why_did_he_change_the_code:

        "To see if I knew your real name":
            am "... What?"

            hl "Yes Ammon, in reality... You’re not named Ammon... but Éric!!"

            am "... Yes and?"

            hl "And?"

            am "Yeah sure my name isn’t really Ammon, it’s a nickname {b}you{/b}’ve come up with because of my apparence."
            am "But what does that have to do with the code?"

            "... He’s right. It’s totally out of topic"

            jump why_did_he_change_the_code
        
        "To see if I knew your birthday":
            am "... Yes you are right."

        "To see if I knew your location of birth":
            am "... And what do you do with my location of birth?"

            hl "You take the department number to input it into the padlock!"

            am "Honestly that’d be a good guess if the department number wasn’t just two digits. The padlock makes 4 digits..."
            am "Good guess... I guess?"

            jump why_did_he_change_the_code
    
    am "The reason I change the code was to check if a friend of mine knew my birthday. Heheh..."

    "You start to feel uncomfortable. A sharp and extreme mingle builds up inside of your abdomen. Your throat gets tighter every second."

    am "So let me ask you another question. I’m sure you don’t mind anyway right?"
    am "You love playing my games anyway so be prepared."
    stop music fadeout 0.5
    play music "audio/music/anger.mp3" loop fadein 0.1
    am "Why the hell did you steal my wallet?"

    "A growing rage fumes out of his ears. His fists are so clenched bloods spills out of his nails. A violent shock bursts through you. He noticed?" 
    "You lose your nerves, coming up with your best innocent impression."

    hl "Huh– No—no Absolutely not! Why would–would I do that?"

    "You stumble on every one of your words. You didn’t expect Ammon to pick on your larceny. You tremble, he musn’t know it was you."

    hl "Maybe you’ve dropped it on the road?"

    am "Bullshit! You know damn well I didn’t drop it, you liar."

    "He slowly approaches you. Every step he takes, you recoil. Every breath he breathes, you gulp, Every piercing glance he casts you, you look away, unable to withstand him."
    "When he reaches a close–enough distance that your whiskers could rub his snout, he pokes and prods at your chest in a similar fashion you were accusing him of concealing his belongings."

    am "At first, I was confused. Why would Gaspard ask me to watch his notebook for the thousandth time? I figured you were just recovering your own way."
    am "Then I felt your warm on your arm on my back... then your warm hand in my jeans’ pocket. What was he doing I was thinking at the moment."
    
    "He wears a sad smile. Bittersweetness and regrets ooze out of his words."

    am "You weren’t that stealthy. You could’ve gone for my pants, it would’ve felt the same."

    "His meek smile disappears for his frowned and scrunchy eyebrows to take place. He’s deeply mad at you. There’s no coming back from that."

    am "But then, here it comes. You take out your hand. My wallet is gone."
    am "I was lost. What could you do with my wallet. For a moment, I thought it was your crooked—out way to play a trick on me or make me a surprise."

    "His words before soft, emanating a deeper irratation, became primal growls. His foul breath moves every hair of your face."

    am "Suddenly, an awful thought came to mind. It couldn’t be possible, you wouldn’t dip dowm that low, would you?"
    am "And there I see you, toying back with that bloody padlock and finally unlocking it."

    "His sharp drooling teeth fill your vision. That reminds you that it was foolish to even believe you could have the upperhand on him."

    am "So this is why I’ve learned today: you don’t trust me any bit that you are willing to snoop around in my stuff, nose deep down, like a vulture."
    am "Next that you don’t even {size=50}fucking{/size} remember my {b}birthday{/b} and that you don’t mind pickpocketting me and steal my wallet."
    am "You really had to look at my ID to guess my birthday? You know you could’ve asked me? Oh no I forgot. You are a sad distrustful scavenger willing to go through my shit to get what he wants."

    "You’re lost for words. You were mistaken on every level and now, your then close friends was tossing at you everything is wrong with you, utterly disappointed."
    "You stare at the ground, in a dead trance, not able to reflect anymore because of your blans mind, this mind ravaged by the missiles launched at you."
    "Arms dangling, you had no purpose in life anymore. Once again, you return to your puppet with no master state, lifeless."

    am "I don’t recognise you anymore, Gaspard. I can’t recognise you since the day you missed my birthday."
    am "It’s like the day of my birth... You’ve died. What really happened that day?"
    am "I know I’ve said I’ll never ask you questions about it. But then, you’ve demonstrated you don’t trust me anymore.{w} So I don’t trust you anymore either."

    "Your mind breaks at his words. Is he going to reject you? Is he going to never approach him again?"
    "You can’t stand that. You can’t stand that Ammon, your childhood friend, the one you’d think you never lose, that always be with you no matter both of your antics, is going to cut ties with you."
    "You have to find something to make him stay. He can’t leave you, otherwise you’ll be alone with your thoughts. With that day in loop."

    hl "Wait! Huu–Huuh I didn’t steal you wallet for that!"

    "You interrupt his plea. You caught his attention. Don’t waste it. You scramble in your mind to think of a good enough excuse."

    hl "I ste— I’ve taken your wallet to make you a surprise, to cheer you up, ok?! I never forgot your birthday, all right??!"

    "You gesticulate around like a madman, with vivid desesperate motions, and your exorbitated eyes, crazed, frenzied. You’d scare yourself."
    "Those same eyes implore him to believe you in vain."

    hl "So please don’t leave me ok? I beg of you!"

    am "Give me back my wallet."

    "Ammon answers sternly, arms crossed, closed, unsensitive to your pleadings."

    am "With all of the shit you’ve put me through, you surely had the time to make your little surprise. I want to see it."

    hl "It’s– It’s not done!"

    am "Don’t care. It’s my wallet anyway. I have the right to get it back any time and I’ve decided that it was right now."

    "Ammon, in an isntant, dashes for your pockets. No you can’t let him, you won’t be able to go back if he puts his hands on it. You have to prevent him at all cost."

    hl "Wait, I’m not done!"

    am "I don’t care! Give it to me!"

    "Ammon grabs the wallet but there is too much at stake to let it go so you clutch his hand like you’d hold for your life."
    "You wrestle for your life to get the wallet back. This is your last chance to set things right so you scratch at him, hiss at him, and even bites him."
    "On the other hand, Ammon won’t let go either. He barks at you, jerks his head in all directions. He’s slipping through your fingers the more you pull that wallet."
    
    hl "Please Ammon!! Trust me!!!"

    "You put you hand out to him, to his shoulder. He might understand if you can grab a hold of him."

    am "{size=60}BACK OFF{/size}"

    "The next moment, his fist connects to your eyebrows arch and you blast through the air on his motorcycle."
    "The wallets sits on the floor, its contents spilled in the grass, last relic of your fleeting friendship, trampled"
    "You hit your head hard on the frame of the motorcycle. Blood trickles down from it. You pass your head on your wound. Just blood."

    am "FUCK, sorry, I didn’t mean to! Let me hel–"

    hl "{size=60}YOU FUCKING BASTARD{/size}"

    "You spring on Ammon. You both roll on the grass. After that it’s a bit of a blur. You don’t remember everything."


    
    stop music fadeout 0.5
    play music "audio/music/uboa.mp3" loop

    "All you remember, is Ammon laid down in the grass, defenseless, his face contorting in pain. He’s out of breath, imploring for air."
    "You, on the other hand, sits on top of him, astride. You watch his unbeckled belt and you can see the tip of his underpants though his fly. You think this would be a thrilling position in any other context."
    "Unfortunately, the more you go up though his body, the more you realise the horror of the situation."
    "His disheveled, torn down, shirt and his black dirty jacket were no different, no the thing that disturbs you were your arms compressing his chest down."
    "This must hurt him so you should stop but your arms keep pressing down and his cries of pain fill your ears. But you keep pressing down, no matter how much he seethes."
    "Even more disturbing, Ammon hits your arms with all his strength but that reveals in vain, your arms planted there like statues, unmovable, whatever may happened."
    "Despite his determination and his fierceness, the fists grew gradually weaker to the point where the wind, passing, judging hits you as hard as him, you couldn’t differentiate whomever was beating you."
    "The knee strikes, beforehand, as piercing as spears, in your back, became bumps comparable to tickles. Although the situation didn’t leave any room for laughter or any kind of foolishness."
    "Then you understand. Your hands are wrapped around the thick neck of your weakening friend."
    "You squeeze and squeeze his squishy throat crushing every chance that air revigorates him. You can feel his adam apple fighting for its freedom but you would prevent that at all cost."
    "You find yourself loving touching his flim skin, and its rough texture. You wished you had done it sooner."
    "Ammon’s face turns pale as you writhe him of his last strands of energy. Drool bubbles out of his mouth, his teeth gritted to keep the remaining air in his mouth."
    "Another thread of drool drops on Ammon and this time, it only comes from you. Your eyes are exorbitated from rage. You have become a feral animal."
    "All of the sudden, you feel a loving touch on your arm. The dying hound shares a gaze with you as his last sparkles of life exit those sad eyes."
    "Close to the death, he had an epiphany."

    am "Pl–please stop."

    "You suceed to make up words from the low raspy sound coming out of his throat."
    
    am "I believ–believe you, ok? You are my friend and I won’t want leave you, ok?"
    am "I know you’re having hard times, so I won’t hold you to what you’re doing right now, I promise."
    
    "His grip weakens, all colours drain out of his face. His throat before, contracting and moving, goes more and more inert."
    
    am "You’re n–not dea–dead. You always ha–have been the s–same cat I met years ago."
    
    "He grins at you, tears streaming down the corner of his lips."
    am "I don’t want to ever leave you. You’re the favourite person I love to trick to."
    am "So... I know it’s not you so stop doing that, I beg you."
    am "Re—remove your h—hands... Please."

    "His hands fall down, unmoving. He doesn’t breathe a lot anymore."
    if ammon_score == 0:
        "But you didn’t care. All you want it to keep strangling his squishy little throat. It brings within you forbidden pleasures."
        "You loved every rictus of pain on his face. You drool even more and these strings mix with his."
        "Your pleasure is indiscernible from his pain. You hate him. You hate him and you hope he suffers enough." 
        "He’s going to regret ever thinking about leaving you."
        "Then a memory goes through your mind. Your hands are also wrapped around his neck. But not your dying friend right here. Your father."
        "You remember everything. The pavement, the fence, the rocks, the blood in the grass mixing in the dirt."
        "You remove your hands. Blood on your hands. Nausea goes up your torso. You feel light–headed. You stand up."
        "He doesn’t breathe anymore."
        "At least you think."
        "You puke."
    
    else:
        "Then you remenmber. All the times Ammon bring up your spirits. All the times you cried out of exhaustion and he was there for you."
        "All the times, he took your yogurt at lunch at middle school and toyed with you for minutes. In the instant, you hated it but in the end, you’d laugh."
        "The time you feel nauseated at this lame party and he came take you home even though he told you not to."
        "The times where he didn’t feel good so you watched over him for day and nights so he’d go better."
        "You grin. You couldn’t have a better friend than him. He was the only one able to fully understand you. Then you realise."
        "You’re strangling him. Your hands are wrapped his neck. What are you doing. What you’re doing is bad, forbidden. You’re committing a crime."
        "You remove you hands of his neck and you stand up so fast, you’re striked with the vertigo."
        "Ammon let out a seething gasp, finally air filling his lungs. However he stays on the ground, too puny of your assault."
        
        if ammon_score >= 1:
            am "Thanks Gap..."
            am "I like you {w}a lot."
            if ammon_score == 3:
                am "No. I lo–"
        
        "He doesn’t talk anymore. He has fallen unconcious."
    
    "Your headache assaults you with greater intensity. You clutch you head. You lose your balance."
    "You collapse."

    jump first_act_part_1
    