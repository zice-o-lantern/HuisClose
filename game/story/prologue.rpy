label prologue:
    
    # Black scene
    scene black
    pause 1.0
    cl "Honestly{w=0.5}, I cant’t believe you could strangle him that hard."
    cl "Or maybe it’s not that complicated. Maybe I’m just too weak. Perhaps you’re just used to it." 
    cl "You’re lucky. To be able to feel his beating heart. His cold carapace heating up with your hands."
    cl "I know I couldn’t{cps=3}...{/cps} {w=1.0}I think."
    cl "God, why do I feel like this. {w}Why, when, for once, I feel alive, must it be so grim? It makes me sick.{w}\nI’m sick of it.{w} I’m a monster."
    cl "God, why? Why must it be me. Stuck in a never-ending cycle of boredom, regrets and suffering where Death isn’t an escape to your macabre plays. {w}Did you have to be so hard with me?"
    cl "I hope that, one day, when I’ll come upon the wicked and wretched god that bestowed me of this condition..."
    cl "I’ll be able to writhe him out every strands of life he ever had."
    cl "That I’ll be able to strangle you harder than you ever could."
    
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
    cl"So I difficultly make my way towards him and I search for something to soothe my thirst."
    cl"I am able to find some flask. I uncork it and stuff it down my dirty throat so the lukewarm water can flow."
    cl"With every gulp, it wash down a bit more."
    cl"That mucus obstruating my throat."
    cl"That warm hot itch that resided there."
    cl"That distress that had built up over the years."
    cl"Those regrets that I didn’t do good enough for him."
    cl"That guiltiness that I failed him, that I am not worthy."
    cl"That shame that I wasn’t good enough for him."
    cl"The only thing remaining is the overbearing numbness of my life."
    cl"I need more water."

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

    show eyes:
        alpha 0.0
        xalign 0.5
        yalign 0.5
        ease 30 alpha 1.0
    show clearing:
        alpha 1.0
        ease 30 alpha 0.05

    play music "audio/music/build_up.mp3" fadein 30 loop

    cl "Hey You know what? Perhaps he loved me. Perhaps he never did. But he won’t be an issue anymore. He can’t hurt us anymore."
    cl "Perhaps You’re responsible for what happened but I am just as guilty as You."
    cl "Let’s just put all that behind us."
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
    extend ", I need You."
    scene black
    scene ruralRoad with fade
    # play sound 'audio/sounds/car_white_noise.ogg' loop
    
    play music "audio/music/The Beatles - Here Comes The Sun (2019 Mix).mp3" fadein 5.0 loop


    "You wake up from your reverie at the cold hands of someone grabbing your shoulder."
    hl "Aaaaaah!"
    
    am "Hey were you sleeping?"
    
    hl "Huh—whuu?"
    
    am "Yes you were. Sorry I had to stop and wake you."
    am "I was starting to feel your head on top of my back and you wouldn’t budge and that didn’t help me drive."

    hl "Oh... Sorry Ammon I didn’t mean to."

    "You can stop reading here I didn’t rewrite the next part"

    am "No worries Howl. I think I’ll stop next stop, I’m starting to get weary too."
    # "You wake up at the hum of the radio, a bit shaken up, with drool staining your helmet visor — Fortunately there’s not enough to hide your vision."
    "Where, before you were stranded away in the milky way, comtemplating about the mysteries of the universe, where the shining stars watched over you, you find yourself on a motorcycle."
    "A sharp feeling pervades your whole being like a blooming rose planting her thorny roots in every part of your spirit."
    "The radio was blastering loud some song from a rock band you appreciated a lot, although you dare not admit it in public, as it was strongly frowned upon among your elders."
    "It’s alright, you think; nobody’s here to disturb you in your little trance."

    "In your little world, you were no more significant than a grain of salt swept over by the wind on a sunny beach. No matter you’ll end up, you’ll be content with the result."
    "The dying sun at the horizon sends you its adieu and lays down behind the horizon at slow but certain pace."
    "The last glimmers of lights highlights the majestic landscapes the road has to offer. \nThere were multiple sceneries you could transfer onto a pellicule for everyone to admire at home."
    "Some black forest, deep as the never–ending void where no light never escapes, some striking high mountains, candidates to the siege of the Olympus."
    "Some sunflowers, dispersed in the grand lands of tall grasses, don’t know anymore where to turn their head to, their leader gone astray, to never be seen again."
    "All these landscapes appear gorgeous and alluring to you on the road but they were even more exquisite from your moderate village, where you have resided from as long as you can recollect your memories."
    "You remember, observing them, from the window of your lonely bedroom, dreaming of one day, going on a journey to find an unestimate treasure."
    "You lived quite some adventures in this very room. Afraid of the outside, your little journey didn’t go very far."
    "It happenend often that you wake up and decide that you’d be a cook or an explorer, or any revelation you had on this particular day."
    "One day, you woke up from bed and you decided that you’d be a doctor! A doctor you say? Some laughed at this sight of naiveté, Some supported your decision, but in the end they were sure unimpressed."
    "Whether it had been whispered by Lady Fate or the fact that your father had said multiple times at this point that he’d be very happy if you were a doctor. You had truly no way of knowing which option was right."
    "You remember going to Father to reveal him your latest epiphany. He went to a pensive state of mind. He’s going to succeed me, huh? \nHe bore a lethargic expression on his face–"
    "—not that it was exceptional. \nHe always seems dead to the outside."
    "Maybe not just to the outside."
    
    az "Fuck this guy."
    az "You should forget him."

    "You went on doing a PhD and your father still wears that apathetic face. At least he would if he’d been still there. You haven’t seen him for a long time..."
    "Or you have? You think you really have but you don’t remember when. Was it Yesterday? Last week? Last month?.. Last year, surely. It’s on the edge of your mind but something prevents you to remember."
    "Anyway, it shouldn’t have been that important if you can’t remember."
    # "At least, I wasn’t {b}bored."

    pause 1.0

    "You close your eyes for a few seconds, in the never ending void, to get a little bit of rest, the road was long today and you’re not even arrived. It really desesperates you."
    "Surely one or seconds of sleep won’t hurt, right?"

    am "Hey Gap? Are you sleepy?"

    "This deep voice calling awakens in you a surge of uncomfortable geyser and you come to find myself jumping and groaning, letting out some squealings go."

    am "Oh my god don't move like that!"

    "Despite hearing an agitated man, gesticulating and whining around, you’re still not quite out of your slumber; The landscapes are all blurry and you can’t really distinguish them from the road."
    "Sandpaper bags obstruct the path of your eyelids and every blink feels like pin and needles. The ruthless spikes pierce through the shutter lids veiling my view."
    "The weariness of the road made your legs drowsy and the numbness flows through your veins in every muscle of your body. Fighting against it, you blink even more."
    "Sootheness and comfort; every time you blink through it, the needles in my eyes fly through the wind, the shards of glass melt up from the spores of your skin between the strands of hair."
    "You are soon out of my reverie when Ammon speaks up again."

    am "Hey are you there??!"

    "Panicking for you, he thinks over how to get you out of it. His arms around your waist tighten and his chest draws nearer to me, and at this moment the warmness emanating from the torso of his invades every piece of hair of your body."
    "Boiling and beating his chest; A shiver runs through your spine, then another one runs though. A old sentiment all too familiar grows inside of you and you don’t like it. you don’t want to find out what happens next if he keeps at it."
    "You shove him off."

    hl "Oh my god let go!!!"

    "Your immediate reaction causes you to veer off track."
    "Slaloming and slaloming, you get hardly back the control of the motorcycle. It shakes you both a lot. Now he’s squeezing you even more and won’t let go."
    "You manage to stabilise the vehicle pretty fast but you’re still quite nauseated from the experience."

    am "Oh good Lord…"

    "He lets go."

    stop music

    pause 1.0
    play sound "audio/sounds/car_white_noise.ogg" loop fadein 1.0

    "After some time, a sort of strange quietness grew and loomed over the both of you two. It was uncomfortable, wondering what might have caused all of this agitation early on."
    "The guiltiness start to take its toll over you, you didn't make a good job to keep focused on the road. A mingle of shame builds up in your throat and it’s stuck no matter how much you gulp."
    "You throw some quick looks in the mirror to see if there’s any casualties with Ammon. Apparently he’s fine so you relax a bit."
    "Although his undecypherable gaze under his helmet makes it difficult to know for sure but his ominous aura penetrates all of your pores and tinges all of your body."
    "At some point, the silence itches you; you want to stop driving and scratch the back of your head, his cold stare is staggering your neck."
    "The hum of the vehicle barely fills the glacial air and no matter how much fast you go, the biting frost won’t stop nimbling on you."
    "With guiltiness creeping up, you fire more and more worried looks in the mirror to check on him."
    "Constating the situation hasn’t evolved—you could’ve not picked enough information given the situation anyway—you try to think up something to break the ice."
    "You hesitate, you didn’t do anything wrong right? You just were unfocused for a moment and got back in control pretty fast. Nothing to write home about."
    "You squeeze the handlebar, fearing the moment you’ll have to open your mouth about it. It couldn’t be that hard, could it?"
    "You gather all of your courage and brace yourself for the challenge to come."
    "You close your eyes, say those two words slowly."

    hl "{cps=10}I apologise{/cps}{nw}"

    am "I’m sorry."

    "Ammon interrupts you. You’re flabbergasted—what did he just say—your ears couldn’t hear it. They quiver and raise like an antenna looking for the signal; it shouldn’t be possible what you just heard."

    hl "What did you just say..?"

    "You can’t help myself but turn your head around. Maybe in front of you, you’ll see that you were mistaken."

    am "I said I’m sorry{cps=3}...{/cps} for yelling at you. Are you happy?"

    play music "audio/music/Eleventh Hour - OneShot.mp3" fadein 1.0 loop

    "He reasserts himself. He crosses his arm sternly. It looks like his pride has been shamelessly plundered. He looks away and avoids your glaze. He shows a face of discomfort and akwardness."
    "That took him a lot of efforts, apparently—he’s the type to be a knucklehead about it—he wronged you a lot of times and he doesn’t usually own up to it."
    ## TODO: maybe add a short anecdote here
    "You grin bittersweetly, realizing you have been cut off in you tremendous amends to make it up to him."

    hl "Oooooooh looks like the Big Bad Wolf can be sorry sometimes?"

    am "Oh shut up and just drive."

    hl "Ahah ok Big Baby Wolf."

    "He contorts himself in his place at your snickering, not pleased by your teasing."
    "It might have been uncalled for but you didn’t care; It was your way to get back at him to all of those years of mocking you endured. You might be the only one he does apologise to anyway."
    "Not that you are the Messiah or anything. You genuinely believe it’s more he doesn’t have a plenty of friends he could apologize to. His irritating attitude repels a lot of people and he also doesn’t like a lot of people."
    "Weirdly, one day, long ago, he set his sight on you and decided you were worthy of his friendship. A tad presomptuous but nowadays you didn’t mind. You know very few people like this so it’s interesting."

    am "You say one more word about it and I’ll push you off the bike."

    hl "You wouldn’t dare, you pussycat."

    am "That’s it, you lost your driving privileges."

    "He jumps on you and starts tickling. You laugh uncontrollably."

    hl "N–No please stop, it’s incredibly stupid what you’re doing!"

    am "You’re the one stupid, You should’ve known better."

    "You brake dryly, unable to withstand his tickling and take a time to catch back your breathing."
    ## TODO: add a bit of between
    "He truly acted like a child sometimes but this didn’t bother you, you did partake in his bickering. In not any circumstances, You would ever cut him off of his childishness."
    "You turn back to him, faking your exasperation to his behaviour, you pout and cross your arms with an exaggerated manner, it all makes you laugh inside."

    hl "Ok Ammon, you should’t DEFINITELY not tickling me while I drive!"

    am "Why should I not?"

    hl "BECAUSE IT’S DANGEROUS YOU MORON."

    am "Not the one driving, not my problem."

    "He pretends to be offended and put his arms over his chest, his face closed to any discussions."
    "But in the end this very, very, tall child needs to be put back in his place, he was becoming a bit too much bratty for your liking."

    $ take_him_out = False
    
    menu very_tall_child:
        "Abandon him here":
            
            $ ammon_score += 1
            "You gracefully get up from the seat. You will have to show him your grandeur so you make up your stance."
            
            hl "You know what? Get off the bike. I'm going alone."
            
            am "No you won't. It's my property, I'm staying on it, I won't budge from an inch."
            
            hl "This might be your bike but I'm driving it."
            
            am "Still."
            
            
            "You had predicted this outcome—Who would willingly let himself get abandonned on the road?—although you find yourself annoyed. If only he submitted, everything would be easier,"
            
            hl "Playing hard to get moved, huh? Be my guest then. I didn't want to come to that but I'm going to bust your fat behind."
            
            "Arms and legs spread; he provokes me and accept your challenge."
            
            am "Make me."
            
            "Your resolve set, you dash to him and grab him from behind, leaving him no room to react. Ammon surprised, tries to wiggle out his way from this situation."
            "Unfortunately for him it's too late, for your claws have tighten the grasp on its prey. He won’t get out any time soon."
            
            am "Stop it! Let me go!"
            
            hl "No, you'll learn to respect me."
            
            am "Please, you will never be able to lift me."
            
            hl "I might! And I might stop if you apologize for tickling me."
            
            am "Never! Let me go or I'll bite!"
            
            hl "Go on!"
            
            "It reached the point where Ammon became an eletric bolt, wiggling and biting in every directions."
            "Now's your last and only chance you might have to lift him off, therefore you put everything once of your strength and start the process."
            "Oh no. He's heavy."
            "Very heavy. More than you thought. Maybe the workout between his studies really paid out. Or he was eating more than he lets on. Whatever may be the case, you find yourself losing control of the big dog."
            "And the bike... I–It–It wont—"
            
            am "It won't stand up!"
            
            "Thusly, the bike loses its balance and the bike, the wiggling dog and you fall to your demise on the grey dirty road."
        
        "Take him down":
            $ ammon_score += 1
            
            $ take_him_out = True
            
            "You gracefully get up from the seat. You will have to show him your grandeur so you make up my stance."
            
            hl "You know what? Get off the bike. I'm going alone."
            
            
            am "No you won't. It's my property, I'm staying on it, I won't budge from an inch."
            
            hl "This might be your bike but I'm driving it."
            
            am "Still."
            
            "You had predicted this outcome—Who would willingly let himself get abandonned on the road?—although you find myself annoyed. If only he submitted, everything would be easier,"
            
            hl "Playing hard to get moved, huh? Be my guest then. I didn't want to come to that but I'm going to take you down."
            
            "Arms and legs spread; he provokes me and accept my challenge."
            
            am "Go on."
            
            "You come up with a plan: I need to lower his guard enough so I could approach him by behind. Then I'll be able to do whatever I want to him. He’ll regret tickling you."
            
            hl "Ok Ammon, you are right. I can't take you down."
            
            "Ammon rises an eyebrow. It's sort of sudden your change of mind but no time to smooth it over."
            
            "First step: Pretending admitting you were wrong; you're both stubborn. Doing that succeeded in confusing him at least."
            
            hl "Besides it wasn't so bad, you're good at tickling. Sure I was driving but I need some tickling from time to time."
            
            "As he looking for a white and black cat named Gaspard, he only sees a stranger in front of him, casually walking closer to him."
            
            "Step 3: Initiate contact."
            
            hl "Let me tickle you, then! You need some too!"
            
            "You jump on Ammon and assault him of tickles, destabilising him enough for him to laugh unconditionally."
            
            am "Ahahah—Stop I can't take it anymore!—Ah ahAhhh."
            
            "You benefit from this window of opportunity for tackling him down on the bike with an armlock of yours he won't get out of so easily."
            
            am "Ouch ouch, okay you've won Gap no need to–"
            
            "You reinforce the armlock shutting him down."
            
            hl "So who thought I couldn't take you down, huh?"
            
            am "Maybe I did... but did you think of that!"
            
            "He pushes the ground with his foot, making the bike fall on you."
            "Thusly, the bike loses its balance and the bike, the submitted dog and you fall to your demise on the grey dirty road."
            
        "Push him off":
            "You quickly get up from the bike and decided that someone needed to learn their lessons."
            "You silently get near him and stay there for a moment, getting Ammon uncomfortable more and more."
            "At your concerning sight, Ammon starts fidgeting with his helmet, lost for words. His boot tapping the ground reinforces his ominous presentiment."
            
            am "Are you alright, Gap?"
            
            hl "Yes, I am."
            
            am "Sooooo... what are you standing here for?"
            
            "You keep my mouth shut. He doesn't have to know what you’re about to do."
            "You slowly reach out your arms to him, innocently. He doesn't have a clue in the world, of your ill-intended thoughts. That'll make his fall even harder."
            
            am "A hug? I thought you didn't like being touch–"
            
            "As he spoke, you thrust him without any warning off the bike"
            
            am "Oh motherfu–"
            
            "He violently hits the ground with a loud thud, the bike following him on his fall. He loudly moans and seethes. He’s hurt everywhere."
            
            am "Dude, what the hell??? What was that for? Why have you done that??"
            
            "You fall silent. You clearly weren’t expecting this outcome. You won’t lie saying you didn’t appreciate seeing him on the ground, all dirty, whining, whimpering and howling."
            "But you’ve come to regret it: You didn’t plan to hurt him that far."
            "Very few moments pass until you mull over it and choose he needed help"
            "You extend your hand to him, apologetically, trying to make up to him."
            
            "But he swats off your hand, get up without any help, dust his clothes off flee your glaze.."
            
            am "No, no, I am good. I guess that's my retribution for tickling you."
            
            "Tinges of sarcasm ooze off his words, accusing, incriminating."
            "It was clear that you misbehaved here."
            "Strips of blood drip off the wounds Ammon has got when he fell from the bike."
            "He sets at licking at it, very intensively."
            
            hl "Maybe you shouldn't do that."
            
            am "Maybe you shouldn't have thrown me off."
            
            "The silence grows heavier between the both of you, you genuinely not knowing how to own up to it."
            
            am "... Let's just go."
            
            "He climbs back up on the bike and you follow his lead. You drag your paws on the ground, a bit regretful to return on it. You wished you hadn’t pushed him off but the misdeed is done, no return possible."
            
            "You take back the road and continue to your destination."
    
    if ammon_score >= 1:
        "Aftermath passed, you both lay on the road. You hear Ammon cough. You look at him worriedly. Is he hurt?"
        "He doesn't look all bad, although he has bruises here and there. The next moment, you notice you are all bruised too. On your hands, arms, head, everywhere." 
        "Your clothes are dirty and you feel bad because you had just washed them this morning."
        "Your primal instinct hits and you lick all of your injuries. Arms above your head, tongue in your armpit; A longing stare hammers at you so you spin toward the source."
        "You contemplate a smirking, dirty dog, snickering. You fluster. He has already seen you doing that; what’s that so funny about it right now? You sulk and embarrassingly continue to lick at the wounds. But he still looks at me."
        
        hl "Could you stop looking at me? I don’t know what’s so interesting about it but it’s embarassing me."
        
        "You turn away, fleeing eyes, wanting to put you into a mouse hole away from the judging world, from any peeping eyes of your unfortunate pulsions."
        "Heats of wave overrun your cheeks and the then pure white turn into a cherry pink of embarassement."
        "All of the sudden, a raspy sound of tongue licking the filthy crusty fur pierces your eardrums and you can’t help but look at the source of the sound." 
        "The spectacle you see there is all intriguing—or you could say—captivating."
        "There before you beholds a filthy dog on the ground, wrist, above in the air, being licked that same raspy tonge you’ve heard." 
        "His damp muscle runs through all over and all abroad his wrist. He stops in his deed and raise his head, interested by your stare."
        "You share a meaningful glaze, could have lasted for centuries, if your limbs didn’t ache on every inches of your body."
        "Although the pain gradually fades away, Ammon, content of his little show, stares at you mischeviously."

        hl "Care to explain?"

        am "It’s just...{w} Everytime I look at you doing that, you start to fluster and get really awkward."

        "Ammon sits back on his behind, extends his legs and look at the sky and the clouds passing by, diamonds in his golden eyes. You look for the meaning of his words in his sunflowers that he uses to see. But I only see a glint of "

        am "When you lick yourself, when you purr, when I throw a ball of yarn at you and you start rolling around fighting to death, I find myself enjoying those moments when you let your guard down, when you show that you are not a stuck–up dork."
        am "But afterwards you always become this grumpy cat ashamed of what he is." 
        am "I just thought I could cheer you up by showing that it wasnt’t that bad, that you shouldn’t feel so bad about it. That it’s not that embarrassing, do you see what I mean?"
        
        "At these words, You couln’t hold it any longer and muffled snickers escape your little nose. Soon it becomes a loud laughter as you unleashed the last strands of your joie de vivre."
        "He was being truly embarassing."
        "Ammon, amused by your sudden change from sultry to euphory, follows and you two lose yourself in the silliness of the situation, reminiscent of older times."
        "You finally calm yourself, wiping out your tears of laugther and you slowly get on two paws. You stretch out to get you back on track." 
        "You purr out of satisfaction. You had not brawled like that for a long time."
        "You realise that the time where you would fight like that with Ammon died long ago, and you only regret now." 
        "The studies and annual exams overflowed your world and you have come to forget your support when you drowned slowly."
        
        hl "Ahah ok ammon let’s go–"

        "Ammon has not got up, he continues to lay there, eyes lost up above in the sky were the stars start to show themselves."

        hl "Ammon, are you alright?"

        "You extends your hand to him, although no immediate reaction seems to get out of the pensive puppy. At last, he notices you and take up your offer and grabs your hand."

        am "Yes I am..."

        "You manage to get him up, standing, despite his weight—or is it you that have really weak arms?— and you wait for the rest of his response."

        am "... By the way thanks for dirtying me, you asshole?"
        
        hl "Me an asshole? It’s you and only you that brought it upon yourself. If you weren’t teasing me so much, I would have to hit you."

        "Ammon reaches his hand to you."

        am "You know what? Let’s make a truce. Let’s say we’ve both assholes. Deal?"

        "Too tired to even argue, I firmly grasp it and shake it confidently."

        hl "Deal."

        "Like that, at a smooth pace, you climb back on the bike and set back on the road."

    "A bit of quiet followed, with the hum of the bike soothing your weary soul, your eyelids becoming heavy again, to your disliking."
    "It reminds you it already happened earlier, when the sun was setting. You had quite an argument with your friendly companion."
    "Then you remember that you never really apologised for what you did."
    "You gather your lost courage and you muster these words, caught in your throat."
    
    hl "Hey buddy?"
    
    am "Yeah pal?"

    "You sigh. You really don't want to do that but you have to."
    
    hl "Remember when I was falling asleep and you woke me up?"
    
    am "Yeaaaah..."
    if ammon_score >= 1:
        am "But you know, I haven't been correct to you either, you don't have to{nw}"
    else:
        "Ammon just stands there, without saying a thing, as if what you are going to say has been due to him for a long, long time ago and he was craving for it."
    
    hl "I forgive you.{w} I apologize too. I should’ve kept my eyes on the road. It’s been irresonsible of me."

    "You lower your head of shame."
    "You don’t know why you were so distracted but you could’ve died both with your tomfoolery. You won over the fatigue thanks to Ammon but will you be so lucky next time?"

    am "Ooh? Mister Responsible Goody Two–Shoes is sorry? Mister is ashamed of what he’s done and wants to atone for he has sinned?"
    
    if ammon_score < 1:
        "{cps=20}Annnnd{/cps} there it is. Your asshole of a friend you know."

    hl "Oh shut up. I will take back what I said"

    am "Nah, nah, don’t worry, I’ll stop teasing you about it."

    "He puts back his boiling arms over your waist to tighten his grip. You don’t push him back as you value his safery more than your comfort."

    am "Besides, the quietness was unsupportable. I couldn’t bear to be mad at you all of the trip and we just started."
    am "And it looks like you’re getting sleepy so I’ll get just right enough on your nerves to keep you awake."

    hl "And you’re damn good at it because I already want to shut close that mouthy trap of yours."

    "As you grit your teeth holding back to steer you in the ditch on the side of the road to not hear his voice anymore, he slids his damp muzzle on your shoulder."
    "You hadn’t noticed but he has raised his visor just jor the sake of this maneuver."

    am "That’s the gist of it."

    hl "Ammon, I don’t know anymore if you’re trying to help or distract me."

    am "Gueeeeessss."

    "He wants to distract me."
    "Get at him, show him who the boss is—he's teasing you, he deserves it."
    
    am "Come on, Gue{nw}"
    
    "He was about to finish this annoying phrase when a sneaky hand grabs his muzzle and squeeze his muzzle shut."
    "It seems you have run out of your clemency toward the teasing dog. A pretty long amount of time pass, interspersed by some squeaking and whining, before you estimate that the little sinner has understood and let him out."

    am "Aargh—"
    
    "Falling out of balance, you squeeze his embrace tight over you to make him stay on the motorcycle."

    am "What the hell was that??"
    
    hl "You shouldnt distract me, Ammon..."

    am "... Get lost."
    
    hl "Yet, here I am, stuckn with you."
    
    am "Don't say to my face you don't enjoy my presence, Gappy."
    
    "You must admit he has got a point. In your so dull life, your friendship with him shines through the in dark deep cloud tide."
    "You grin."

    am "Anyway, aren’t you excited?"

    hl "For what?"

    am "For what??? Do you really know where you’re going???"

    hl "Yes yes, I know… Oh yeah right."

    am "Yeah you know, the hotel??"

    "Yesterday You were appalled by Ammon for he had something important to tell you. Apparently you’ve been \"broodier\" than usual——according to his words."
    "So he presented a solution for you: he was invited to a trip to a luxurious hotel in Paris."

    am "Aren’t you a little curious about it?"

    hl "Yes I am…"

    am "So what do you want me to tell you?"

    menu the_hotel:

        "How did you get it?":
            hl "I mean, you’ve come out of nowhere and brought it up"
            hl "I’m just wondering how possibly you could’ve get a trip to an very fancy hotel."
            hl "I’m a bit confused, no matter how many times you say it to me."

            am "Ahah it’s a {cps=10}secreeeet{/cps}."

            hl "Oh please stop being mysterious and just tell me."

            "He takes a pause for a moment, his eyes looking around."

            am "{cps=5}I...{/cps} I got invited to it."

            hl "You got invited? What do you mean? Have you been selected to a lottery or something like that?"

            am "Not exactly… I’ve received a letter saying I’ve been selected."

            "He shifts uncomfortably in his place, searching for a better position."

            am "It said I could bring a plus one…{w} So I choose you."
            am "You looked kinda down lately…"

            "Having been told this repeatedly, you brush off this last comment and focus in the elephant in the room."

            hl "Who invited you..?"

            am "… Nicolas Lecloq."
            hl "Nicolas Lecloq??? {b}THE{/b} bilionaire?."

            am "Him in person."

            hl "How’d you know it’s not fake?"

            am "I’ve made my research."

            "That’s a pretty vague answer he just told. You can’t help myself but squint."

            am "I know it’s not clear——but trust me."

            "Well you are already on this bike on the road of Paris so it’s bit late to turn around."

            hl "{cps=3}...{/cps} Alright."

            am "Good."
            am "Have you any other questions?"

            jump the_hotel
        
        "Do we have to pay for anything?":
            hl "I mean, I’m not really whealthy lately so I don’t know if I could pay it all."

            am "Think for a second, Gap."

            "He locks his gaze in yours and yours could only focus the periodic sunset simulated by his eyelids on his gold eyes."

            am "It doen’t look you’re thinking, right now."

            hl "Yeah, I was thinking of a sunset."

            "Ammon tilts his head quizically."

            am "{cps=3}...{/cps} Anyway. What I meant to say, do you think you would have to pay if you were invited to sleep to your friend’s house?"

            hl "Um… no. Because I was invited?"

            am "Exactly Gap, so do you really think we’d have to pay when we were invited to a hotel?"

            hl "I don’t know, Am… all is not very clear…"

            am "I’m going to reassure you: it’s all fees included even the food and the drinks."

            hl "Ok…"

            am "Anyway do you have any other questions?"
            jump the_hotel

        "What’s so interesting about it":
            hl "I mean, you seem very excited by all of it."

            am "Why should’t I? You’re the one who isn’t enough excited for me."

            hl "What’s in this hotel that gets you so much hyped up?"

            am "Do you listen to me sometimes? This isn’t just a simple hotel. It’s like a fancy complex!"

            "Yeah the name gives the mood much——{i}Le Jardin d’Éden{/i} or The Garden of Eden."
            "Pretty obnoxious name."

            am "There’s a pool, a theatre, a casino and most importantly an exposition!"

            hl "An exposition? About what?"

            am "Oh many things but more importantly, about World War II!"

            hl "Oh right... for you PhD in History."

            "To be honest, it wasn’t just for the studies. Ammon is usually very passionate about History."
            "But the span of time he is the most passionate about is the 39—45 period."
            "For a long time, even talking about it was frowned upon. It was a clear taboo of our society"
            "It was clearly an effort of our traumatised population to get over it, to turn the page so not talking about it was easier."
            "The only thing it was talked about was the Resistance and its wonderful endeavors to fight off the invaders out of our country."
            "However lately people have started to bring this thorny and touchy topic back on the table."
            "Hence this exhibit somehow."
            "It looks like Ammon wants to take part into this endeavour."

            am "Anyway, do you have any other questions?"
            jump the_hotel
        
        "I’m all good.":
            hl "I think I’m all filled in."

    am "Well if you haven’t anymore questions, you sure are all filled in!"

    hl "If you say so…"

    "While you say that, you pass in front of a road sign, indicating a rest area nearby."

    am "Gapgap?"

    "You can’t help yourself but roll my eyes to the back of your head hearing this corny nickname that you hate."

    hl "Yes Amoney..?"

    "Not at all in the world fazed by the sweet nickname I just gave him, he jumps on his seat, his butt shaking moderately the bike, your could even hear his tail wiggling."
    
    am "Can we make a stop? You are quite sleepy? And…"
    hl "And?"

    am "I need to take a piss."

    hl "Fiiiiiiine, we’ll make a stop. I do need it."

    am "Thanks Gapgap!"

    hl "Stop saying that or I’ll break your knees and make you piss on yourself."
    
    am "You wouldn’t dare Gapgap…"

    hl "Don’t test me, Ammon."

    "And like that we leave the road onto the branching exit path."
    jump rest_area_1
    
