style bottom:
    xalign .5
    yalign .98

screen restarea(screen_active=True):
    tag restarea
    layer "front"

    on "show" action [SetVariable("current_screen", "restarea")]
    
    imagebutton:
        pos (300, 400)
        anchor (.5, .5)
        idle 'ammon_pn'
        hover 'ammon_pn_hovered'
        action [Call("restarea_ammon")]
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
    layer "back"

    on "show" action SetVariable("current_screen", "restareatrunk")
    on "replace" action SetVariable("current_screen", "restareatrunk")

    imagebutton:
        pos (350, 800)
        anchor (.5, .5)

        idle 'ammon_bag'
        hover 'ammon_bag_hover'
        action Call("restarea_bag")
        sensitive screen_active
    
    if not any(item.image == "stick" for item in ga_inventory):
        imagebutton:
            pos (900, 700)
            anchor (.5, .5)

            idle 'stick_idle'
            hover 'stick_hover'
            action Call("restarea_stick")
            sensitive screen_active

    if not any(item.image == "notebook" for item in ga_inventory):
        imagebutton:
            pos (1400, 800)
            anchor (.5, .5)
            idle 'notebook_idle'
            hover 'notebook_hover'
            action Call("restarea_notebook")
            sensitive screen_active
            at custom_zoom
    
    if screen_active:
        imagebutton auto "gui/backbutton_%s.png" action Call("restarea_trans"):
            style 'bottom'
            at custom_zoom

transform start_code:
    pos (1005, 520)

init python:
    def check_code():
        # nice_code = [6, 9, 6, 9]
        basic_codes = ([0,0,0,0], [1,2,3,4], [5,6,7,8], [9,0,1,2])
        if padlock_code == good_code:
            renpy.jump("ammon_padlock_good_code")
        
        elif padlock_code == [6, 9, 6, 9]:
            renpy.jump("ammon_padlock_nice_code")
        
        elif any(padlock_code == basic_codes[i] for i in range(len(basic_codes) - 1)):
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
                    sensitive screen_active

                text str(padlock_code[i])

                imagebutton auto "gui/padlock_rightbutton_%s.png" action [SetDict(padlock_code, i, (padlock_code[i] + 1) % 10), Function(check_code)]:
                    at c_zoom
                    sensitive screen_active

    if screen_active:
        imagebutton auto "gui/backbutton_%s.png" action Return():
            style 'bottom'
            at custom_zoom


label restarea_trans:
    call hide_customgui
    with None
    hide trunkopen onlayer back
    show parking at zpos_bg onlayer farback
    with dissolve
    show screen restarea(screen_active=False) 
    with dissolve
    pause 0.1
    return