label rest_area_1:
    
    stop music
    stop sound

    scene parkingLot
    with fade
    play sound "audio/sounds/bird_chirping.ogg" loop
    
    "The moto steers over on the parking lot. The wind has taken his liking over his liking over a blade of grass and a can of soda."
    # "With a lazy eye, you follow those lost souls. I hope for them that they'll find a place to rest. The trash passes in front of some restrooms, deserted of all life and not very well maintained." 
    # "The leaves fly, of trees that has seen more you could ever account for them into the breeze then onto the vast lands of grass."
    "You clumsily stumble out of motorcycle and try to get rid of my helmet in vain. Your ears are stuck in it and the motivation to get them ebb away to the shores of your mind."
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
            
            "For a moment Ammon still struggles to remove your helmet. The pain is really insufferable and you both pull like idiots trying to pull out Excalibur. You yell out of pain and he apologises hoarsely."
            "At some point, you feel with your united combined effort, you have made a difference on the helmet and is ready to give in. Suddenly there's a pop and you fly out of the helmet on the grass rolling for a considerate amount of time."
            "When your frenetic charge comes to stop, you cough out the dirt and the blades of grasses caught in your mouth. You shake up your head so your blood flows back in it. When you come back to your senses, you are met with a laughing dog unable to stop."
            "His piercing laughter overwhelm your space and you get red of embarrassement irresistibly, despite you. You clutch the grass and pluck it out of rage. You throw some at him to make him shut its long snout trap that serves him as a mouth."
            
            hl "Oh my god, you irritating imbecile! I told you you shouldn't pull that hard! I'm all scratched and dirty now. I hate you, you hear me??"
            
            "Ammon wipes out his tears of laughter and approches, triumphing, over you. His wicked smile pierces his helmet as he hands you your helmet and reach a hand to you."
  
            am "Okay you crykitten, keep whining all you want. But if you stay on the ground, you won't get anywhere, will you?"
      
            "You grit your teeth as you clutch his hand. He carries you off the ground that you find yourself levitating. You often forget his undog force and that comforts as you can trust your dear friend."
        
        "I can do it on my own, no thanks":
            "You don't need the help of that prick. You already did it without his help before, so why couldn't you do it again now... or did you?"
            hl "I don't need your help. I can deal with it on my own."
            
            am "Alright... Suit yourself."
            
            "You don't wait for him to try removing yout helmet. However you are met with a very concerning issue: It really is stuck. No matter how much you pull or the angle you use, your ears won't budge so it won't come off."
            "As you panick, you wiggle out in every directions possible, almost rushing in the motorcycle or Ammon, concerned by the show you're putting on."
     
            am "Are you sure you don't need any help? you sure look like so."

            hl "I'm fine! I don't your help or anyone help! I'm going to do it alone like I used to!"
            
            am "Um, ok... I guess?"

            "In your wrestle against the helmet, you keep spinning around until you get nauseated from the all over experience."
            "By a thread of luck or misfortune, you manage to get rid of your helmet. However with all your dances and twirling, you lost sense of directions and you lose balance making you fall into the grass."
            "When your frenetic charge comes to stop, you cough out the dirt and the blades of grasses caught in your mouth. You shake up your head so your blood flows back in it. When you come back to your senses, you are met with a laughing dog unable to stop."
        
            am "Deserved it, jackass."
      
            hl "What did you say?"
 
            am "Nothing. Just get up. You won't get anywhere like this."
            
            "You get up. You rub your head out of pain and you can feel a nasty bump on your head. Maybe you should've asked for Ammon."

    "You scramble out of the grass and rush toward the rear mirror of the motorcycle to watch your face and check any scratches that might have landed there."
    ## TODO: Illustration of gap looking in the mirror
    "As you look into it, you behold a scrawny cat in his twenties, with a medium stature, not really delighted but a bit grumpy." 
    "You sigh. You would not want to be a relative of this cat. Then you have to remember. It's you."
    "Unfortunately you were not so lucky and your usual pure white–crystal hair face is tainted by some dirt and injuries." 
    "You lament yourself on your state. Other than your scratches, you don't look so good either."
    "Your tired eyes look like you haven't slept for a week—and you might not have—as the dark rings under your eyes draw themselves on a too much big surface." 
    "You scrub them, however they remain unchanged and any try to make it go make clear that they won't go away."
    "You check your red eye, swollen by the fatigue, you prod the inferior eyelid at it. The capillaries running through your green jade eyes sclera pulse a like a living entity."
    "It surveys you. It judges you. It's going to create problems for you as your intimacy is its too and will make what it wants about it." 
    "You are annoyed at it and even more you are scared of it."
    "The newt moment, it disappears and you are then alone with your no better thoughts, still uncomfortable that someone might be watching you." 
    "Just a wrong step and you're done for. Don't ever misstep, you hear me? Not ever. You are a deviant and you know it."

    am "Hum Gap, what are you looking at? You've been staring it for quite some time now."
   
    "Ammon tilts his head from the other side of the motorcycle to look at your reflection in the mirror, searching for the thing you've been looking at with a fierce intensity." 
    "Obviously he doesn't find it so he tilts back his head uninterested."

    am "You've got to stop looking at yourself like that. You look like you are on the brink of murdering your wife."

    "With this disturbing statement, Ammon goes on to get rid of his helmet." 
    "Realising he has got some points, you cut off your sight from your other you and you look at him inquisitively, wondering where he might have had this idea. You weren't that unhinged, were you?"
    
    hl "Do you need help with your helmet, Ammo? You may use some given.. your head shape..."
    
    am "It's alright, pal. I can deal with it on my own. I'm used to."

    "The cocky dog removes his helmet elegantly without any issues nor events whatsoever. He wiggles his head finally free from his protective plastic jail." 
    "What a show–off. But a good show–off."
    "The thing to catch your attention within him is his eyes. His priceless golden eyes shining more than any sun you've seen." 
    "You find yourself mesmerising in these luxurious jewels." 
    "These piercing cruel eyes look through your soul and you are read like a dirty open book. At any time, if he feels like so, he can pick an excerpt from it and study it attentively to your expense and guess who you are from it alone."
    "One thing you are grateful for is that he isn’t your enemy. He’d bring you down in an instant and you hate it so you always bicker with him to make you forget that he is objectively better than you in every domain possible."
    "He is handsome, he is charming, he is charismatic, he has a sense a sense of style you try to copy but you have ultimately not." 
    "You may want to say that to him but he’d say that you’re being too emotional and being girly so you always shut yourself."
    "He often wears biker suits because that fits his life style he told me. He rocks it and he knows it so his outfit justifies his usual cockiness and his smiling mug." 
    "He also wears golden face piercing. It really amplifies his rebel attitude."
    "He happened to be a black pharaoh hound and he loves ancient egyptian history so during his teenage years he fully embraced the imagery of it and it suits him so well that you can’t separate Ammon of his extravagant jewelry."
    "You wish you could be as extravagant as him and take crazy risks but you are not as bold as him so you keep to your little classic shirt with your tie." 
    "It goes well on you so you don’t try to be original, scared to get ridiculed."
    "You hope, one day, you’ll break the ties that roots you to your plain life and take the chance to be as free, as liveful as liberated as him." 
    "But waiting for that moment, you admire him from afar, sleeping in his shadows."
    
    "Despite your fixation on Ammon, you come to notice the deserted rest area you just stop in." 
    "Dead leaves piled up on the border of the roads, signaling the fall has come and taken his toll on Nature." 
    "The brownish orangey landscape contrasted with the bright green of Summer." 
    "The mourning trees stand there, waiting for better times, not expecting for what they’ll have to fight against the hard cold of the winter."
    "Sooner or lather, even their melancholic colours will be replaced by scarcerd branches and the glacial white tucking them to their warm sleep." 
    "Tall grasses remain nonetheless undefeated by the time passing. Some sunflowers still resist, searching for their lead."
    "The usual restrooms stick out of the surrounding nature. They are not at all well–maintained and you come to pity whomever has a pressing desire." 
    "They’ll have to make some concessions and sacrifices on their hygiene and dignity."
    "You stand, wordless, to this pitiful scenery, slowly veiled by the surrounding darkness, the sun setting itself for their desereved sleep." 
    "You wished you had come sooner, as in the present moment, only agonising cries reach over your ears"
    "However, a ghost of future times rises within the dead landscape." 
    "A tall metallic structure stand out with all this misery, a shine, a beacon of what lies ahead. You have seen them a handful of times. A phone booth." 
    "You rarely see phone boothes out in city so to find one in a rest area is even more incredible. Technology goes fast, you think, nowadays."

    hl "Hey look, Ammon! They have a phone booth around here. Isn’t that wonderful?"

    am "Huh? Oh yeah... sure."

    "Ammon doesn’t seem very interested in these incredible structure. You lower your gaze and notice his hand pressing his crotch, clutching his fist at a gradually faster pace." 
    "This explains his lack of interest, you guess."

    am "So you’re going to use it, right? Who you gonna call?"

    "You mull over the question, even though you don’t know a lot of people who owns a phone at home. Only two persons comes to mind."

    am "Is it gonna be you mom?.. Or... Marie–Jil?"

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
    "As he disappears from your vision, you are now alone with your thoughts... and the phone booth. It attracts, implore you to come."
    "So you stare at it longingly. For a moment, you can only stand there, in front of the cubicle, as your eyes runs through it, intrigued."


    
    jump phone_booth

label phone_booth: 
    stop music fadeout 0.5
    scene phone_booth with fade

    play music "audio/music/night_sky.mp3" fadein 1.0 loop

    "You jog towards the deserted phone booth. You hurry yourself to talk to her, to get it done. Dragging yourself the door, you grab with a grand difficulty the handle, not being able to find the motivation to penetrate into the dark cubicle."
    "You turn an inconsiderate amount of times the handle, at last, the dore opens when you shove into it. You mustn’t be in the right mindset to not notice that pulling a thousand times a door will not work on the 1001th time."
    "But you couldn’t give more than a care, your gloominess crashing down at its lowest as you finally set paw in the somber void, pierced by rays of declining sunlight."
    "Blind, by the low current luminosity of the place, you put a considerate time to even find the phone."
    "On the phone box, on a little sign at the bottom of it, it is written \"10 francs for 10 minutes!\" You think the sign bargains a fair deal to you."
    "You search your pockets looking for coins and you find one of 10 francs. Although you are not looking for long as you grab on a well—placed one. The coin has presended itself in your pocket in convenient circumstances you can’t explain."
    "But you sure won’t complain as you slid it into the coin slot. Soon after, the phone screen lits up awaiting your input. You observe carefully as some featuers disturb you: they never had a screen before."
    "With slothness, you press the phone number on the keypad, with petite–size buttons but you manage to input it on your first try, like it has always been your purpose in life."
    "You pick up the phone and wait for the ringing to come and let it resonate in the booth soothing the emptiness of the place. You liked the music tone and you daydream a bit of time."
    "You’ve wandered in your head for a undefinite span of time, the ringing going on and on, the sound receding away in the dark void."
    "You wonder why she puts this much amount of time to respond. Must it be the hour? Or is she’s not home right now? Maybe she has got an extended work shift and wasn’t still able to come this evening."
    "Whatever the reason, it has to be a valid one. You mull over it a bit. She wouldn’t ignore you, would she? Perhaps she is ignoring you and is looking at the phone ringing right now."
    "Suddenly a click travels from the other side of the line as to prove you wrong and make you guilty that she would ever be dishonest with you. You hear an inquisitve, quite sly, feminine voice answering the call."
    
    "???" "... Hello, who is it?"
    
    hl "Marie–Jil, it’s me, Gap!"
    
    mj "Gappounet! It’s really you! I’ve been waiting for your call all day long!"

    "A deep sigh escapes of her long mouth, relieved to hear your voice."

    mj "Have you reached the hotel, yet?"

    hl "No, not yet."

    mj "You’re still on the road? How did you do to contact me then?"

    hl "Well apparently, they started to install phone booths on rest areas over the roads. Isn’t it amazing? Some day, I’ll be able to find phone booths everywhere and to call you anytime I want!"
    hl "Imagine all of the possibilities! One day, maybe, we’ll truly never be apart. This is really wonderful! Technology is going so fast! Everything is going so fast!"
    
    "For a very enigmatic reason, your passion for latest high-tech overhauled your usual gloominess and you find yourself very eager to indulge yourself in this pit of wonders, dreaming for the future of all living beings."

    hl "Imagine for a second, how the americans reached the moon, {cps=120.0}how we will in the future be able to travel to space {cps=150.0}and also how we will be able to even eat without opening the mouth."
    hl "{cps=200}don’tyouthinkit’sfantasticsometimesyouthinkwowtechnolgyandallh\nowrapiditwillreachveryhighstandads??it’sreallywonderfulwhenyouthinkaboutitIwanttoneverdietowitnessthis{nw}"

    "You couldn’t hold my excitation anymore. The words leaving from your mouth were forming before your brain could even process the information you were spilling out at her. Your speaking functions were not functioning anymore."

    mj "Gap, Calm down! Calm down. You’re going to choke on your own words. Take a breath ok? Breathe with me, alright? At the count of three you’ll breathe out, ok?"

    "You follow Marie—Jil’s instructions and soon enough, you manage to calm yourself down and in the end you are able to talk at steady pace."
    "Once calmed down, your lungs stops contorting and burning the air within is able to bring you tranquility to you. Her voice helps you catch back and stand on your two paws."
    "You’re finally able to talk normally now."

    hl "Ahah, sorry, MJ. It’s been so long that I haven’t talked to you! It’s been like what? a week?"

    mj "You’ve talked to me this morning, Honey. But I don’t mind, I love it when you get all worked up over me, my little kitten."
    mj "I didn’t think that you’ll be missing me so much. You’ll only stay 3 day over there and you’re already panting your insides out not even having reached the hotel."
    mj "You’re lucky that I was the one answering the phone. Had it been Dad or Mom, they would have teased the heck out of you. Don’t thank me huh? I almost didn’t answer given the hour."

    hl "It’s not that late..."

    mj "It’s like fifty to eight, at least it’s starting to get late, don’t you think? I don’t think I’ll answer later in the evening. Or my parents will. I don’t think you want to talk to them that late, huh?"

    "She’s got a point. As much as you like her parents, the situation you would find yourself, head–to–head with them, not knowing what to say would be very akward."
    "So you agree with her, not very much a lot you can do more to talk to her later."

    hl "Yeah you are right..."
    hl "Hey, you should’ve come too, to the trip with us! I really miss you!"

    mj "Me? You’re doing great without me, don’t worry. And I wanted to come but you know I can’t, I’ve got to work tomorrow. Have to help out Mom with her restaurant."
    
    hl "You could’ve explained the situation to her. I’m sure she would have let you come."

    mj "It’s not like that, Gap. She just opened her restaurant. I can’t let her down like that. She really needs me, I don’t have the time to travel to a luxuous hotel unfortunately."

    hl "Alright... but next time, you gotta come!"

    "She softly chuckles at your liveliness."

    mj "You know, your attidude earlier reminded me of the time where we fisrt–"

    "Leaned on the booth glass, you twist and twist frenetically the phone cord, and from times to times, you brush your whiskers. A low purring swell up you chest and you try to contain it."

    ## TODO: Illustrate this scene with village
    "You really liked her, she’s a wonderful girl and you wonder everyday how your life would have played out, had she not been in your life at all." 
    "But you chase that thought rapidly as it always sets you in a desesperate state."
    "You are childhood friends and you were stuck together like hand in glove and never you has been seperated from her." 
    "She lived in your birth village, so you used to play together every day."
    "For some reason, she could stand your presence, contrary to most of your peers of your age. That made her a precious friend." 
    "She was always fond of your fantaisies and your games, you had a lot of them when you were young."
    "You would read a book about a boy in a green tunic going for adventures and you would pretend that you are this same boy reenacting the events of the book." 
    "Most kids would take you for a social case and most have."
    "But not Marie–Jil. Marie–Jil played with you in your little pretend games." 
    "You really enjoyed her creativity to modify to the story to her liking, even if at first you really detested her interventions, it had to stay on the rails of the story."
    "One day, a new boy moved in the village and he was a particular boy for sure. Rude, spiteful, trickster, troublemaker, always malicious to people." 
    "Everything you hated within a person. That boy was Ammon."
    "Ammon was a friend of her and you really didn’t like him that much, he would often declare that your games were really lame." 
    "You would argue a lot without a satisfying conclusion. Still Marie–Jil really wanted to you get along."
    "So we gradually stopped playing pretend and Marie–Jil brought out some board games his father got for her from his work or abroad." 
    "You were devastated of that because of that annoying dog, you weren’t able anymore to play what you want with Marie–Jil."
    "So you set you ought to beat him at everything he does. Unfortunately he was no little player, crushing you at everything he does. That only managed to enrage you and make you hate him even more."
    "You wonder how you are still friends with him."

    mj "So um Gaspard, Gaspard, are you listening?"

    "You wake up from your daydreaming, all of these memories have had left you groggy and you are uncomfortably brought back to the current discussion, bitter as you wish to dwell more in your childhood."

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

    hl "Yes I do?"

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

        "I’m having a great time with him and I love it" if ammon_score >= 2:
            $ ammon_score += 1

            mj "Oh really? Surprising... I wouldn’t have expected that you two would get so much along together."

        "He’s been nice with me but his tricks are really bothering me" if ammon_score >= 2:
            mj "I had expected that much with you two."


        
        "I can tolerate him" if ammon_score >= 1:                                                                                                                                                                                                           
            hl "He’s been supportable so far"
        
        "I wish you were with me, not him":
            mj "...Really?"
    
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
    "A burst of voice surges through the phone and you almost drop it. You regain composure. She is rarely mad at you and this time you don’t have a clue what may have released her wrath." 
    "You panic. What happened, for Jesus’ sake? You dig through you mind."
    "Nothing. Just nothing. You’d be satisfied to just see a grain of sand in a sea of nothingness but you won’t even get that satisfaction." 
    "You’re in the void, your head absent, beholding a black box. You open it. Even more void. You’re afraid. You shouldn’t go deeper"
    "You hand’s wet. Every second, you are to the point of letting it slip." 
    "You sweat profusely and you wipe, wipe, wipe and wipe but you can’t fight against the downfall of your mind, wrecking havoc on every light of your soul."
    "You fall silent. Who are you."

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
    