label ammon_padlock_good_code:
    show screen restarea_padlock(screen_active=False)
    
    play sound "audio/sounds/unlock.ogg"

    "Finalement, tu ouvres le cadenas. C'est le moment de fouiller dans ses affaires."

    hide screen restarea_padlock with dissolve

    "Tu trouves quelques vêtements, les produits d'hygiène classiques et une quantité inhabituelle de médicaments en tout genre et tu penses que c'est son carnet ?."
    "Tu remarques une autre chose. Une gourde bleue. Tu as déjà vu cette gourde."

    az "Le carnet a l'air intéressant. Tu devrais le prendre."
    az "Peut-être qu'il y écrit ses vilains secrets ? Qui sait ?"

    dk "Attention aux médicaments ! Peut-être qu'il te dit tout. Peut-être qu'il est dangereux et qu'il peut te faire du mal."

    $ picked_from_the_bag = ""

    menu:
        "Saisir les médicaments" :
            $ picked_from_the_bag = "médicament"
            "Le médicament est ce qui a le plus piqué ton intérêt."
            "Tu en attrapes un, et bien sûr, c'est un antipyrétique. Rien qui ne sorte de l'ordinaire. De nos jours, il est utilisé pour traiter les douleurs légères."
            "Tu le remets à sa place. Il reste encore beaucoup de médicaments que tu dois vérifier." 
            "Le simple fait qu'il ait autant de médicaments de types différents est inquiétant."
            "Tout le monde n'a pas une trousse de premiers secours disponible sur soi à chaque seconde."
            "Puis tu tombes sur un médicament très intéressant. Tu reconnais la marque."
            "Tu l'attrapes et tu le tournes dans tous les sens au cas où tu te serais trompé. Tu en as déjà pris."
            "C'est un antidépresseur."
            hl "... Hein ?"
            jump confront_him
        "Saisir le carnet" :
            $ picked_from_the_bag = "carnet"
            "Le carnet est ce qui a le plus piqué ton intérêt."
            "Tu le saisis, tu tournes un peu dans tous les sens."
            "Il n'a pas du tout l'air jeune. Même qu'il a l'air d'exister depuis des lustres. Le cuir usé de la couverture présente beaucoup de coupures en son sein."
            "Il y a des morceaux qui ont disparu. Le livre tient à peine debout. Tu n'oses pas trop le déplacer, de peur qu'il ne se froisse."
            "Tu cherches une écriture sur le recto ou le verso pour savoir s'il y a un nom ou quelque chose qui pourrait t'indiquer la nature du carnet."
            "Bien que, pas de chance."
            "Tu décides d'ouvrir le livre. L'intérieur n'est pas mieux que l'extérieur."
            "Les pages sont devenues légèrement jaunes, certaines pages sont déchirées, beaucoup d'écritures illisibles, des griffures partout. Un vrai gâchis."
            "Dans tout cela, tu parviens à déchiffrer l'écriture d'Ammon et tu es capable d'en lire certaines parties."
            "Une page en particulier attire ton attention. Tu commences à la lire."
            ###TODO:Peut-être le mettre en mode nvl.
            "Samedi 14 septembre 1975"
            "« Cher journal "
            "{cps=50}Aujourd'hui, Howl m’a em{nw}"

            jump confront_him
        "Saisir la gourde" :
            $ picked_from_the_bag = "gourde"
            "Tu ne peux pas détourner le regard de la gourde."
            "Tu as craqué le sac pour ça finalement."
            "Tu le retournes avec précaution, n'arrivant toujours pas à croire ce que tu as devant les yeux."
            "Tu as du mal à te souvenir de l'endroit où tu l'as vu. Cela te démange à l'arrière de ton cerveau. Il te met mal à l'aise. Tu ne peux plus le poser."
            "Il faut que tu trouves d'où ça vient."
            show eye_lid
            show expression "#000" with blink_reverse
            "Alors tu respires profondément, tu fermes les yeux et tu te frottes les tempes. Tu devrais pouvoir te souvenir, n'est-ce pas ?"
            "Tu fais le vide dans ton esprit. Tu as besoin de toute ton énergie. Tu te concentres sur les démangeaisons. Un mille-pattes rampe dans ton crâne."
            "Tu inspires lentement."
            "Tu expires."
            stop music fadeout 1.0
            "Tu es prêt."
            "Tu plonges ta main profondément dans ton oreille et tu frappes la cage de ton cerveau. Tu agites tes griffes dans tous les sens, au hasard. C'est mou." 
            "C'est plus ardu que tu ne le pensais. Même si tu es plus déterminé que cela. Il ne pourra plus échapper à ton emprise plus longtemps."
            "Finalement, tu saisis l'une de ses pattes et tu tires sans sommation. Mais il ne cède pas facilement. Il gratte toutes les surfaces auxquelles il peut s'accrocher. Il est désespéré."
            "La douleur qu'elle provoque te déchire de l'intérieur, c'est comme si on t'ouvrait en deux et que petit à petit, lentement, très lentement, on t'éventrait."
            "Tu te tords de souffrance mais tu n'abandonnes pas. Tu dois te souvenir."
            "Tu extrais le rampant de ton oreille, tu le tiens immobile et tu le gardes sous ton contrôle. Il se met à convulser. Tu dois continuer."
            "Tu enroules tes doigts autour de l'insecte. Tu veux le jeter sur le sol. Ses mille pattes s'agitent sous ta peau à tel point que ton estomac commence à se retourner."
            "Mais tu ne bouges pas. Il le faut."
            "Alors tu l'écrases. Elle ne bouge plus. Tu as réussi."
            "Les entrailles avant chaudes et moelleuses de l'insecte deviennent solidement froides. Tu es troublé. Tu rouvres ton emprise."
            "Un magnifique cocon est posé là. Tu l'admires. Le mille-pattes s'est transformé."
            show eye_lid
            hide expression "#000" with blink_transition
            play music "audio/music/moment_orange.mp3" fadein 0.5
            hide eye_lid with dissolve
            "Attends, tu te souviens maintenant."
            "Pourquoi Ammon a-t-il la fiole de ton père ?"
            jump confront_him

label ammon_padlock_nice_code:
    show screen restarea_padlock(screen_active=False)
    "Sympa le code ."
    "Tu l'utiliserais si ce cadenas t'appartenait. Tu glousses comme un enfant de six ans, tu ne peux t’en empêcher."

    az "C'est très drôle en effet."

    dk "Ne l'écoute pas. Continue à chercher."

    jump restarea_padlock_loop_local

label ammon_padlock_basic_code:
    show screen restarea_padlock(screen_active=False)

    if being_basic == 0:
        "Malgré la saisie du premier code qui te vient à l'esprit, le cadenas ne se soumet pas."
        "Pensais-tu vraiment qu'Ammon serait aussi basique ? Tu es déçu de toi-même."
        "Eh bien, tu devrais quand même continuer à chercher."
        "Et arrêter d'entrer des codes basiques que n'importe qui pourrait craquer. Il est plus intelligent que ça. Cela devrait être quelque chose d'important pour lui."
    elif being_basic == 1:
        "..."
        "Comme dit précédemment, {font=gui/fonts/ApercuBold.otf}Ammon est plus intelligent que ça.{/font}"
        "Essaie autre chose."
    elif being_basic >= 2:
        "..."
        "{font=gui/fonts/ApercuBold.otf}Arrête{/font}."
    
    $ being_basic += 1

    jump restarea_padlock_loop_local

transform custom_zoom:
    zoom 0.2
transform c_zoom:
    zoom 0.05


label restarea_ammon:
    $ persistent.parallax_on = False
    show ammon at american_shot onlayer front
    with dissolve

    am "Salut Howly. T’as besoin de quelque chose ?"
    am "T'as trouvé ce que tu voulais ?"

    if checked_padlock >= 1:
        "Tu remarques qu'il a son portefeuille dans son pantalon sur ses poches arrière."
        "Tu es sûr qu'il contient des informations précieuses sur le code du cadenas. Comme sa carte d'identité avec sa date d'anniversaire dessus."
        "Si tu es prêt à voler son portefeuille..."

    menu:
        "Je veux parler de quelque chose avec toi" :
            am "Qu’y a–t–il ?"

            menu ammon_questions:

                "Tu es sûr que tu n'as pas d'eau ?":
                    "Essayons de le faire ouvrir son sac."

                    hl "J'ai soif et je n’arrive pas à trouver de l’eau.."

                    am "Oui, je suis sûr."

                    hl "Il n'y en a pas un tout petit pour moi ?"

                    am "Non Howl, tu auras beau demander, la réponse restera la même."
                    am e_disgusted " Tu veux que je secoue le fond de mon sac pour que tu voies bien que je ne mente pas ?"

                    hl "Non..."

                    am e_neutral "Alors ne demande pas."

                    "Raté."
                    jump ammon_questions

                "Quel est ton numéro préféré ?" if checked_padlock >= 1 :
                    hl "Hé Ammon, tu as un numéro préféré ?"

                    am e_disgusted "... Qu'est-ce que tu veux dire ?"

                    hl " Genre un numéro à 4 chiffres, tu sais comme 4562 ? 6512 ? 2313 ? Ce sont des nombres intéressants ! Des nombres vraiment intéressants..."

                    am j_noway "Hum non ? Pourquoi j’aurais un numéro préféré à 4 chiffres ? C'est juste stupide ?"

                    show ammon j_neutral

                    hl "Je ne sais pas, j'ai un numéro préféré à 5 chiffres ! Alors pourquoi pas un numéro à 4 chiffres ?"

                    am "... ce qui est... ?"

                    hl "Huuuuuh, {cps=5}6... 8...{cps=2} 83... 1"

                    am right e_smug j_disgusted "Bieeeeeeen...."

                    hl "Mais j'ai aussi un numéro préféré à 2 chiffres !"

                    am j_noway "Oui, je le connais celui-là. Tu n'as pas besoin de me le dire."

                    az "Mais c'est tellement drôle..."

                    dk "Arrête."

                    hl "Oh ok..."
                    jump ammon_questions

                " C'est quand ton anniversaire ? " if birthday and checked_padlock >= 1:
                    $ birthday = False
                    
                    "Qu'est-ce que tu fais ???"
                    "Quel genre d’ami ne connaîtrait pas sa date d’anniversaire ?"

                    dk "Ça peut arriver à tout le monde."

                    az "On dirait que quelqu'un cherche à se faire démonter par Ammon"
                    az "Pas que ça ne déplaise."

                    dk "... Tu ne pourrais pas faire ça ?"

                    "De toute façon, tu ne diras pas ça."
                    jump ammon_questions
                

                "Donne-moi ton portefeuille" if checked_padlock >= 1:

                    am e_disgusted j_disgusted "{cps=3}...{/cps}"
                    show ammon j_noway
                    extend "Quoi ?"

                    hl "Tu sais, le truc carré que tu as dans ta poche arrière ?"
                    hl "On peut y ranger de l'argent, des cartes, des papiers d'identité..."

                    am e_neutral "Je sais ce qu'est un portefeuille."
                    am e_neutral j_neutral "Ce qui me dérange, c'est pourquoi tu me demandes mon portefeuille."
                    am "Tu n'as pas besoin de mon portefeuille."

                    hl "C'est parce que tu n'as pas assez réfléchi à la question."

                    am e_disgusted "..."
                    am "Je vais ignorer ce que tu viens de dire si cela te convient."
                    jump ammon_questions
                "Non rien.":
                    am "Bah casse toi alors"
                
                

        
        "J’ai quelque chose pour toi." if ga_inventory != []:

            am "Qu’est que tu as pour moi ?"

            label ammon_item_present:
                $ evidence_needed = True
                # call screen inventory
                
                if selected_item.name == "Notebook":

                    hl "Ammmon"

                    "Ammon soupire. Il voit ce que tu as entre les mains."

                    am "C'est ton carnet ?"
                    am right "Pourquoi tu me montres ça ? Je l'ai déjà vu."

                    hl "Oui je suis au courant... J'ai l'impression que tu peux me donner des conseils sur un de mes croquis."

                    am "Tu n'as pas besoin de mes conseils, tu te débrouilles déjà très bien tout seul."

                    hl "Je ne sais pas..."

                    am "D’accoooord mais c'est la dernière fois que tu me le montres ok ?."

                    hl "Ok."

                    show ammon front e_neutral j_neutral

                    "Tu lui tends le carnet et il l'ouvre, d'un air bougon, en parcourant les pages."
                    "De temps en temps, tu pointes quelques croquis te rappelant certains souvenirs. Certains que tu as faits au collège. D'autres chez MJ. D'autres chez Ammon, etc"
                    show ammon pupils_down j_happy
                    "Malgré les premières réticences d'Ammon, tu vois un sourire se dessiner sur son visage."
                    
                    am "Honnêtement, je ne sais même pas pourquoi tu me demandes ça, ils sont tous bien."
                    if checked_padlock >= 1:
                        "Pendant ce temps, tu te penches sur lui pour essayer d'attraper le portefeuille qui se trouve dans sa poche."
                        "Le problème, c'est que tu n'es pas vraiment sournois, discret ou quoi que ce soit d'autre."
                        "Alors tu finis par coller ton corps sur le sien, ce qui crée une situation assez embarrassante."
                        show ammon j_disgusted e_disgusted pupils
                        "Ammon hausse un sourcil."

                        
                        am "Hum, qu'est-ce que tu fais ? Il y a quelque chose qui ne va pas ?"

                        hl "Non- Non ! Je voulais juste mieux le voir, c'est tout. C'était difficile à voir de là où j'étais."

                        am j_noway "Hum ok ?"

                        show ammon j_neutral

                        "Tu récupères rapidement ta main de son dos. Pas besoin de rendre la situation plus gênante."

                        az "Tu devrais essayer de voler plus souvent."
                        dk "Ne l'encourage pas."
                        
                    
                    show ammon right e_neutral j_neutral
                    "Ammon referme le carnet et te le rend."
                    am " Content ? "

                    hl "Oui..."

                    am front "Eh bien je suis content d'avoir pu t'aider."

                elif selected_item.name == "Stick":
                    hl "J'ai quelque chose pour toi, Ammon !"

                    am e_disgusted "... Quoi ?"

                    hl "Vite, va chercher, bon chien !"

                    "Tu lances le bâton dans l'herbe derrière lui. Confus, il te tourne le dos."
                    "Tu en profites pour glisser ta main dans sa poche arrière. Tu réussis à l'attraper."
                    "Tu récupères rapidement ta main avec le portefeuille."
                    ## TODO : Show item gettings
                    "(Tu devrais examiner le portefeuille dans ton inventaire.)"
                    $ ga_inventory.append(ammon_wallet)

                    "Au bout d'un certain temps, Ammon te fait à nouveau face, encore plus confus."

                    am " Mais qu’est–ce que c’était que ça ? Qu'est-ce que t'attendais de moi ?"

                    hl "... que tu ailles le chercher ?"

                    am e_neutral j_disgusted "... Je vais poliment ignorer ça."
                
                elif selected_item.name == "Ammon’s Wallet":
                    "Attends !!!!! Ne fais pas ça !!!"
                    "Tu es complètement débile ? Rengaine ça."
                
                else:
                    "C'est bien."
    hide ammon onlayer front with dissolve
    return

label restarea_trunk:
    call hide_customgui
    with None
    hide parking onlayer farback
    show trunkopen onlayer back with dissolve
    show screen restareatrunk(screen_active=False) with dissolve

    pause 0.5
    if not trunk_explored:
        "Tu ouvres le petit coffre à l'arrière de la moto."
        "C'était tellement bourré que t'as été un peu surpris que tu aies réussi à tout faire tenir dans un tel espace."
        "Découragé par cette vue, tu avachis tes épaules - tu ne trouveras jamais l'eau."
        $ trunk_explored = True
    return
    
label restarea_bag:
    $ persistent.parallax_on = False
    # $ renpy.show_screen(current_screen, _layer="front", screen_active=False)
    show screen restareatrunk(screen_active=False)

    if checked_padlock == 0:
        
        "Tu t'approches furtivement du sac de ton ami et tu essayes de l'ouvrir. Tu jettes quelques regards rapides à Ammon tout en accomplissant ton petit crime, mais il semble distrait, ailleurs."
        "Comme tu es discret, tu ne peux pas forcer l'ouverture du sac, alors tu remarques quelque chose qui t'empêche d'aller plus loin sans faire d'histoires."

        # $ renpy.show_screen("restarea_padlock", screen_active=False)
        # $ renpy.transition(dissolve)
        show screen restarea_padlock(screen_active=False) with dissolve


        pause 1.0

        "Tu te souviens qu'Ammon est un type assez prudent, alors évidemment, il a posé un cadenas à code sur ses affaires de voyage. Y jeter un coup d'œil se révélera plus difficile que tu ne le pensais."
        "Tu vérifies si le sac a un trou ou une quelconque ouverture, ce qui te rendrait capable de contourner sa sécurité." 
        "Malheureusement, pas de chance. Pas de déchirure, pas de défaut de fabrication, pas de trou, rien." 
        "Tu secoues le sac.{w} Il est rempli à ras bord."
        "Tu réfléchis un temps, ça ne devrait pas faire de mal d'essayer quelques combinaisons avant d'abandonner."
    
    elif checked_padlock == 1:

        "Tu te dis que tu n'as pas assez essayé et qu'il faut continuer à deviner. Tu trouveras sûrement un jour. Avec suffisamment de détermination, tu le craqueras ne t'inquiète pas !."
        "Mais n'oublie pas qu'il a sûrement entré une date qui lui est chère, comme tu pourrais le deviner, son anniversaire, d'accord ?."
    
    else:

        "Tu pourrais faire un autre essai. "
    
    label restarea_padlock_loop_local:
    # window hide
        call screen restarea_padlock(screen_active=True)
    
    if checked_padlock == 0:

        "Eh bien, à quoi pensais-tu de toute façon ? Tu penses vraiment qu'il a mis un numéro au hasard dans son cadenas ? Non, ce n'est pas possible. Ammon a sûrement mis un code comme une date qui lui est chère ou quelque chose comme ça."
        "Peut-être son anniversaire. Ça devrait être assez facile. Tu n'as qu'à mettre sa date de naissance dans le cadenas et tu pourras le déverrouiller, n'est-ce pas ? Allez, fais-le. Tu es{cps=3}...{/cps} capable de le faire{cps=3}...{/cps}..."
        "{cps=3}...{/cps} Attends. Tu as vraiment oublié l'anniversaire d'Ammon ? Tu as vraiment honte. Quel grand ami tu es. Oublier son anniversaire. Beau travail."
        "Très bien, continuons. Tu sais ce qu'il faut faire. Tu devrais chercher à connaître son anniversaire. Mais ne lui demande pas directement. Il {b}se mettra{b} en colère. Ce serait mieux si tu pouvais le trouver en secret."
        
        $ checked_padlock += 1
    
    elif checked_padlock == 1:
        
        $ checked_padlock += 1 
        "Ok, on dirait vraiment que tu n'iras nulle part avec ce que tu fais. Il y a des façons plus intelligentes de procéder."
        "Cherche juste le code, ok ?"
    else:
        "Ok, tu devrais juste retourner à tes recherches."

    return

label restarea_stick:
    show screen restareatrunk(screen_active=False)
    "Oh un bâton."
    "Tu te demandes comment il est arrivé là."
    "Eh bien, autant le prendre alors. Tu pourras peut-être l'utiliser avec Ammon."
    
    $ got_stick = True
    $ empty_inventory = False
    $ ga_inventory.append(stick)

    return

label restarea_notebook:
    show screen restareatrunk(screen_active=False)
    "Oh voici ton carnet bien aimé que tu emmènes partout avec toi."
    "Tu devrais lui montrer à nouveau à Ammon."
    "Tu pourrais aussi continuer à faire des croquis avec. Emmène–le."
    
    $ ga_inventory.append(notebook)
    # $ check_inventory_empty()
    $ empty_inventory = False
    $ got_notebook = True

    return