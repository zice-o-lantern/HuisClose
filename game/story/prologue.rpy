label prologue:
    
    queue sound "sounds/cold_wind.mp3" fadein 2.0 loop
    # Black scene
    scene black
    
    cl "Jamais je ne l’aurais cru."
    cl "Jamais je n’aurais cru que tu puisses l’étrangler ainsi."
    cl "Même{w}, je n’arrive toujours pas à y croire."
    cl "Je me tiens là{w}, hagard, et pourtant, je n’arrive pas à détourner le regard."
    cl "Tes mains, onduleuses, rugueuses, effilées comme des branches mortes se serrent autour de son cou, perçant sa carapace."
    cl "Je déglutis.{w} Je ne devrais pas contempler ça. Ce macabre spectacle devrait me dégoûter."
    cl "Pourtant je ne détourne pas le regard. Tes yeux luminescents, chatoyants, amarrent ma raison dans cet océan d’étoiles."
    cl "L’insecte dormant en mon cœur se réveille, enfin... ou avait–il ouvert ses yeux auparavant ?" 
    cl "Peut–être que ce cœur ne m’appartient pas, finalement."
    cl "Quoi qu’il en soit, ces sentiments familiers, que Dieu m’a maudit avec, fourmillent en moi. Je ne peux plus le nier."
    cl "Je sais que ces deux feux follets avec lesquels tu m’épies, me scrutes ne sont que des illusions.{w} Des leurres pour corrompre le peu qui reste de moi."
    cl "Je sais, cependant, que ton pouvoir, ta lumière, ton don..." 
    cl "Il peut les apprivoiser, les recueillir, ces monstres de l’au–delà{w}, au sein de ton phare au milieu de la mer déchaînée."
    cl "{cps=3}...{/cps}{w} Combler ce vide qui ronge cet être{w}——Mon être——{w}flétrissant."
    cl "C’est pour cela que,{w} jusqu’à présent,{w} et pour toujours..."
    cl "Je t’aime{w}, Charles{w=2.0}{nw}"
    ### TODO: Show title logo
    stop sound
    $ config.window_hide_transition = None
    window hide
    pause 1.0
    # play sound 'audio/sounds/car_white_noise.ogg' loop
    jump little_road

label little_road:
    # show ruralRoad
    # with Fade(0.5, 4.0, 0.5)
    scene black

    show ruralroad
    with Fade(0.5, 4.0, 0.5)
    camera at zpos_camera

    "Tu te réveilles, au toucher glacial qui s’empare de ta nuque."

    hl "Ahhhh—"

    "???" "Alors, pas trop fatigué ?"

    "Tu lèves les yeux et malgré le voile noire recouvrant ta vue, tu arrives toujours à distinguer les traits de la personne en face de toi."
    "Elle porte un casque et une veste de motard noirs. Impossible de voir son visage. Mais tu n’as pas vraiment besoin de le voir."
    "Tu sais qui elle est."
    "Elle reprend sa typique posture, croisant les bras, tapant du pied."
    show ammon at american_shot with dissolve
    
    "???" "En train de pioncer, hein ?"

    hl "Huh, de quoi ?"

    "Elle te laisse reprendre tes esprits à ton rythme."
    "Tu enlèves le casque, te compressant la tête. Ces fichues longues oreilles ne te facilitent pas la tâche."
    "Après avoir remué tes petites moustaches, et toute pilosité faciale qui te reste, tu retires tes lunettes de ton fin museau et tu te frottes les yeux."
    
    hl "Quelle heure il est ? Il est tard, non ?"

    "L’homme au casque pouffe."

    "???" "Il est environ 18h, il est pas si tard."
    "???" "Tu peux bien rester éveillé quelques heures de plus non ?"
    "???" "Je voulais arriver à la Maison avant la tombée de la nuit mais c'est un peu tard pour ça"

    "Tu baisses les yeux et étonnamment, tu te trouves sur une moto, assis."
    "Sortant ton chiffon, tu essuies la buée qui obstrue les verres de tes lunettes." 
    "Tu aimes penser que tu n’as pas une si mauvaise vue mais tu ne peux qu’admettre que, sans elles, tu aurais dû mal à te concentrer, amplifiant la constante fatigue mentale sur tes épaules."
    "Une fois les lunettes posées sur ton visage, l’écriture en face de toi, auparavant trouble, devient clair, la mise en point moins laborieuse qu’avant."
    "Tu peux y lire la marque de la moto et tu ne retiens guère le nom, les automobiles ne faisant pas partie de tes intérêts."
    "Tu tournes ta tête pour observer les alentours. Des étendues de champs de tournesols. Une route déserte mal entretenue avec des crevasses à gauche et à droite."
    "Au loin, dans ton dos, tu aperçois des chaînes de montagnes survolant les horizons. Cela semble si loin de chez toi."
    

    hl "Ah oui c’est vrai..."

    "L’Homme au casque ricane."

    "???" "T’es un peu long à la détente, tu le sais ça ?"

    hl "Arrête de dire ça, On me le dit bien trop souvent."

    "???" "Comme tu veux mais si tu rêvassais moins souvent, je n'aurais sûrement pas te le dire aussi souvent." 
    "Tu ravales les remarques acerbes au fond de ta gorge et tu te contentes d’un claquement de langue."

    az "C’est vrai que t’es long à la détente, au fond."
    dk "Tu ne l’es pas ; tu considères toutes les options, plus que la moyenne, ce qui te prend plus de temps."

    "???" "Par contre, je peux pas te laisser te rendormir."
    "???" "Tu commençais à piquer du nez et je n’apprécie pas les gros objets lourds et froids qui me martèlent le dos pendant que je conduis."
    "???" "Donc tu vas garder tes petites mirettes ouvertes le temps qu’on arrive à la Maison, compris ?"

    hl "D’accord...{w} Ammon."

    am "Bien."

    az "Bon chienchien."

    "Pendant qu’Ammon remonte sur la moto, tu en profites pour renfiler ton casque."
    "Enfin le renfiler, te le fourrer de toutes tes forces."
    "Ces oreilles seront toujours un calvaire quoi qu’il arrive."
    "D’un coup de pédale, Ammon redémarre brusquement la moto."
    "Surpris par la soudaine vitesse, tu agrippes à la veste de l’homme masqué."

    hide window
    pause 1.0

    "Après quelques minutes de secousses et valdingues causées par la prudente conduite d’Ammon, vous vous retrouvez à une allure soutenue."
    "Le vent parcourt ton corps et s’infiltre dans toutes les petites ouvertures de tes vêtements. Le blazer, virevoltant à la brise, noir n’offre que peu de protection."
    "Tu aurais voulu qu’Ammon te laisse plus de temps pour te préparer et fermer ce blazer."
    "La cravate autour de ton cou, contrairement à ce que tu t’attendais, ne bouge pas tant que ça."
    "Tu peux remercier le dos grand et large d’Ammon t’offrant une protection à la vitesse, dont la cravate est coincée entre lui et ton torse."
    "Cependant cela ne lui dérange pas d’être compressée, pouvant bénéficier de la chaleur de l’homme froid."

    am "Tu pourrais me lâcher, s’il te plaît ?"

    "Réalisant que tu es toujours accroché à sa taille, gêné, tu le relâches maladroitement."

    az "C’était agréable le temps que ça a duré."

    dk "Ce n’aurait pas pu durer pour toujours."
    dk "Tout a une fin."

    am "Merci."

    "Ne savant plus où mettre tes mains, tu les places à côté de tes jambes, sur le siège, les bras tendues et tu observes le paysage d’un regard inattentif."
    "Ta gorge se noue. Tu connais Ammon et il n’est pas tès tactile. Tu l’as énervé plus qu’il ne l’était."

    dk "Arrête de te triturer le cerveau sur ça. Ce n’était pas voulu, tu le sais bien."

    "Il n’empêche que le mur de glace se formant entre vous deux ne cesse de grandir. Son casque d’un noir froid occupe de plus en plus de place dans ton champ de vision."
    "Toutes tes tentatives de regarder au loin, dans l’horizon, où que ce soit, juste n’importe où, se révèlent infructueuses, tes yeux finissant par se poser sur la tête d’Ammon, impassible."
    "Tu déglutis, gesticulant inconfortablement sur ton siège."

    am "Euh, Howl ?"

    "Tu trésailles à sa voix, t’apprêtant à recevoir une autre remarque désagréable."

    hl "Oui ?"

    am "Ça te dirait que je mette un peu de musique ?"

    hl "De musique ?"

    am "Oui... J’ai une autoradio sur ma moto.{w} En cas de longs trajets."
    am "Et il s’avère que ce trajet est plutôt long, tu vois ?"

    hl "Oui je vois..."

    "Tes muscles se décontractent, réfléchissant une réponse à la question."

    $ radio_on = False

    menu radio:
        "Pourquoi pas":
            $ ammon_score += 1
            hl "Euh oui, je veux bien."
            hl "{cps=3}...{/cps} Enfin si tu veux, hein"

            am "D’accord."
            
            "Ammon se baisse et enclenche la radio sur son tableau de bord."
            ### TODO: Put rock song here
            "Une chanson rock, quoique peu vieillot de nos jours, retentit de haut—parleurs."
            "Tu espères te détendre. Malheureusement, cela n’a aucun effet."
            "Malgré la radio, le silence assourdissant entre vous ne fait que peser encore plus sur tes épaules."


            $ radio_on = True

        
        "Non merci":
            hl "Ça va, j’aime bien le son de la moto, au final."
            
            "Tu mens, murmurant entre tes dents."
            
            am "C’est comme tu veux"

            "Ammon soupire et retourne à ce qu’il faisait auparavant{w}, c’est—à—dire, conduire sans dire un seul mot."
            "Le silence assourdissant entre vous se retrouve amplifié par ton refus de le combler."
            "Tu te sens stupide."
    
    "Tu cherches désespérément un sujet de conversation pour passer le temps."
    "Tout autre personne aurait été à ta place, aurait–elle pensé sage de plutôt profiter du rafraîchissant air{w}, pour une fois que tu sors de chez toi."
    "Cependant, pour toi, cela se montre impossible. Tu ne peux pas le quitter des yeux."
    "Tu continues de fixer ce casque."

    az "Tu ne peux plus détourner le regard. Il aspire ton champ de vision."
    az "Tu l’as enfin devant toi.{w} Toutes ces années tu as rêvé de ce moment.{w} Toutes ces années tu souhaitais enfin pouvoir l’atteindre"
    az "Pourtant aucun de tes mots ne lui parvient.{w} Que c’est misérable."

    dk "Il représente tout pour toi."
    dk "C’est ton emblème{cps=3}...{/cps}{w} de ton échec{w}, de tes échecs"

    am "Howl ?"
    
    hl "Oui ?"

    "Tu lèves la tête avec appréhension."

    am "Tu pourrais arrêter de te tortiller dans tous les sens, comme ça ? Ça me déconcentre."

    hl "Ah d’accord..."

    "Tu t’affaisses vaincu. Maintenant c’est sûr, tout est fini. Ce voyage va être très douloureux."

    am "Tu as mal quelque part ?"

    hl "Hein ?"

    am "Il y a bien une raison pour laquelle tu te tortilles comme ça non..."

    az "Si tu lui dis que t’es frustré parce que t’arrives pas à aligner plus de deux mots avec lui, il va te prendre pour un cas."
    az "{w}Pas que ce soit déjà le cas, de toute façon."
    az "Mens–lui."

    dk "Lui mentir ne fera qu’augmenter la distance entre vous."
    dk "Sois franc."
    dk "Et non tu n’es pas un cas..."

    menu excuse:
        "Mon casque me démange":
            $ azzy_score += 1
            "Tu lèves ta main pour te frotter le menton, comme à ton habitude, lorsque tu veux réfléchir."
            "Cependant, elle se heurte à ton casque.{w} De là te vient une idée."
            
            hl "C’est juste que mon casque me démange un peu ahah."
            hl "Je n’ai pas vraiment l’habitude d’en mettre, tu sais."
            hl "Je ne sors pas souvent en moto, ahah."
            hl "Puis tu sais avec mes oreilles et tout, c’est pas super facile."

            am "Tu sais que j’ai de plus grandes oreilles que toi ?"

            hl "Oui mais quand même tu sais comment je suis, ahah."

            "Tu ne peux t’empêcher de rire inconfortablement. Oui le casque est un peu inconfortable mais pas à ce point."
            "Ammon grince à des dents."

            am "Sensible à un point que tu ne peux pas porter un casque plus de 5 minutes ?"

            hl "... Ce n'est pas ce que je voulais dire mais si tu le dis{nw}"

            am "Mais malgré ça, tu ne dis pas ce que tu penses et laisses les choses s'empirer jusqu'à ce que tu craques et fasses des caprices ?"
            am "Oui, je sais comment tu es."

            "Ammon se tait, impassible comme toujours. Les mots qu'il vient juste de déverser, teintés d'un macérant venin se heurtent à ton égo."
            "Tu retournes les phrases dans tous les sens pendant un bon moment avant que tu ne réentendes la voix, coupable, du chien grincheux."

            am "... Si tu veux on pourra faire une pause sur le chemin ? Comme ça je pourrais t’aider avec ton casque, que t’aies plus mal."

            hl "J’ai pas mal, Ammon ...{w} Mais je voudrais bien qu’on s’arrête sur le chemin si c’est possible..."
            hl "Je suis un peu fatigué."
            
            am "...{w} Pas de problème, Howl. Moi aussi je pense avoir besoin d’une pause."

        "Les sièges sont inconfortables":
            $ azzy_score += 1
            "Dans ta panique pour trouver un assez bon mensonge tu te tortilles encore plus."
            "Malgré le cuir les enveloppant, tu réalises que les sièges sont vraiment durs."
            
            hl "C'est juste que... ça fait plusieurs heures qu'on roule donc avec la rigidité de mon siège, disons que..."
            hl "Que je commence à avoir mal."

            "Ammon ricane."

            am "Quoi ? Le siège de mon humble moto ne lui sied guère à Monsieur le Monarque ?"
            am "Sa Majesté voudrait un coussin pour son popotin, peut-être ?"
            
            "Ses remarques sarcastiques te tapent sur les nerfs."
            
            dk "Ne peut-il pas te prendre 5 min au sérieux ?"
            
            az "Ne t'inquiète pas, c'est sa façon d'aimer."

            "Tu ne réponds pas. Que tu n'aies rien à dire ou que tu n'estimes que cette réponse ne mérite pas ton attention..."
            "Tu restes silencieux."
            "Ammon ne réagit pas en premier lieu. Puis ses épaules se baissent, quoi que légèrement."
            "Il reste dans cette position pendant quelque temps. Finalement il prend une grande inspiration et soupire doucement, exaspéré."

            am "Je t'ai vexé, n'est-ce pas ?"
            
            hl "Non."

            am "... Bref, False ou pas, je peux pas faire grand-chose à ton problème."
            am "Mais on peut s'arrêter faire une pause{w}, tu sais le temps de reposer tes fefesses ?"

            "Tu glousses malgré toi."

            hl "...D'accord. Ça me pose pas de problème."

        "La radio me dérange, au final." if radio_on:
            $ azzy_score += 1
            $ ammon_score -= 1
            "Essayant de réfléchir à une excuse valable, la musique, auparavant inoffensive tambourine graduellement tes tympans."
            "Plus tu cherches plus tu ne peux qu'entendre les paroles qui passent à la radio."
            "Tu serres les poings. Tu serres les dents."

            am "Alors t'as pas mal ? C'est autre chose-{nw}"

            hl "RAAAAH CETTE PUTAIN DE CHANSON, ELLE VA SE LA FERMER !!"
            
            "Tu te crispes de honte, réalisant ton erreur, trop tard."

            "Lorsque tu trouves le courage d'affronter Ammon, deux grands yeux jaunes ronds écarquillés te dévisagent."
            "Pendant un court instant vous croisez le regard, son air abasourdi te submergeant, tu voudrais t'enfouir dans un terrier de lapin."
            "Mais tu maintiens le regard. Tu ne peux détourner le regard de ces deux feux ardents célestes."
            "Soudainement, Ammon se retourne."
            
            am "... Compris, je vais arrêter la radio."

            "En silence, tu acquiesces. Tu n'oses plus dire plus."

            am "Je pense qu'on va bientôt faire une pause. Je sens qu'on est tous les deux fatigués."

            "Les yeux baissés, tu fixes le châssis de la moto, non particulièrement intéressant."


        "Lui dire la vérité":
            $ derek_score += 1
            $ ammon_score += 1

            "Tu as beau réfléchir mais rien ne vient."
            "Plus précisément, plus tu y réfléchis, plus une douleur aiguë se forme au centre de ta poitrine."
            "Telle une longue aiguille s'enfonçant dans ton cœur, tu hisses à travers les dents."
            "Ta gorge se noue."
            
            hl "Honnêtement...{w} ça fait longtemps que je me demande : est-ce que tu veux que je sois là ?"

            am "Hein ? Qu'est-ce que tu dis ?"
            
            hl "C'est juste que j'ai l'impression...{w} que je te dérange."
            hl "À chaque fois que je fais quelque chose, tu m'envoies balader."
            
            am "Mais je t'envoie pas balader, qu'est-ce que tu racontes ?"
            am "J'aime bien te taquiner, c'est tout."

            hl "D'accord, je vois..."

            "Tu t'affaisses dans ton siège, vaincu."

            am "Bon j'admets :{w} J'ai pu être un peu grognon durant ce voyage."
            am "Mais tu sais bien que c'est comme ça avec moi, le prends pas personnellement."
            am "C'est dans ma nature d'être grognon."

            "Tu souffles doucement du nez."

            hl "Si tu le dis."

            am "Tu sais quoi ? On va faire une pause sur le chemin. Je vois bien qu'on est tous les deux sur les nerfs."

            hl "Oui ce serait sympa merci."

            "Tu souris légèrement{w}, content d'avoir pu transmettre ce que tu ressentais à Ammon"
    
    pause 1.0

    hl "En parlant du voyage..."

    am "Oui ?"

    hl "On va où exactement ?"

    "Ammon te dévisage, confus."

    am "Comment ça, on va où exactement ?"

    hl "Eh bien on va où, où, tu sais... le lieu ?"

    am "...{w} Tu es en train de me dire que tu es monté sur ma moto sans savoir où tu allais."
    
    hl "Non...{w} Enfin oui mais je pensais que tu l'allais me le dire au bout d'un moment."

    am "Mais je te l'ai déjà dit !{w} La veille je te l'ai dit"

    hl "Vraiment ?"

    "Tu te frottes la tête, tu n'as aucun souvenir d'avoir eu cette discussion avec lui."
    "D'ailleurs, tu n'as également aucun souvenir de la veille."
    
    "Ton cou te démange."

    am "Oui... Tu es sûr que tu ne te souviens pas ?"

    hl "Oui je suis sûr, Ammon.{w} Je ne t'aurais pas demandé si je le savais..."

    am "C'est inquiétant... Après j'aurais dû m'en douter que tu n'es pas très concentré."

    "Ammon triture un temps avec le col de sa veste avant de reprendre le guidon."

    am "J'imagine que tu veux vraiment savoir où on va, hein ?"

    hl "Eh bien tout ce que j'ai compris c'est qu'on allait à la... Maison ?"

    am "... Je vois, à ce point ?"

    am "Bon tu veux savoir quoi sur \"La Maison\" ?"

    ## NOTE: Set up choices variables

    $ where_it_is = True
    $ why_there = False
    $ work = False
    $ what_else = False
    $ been_there = False
    $ real_reason = False

    menu destination_questions:
        "Questions sur la Maison"

        "Où elle est ?" if where_it_is:
            $ where_it_is = False
            hl "Où elle se trouve, la Maison ?"
            hl "Je veux dire, on roule depuis un bon bout de temps quand même."
            hl "Je ne me rappelle pas qu'aller chez moi ou chez toi était si long."

            am "N’exagère pas, ça ne fait que deux ou trois heures."

            "Tu baisses les yeux, tu n'as jamais roulé aussi longtemps de ta vie en moto."
            "Même c'est la première fois que quelqu'un t'emmène en moto. Tu ne t'attendais pas à la rigidité des sièges."
            "Aux picotements qui commencent à monter dans ton postérieur, tu décides de te remettre plus confortablement sur le siège."
            "Cependant tu as beau t'asseoir de plusieurs manières différentes, les vives douleurs comparables à des punaise restent bien logées."
            "Dans une dernière tentative désespérée, tu saisis ta queue et la tires autant que tu le puisses, comptant sur ces étirements pour apaiser des douleurs... {w}Sans succès."
            "Ammon, t'observant jouer avec ta queue, soupire."

            am "...{w} Bref, pour répondre à ta question, on va à Sainte-Mère."

            hl "Sainte-Mère ?"

            "Ce nom ne te dit rien. Il devrait rien te dire."
            "Pourtant tu te retrouves à te gratter la nuque.{w} Ça démange."

            am "...{w} Oui. C'est en Normandie. Tu y es déjà allé,{w} en Normandie ?"

            "Quelque chose te chiffonne."
            "Jamais Ammon n'a mentionné qu'il s'intéressait à la Normandie. Ni qu'il y était déjà allé, d'ailleurs."

            hl "Non..."
            hl "On va y rester combien de temps d'ailleurs ?"

            am "Une semaine environ."

            "Tu comprimes un petit cri de surprise. Peux-tu vraiment faire un séjour d'une semaine à l'autre bout du pays sans répercussion ?"
            "La Toussaint arrive à grands pas donc tu peines à voir ce que tu fais ici.{w} Tu peines à voir ce qu'Ammon fait ici. N'a-t-il pas un travail ?"

            hl "Elle est à toi, la Maison, alors ?"

            am "Non elle n'est pas à moi. Elle est à un ami."

            "À travers de son dos noir, un vent glacial percute tes moustaches et tu frissonnes. L'air devient de plus en plus froid."

            hl "Et cet ami, il s'appelle ?..."

            am "Pas tes oignons."

            "Le froid polaire te mord les bras et tu te les frottes en vain."

            hl "Joli nom..."

            "Même le sarcasme ne peut t'aider contre la froideur de l'Automne..."
            
            pause 1.5

            "Quelque chose te tracasse."
            "Tu as besoin d'en savoir plus sur cette ville."
            "Tu te grattes la nuque, ça te démange."

            $ why_there = True
            $ work = True 

            jump destination_questions

        "Pourquoi là-bas ?" if why_there:
            $ why_there = False
            hl "Du coup, pourquoi on va là-bas ?"

            hl "Pourquoi la Normandie ? Pourquoi cette ville en particulier ?"
            hl "Je ne me rappelle pas que tu aies vraiment mentionné vouloir aller là-bas, tu sais."

            am " Euuuh... Je te l'ai dit, pour se distraire de la vie en général ?{w} Il y a une plage où tu peux t'y promener."

            hl "T'es en train de me dire qu'on fait tout ce chemin juste pour se promener ? Pas mal."
            hl "Mais on aurait pu se promener dans les bois autour du village{w}, comme avant."

            am "Peut-être. Mais je voulais faire changer un peu."
            am "Et puis, j'aime bien les plages de la Manche. Elles sont rafraîchissantes, Elles ont une ambiance particulière en automne."
            am "Je ne peux pas m'empêcher de les prendre en photo."
            am "Les gens sont souvent repoussés par le temps grisâtre mais pas moi.{w} Moi, ça me plaît."
            am "Le bruit blanc des grains de sables et des rochers tout ça, c'est parfait pour mon appareil photo. Personne ne pense à saisir ces instants, oui moroses, mais nécessaires."
            am "Tu peux t'asseoir, laisser tes doigts se faufiler entre les galets et écouter les bruits des vagues trépassant à l'horizon. Et personne te sera là pour te casser les pieds."

            "Il marque une pause. Tu le regardes, surpris. Tu ne t'attendais pas qu'Ammon soit si sentimental pour des plages."
            "Cependant, ne voulant pas le contrarier, ni l'interrompre dans ce moment vulnérable, tu te retiens tout commentaire."
            "Ammon aimait bien faire des photos quand tu sortais avec lui, dans la nature. Tu es content qu'il n'ait pas abandonné la photographie"

            am "Puis aussi, il y a pas beaucoup de gens parce que l'eau de ces plages là-bas sont très froides."
            am "Donc si jamais tu as envie, je pourrai t'y pousser."

            "Ammon se retourne. Tu ne peux pas le voir, mais son sourire malsain transperce la visière de son casque. Les yeux jaunes narquois qui te fixent n'aident pas."
            "Tu glousses, te frottant le derrière du crâne, implorant intérieurement que son invitation à la baignade glaciale forcée ne soit qu'une plaisanterie."
            "Malheureusement avec lui, la possibilité que ce ne soit qu'une blague ne prédomine pas."

            # dk "Tiens-toi loin de l'eau en sa présence, ça vaudra mieux pour toi."
            # az "Non, au contraire, tiens-toi très près de l'eau. Puis quand il se faufilera derrière toi, contre-attaque et emmène le avec toi dans l'eau !"
            # az "Il verra s'il ose retenter ce genre de cachotteries."

            hl "Donc tu veux dire que t'es venu exclusivement à Sainte-Mère pour...{w} la plage ?"

            am "Pas qu'exclusivement mais c'est l'idée."

            "Tu as du mal à croire qu'Ammon se déplace aussi loin juste pour des plages."
            "Il ne peut pas y avoir que des plages dans cette fichue ville de Sainte Mère. Il doit y avoir quelque chose de vraiment très important pour lui."
            "Étant donné la façon dont il en parle, il a l'air d'y avoir déjà été.{w} Il faut que tu creuses."
            "Tu te ronges les griffes. Les marques de griffes sur ta nuque brûlent de plus en plus."

            $ what_else = True
            $ been_there = True
            $ real_reason = True

            jump destination_questions

        
        "Il y a quoi dans cette ville ?" if what_else:

            $ what_else = False

            hl "Il y a quoi d'autre dans cette ville ? Il n'y a pas que des plages, n'est-ce pas ?"
            hl "Il y a sûrement autre chose dans cette ville."

            am "Hum, je suppose que c'est vrai. Je suis aussi venu pour le Chateau du Gris."

            hl "Le Château du Gris ? C'est un château qui est tout gris ?"

            "Ammon ne bouge pas. Tu regardes dans le rétroviseur de la moto. Un regard perçant te fixe sans mouvement ni clins d'œil."
            "Il te semble qu'il ne soit pas fan de ta blague."

            am "... {w} Bref, ils font aussi hôtel."

            hl "Pourquoi on y va pas alors ?"

            am "Parce qu'on a déjà un endroit où dormir ?{w} Puis je n'aime pas les hôtels."

            hl "Comment ça ?"

            "Ammon serre le guidon. Sous son casque, ses oreilles se relèvent d'exaspération. Il semble que tes questions incessantes ne lui plaisent pas."

            am "T'en as d'autres questions pertinentes comme ça ?"

            hl "Désolé ...{w} C'est juste que je suis vraiment dans le noir, ici."

            am "Si tu faisais attention autour de toi plus de 5 secondes, on n'en serait pas là."

            "La brise du morne automne reprend de plus belle. {w}Tu pondères la raison pour laquelle tu ne sais, au final, rien de la personne que tu appelais ton meilleur ami il y a des années."
            "Aussi pourquoi tu n'as pas pris le temps de te renseigner d'où il t'emmenait."
            "Tu supposes l'instant où il t'a proposé, tu as sauté sur l'occasion sans même y réfléchir une seconde."
            "Que pensais-tu qu'il allait arriver ? Un mec bizarre qui n'aligne pas deux mots et une connard irritable sur une moto ensemble, ça n'amène rien de bon."

            az "Pas que bizarre."

            dk "Et pas qu'irritable."

            if azzy_score >= 1:
                az "Irritable, peut-être mais tu adores ça."
                az "Tu ne veux pas te l'admettre mais si tu pouvais — Non — si tu le voulais, tu lui répondrais tel une vipère."
                az "Vous vous plaisiez, vous vous baigniez dans vos toxines. Vous adoriez ça. Marie-Jil avait beau essayer de rabibocher votre relation, finalement elle ne la comprenait pas."
                az "Elle était impuissante, car elle n'était pas digne de votre don. Elle est aveugle au lien qui vous relie tous les deux."
                az "Un lien maintenu dans les échanges virulents, les mensonges, les petits jeux de supercherie... {w}la haine."
                az "Tu le haïssais et tu adorais ça."

                dk "Mais ça c'était avant, tu n'es plus comme ça."

                az "Exactement. Qu'est-ce qu'il s'est passé pour que tu deviennes un chaton apeuré, effrayé de dire un mot de travers au mec que tu détestes"
                az "Ah oui, t'as une idée non ? C'est parce qu'il prend ses médicaments le bon toutou."
                az "Parfois, ne te demande-tu pas qui est la chienne de vous deux ?"

                dk "..."

            "Un moment de silence. Le chien reprend la parole."

            am "... C'est comme ça."

            hl "... Hein ?"

            am "Je n'aime pas les hôtels c'est comme ça. Je ne me sens pas à l'aise dans des endroits inconnus et encore moins y dormir."
            am "On ne sait jamais qui était là avant."

            hl "Je vois..."

            am "Sinon, il y aura aussi une exposition sur l'Anniversaire du Débarquement."

            "Tu pouffes discrètement. Tu t'attendais à qu'il soit toujours obsédé avec la Seconde Guerre Mondiale, donc tu ne comprends pas ta surprise ni ton amusement."
            "Néanmoins, tu n'étais pas vraiment enthousiaste. Si tu voulais qu'il lâche une passion en particulier, c'était bien la Seconde Guerre Mondiale."
            "Même de nos jours, la population est toujours traumatisée donc avoir quelqu'un dans les parages s'extasiant en reconnaissant des modèles précis de casque utilisé par l'armée allemande te mettait mal à l'aise."
            "Tu ne voulais pas lui reprocher ça parce que tu sais qu'avec tes obsessions, tu étais encore pire que lui. Cependant cela n'atténuait pas ta gorge nouée."
            "Tu n'avais vraiment pas envie de passer tes congés à regarder des chars d'assaut ou des bombes pouvant rayer des villes de la carte,{w} ayant déjà le cafard sans aide."
            "À force d’y réfléchir, tu te rends compte que quelque chose cloche."
            "Tu n'es pas le meilleur en histoire mais si tu te rappelles bien de tes cours..."
            "Juste une seconde..."

            am "Avant que tu ne le dises, oui ce n'est plus l'anniversaire depuis au moins 4 mois mais elle est toujours là pour une raison ou une autre."
            am "Il y a aussi une autre exposition... une exposition de biscuits."

            "Ammon ricane."

            am "Incongru tu penses pas ?"
            

            hl "Bon au moins, entre deux bombes, on pourra se manger un petit BN, c'est pas si mal."

            "Ammon pouffe."

            am "Bref, celle des biscuits est permanente donc c'est pas comme s'ils avaient le choix."

            "Plus tu discutes avec Ammon, plus tu réalises qu'il a une définition anormal de vacances."
            "Des expositions sur des bombes et des biscuits ? Ce qui est sûr, c'est que ce n'est pas ta tasse de thé."
            "Ammon doit vraiment vouloir partager ça avec toi, pour t'avoir emmené avec toi."
            "... Ta nuque brûle, incandescent, les plaies exposées souffrant à l'air pur et froid."
            "Tu dois creuser."

            jump destination_questions
        
        "Tu y as déjà été ?" if been_there:
            $ been_there = False

            hl "Au passage, Ammon, tu y as déjà été ?"

            am "Où ça ?"

            hl "Bah à Sainte-Mère."
            hl "Tu en parles comme si tu y es déjà allé{nw}"

            am "Non jamais."

            "La voix d'Ammon résonne dans ta tête."
            "Perturbé par son interjection, tu restes silencieux."

            hl "... Tu es sûr ?"

            am "Oui je suis sûr."

            hl "Tu ne parlais pas la super plage de la ville ? Tu avais l'air de l'apprécier un peu quand même non ?"

            am "Il y a d'autres plages en Normandie, il y en a pas qu'à Sainte-Mère."

            "Peut-être que tu as mal compris au final. Peut-être qu'il est déjà allé en Normandie mais pas spécialement Sainte-Mère"
            "Sa passion des photos de plages grises ne vient pas de nulle part."

            hl "... Donc tu es déjà allé en Normandie ? T'aimes bien y prendre des photos, j'ai cru comprendre."

            am "... Oui j'y ai déjà été."

            hl "Alors ?"

            am "... Alors quoi ?"

            hl "Bah c'était bien ? Tu y as fait quoi à part de la photo ?"

            am "Pas grand chose..."

            hl "Donc c'était pour un petit boulot ? Tu y as fait de la photographie ?"

            am "Je ne suis pas assez bon pour que je m'amuse à faire des photos à droite et à gauche de la France pour de l'argent."

            hl "...D'accord."

            "Ammon se renferme sur lui, une carapace impénétrable."
            "Tu retournes la précédente discussion dans tous les angles, à la recherche de la chose déplacée que tu aies dite."
            "Mais rien. Ce n'est pas inhabituel d'Ammon de te couper dans tes tentatives d'approche."
            "Les épaules retroussées, le chien brut ne bouge plus d'un pouce. Sa queue, qui se remuait il y a encore quelque temps, se durcit comme du marbre."
            "Il a aucune raison d'être autant sur la défensive. Ça ne t'aurait pas dérangé qu'il y soit déjà allé sans toi."
            "Tu es de plus en plus confus par sa réaction."
            "Tu regardes tes griffes. De le peau, des poils arrachés et du sang frais s'accumulent sous tes ongles. Ta nuque te brûle."
            "Tu resserres fermement le châssis."

            jump destination_questions
        
        ## TODO: Faire une question Real Reason 
        ## TODO: Faire une question Work 
 
        "Tu n'as pas un travail ?" if work:
            $ work = False 
            hl "Dis Ammon ?" 
 
            am "Oui ?" 
 
            hl "Tu es professeur d'Histoire à l'Université, non ?" 
 
            am "C'est l'idée, oui." 
 
            hl "Tu ne devrais pas être à l'université alors ?"

            "Ammon te dévisage à travers le rétroviseur."

            am "... Non ?"

            hl "Heu pourquoi ?"

            am "Parce que c’est la Toussaint ?"

            "Son regard qui s’ensuit ne peut pas être plus évocateur : de l’incrédulité et du dédain."

            hl "Ah oui c’est vrai..."

            am "T’en as d’autres questions pertinentes comme ça ?"

            jump destination_questions 
         

        
    "Après toutes les questions, tu te sens épuisé."
    "La somnolence que tu avais contenu jusque-là, charge à pleine force à nouveau."
    "Bientôt tes paupières deviennent lourdes et la gravité jusque-là inoffensive t'arrache de la moto."
    "Ta tête se heurte au dos du grincheux chien."

    if ammon_score >= 1:
        am "Hé, fais attention !{w} Qu'est-ce qui te prend de frapper comme ça ?!"
        
        hl "Désolé... Je me suis laissé emporter par la fatigue."

        am "Tu es si fatigué que ça ?"

        ### TODO: Réécrire ça mdr

        "N'ayant plus d'énergie, tu hoches de la tête, savant pertinemment qu'il ne pourrait pas le voir."
        "Cependant il comprit——notamment grâce aux frottements du casque sur sa veste——et une pensée lui vient en tête."
        "Hésitant à le dire, il se décida subitement."

        am "Attrape-moi la queue."

        hl "... Hein ?"

        am "Attrape-moi la queue."

        "Même la deuxième fois, tu n'arrives pas à comprendre ce qu'il vient de dire."

        am "Pour que tu puisses t'accrocher à quelque chose, pendant que tu dors..."

        hl "Pourquoi spécialement la queue... ?"

        am "Parce que c'est plus facile..."

        hl "T'as pas horreur qu'on te touche la queue ?"

        am "Si... mais si c'est pour ta sécurité je veux bien faire des concessions."
        am "Tu vas dormir de toute façon donc autant que tu tiennes quelque chose."

        hl "... Je pourrais m'accrocher à mon pantalon. C'est plus sûr que ta queue de deux centimètres."

        "Une vive douleur survient dans ton torse. Ta respiration se coupe pendant un temps."
        "Il vient de te donner un coup de coude." 
        
        hl "Hé, d'où ça vient ?"

        am "...{w}Elle fait pas deux centimètres, elle en fait vingt !"
        am "Mais oui je comprends ce que tu veux dire..."
        am "T'accrocher à mon pantalon est sûrement plus efficace que de tenir un truc pas très long..."
        am "Tout compte fait, peut-être que te proposer ma queue était un peu bizarre. J'aurais dû te proposer mon pantalon."

        "Tu ricanes."

        if azzy_score >= 1:
            az "Il a été plutôt rapide à proposer ça, ne penses-tu pas ?"
        elif derek_score >= 1:
            dk "Mais à quoi il pensait ?"
        
        hl "C'est décidé, alors."
        hl "Réveille-moi quand on est arrivé."

        am "Oh t'inquiètes, je te réveillerai avant."

        "Ignorant sa dernière remarque, tu poses ta tête contre long dos du canidé."
        "Le casque te sépare de sa veste en cuir mais tu supposes qu'il est dur et inconfortable."
        "Néanmoins tu aurais préféré sans le casque."
        "Agrippant son pantalon rugueux, tu laisses les bras de Morphée t'emporter."

    else:
        "Malgré le chien gesticulant et pestant, te criant dessus, tu nne trouves plus la force d'y faire attention."
        "Plutôt, à ce point, si tu voulais t'en soucier, tu l'aurais fait."
        "Pourtant, te voilà, ignorant les plaintes de ton ami, touchant enfin du bout du doigt, une paix longtemps perdue."
        "Il t'a baladé à droite et à gauche sans jamais prendre en considération ton ressenti."
        "Parfois tu te demandes pourquoi tu l'as suivi. Il n'a pas changé d'un pouce."
        "Toujours brut, toujours peu soucieux de son environnement, toujours une attitude rebelle exécrable à son âge."
        "Il ne t'a jamais regardé, et ne le fera jamais. Il t'a sûrement invité pour mieux te tourmenter."
        "Pourtant tu restes. Tu ne t'en vas pas. Tu ne t'enfuis pas. Tu aurais pu à tout moment refuser son invitation et retourner tes préoccupations."
        "Mais non. Tu as accepté sur le champ. Le moment où il a remis un pied dans ta vie, tu t'es jeté aux siens."
        "...{w} Pourquoi."

        az "Parce que vous ne pouvez pas vivre l'un sans l'autre. Au fond de ton cœur, tu le sais."
        az "Tu as essayé de l'oublier plusieurs fois, en vain. Il t'a laissé tout seul, il t'a abandonné. Il t'a fait souffrir."
        az "Tous les jours, tu espérais qu'il souffre aussi, autant que toi. Il n'avait pas le droit de partir sans tracas, toi laissé derrière à ton compte, immergé par la Solitude."
        az "Au fond de toi, tu savais qu'il n'en allait pas autrement. Tu savais ce qu'il se passerait lorsqu'il reviendrait. Vous êtes liés, que tu le veuilles ou non. {w}La Fatalité en a décidé ainsi. Tu es trop faible pour y lutter"
        az "Destinés à se baigner dans votre incompréhension de l'autre mais incapable de comprendre les bénéfices de la distance entre deux personnes incompatibles."
        az "En espérant que tu as eu ce que tu voulais{w}, lâche."

        "Sur ces mots, le néant t'emporte et bientôt ta conscience s'y fond."
label dream_1: 
    camera:
        perspective True
        subpixel True
        zpos -300
        ease 1 ypos 125
        ease 1 ypos 100
        repeat
    pause 0.5
    show clearing:
        ease 1 blur 128
        ease 1 blur 32
        repeat
    with dissolve

    pause 0.5
    # play music "audio/music/griff.mp3" fadein 1.0 loop
    window show
    
    cl "{w=1.0}Aux frontières de la forêt, dans la clairière, je reste allongé, accablé, à bout de souffle. Je respire autant que je peux mais l'air chaud me brûle la gorge."
    cl "Puis je sens ta présence rassurante, je me rappelle que je ne suis pas seul. Que tu es là avec moi."
    camera:
        ease 1 ypos 125
        ease 1.15 ypos 105
        ease 1.30 ypos 125
        ease 1.5 ypos 115
        ease 2.0 ypos 125
    
    show clearing:
        blur 128
        linear 5.0 blur 32

    extend "Alors je respire profondément et enfin mon torse battant s'abaisse à un rythme régulier."
    cl "Entre deux expirations soulagées, je regarde autour de moi pour te chercher et mes yeux se croisent avec lui, quelqu'un que je connais très bien, quelqu'un que je n'oublierai jamais, quelqu'un que je souhaite oublier, un monstre sans cœur."
    cl "Je le fixe profondément mais les lueurs qui brillaient dans ses yeux ont disparu depuis longtemps{w}, si tant est qu'il y en ait jamais eu."
    cl "Parfois, je me demande si ma vie aurait pu se dérouler différemment, ce que j'aurais dû faire pour ne pas finir dans une forêt, au milieu de la nuit, assommé, avec cet être sans valeur."
    cl "S'il m'avait plus souri, s'il m'avait plus parlé, s'il m'avait plus pris dans ses bras, s'il s'était plus soucié de moi, s'il avait fait tout ça, peut-être, juste peut-être, j'aurais eu pitié."
    cl "De la pitié quand tu l'as fait fulminer par les dents, en régurgitant, en vomissant."
    cl "Des regrets quand il te suppliait de te souvenir de tous les bons moments."
    cl "Remords quand il t'implorait de le laisser partir, qu'il ne parlerait pas de ce qui s'est passé ce soir."
    cl "Mais je ne l'aurais pas fait. Je n'aurais rien ressenti pour lui."
    cl "Pendant ces instants durables, où, avec sa dernière corde d'énergie, il a serré mon bras, {w=.5} il n'y a rien eu."
    cl "Pas de tristesse, pas de supplication, pas de tourment, pas de colère, pas de rage, pas de courroux."
    cl "Pendant que je restais là, j'avais soif d'un signe quelconque montrant qu'il était un être conscient et chaud. Quelque chose, n'importe quoi"
    cl "Non. Juste des yeux morts. J'ai beau regarder, je vois toujours ces mêmes yeux morts. Qui me regardent."
    cl "J'aurais aimé que ce ne soit pas les mêmes yeux. J'aimerais pouvoir dire qu'un frisson m'a parcouru, que la tristesse m'a envahi quand tout cela s'est déroulé."
    cl "Non, juste des yeux morts, pour les années passées et maintenant pour toujours.{w} Ou du moins, je n'ai pas réussi à le percevoir. Comme beaucoup de choses dans ma vie."
    play sfx "sounds/rope_squeak.ogg" fadein 0.5 volume 0.3
    show clearing:
        ease 1 blur 128
        ease 1 blur 16
    cl "Chaque régurgitation, j'aurais voulu qu'il prête plus attention à moi."
    stop sfx fadeout 1.0
    cl "Qu'il me prenne dans ses bras, qu’il me parle plus qu'une douzaine de mots dans toute ma vie."
    play sfx "sounds/rope_squeak.ogg" fadein 0.5 volume 0.3
    show clearing:
        ease 1 blur 128
        ease 1 blur 16
    cl "Je voudrais qu'il me sourit à cet instant."
    stop sfx fadeout 1.0
    cl "Sauf qu'il ne peut pas. Il conservera toujours cette expression cadavérique."
    cl "Tous ces souhaits, ces réponses, ces aspirations, ces rêves, enfouis avec lui."
    window hide

    pause 1.0

    window show
    show clearing:
        ease 2 blur 0

    cl "La brise rafraîchissante caresse mes longues oreilles, le hurlement surnaturel du vent me rafraîchit mais ma gorge brûle toujours."
    cl "J'essaie de la faire disparaître mais les milliers d'aiguilles enfoncées au fond de ma gorge protestent.{w}\nIl me faut de l'eau."
    cl "Je me dirige donc difficilement vers lui et je cherche quelque chose pour apaiser ma soif."
    cl "Je parviens à trouver une gourde. Je la débouche et l'enfonce dans ma gorge sale pour que l'eau tiède puisse couler."
    cl "À chaque gorgée, ça lave un peu plus."
    cl "Ce mucus qui obstrue ma gorge."
    cl "Cette démangeaison chaude qui y résidait."
    cl "Cette détresse qui s'était accumulée au fil des années."
    cl "Ces regrets de ne pas avoir été assez bon pour lui."
    cl "Cette culpabilité de l'avoir déçu, de ne pas en être digne."
    cl "Cette honte de ne pas avoir été assez bien pour lui."
    cl "La seule chose qui reste, c'est l'engourdissement envahissant de ma vie."
    cl "J'ai besoin de plus d'eau."

    pause 0.5

    cl "Je regarde, dans les environs et non loin de moi, se dresse un marais à plusieurs mètres de moi."
    camera:
        ease 0.5 zpos -280
        ease 1 zpos -350
        ease 0.5 zpos -320
        ease 1 zpos -400
        ease 0.5 zpos -370
        ease 1 zpos -450
    cl "J'ai rampe désespérément jusqu'à elle et je me gave d'eau."
    cl "Mais même mon âme immonde ne peut supporter cette eau fétide et je régurgite tout ce qui se trouve dans le marais."
    camera:
        ease 0.5 ypos 150
    cl "De la bave accrochée à mon museau, des larmes qui coulent sur mon visage, je m'effondre dans l'herbe, vidée de toute mon énergie."
    cl "Ma vision reste bloquée sur le milieu de ce marais."
    
    call spawn_fireflies from _call_spawn_fireflies
    
    cl "Une petite colline avec une centaine de lucioles se projette sur moi, m'offrant un spectacle que je n'oublierais jamais. Quelque chose que je pensais ne jamais voir."
    cl "Un phare d'une lumière langoureuse dans l'obscurité écrasante de la nuit qui m'entoure et qui me fait vivre."

label rest_area_1:
    # "Eventually, Ammon, who had stripped away his helmet since a long time ago, notices you."
    scene black
    # show ruralRoad
    # with Fade(0.5, 4.0, 0.5)
    
    camera at zpos_camera
    pause 1.0

    show parkinglot with dissolve

    show ammon right at american_shot

    "Encore une fois tu ressens une main froide sur ta nuque."

    am "Hé ho réveille–toi on est arrivé."

    hl "Ah bon ?"

    am "Oui, lève–toi vite."

    "Grincheux, tu descends de la moto et tu enlèves ton casque."
    "Tu galères."

    am "Tu veux de l’aide ? T’as l’air de galérer un peu."

    menu let_ammon_help_you:
        "Demander de l’aide":
            $ ammon_score += 1 
            "Normalement, c’était le moment où tu détournes toute sorte d’aide. Mais..."
            hl " D’accord, vas–y... "
            "Tu n’as pas la force de lutter ni de protester, alors tu cèdes à Ammon."

            show ammon front

            "Ses mains volumineuses et rugueuses saisissent la base de ton casque et ses ongles effleurent ton cou. Un frisson te parcourt. Tu n’aimes pas qu'on te touche."
            "Tes poils se hérissent, t'implorant d'en finir au plus vite. Tu ne peux pas être plus d’accord. Plus vite le casque enlevé, mieux tu te porteras"
            "Néanmoins, il a, lui aussi, du mal à débarrasser ta tête du casque. Il tire de toutes ses forces sur toi. La douleur submerge tous tes sens"
            hl "Oh mon dieu, Ammon, sois plus doux ! !! Moins fort ! Tu vas me faire mal !"
            
            am "si ton trou n’était pas si étroit..."
            
            hl "Qu'est-ce que t’as dit ?!"

            am "J’ai dit si le trou du casque n’était pas si étroit... et que tu n’avais pas une aussi grosse tête !"
            
            hl "Tu peux parler avec ta gueule !"
            
            am "Si tu te la fermes pas, j’enlèverai ton casque d’un manière ou d’une autre"
            show ammon right e_smug
            extend "avec ou sans ta tête."
            
            hl "La ferme avec ta gueule et juste enlève–le, on s'en portera mieux tous les deux !"
            
            "Pendant un moment, Ammon lutte encore pour enlever ton casque. Vous tirez tous les deux comme des idiots en essayant de retirer Excalibur." 
            "Tu cries et il s'excuse sèchement."
            "À un moment donné, vous sentez qu'avec vos efforts conjugués, le casque est prêt à céder." 
            "Tout à coup, un pop se fait entendre et tu t’envoles du casque, atterrissant dans l’herbe."
            "Tu expulses la terre et les brins d'herbe coincés dans ta bouche."
            show ammon front e_happy j_noway
            "Tu secoues ta tête pour que ton sang y circule à nouveau. Lorsque tu reprends tes esprits, une hyène se tient devant toi, incapable de s’arrêter de rire."
            "Son rire perçant t’envahit et tu rougis de gêne, malgré toi. Tu t'agrippes à l'herbe."

            menu:
                "Lui lancer de l'herbe" :
                    $ ammon_score += 1 
                    "Tu arraches de l'herbe et tu lui en jettes pour qu'il ferme son long piège à museau qui lui sert de bouche"
                    hl "Putain d’abruti ! !! Je t'avais dit qu'il ne fallait pas tirer aussi fort ! Je suis tout égratigné et sale maintenant. Je te déteste, tu m'entends ?"

                    show ammon j_neutral
                    "Ammon essuie ses larmes de rire et s'approche, triomphant, de toi. Son sourire malicieux transperce son casque alors qu'il te remet ton casque et te tend une main."
        
                    am e_neutral "D'accord mon chaton, plains–toi autant que tu veux. Mais si tu continues à te rouler au sol, tu n'arriveras à rien, si ?"

                    "Tu serres les dents en t'agrippant à sa main. Il te transporte hors du sol que tu te retrouves à léviter. Tu oublies souvent sa force inhuchienne."
                
                "Rester calme" : 
                    "Tu t'agrippes de plus en plus fort à l'herbe. Tu veux déchaîner ta rage sur lui, lui jeter de l'herbe et de la terre."
                    "Mais tu ne peux pas. Tu es trop faible pour ça. Il ne ferait que se moquer de toi encore plus fort. {w}Tu le détestes."

                    show ammon j_neutral
                    "Ammon essuie ses larmes de rire et s'approche, triomphant, de toi. Son sourire malicieux transperce son casque alors qu'il te regarde."

                    am e_noway "Euh, tu vas bien ? T’es blessé ? T’as l'air tendu."

                    show ammon e_neutral
                    "Il se précipite vers toi."
                    "Une fois près de toi, il tend sa main vers toi"

                    "Mais tu la repousses d'un revers."

                    show ammon e_noway j_disgusted
                    hl "Je vais bien, tu n'as pas besoin de t'inquiéter pour moi."

                    "Tu te lèves et tu brosses rapidement tes vêtements de la poussière et tout végétaux."

        
        "Le faire tout seul" :
            "Tu n'as pas besoin de l'aide de ce con."

            hl "Je n'ai pas besoin de ton aide. Je peux me débrouiller tout seul."
            
            am pupils_right "Très bien... Comme tu veux."
            
            "Tu n'attends pas son signal."
            "Cependant, quelque chose ne va pas : il est vraiment coincé. Peu importe la force avec laquelle tu tires ou l'angle que tu utilises, tes oreilles ne bougent pas et il ne se détache donc pas."
            "En paniquant, tu t'agites dans toutes les directions, te précipitant sur la moto et sur Ammon."

            am pupils "Tu es sûr que tu n'as pas besoin d'aide ? Tu en as l'air."

            hl "Je vais bien ! Je n'ai pas besoin de ton aide ni de celle de personne !"
            
            am pupils_left "Um, ok... Je suppose que..."

            show ammon pupils

            "Dans ta lutte contre le casque, tu continues à tourner sur toi-même jusqu'à ce que tu aies la nausée à cause de l'expérience généralisée."
            "Par un fil de chance ou de malchance, tu parviens à te débarrasser de ton casque. Cependant avec toutes tes danses et tes virevoltes, tu perds l'équilibre tombant dans l'herbe."
            "Lorsque ta charge frénétique s'arrête, tu craches la terre et les brins d'herbes pris dans ta bouche. Lorsque tu reprends tes esprits, tu es confronté à un chien rieur incapable de s'arrêter."
        
            am pupils_left j_smug "Bien fait, abruti."

            hl "Qu'est-ce que t’as dit ?"

            am pupils j_neutral "Tu m'as entendu. Lève-toi. Tu n'arriveras à rien comme ça."
            
            "Tu te lèves. Tu te frottes la tête par douleur et tu sens une méchante bosse sur ton crâne. Tu aurais peut-être dû demander Ammon."

    hide ammon with dissolve

    "Tu te débrouilles pour sortir de l'herbe et tu te précipites vers le rétroviseur de la moto pour regarder ton visage et vérifier qu'il n'y ait pas d'égratignures."
    ## TODO : Illustration de l'écart en train de regarder dans le rétroviseur.
    "En y jetant un coup d'œil, tu contemples un chat maigre d'une vingtaine d'années, de stature moyenne et grognon." 
    "Tu soupires. Tu aurais "

    dk "N'oublie jamais, c'est toi et ce sera toujours toi."

    "Malheureusement, tu n'as pas eu cette chance et ton visage aux poils blancs habituellement purs comme du cristal à l’exception de ton museau marron, est entaché de quelques saletés et blessures." 
    "Tu te lamentes sur ton état. À part ces égratignures, tu n’es pas en forme non plus."
    "Tes yeux fatigués donnent l'impression que tu n'as pas dormi depuis une semaine - et c’est peut—être le cas - les cernes sous tes yeux se dessinant sur une surface trop grande." 
    "Tu les frottes, cependant elles restent intacts et toute tentative de les faire disparaître se révèlent infructueuses."
    "Tu vérifies ton œil rouge, gonflé par la fatigue, tu lui prodigues la paupière inférieure." 
    "Les capillaires qui parcourent la sclérotique de tes yeux verts jade pulsent comme une entité vivante."
    
    "Ils t'agacent et plus encore ils t'effraient. "

    am "Euh Howl, qu'est-ce que tu fixes comme ça ?"

    show ammon at american_shot
    with dissolve

    "Ammon penche la tête depuis l'autre côté de la moto pour jeter un coup d’œil dans le rétroviseur"

    am "Il faut que t’arrêtes de te regarder comme ça. On dirait que tu es sur le point de trucider quelqu'un"

    "Avec ce commentaire inquiétant, Ammon poursuit en se débarrassant de son casque" 
    "Réalisant qu'il a un point, tu détournes le regard du toi de l’autre côté du miroir, n’ayant pas arrêté de te dévisager."
    
    hl "T’as besoin d'aide avec ton casque, Ammon ? Tu sais... la forme de ta tête..."
    
    am right "C'est bon, mec. Je peux m'en occuper tout seul. J'ai l'habitude."

    "Le chien arrogant enlève son casque élégamment sans aucun problème ni souci quelconque" 
    "Il remue la tête enfin libérée de sa prison protectrice en plastique"

    show ammon pupils_right 
    az "Quel frimeur !" 
    az "Mais quel bon frimeur."
    camera at close_shot
    show parkinglot:
        parallel:
            easeout 1 blur 64
    "Ce qui attire toujours ton attention chez lui, ce sont ses yeux. Ses yeux dorés inestimables qui brillent plus que tous soleils que tu aies vu." 
    "Tu te retrouves hypnotisée par ces bijoux"
    show ammon pupils
    "Ces yeux cruels et perçants te regardant à travers ton âme"
    show ammon pupils_right 
    extend "et te lisant comme un sale livre ouvert." 
    "À tout moment, s'il en a envie, il peut en choisir un extrait et l'étudier attentivement à tes dépens." 
    "Il est objectivement meilleur que toi dans tous les domaines possibles"
    camera :
        easeout 15 ypos 400
    "Il est beau, il est charmant, il est charismatique, il a un sens un sens du style que tu n'auras jamais." 
    "Il porte également des piercings dorées au visage."
    "Tu aimerais pouvoir être aussi extravagant que lui et prendre des risques fous" 
    "Tu n'es pas aussi audacieux que lui alors tu restes sur ta petite chemise classique avec ta cravate"
    "Tu espères qu'un jour, tu briseras les liens qui t'enracinent dans ta vie ordinaire et que tu prendras le risque d'être aussi libre, aussi vivant que libéré que lui."

    am "Qu'est-ce que tu regardes ?"

    pause 0.5

    camera:
        easein .5 ypos -200
    
    show ammon pupils e_smug

    am "J’ai quelque chose de spécial en dessous ?"

    hl "Huh pas du tout ahah"

    "Tu grimaces tout en te frottant le cou"

    hl "C'est juste que j'aime beaucoup ta ceinture, ahah"

    am "{cps=3}...{/cps} ok, merci, je suppose ?"
    # am pupils_right "{size=20} you weirdo"
    
    camera :
        parallel :
            ease 2 zpos 0
        parallel :
            ease 2 ypos 0

    pause 1.0

    hide ammon with dissolve
    "Malgré ta fixation sur Ammon, tu en viens à remarquer l'aire de repos déserte sur laquelle tu viens de t'arrêter." 
    "Les feuilles mortes s'entassent sur le bord des routes, signalant que l'automne est arrivé et qu'il a fait des ravages dans la nature." 
    "Le paysage brun orangé contrastait avec le vert éclatant de l'été" 
    "Les arbres en deuil se tiennent là, attendant des temps meilleurs"
    "Tôt ou tard, même leurs couleurs mélancoliques seront remplacées par des branches et le blanc glacial qui les borde dans leur sommeil chaleureux." 
    "Les herbes hautes restent néanmoins invaincues par le temps qui passe. Quelques tournesols résistent encore, à la recherche de leur guide."
    "Les toilettes habituelles se détachent de la nature environnante. Elles ne sont pas du tout bien entretenues..."
    "Une haute structure métallique se détache de toute cette misère. Tu en as vu une poignée de fois. Une cabine téléphonique." 
    "Tu vois rarement des cabines téléphoniques au village, alors en trouver une sur une aire de repos est encore plus incroyable. La technologie va vite, penses-tu, de nos jours."

    hl "Hé regarde, Ammon ! Ils ont une cabine téléphonique par ici. N'est-ce pas merveilleux ?"

    show ammon pupils_right at american_shot with dissolve

    am "Huh ?"
    show ammon pupils 
    extend "Oh ouais... bien sûr."

    "Ammon ne semble pas très intéressé par cette incroyable structure. Tu baisses ton regard et tu remarques qu’il n’arrête pas de se dandiner, son pied n’arrêtant pas de bouger dans tous les sens." 
    "Cela explique son manque d'intérêt, tu supposes."

    am "Alors tu vas l'utiliser, c'est ça ? Qui tu vas appeler ?"

    "Tu réfléchis à la question, même si tu ne connais pas beaucoup de gens qui possèdent un téléphone chez eux. Seules deux personnes te viennent à l'esprit."

    am j_noway "Ta mère ? Ou..." 
    show ammon pupils_left
    extend "MJ ?"

    show ammon pupils j_neutral

    "Un petit silence s’ensuit"

    hl "Oui je vais l'appeler."

    am pupils_right "Ok, comme tu veux."
    am "Je vais pisser. Attends-moi et ne t'éloigne pas, d'accord ?"

    "Ammon change rapidement le sujet de la discussion et revient sur l'affaire urgente." 
    "Tu le regardes se dandiner sur place, sauter comme un lapin en retard."
    "Tu ne souhaites pas le retenir plus longtemps"


    hl "Ok, ne te perds pas en route !"

    am "Ne t'inquiète pas. À plus tard."

    hide ammon with dissolve

    "Dès qu'il a terminé sa phrase, tu le vois sprinter vers les toilettes abandonnées et tu glousses." 
    "Alors qu'il disparaît de ta vision, tu es désormais seul....{w} Pas tout à fait... Il y a la cabine téléphonique. Elle attire, t'implore de venir."
    "Alors tu la fixes avec envie. Pendant un moment, tu ne peux que rester là, devant la cabine, tandis que tes yeux la parcourent, intrigués."


    
    jump phonebooth

label phonebooth: 
    stop music fadeout 0.5
    stop sound
    scene phonebooth with fade

    play music "audio/music/night_sky.mp3" fadein 1.0 loop

    "Te traînant jusqu'à la cabine, tu saisis avec une grande difficulté la poignée, ne parvenant pas à trouver la motivation nécessaire pour pénétrer dans la cabine obscure."
    "Tu tournes un nombre inconsidéré de fois la poignée, enfin, la porte s'ouvre quand tu la pousses." 
    "Tu ne dois pas être dans le bon état d'esprit pour ne pas remarquer que tirer mille fois sur une porte ne fonctionnera pas la mille et unième fois."
    "Mais tu n'as pas pu t'en préoccuper plus que ça, ta morosité s'écrasant au plus bas lorsque tu poses enfin la patte dans le vide sombre, transpercé par les rayons d'un soleil déclinant."
    "Aveugle, par la faible luminosité actuelle du lieu, tu as mis du temps à même trouver le téléphone"
    "Sur la cabine téléphonique, sur une petite pancarte au fond de celle-ci, il est écrit : « 10 francs pour 10 minutes ! »."
    "Tu sors une pièce de ta poche et tu la glisses dans le monnayeur. Peu après, l'écran du téléphone s'allume et attend ta saisie." 
    "Tu observes attentivement car certaines fonctionnalités te dérangent : elles n'ont jamais eu d'écran auparavant."
    "Avec lenteur, tu appuies sur le numéro de téléphone du clavier, aux touches de petite taille, mais tu parviens à le saisir du premier coup."
    "Tu décroches le téléphone et tu attends que la sonnerie arrive pour la laisser résonner dans la cabine en apaisant le vide environnant."
    "Tu as erré dans ta tête pendant un temps indéfini, la sonnerie se prolongeant, le son s'éloignant dans le vide obscur."
    "Tu te demandes pourquoi elle met autant de temps à répondre. Elle n'est pas chez elle en ce moment ? Peut-être qu'elle a eu des heures de travail supplémentaires et qu'elle n'a pas pu venir ce soir."
    "Quelle que soit la raison, elle doit être valable. Réfléchis un peu. Elle ne t'ignorerait pas, n'est-ce pas ?{w} Peut-être qu'elle t'ignore et qu'elle regarde le téléphone qui sonne en ce moment même."
    "Soudain, un déclic se fait entendre de l'autre côté de la ligne, comme pour te prouver que tu as tort. Tu entends une voix féminine inquisitrice, qui répond à l'appel."
    
    " ???" "... Allô, qui est-ce ?"
    
    hl "Marie-Jil, c'est moi, Howell !"
    
    mj "Howell ! C'est vraiment toi ! J'ai attendu ton appel toute la journée, tu le sais ?"

    "Un profond soupir s'échappe de sa long museau, soulagée d'entendre ta voix"

    mj "Tu es déjà arrivé à la Maison ?"

    hl "Non, pas encore."

    mj "Tu es toujours sur la route ? Comment as-tu fait pour me contacter alors ?"

    hl "Eh bien apparemment, ils ont commencé à installer des cabines téléphoniques sur les aires de repos le long des routes." 

    mj "Ah oui ça me dit quelque chose. J’en avais vu la dernière fois que j’étais allé en ville."
    mj "Je n’avais pas percuté sur le moment mais ça veut dire que bientôt, il n’y aura plus un seul endroit sur Terre où je pourrais pas te contacter, hein ?"

    hl "Oui sûrement..."

    mj "À ce rythme, où que tu sois sur Terre, jamais nous pourrions être séparés, toi et moi."
    mj "Ne trouves–tu pas ça merveilleux ?"

    "Tu serres le combiné. Tu considères la question."
    "Ça devrait être le rêve non ?"
    "Pourtant la boule dans ta gorge te dit le contraire."
    "Tu la ravales et tu énonces avec difficulté ta réponse."

    hl "Oui, sûrement."
    hl "Ce serait... Merveilleux."

    "Le silence au bout du fil te perce les oreilles."
    "N’as–t—elle pas aimé ta réponse ?"
    "N’était–ce pas ce qu’elle voulait entendre ?"
    "Finalement, tu l’entends glousser."

    mj "Tu es sûr, Howl ?"
    mj "Je sais que c’est moi qui ai proposé mais pour toi ce serait trop, non ?"
    mj "J’aime aussi bien avoir mes moments à moi."

    hl "Si si, c’est... vrai"
    
    hl "Mais tu sais, pas besoin d’être connecté, tu aurais dû venir, toi aussi, faire le voyage avec nous ! Tu me manques vraiment !"

    mj "Moi ? Tu te débrouilles très bien sans moi, ne t'inquiète pas. Et je voulais venir mais tu sais que je ne peux pas, je dois travailler demain. Je dois aider ma mère avec son restaurant."
    
    hl "Tu aurais pu lui expliquer la situation. Je suis sûr qu'elle t'aurait laissé venir."

    mj "Ce n'est pas comme ça, Howl. Elle vient d'ouvrir son restaurant. Je ne peux pas la laisser tomber comme ça." 
    mj "Elle a vraiment besoin de moi, je n'ai pas le temps de me perdre dans une maison perdue au fond de la campagne normande malheureusement."

    hl "D'accord... mais la prochaine fois, tu devras venir !"

    "Elle s'esclaffe doucement devant ta vivacité."

    ### TODO: Allonger le temps que MJ parle

    mj "Tu sais, ton attitude de tout à l'heure m'a rappelé la fois où nous nous sommes pour la première fois-{nw}"

    az "La voilà qui repart. Sur sa lancée, comme toujours."
    
    dk "Eh bien, ce serait impoli de l'interrompre, tu ne crois pas ?"

    az "Alors ne le fais pas"
    az "Pense à autre chose."

    menu:
        "L’écouter" :
            $ derek_score += 1
            "Tu décides que tu devrais au moins l'écouter un chouïa avant de déclarer qu'elle est ennuyeuse"
            mj "-nous sommes allés à la plage pour la première fois ?"

            hl "Oui... Je crois que oui..."

            mj "Eh bien Ammon a toujours aimé faire le con pour te taquiner ; et je dois admettre avec lui que tes réactions en valaient la peine."
            mj "Ce jour-là, Ammon a décidé qu'il allait danser sur les rochers et vous provoquer pour que vous veniez le chercher..."
            mj "C'est du moins ce qu'il semblait de loin."
            mj "Quoi qu'il en soit, je pense qu'à un moment donné, ça a marché et tu l'as chargé. Il a tellement eu peur qu'il est tombé du rocher et s'est foulé la cheville. Je ne pense pas que les cailloux l'aient aidé."
            mj "Heureusement que ton père qui nous a conduits à la plage était dans les parages parce qu'il a pu lui prodiguer les premiers soins avant d'arriver à un médecin."
            mj "Bon, ça a un peu gâché notre petite sortie mais en y repensant, Ammon et toi étiez toujours à la gorge l'un de l'autre mais vous avez tout supporté contre vents et marées."
            mj "C'est fascinant de voir comment vous avez réussi à rester ensemble."

            mj "Au fait, tu te souviens quand on s'est mis ensemble pour la première fois ?"

            "Marie–Jil souffle doucement du nez, amusée."

            mj "J’imagine que non. Ce serait pas anormal pour toi d’oublier de ce genre de truc de toute façon."
        "Penser à autre chose" :
            $ azzy_score += 1
            "Tu laisses ton esprit vagabonder ailleurs. Tu es déjà passé par là. Écouter ses diatribes interminables. Tu n'as jamais réussi à te concentrer plus d'une minute."
            "Alors cette fois, tu abandonnes instantanément, trop fatiguée pour lutter contre ton ennui."
            "Cela ne veut pas dire que tu ne l'appréciais pas."
            "Tu l'aimais bien, c'est une fille merveilleuse" 
            "Vous êtes des amis d'enfance et vous étiez collés l'un à l'autre comme la main dans le gant et jamais tu n'as été séparé d'elle" 
            "Elle vivait dans ton village natal, alors vous aviez l'habitude de jouer ensemble tous les jours"
            "Pour une raison ou une autre, elle supportait ta présence, contrairement à la plupart de tes camarades de ton âge. Cela faisait d'elle une amie précieuse." 
            "Elle a toujours été friande de tes fantasmes et de tes jeux, tu en avais beaucoup quand tu étais jeune."
            "Tu lisais un livre sur un garçon vêtu d'une tunique verte qui partait à l'aventure et tu faisais semblant d'être ce même garçon en rejouant les événements du livre." 
            "La plupart des enfants te prendraient pour un cas social et la plupart l'ont fait"
            "Mais pas Marie-Jil. Marie-Jil jouait avec toi dans tes petits jeux imaginaires." 

            mj "Alors hum Howl, Howl, tu m'écoutes ?"

            "Tu te réveilles de ta rêverie, tous ces souvenirs t’ayant laissé groggy"

            hl "Oui, MJ, tu disais ?"

            mj "... je disais, tu te souviens quand on s'est mis ensemble pour la première fois ? Sûrement pas. Ce serait anormal pour toi d’oublier de ce genre de truc de toute façon."
    
    "Sa dernière remarque ne te revient pas vraiment. Une note d’amertume suinte de ces mots."
    "Confus, te grattant le cuir chevelu, tu te remémores ces derniers mots."

    show canteen at zpos_bg with dissolve
    show canteen:
        ease 1 blur 16
    "Quand vous vous êtes mis ensemble pour la première fois, hein ? Oui, tu t'en souviens, comment pourrais-tu ne pas t'en souvenir ? C'était un jour très spécial après tout."
    "Tu ne t'y attendais pas. Un jour, vous mangiez à la cafétéria de votre lycée." 
    "La foule habituelle de la cafétéria s'était envolée pour un événement qui ne t'intéressait sûrement pas, alors il ne restait plus grand monde ici."
    "Tu tapotais faiblement la nourriture devant toi, n'ayant pas vraiment faim." 
    "Le calme inhabituel, cependant, t'avait aidé à te concentrer et à prendre quelques bouchées dans ton assiette, mais tu avais beau essayer, ton assiette était restée, pour la plupart, intacte."
    "À ta gauche, Ammon était allongé sur sa chaise, son ventre lui faisant mal." 
    # "Tu avais accepté docilement, par principe, tu ne refuserais jamais un défi lancé par ton trublion préféré."
    # "Mais tu n'as pas eu le cœur - ni l'estomac - de le suivre dans son défi." 
    # "Tu avais été surpris par son dévouement, ce jour-là vous aviez été nourris de hachis parmentier et vous aviez tous les deux pris des rations doubles, alors ça lui pesait beaucoup sur l'estomac."
    # "Il était tellement rassasié que sa chemise ne tenait plus son ventre, tu pouvais donc admirer son nombril et la bosse que la nourriture avait formée dans ses entrailles."
    # "Essayant de lui remonter le moral, tu as frotté son abdomen et tu as été accueilli par une agréable bouillie."
    # "Vous ne pouviez pas vous arrêter alors vous avez continué à frotter, espérant l'apaiser. À ton grand désarroi, Ammon n'y a pas vu d'inconvénient et il a même laissé échapper quelques grincements de rire et de satisfaction."

    # hl "Heheh, qu'est-ce que tu crois que ça va être ?"

    # "Des roses de confusion sur le visage d'Ammon, encore contorsionné par la douleur mêlée de douceur."

    # am "Je-je pense que ça va être quoi ?"

    # "Je regarde son ventre."

    # hl "Un garçon ou une fille ?"

    # am "Un-une fille- *Buuuurrurp* oh shut u-up man."

    # "Ammon continuait à roter de façon incontrôlée, alors tu retires ta main de lui, dégoûtée" 
    # "Tu étais moins pressé qu'avant de finir ton repas alors tu as muloté sur la table, tu t'es appuyé dessus, perturbé."
    "Pour une raison ou une autre, ce jour–là, il avait décidé de se gaver de nourriture. Même il avait acheté une deuxième portion à la cafétéria."
    "Qui plus est, le plat du jour étant hachis parmentier, une étrange admiration monta en toi : d’où venait cet appétit ?"
    "Malgré toutes tes tentatives d’en savoir plus sur son enthousiasme, il ne répondit pas et continua de manger en silence sa bouillie."
    "Cependant, cette poussée d’énergie fut de courte durée, parce qu’il finit par se rouler en boule sur sa chaise, le mal au ventre."
    "Il voulait te parler de quelque chose auparavant ; mais avec sa frénésie alimentaire, tu avais laissé tomber."
    "Quelque chose de plus urgeant te préoccupait."
    "Cela commençait à t'inquiéter : Marie-Jil n'était toujours pas venue à la cafétéria, aujourd'hui. Vous mangiez toujours ensemble tous les trois à midi, alors tu t'es demandé où elle pouvait bien être." 
    "D'habitude, elle n'était jamais en retard"
    "Peut-être qu'elle est allée au match qui se déroulait pendant le déjeuner, mais elle n'était pas vraiment intéressée par le sport et elle vous l'aurait dit, si c'était le cas." 
    "Ou alors son cours durait plus longtemps que prévu. Mais encore une fois, tu ne pensais pas que c'était ça."

    hl "Je me demande où elle est..."
    "À voix haute, tu t'attendais à ce qu'Ammon te réponde, ou au moins dise quelque chose, mais aucune réponse alors qu'Ammon gisait maintenant apparemment inconscient sur sa chaise, la tête dans son plat."
    "Tout à coup, Marie-Jil s’approcha de toi, n'apportant aucune nourriture mais un air tendu sur son chemin."
    # "Marie-Jil s'est tenue enfermée par terre, très anxieuse, ne sachant pas où se placer.  la nervosité de la situation t'a fait faire des mouvements de queue à la tienne."
    ## TODO : ajouter le sprite de Marie-Jil ?
    mj "Salut Howl..."

    hl "Salut MJ... Pourquoi t’es en retard ? Quelque chose ne va pas ?"

    "Marie-Jil releva la tête, choquée, comme si elle avait été démasquée."

    mj "Hein, qu'est-ce que tu veux dire ?"

    hl "Tu es toute nerveuse. T’es pas souvent comme ça. Qu’est–ce qu’il s’est passé ?"

    mj "Il s’est rien passé !!!{w} Oh... Salut Ammon..."
    mj "Ammon, pourrais-tu laisser Howl et moi seuls ?"

    "Après plusieurs demandes, elle finit par remarquer Ammon et son état déplorable. Désespérée par le vue qu'elle contemplait, elle finit par l’ignorer et reporta son attention sur toi."

    mj "S'il te plaît, avant que tu ne dises quelque chose, laisse-moi finir, Howl."

    "Sentant la gravité de la situation, tu la regardas dans les yeux. Tu as estimé qu'elle avait besoin de toute ton attention"
    "La biche découragée joignit les mains, inspirant, essayant de rassembler tout le courage nécessaire." 
    "Elle s'attarde un temps à savoir si elle avait fait le bon choix" 
    "Ne pouvant pas l'aider à ce moment-là, tu la laisses respirer. Elle avait beaucoup de choses en tête et tu vois des brins de doute, de confusion et de détermination tressaillir au coin de son long museau."
    "Elle frotte ses paupières une dernière fois et la résolution monta dans ses yeux, déterminée à en finir."
    
    mj "Tu sais que nous sommes amis depuis très longtemps, Howl ?"

    hl "Oui, je le sais ?"

    mj "Eh bien je suis vraiment heureux de notre amitié en ce moment, de la façon dont tu as toujours été là pour moi."

    hl "Et tu as toujours été là pour moi ! Pas besoin de s'inquiéter o-{nw}"

    mj "Une seconde s'il te plaît...{w} Ce que je voulais dire, c'est que tu es une personne merveilleuse et que j'apprécie chaque moment passé avec toi."

    "Ammon se releva lentement d'entre les morts, prêtant une oreille intéressée à la direction que prenait la discussion. Au fond de toi, tu savais où elle allait et il le savait aussi. Tu regardas Marie-Jil."

    mj "Mais ces derniers temps, j'ai senti un changement en moi. Je veux passer plus de temps avec toi, je veux être plus proche de toi. Plus proche que notre lien actuel."
    mj "Ces dernières années, j'en suis venu à vouloir un changement dans notre relation, quelque chose que l'Amitié ne peut pas offrir. Ces derniers mois, j'ai réfléchi à la question."
    mj "Est-ce vraiment bien ? Ai-je besoin d'une relation plus étroite que celle que nous avons actuellement. Puis j'ai réalisé."

    "Pendant qu'elle prononçait tout cela, elle tirait à répétition sur son cardigan, le regard ailleurs, cherchant à se détendre."
    "Cependant, elle croisa ton regard."
    "Son visage a commencé à rosir alors elle s'est retournée, rompant le contact visuel avec toi, te rendant incapable d'observer encore les traits de son visage." 
    "Ammon, à ce moment-là, était totalement alerte, écoutant ses moindres mots, ses moindres sons sortant de sa bouche, ses moindres mouvements de doigts, ses moindres tics d'anxiété."
    "Tu avais dû exercer une pression trop forte sur elle car elle a crié la phrase suivante"

    mj "Arrête de me fixer ! !! Tu me rends anxieuse. Très bien ! Ce que je veux dire, c'est que..."
    mj "Je ne peux plus continuer comme ça. Il faut que je sache. Je suis sûr que, si je n'ai pas la réponse que je souhaite, nous pourrons revenir en arrière."
    mj "Alors... je voulais savoir, si ces sentiments sont réciproques et si tu veux explorer et comprendre ces sentiments avec moi, alors j'en serais très heureuse.... Ce que je veux vraiment dire c'est :-"

    "Elle serra fort son cardigan, ne voulant pas lâcher son seul dernier soutien. Ammon et toi étiez tous deux suspendus à ses lèvres en attendant ses prochains mots."

    mj ".... Veux-tu sortir avec moi... ?"

    am "QUOI ?"

    # J’ai envie de vomir chaque fois que je lis ça

    "Ammon n'a pas pu rester en place et s'est levé de sa chaise sous le choc, la mâchoire pendante. Après son interjection, il est resté silencieux, incapable d'en dire plus."
    "À ce moment-là, un déclic s'est produit en toi. Tous tes proches n'ont pas cessé de te répéter que Marie-Jil et toi feriez un couple formidable." 
    "Tu n'y avais jamais pensé, c'était ton amie la plus proche, pas une amante."
    "Mais maintenant que Marie-Jil le pensait aussi, tu y réfléchis. Comme tu es bête de ne pas y avoir pensé !" 
    "C'est tout à fait naturel et logique que vous finissiez ensemble. Vous êtes un garçon et une fille et vous êtes si proches l'un de l'autre. Bien sûr que ça doit être le cas"
    "Une fois que l'épiphanie t'a traversé la tête, tu savais ce qu'il fallait faire" 
    "Marie-Jil est une personne tellement géniale, elle est intelligente, elle est créative que tu veux être avec elle toute ta vie ; et si être un couple signifiait cela, alors tu serais de tout cœur d'accord."
    "Tu t'élanças vers elle et tu la prends dans tes bras, dans une étreinte amoureuse qui ne peut signifier qu'une seule chose, et qu'une seule réponse possible, mais tu ne peux pas t'empêcher de la dire à voix haute."

    # scène phonebooth with dissolve
    hide canteen with dissolve

    mj "Je me souviendrai toujours de ce que tu as dit..."

    show canteen at zpos_bg with dissolve

    "Howl + Marie-Jil" "Bien sûr, je serai ton petit ami ! Pourquoi ne l'avons-nous pas fait plus tôt !"

    am "Je crois que je vais vomir..."

    "Ammon s'est brusquement levé et s'est précipité vers les toilettes"

    # scène phonebooth with dissolve
    hide canteen with dissolve

    hl "J'ai dû allé le voir ce jour-là aussi... Il n'aurait pas dû manger autant."

    mj "En fait Howly... C'est moi qui suis allé le voir, je t'ai fait rester à notre table pour surveiller nos affaires."

    "Un sentiment de gêne et d'inconfort émane des paroles de Marie-Jil comme l'ouverture de poupées matriochka." 
    "Elle a dû assister à son bain dans son vomi après tout. Tu ne voudrais pas être celui qui a dû y aller ce jour-là."
    
    mj "Au fait, puisqu'on parle de lui, est-ce que tout va bien avec Ammon ?"

    hl "Qu'est-ce que tu veux dire par là ?"

    ## TODO: Retoucher ces deux lignes

    mj "Je sais qu'il peut être épuisant, parfois. Tu n'as rien fait d'imprudent avec lui, n'est-ce pas ?"
    
    "Une voix inquiète sort du combiné. On devient toujours audacieux avec un chien crétin dans les parages."

    hl "Non, rien de tel, heureusement."

    "Le silence emplit l'air. Marie-Jil te renvoie un rire."

    # mj "Bien sûr Howl."
    # mj "Quelque chose qui vaille la peine de me parler de lui ?"
    
    # menu:
    #     "Rien de spécial" :
    #         mj "Tu es sûr ? Rien avec Ammon ? Tu ne dis pas qu'il ne s'est rien passé de spécial lorsque tu as voyagé avec LE Ammon ?"
    #         "Tu fais une pause."
    #         hl "{cps=3}...{/cps} Non, je ne me souviens de rien de spécial."
    #         mj "{cps=3}...{/cps} Tu ne te souviens pas..."
    #     "Ammon est un con" if radio_on :
    #         hl "Ammon est un connard"
    #         mj "Qu'est-ce qu'il a fait déjà ?"
    #         hl "Eh bien je commençais à avoir mal à la tête à cause de sa musique. Alors je lui ai demandé d'éteindre la radio. Il m'a demandé pourquoi."
    #         mj "Qu'est-ce que tu as répondu alors ?"
    #         hl "Que je n'aimais pas la musique, je n'avais pas envie de lui dire que ça me gênait alors j'ai dit ça."
    #         mj "Eh bien je me suis dit . Tu aurais dû lui dire que tu avais mal à la tête, il aurait compris."

    #         "C'est trop tard pour arranger les choses, ne t'embête pas avec ça"

    #         mj "Ne me dis pas que tu as oublié à quel point il pouvait être têtu sur ses préférences ?"
    #         hl "Peut-être que oui."
    #         mj "Tu ne t'en souviens pas, hein ?"
    
    mj "Enfin bref, je voulais te parler de quelque chose qui me tracassait ces derniers temps..."

    hl "Huh qu'est-ce que c'est ? Tu t'es encore disputé avec tes parents ?"

    mj "Non, ce n'est pas ça. C'est quelque chose qui me préoccupe. Quelque chose qui se passe ces derniers temps."

    "Elle s'agrippe plus fortement au téléphone qu'auparavant. La question était accrochée à son cœur depuis un bon moment."

    hl "Hein, d'accord ? Qu'est-ce qu'il y a ? Qu'est-ce que ça a à voir avec moi ?"

    mj "Je voulais te parler de toi ces derniers temps"

    "Déstabilisée, elle peine à trouver les mots sur ses pensées. Son attitude générale te perturbe."
    "Elle s'impatiente. Tu la laisses s'expliquer."

    mj "Ça va ?"

    hl "Qu'est-ce que tu veux dire ?"

    mj "Avec ton voyage, as-tu pu repenser, éclaircir tes idées, réfléchir à ce qui s'est passé récemment."

    "Elle a l'air préoccupée. Irritée. As-tu été à ce point à côté de la plaque ces derniers temps ?" 
    "Tout au plus, tu t'es sentie un peu fatiguée par la pression, mais c'est tout"
    "Elle attend ta réponse, attendant à une justification approfondie. Tu n'en as pas. Tu es complètement confus." 
    "Tu te grattes la nuque, espérant que quelque chose en sortira, mais rien. Seulement l'oubli et le vide obscur."

    hl "Je ne sais vraiment pas de quoi tu parles. Je ne me souviens de rien de notable qui se soit passé tout à l'heure. Tout va bien, mais..."

    stop music
    play music "audio/music/anger.mp3" 

    mj "Oh mon dieu, pour Jésus Christ." 
    mj "Tu es sérieux, Howl ???? Ça fait un mois que tu prétends que tout va bien et tu veux que je te croie !??"
    
    hl "Huh..."

    show phonebooth:
        ease 1 blur 32
        ease 1 blur 16
        repeat
    "La confusion monte en toi"
    "Un éclat de voix déferle dans le téléphone et tu manques de le lâcher." 
    "Tu paniques. Que s'est-il passé, pour l'amour de Dieu ? Tu fouilles dans ton esprit."
    "Tu es dans le vide, la tête absente, et tu contemples une boîte noire. Tu essaies de l'ouvrir. Tu n'y arrives pas. Tu as peur. Tu ne devrais pas aller plus loin"
    "Tes mains sont mouillées. À chaque seconde, tu es à deux doigts de le laisser glisser" 
    "Tu transpires abondamment. Ta gorge se serre."
    "Tu te tais."

    mj "Howell ! réponds-moi s'il te plaît !" 
    mj "Ta mère était morte d'inquiétude pour toi !"
    mj "Alors s'il te plaît, aide-moi, Howell... S'il te plaît Howell, laisse moi t’aider. Veux-tu me dire ce qui s'est passé le mois dernier ?"
    
    hl "Le mois.. Dernier ?"
    
    "Tu as demandé confus. Tout ce qu'elle dit, tu ne l'entends pas." 
    "Plus exactement, tu l'entends parfaitement mais tu refuses de l'entendre. La boîte noire ne doit jamais être ouverte et chaque tentative envoie une palpitation dans ton cerveau." 
    "Tu as mal à la tête. Tu fulmines. S'il te plaît, arrête. S'il te plaît, arrête, tu n'en peux plus."
    
    menu:
        "L’arrêter" :
            hl "S'il te plaît.... arrête."
            mj " ... Je ne m'arrêterai pas. J'en ai {w=1.0}assez. Je ne m'arrêterai pas tant que je n'aurai pas fini. " 
        
        " Essayer de changer de sujet " :
            hl "On ne peut pas... parler d'autres choses ?"
            mj "Non, on va pas faire ça ! J'en ai assez. Tu me laisses finir."

    
    mj "Tu répondras à mes questions, Howell et tu ne pourras pas t'échapper éternellement"
    mj "Nous n'avons jamais posé de questions, nous ne voulions pas te mettre la pression. Nous t'avons laissé respirer, te reposer, faire ton deuil." 
    mj "Mais j'en ai marre."
    mj "Mais un jour ou l'autre, tu devras nous dire ce qui s'est passé et j'en ai marre de ne pas savoir la vérité."
    mj "Alors dis-moi Howell. Que s'est-il passé, le mois dernier, le jour où tu as disparu dans la forêt ?"
    mj "Nous t'attendions ce jour-là."
    
    "Tu paniques encore plus. Porté disparu, ça fait tilt. Tu réalises. La boîte se resserre encore plus. Ce qui s'est passé ce jour-là doit rester secret à tout prix." 
    "Elle ne doit pas aller plus loin dans sa croisade de questionnement. Tu devrais la faire taire, sinon tu ne sais pas ce qu'il peut advenir de toi."
    "Elle représente une menace pour ta tranquillité. Ton apathie."
    
    hl "Je te l'ai dit et je te l'ai dit, je ne sais pas ! Combien de fois dois-je te le dire ? !! Je ne sais pas, je ne sais pas et je ne sais toujours pas ! Comment ça se passe pour toi !"
    
    mj "J'en ai marre de toi et de tes « je sais pas », « je sais pas » ! Tu me mens comme tu respires ! Tu sais et j'obtiendrai la vérité sur ce jour."

    "Le déluge de ton corps s'écoule sur tes paumes moites. Tes mains tremblotantes tremblent comme un pécheur le jour du jugement dernier."
    "Le téléphone glisse de tes mains et tombe ; ainsi, son bruit sourd résonne lourdement dans la cabine. Tu le ramasses précipitamment et l'enfonce dans ton oreille par peur d'agacer le Porteur de tes rétributions." 
    "Tu en as peur, tu as peur de ton jugement, tu as peur de la Vérité"
    
    mj "N’essaye pas de t'éclipser. Si ce n'est aujourd'hui, je te ferai avouer demain, ou après demain, dans quatre jours, dans une semaine, dans un mois, l’année prochaine, juste attends-moi."
    mj "Je veux dire, pour l'amour du ciel, tu as disparu pendant une semaine ?? Une semaine entière et tu n'as même pas été blessée."
    mj "Ça n'arrive jamais ! Tu comprends ça ??? On pensait tous que tu étais mort, putain."
    mj "Ammon n'a pas dormi une nuit, ta mère a pleuré toute la journée sans arrêt, et je t'ai cherché partout dans cette putain de forêt."
    mj "Je ne pouvais pas m'arrêter. Rien que l'idée de te voir, vivant, dans le noir, dans les bois, tout seul, me rendait folle."
    mj "Mais nous avons eu beau chercher, nous ne t'avons jamais trouvé. Tout le village t'a cherché !"
    mj "Je pouvais presque croire que t’étais évaporé..."
    
    "Marie–Jil déglutit"
    
    mj "Et puis, de nulle part, tu réapparais comme si rien ne s'était arrivé ?"
    mj "Pas blessé, sans aucune conséquence, quoi qu’elles en soient ! C'est comme si tu n'avais jamais disparu..."
    mj "Tu sais à quel point c'est étrange ?"
    mj "Howell, le mec qui n’a jamais quitté sa chambre de sa vie, devient un expert en survie ??"
    mj "Tu n'avais rien sur toi, tu t'attends à ce je croie que tu n'aies ni bu ni mangé pendant toute une putain de semaine ??"
    mj "Comment t’as survécu ??"
    "Tu n'avais besoin pas de boire."
    "Pas qu’elle puisse comprendre de toute façon."

    mj "Tu sais que ce jour-là, tu n'étais pas le seul à avoir disparu ?"
    mj "Tout le monde n'a pas eu de ta chance..."
    pause 1.0
    mj "Alors s'il te plaît, dis-moi ce qui s'est passé. Il n’a pas pu aller bien loin ! Nous pouvons encore le retrouver !"
    mj "Je m’en fous qu’il soit vivant ou qu’il soit crevé la gueule ouverte dans une rivière dans ces bois de MERDE."

    "Elle sanglote. Des larmes chaudes coulent sur le téléphone."

    mj "S’il te plaît, Howell... Rends–le nous... Rends–le moi..."
    mj "DIS MOI OÙ IL EST."

    "Après son éclat, elle ne parle plus. Les pleurs envahissent la cabine."
    "Pourtant tu restes silencieux."
    "Tu rassembles ce qui te reste de courage."

    hl "Je ne sais pas..."

    "Les pleurs s’arrêtent. Un fort soupir torturé saturent le combiné"

    mj "Je savais que tu dirais ça. Tu es content qu'il ne soit plus là, c’est ça ? Pas moi."

    mj "Alors réponds-moi s'il te plaît..."

    hl "Je sais pas... Je sais pas, je te jure... Je me souviens plus."

    mj "Ok laisse moi reformuler plus clairement pour que tu puisses t'en souvenir..."

    "S'il te plaît. Elle ne devrait pas. Pourquoi est-elle toujours comme ça ?"
    "Tout le monde s'en sortirait mieux si elle se mêlait de ses affaires..."
    "Il y a des choses qu'il vaut mieux oublier."

    hl "S'il te plaît... Ne fais pas ça."
    
    mj "Que faisais-tu le 13 septembre ? Est—ce que t’étais avec lui ?"
    stop music
    extend "avec ×××××××××××××××××××××××{nw}"

    "Ça te percute à plein fouet. Cette date. Tu ne voulais pas l'entendre."

    dk "Ça commence à devenir incontrôlable...{w} Comme toujours."

    az "La boîte s’entrouvre."
    
    menu:
        "Laisser aller" :
            jump you_dont_understand
        "Contenir tout prix" :
            jump you_dont_understand
    
    label you_dont_understand:
            az "J’ai peur que tu comprennes pas ce qu’il se passe ici."
            
            dk "Ce n'est pas toi qui décides."
    
    "Tu regardes vers le bas. Tu tiens la boîte. Tu la laisses glisser. La boîte s'ouvre."

    show expression "#000" with blink_reverse
    "Tu contemples la colline. Il t'attendait. Tu as amené quelqu'un. Il est euphorique."
    "Toi aussi, tu es euphorique. Tu as fait ce qu'il a demandé."
    "Il effleure ta joue. Une poussée d'adrénaline te traverse. Tu veux que sa main soit éternelle, qu'elle ne quitte jamais ta peau."
    "Tu veux son étreinte plus que tout. Tu es prête à faire n'importe quoi pour lui. Il sait comment remplir ton cœur malade. Ton cœur déviant."
    "Tu sais que tu es déjà un cas perdu, alors tu le laisses te corrompre encore plus. Qu'y avait-il de bon en toi de toute façon ?"
    "Tu lui présentes ton partenaire."
    "Il enroule ses mains autour de son cou. {w} Tu aimes ça.{nw}"

    hl "Non."
    
    hide expression "#000" with blink_transition

    "Tu aimes ça."
    
    hl "Non..."

    "Tu aimes ça."

    hl "Non................."

    "Tu as aimé ça."
    
    hl "Non......................................"

    "Tu as aimé."

    hl "NON, c’est faux."
    hl "Je n'ai pas aimé."

    "Si, tu as aimé"

    mj "Attends, Howl, qu'est-ce qui se passe ??? Qu'est-ce que tu racontes ?"

    hl "JE N’AI PAS AIMÉ."

    "..."

    "Si tu as aimé, sale monstre."

    play music "audio/music/uboa.mp3"

    show phonebooth at shaking
    
    hl "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    show phonebooth:
        xoffset 0
        yoffset 0

    hl "Tais-toi, je ne suis pas un monstre"

    show phonebooth:
        easein 0.5 blur 96
        easein 0.5 blur 128
        repeat

    mj "Qu'est-ce qui se passe, Howl, je comprends pas."
    mj "Tu marmonnes comme pas possible !!"
    mj "S’il te plaît réponds moi ???"

    hl "Je ne suis pas un monstre, je ne suis pas un monstre je ne suis pas un monstre"
    hl "je vais juste inspirer et expirer et tout ira bien"
    hl "puces et lucioles amicales puces et lucioles amicales"
    hl "les puces et les lucioles amicales les lucioles et les puces amicales"
    hl "les mouches à feu et les puces les mouches à feu et les puces les mouches à feu et les puces les mouches à feu les puces les puces les puces les puces les puces les puces les puces les puces les puces les puces les puces"
    hl "amicales les puces les puces les puces les puces les puces les puces les puces les puces les puces les puces les puces les puces les puces les puces les puces les puces les puces les puces"


    mj "Qu'est-ce que tu racontes ???"
    mj "Écoute moi !{nw}"

    hl "{size=60}LA FERME{/size}{w=0.5}{nw}"
    stop music

    play sound "audio/sounds/glass_breaking.ogg"
    ### TODO : Effet d'ivresse
    show phonebooth:
        ease 2 blur 128
    with sshake
    
    play sfx "audio/sounds/ear_ringing.ogg" fadein 0.5 volume 0.3
    
    show expression "#F00" :
        alpha 0.0
        zoom 2.535
        align (0.5, 0.5)
        ease 2 alpha 0.5
    pause 2.0
    
    "Un grand fracas se répercute et résonne dans la cabine téléphonique" 
    "Affalé, tu ne bouges plus" 
    "La tête vide, un bruit blanc strident et perçant résonne dans tes oreilles. Tu es agrippé au sol et tu ne te relèveras plus."
    show phonebooth:
        ease 1 blur 32
    "Lorsque ta vision ensanglantée revient en place, d’un œil mort, tu observes le récepteur détruit en mille morceaux au sol{w}, tu en viens à te demander ce qui t'a guidé jusqu'ici." 
    "Tu lèves tes mains à hauteur d’œil, le sang coulant le long de tes poignets." 
    "Que s'est-il passé pour que tu en viennes à les salir. {w}Que s’est–il passé{w}, le vendredi 13 septembre."

    jump rest_area_2

label rest_area_2:
    stop music
    stop sfx fadeout 10.0

    scene parkinglot :
        zoom 1.25
    with Fade(0.5, 6.0, 0.5)

    "Tu t'allonges sur le châssis de la moto. Tu ne peux pas rester debout. Se traîner jusqu'ici depuis la cabine était déjà assez difficile comme ça."
    "La fatigue et ton récent comportement agité te plongent dans un état second - là mais tout à fait pas là."
    "Tu te frottes les yeux. Si tu avais envie de dormir, ce n'est plus le cas. Tu as juste la nausée et tu veux rentrer chez toi le plus vite possible."
    "Mais tu ne le feras pas. Alors tu te contentes de comater. En attendant Ammon."
    
    am "Huh tu vas bien Howl ?"

    show ammon at american_shot with dissolve

    "Tu sens une main sur ton épaule. Tu es sur le point de lever la tête"
    camera at close_shot
    extend " mais le chien s'accroupit à hauteur de tes yeux. "
    "Le fait d'avoir son visage près du tien te met mal à l'aise mais tu ravales ta salive et tu le fixes en retour."

    am "T'as pas l'air bien."
    am "Je suis désolé d'avoir pris autant de temps. J'avais quelques affaires à régler. Je ne pensais pas que cela prendrait autant de temps."
    am "Peut-être qu’on devrait faire une pause plus longue. Va faire une sieste, d'accord ?"

    "Tu repousses sa main d'un coup de poing."

    hl "Je vais bien, je vais bien, laisse-moi respirer."

    am e_noway "... Que s'est-il passé ?" 
    
    hl "Rien."
    
    # colère
    am right e_angry "Tes mains sont pleines de sang"

    show ammon e_neutral pupils_right
    
    "Il regarde la cabine téléphonique"

    am "T’as brisé la vitre ???"

    hl "Non... c’est pas moi..."

    am e_smug pupils "Dis-le avec moins d'enthousiasme la prochaine fois.{w} J'ai failli ne pas te croire."
    am j_noway "Sérieusement. C'est quoi ce bordel ???"

    hl "Rien."

    show ammon front e_neutral j_disgusted
    "La bouche d'Ammon se tord. Il te lance son regard habituel."

    am j_noway "Non y’a pas rien. Tu vas pas bien !"
    am j_disgusted "Crois-moi, tu as une sale tête. Tu devrais te reposer au moins."

    "L'attention soudaine d'Ammon te met sur les nerfs. Il a été froid avec toi pendant tout le trajet. Pourquoi s'intéresser à toi maintenant ?"

    hl "Ammon, je te jure qu’il y a rien."

    "Tu te lèves mais le monde tourne progressivement autour de toi."

    ### TODO: Drunk mode 

    "Le ciel crépusculaire, qui était vide jusqu'à présent, se remplit d'étoiles de toutes les couleurs, cela te rappelle les étranges artefacts que l'on peut trouver sur les photographies de mauvaise qualité."
    "Un mal de tête soudain s'empare de ta tête comme un étau qui la resserre"
    show ammon e_noway j_disgusted
    "Ton estomac se met à trembler. Tes jambes tremblent et ne peuvent plus supporter ton poids. Elles lâchent."

    am j_noway "Howell !"

    "Il te rattrape avant que tu ne heurtes le sol."

    am "Je t'ai dit que tu n'allais pas bien. Ne fais pas ce genre de choses sur moi, d'accord ?"

    show ammon e_neutral pupils_right j_neutral

    "Ses bras musclés s'enroulent autour de toi. Une odeur de lavande se répand dans ton nez."
    
    if azzy_score >= 1 :
        az "Tu devrais t'évanouir plus souvent"
        az "Ou casser de l'herbe"

    show ammon

    "Il t'aide à t'asseoir sur l'herbe. Il s'accroupit encore et te prend à deux mains"

    am "Qu'est-ce qui se passe !"

    hl "J'ai mal à la tête."

    am "C'est peut-être la perte de sang qui te fait ça. Bon je ne suis pas sûr que tu aies perdu tant de sang que ça mais il vaut mieux rafistoler."

    "Tu effleures ton front et les pulsations de ton crâne chauffent ta main"

    am "Fais-moi voir."

    "Il pose aussi sa main sur ton front"

    am j_disgusted pupils_left "Ok je n'ai pas l'impression que tu as de la fièvre mais il faut soigner ton mal de tête et tes mains."
    am "Je crois que j'ai des aspirines et des pansements dans mes affaires, je vais les chercher"

    hide ammon with dissolve

    "Ammon se lève et se dirige vers le coffre de la moto"
    "Encore nauséeux, tu ne peux pas faire grand-chose de plus que de rester assis et que de regarder."
    "Il ouvre le petit coffre et récupère son sac de voyage. Il est de taille moyenne, assez grand pour un voyage de trois jours."
    "Cependant, tu ne peux pas ne pas remarquer quelque chose de familier avec l'une de ses affaires."
    "Quelque chose de cylindrique, quelque chose de bleu."
    "Enfin, Ammon sort de son sac une boîte de médicaments et de pansements et te la donne"

    hide ammon at american_shot with dissolve

    am "Tiens, avec ça, ta tête te fera un peu moins mal qu'avant."

    hl "Merci."

    "Tu attrapes la petite boîte"

    am "Et maintenant, laisse-moi rafistoler ça."

    "Il prend ta main une à une et commence à enrouler le tissu autour des plaies"
    "Il sait ce qu'il fait."

    am "Je n'ai pas de solution antiseptique mais je ne pouvais pas laisser saigner ça."

    am "Attends, tu vas sûrement avoir besoin d'eau. Laisse-moi aller t'en chercher."

    "Il commence à marcher vers le top-box puis s'arrête à mi-chemin."
    "Il réfléchit un moment, pendant un temps étrange puis fait demi-tour."

    am "Je viens de me rappeler que je n'ai pas d'eau. Il y a des robinets dans les toilettes, laisse-moi te..."

    hl "C'est bon tu en as déjà fait assez pour moi."

    "Tu avales l'aspirine d'un seul coup"

    if azzy_score >= 2 :
        az "Fais le malin"
    
    hl "J'ai l'habitude de les prendre sans eau..."

    am "Huh je vois... C'est super. Pas besoin d'aller aux toilettes alors"
    am "Eh bien prends ton temps alors... on partira quand tu seras prêt."

    "La discussion retombe dans le silence. De toute façon, tu es trop fatiguée pour la faire vivre."
    "Tu essaies de te reposer un peu, mais petit à petit, quelque chose commence à te gêner."
    "Tu as déjà vu cette chose qu'Ammon avait dans son sac."
    "Ça ne devrait pas attirer ton attention comme ça. Après tout, ce n'est que son sac. Néanmoins..."
    "Tu te mords la lèvre. Plus tu regardes, plus ça n'a pas de sens. Ton monde tourne, non, se déforme autour de lui."
    "Il t'hypnotise. Tu es attiré par lui. Tu ne peux plus perdre le sac de vue. Le papillon de nuit qui est en toi doit suivre cette luciole."

    "Il faut que tu vérifies ce sac."
    camera at zpos_camera
    "Encore passablement étourdi, tu parviens à te lever. Tu dois te servir de la moto comme support."
    "Mais tu te lèves quand même."

    hl "Hé tu sais quoi ? J'ai soif. Je crois qu'il me reste un peu d'eau dans mon sac."

    am "Tu es sûr, tu ne veux pas que j'aille te la chercher ? Tu n'as pas l'air de pouvoir tenir debout dans ton état."

    hl "Je me sens mieux maintenant. Je me sentirai encore mieux quand je boirai de l'eau, n'est-ce pas ?"

    am "Oui, sûrement..."

    hl "Regarde, je peux me tenir debout ! Je suis un grand garçon, non ?"

    show ammon j_disgusted at american_shot

    "Ammon te regarde, sans être amusé. Tes tentatives pour le taquiner tombent dans l'oreille d'un sourd. Tu roules les yeux."
    "Tu soupires et tu te pinces l'arête entre les yeux."

    hl "Ok, je vais chercher l'eau."

    am "... {w} va."

    label restarea_pointnclick_start:
        python :
            ammon_talked = 0
            current_screen = "restarea"
            current_subscreen = "restarea_butt"
            trunk_explored = False

            padlock_code = [6,1,5,3]
            being_basic = 0
            checked_padlock = 0 
            
            got_stick = False
            got_notebook = False
            good_code = 1309

            birthday = True

        
        # affiche l'écran custom_quickbarç
        camera :
            # perspective False
            zpos 0
            perspective False
        hide ammon
        scene black
        stop music
        show parking at zpos_bg onlayer farback
        play music "audio/music/moment_orange.mp3" loop fadein 1.0
        jump pointnclick_interact_loop


label confront_him:
    # python :
    # del ammon_talked
    # del trunk_explored
    # del code_cadenas
    # del good_code
    # del checked_padlock  
    # del got_stick

    # current_screen = "" 
    stop music fadeout 1.5
    am "Je peux t’aider ?"

    
    show parkinglot :
        xpos -2144
    show ammon at american_shot :
        xpos -1073
    
    pause 0.5

    camera :
        perspective True
        easeout 3 xpos -2032

    pause 1.5
    
    
    play music "audio/music/anger.mp3" loop fadein 0.5
    "Un chien en colère se tient là"
    camera:
        perspective False 
        xpos 0
    
    scene black
    show parking
    show ammon at american_shot
    am "Puis-je savoir ce que tu fais avec mon sac ?"

    "Tu trembles de peur. Pourquoi fallait-il qu'il te voie faire cela. Si seulement tu pouvais voler très loin d'ici."

    hl "Ce n'est... pas ce que tu penses, Ammon..."

    ### TODO : Étendre les conditions avec des objets choisis

    am j_growl "Alors que fais-tu avec mon [picked_from_the_bag] dans ta main ?"

    hl "Je ne sais pas, je l'ai juste pris, je le jure !"

    "Ammon te crie dessus."

    am j_yell "Tu l'as juste pris ? ?? Le cadenas a disparu comme ça ? C'est ce que tu vas me dire ?"
    am j_disgusted "Parce que si c'est le cas, ne me montre plus ta tête de merde."
    am j_growl "Tu as craqué le cadenas, putain, connard"
    am "J’imagine que c’était vraiment compliqué de trouver le code, hein ?"
    am "Bah oui, c’était la date de mon anniversaire. Bien trouvé, Sherlock."
    # am "Je suis content que tu te souviennes de mon anniversaire maintenant. J'espère que ça t'a aidé à déchiffrer le code."
    am "J'aurais préféré que tu le devines il y a un putain de mois ??? Tu ne crois pas ?!"
    am "Au lieu de te perdre dans le bois comme un sale con."
    am "Même, pourquoi t’as fait ça ? Tu me fais pas confiance à ce point ?"
    am "Tu m’as fait chier plus fois qu’il n’en est possible{w} et même là, j'ai tout essayé pour te mettre à l'aise, même te réconforter quand tu râlais et que tu faisais un de tes trop nombreux caprices."
    am pupils_down j_disgusted "Je t'ai mis un bandage..."
    am pupils "Je t’ai accompagné avec ton comportement hystérique toute la journée."
    am j_yell "Et c'est comme ça que tu me remercies en retour ?? En fouillant dans mes affaires ??"

    show ammon j_growl

    "Tu restes fermé. Les larmes débordent de tes yeux. Tu ne voulais pas faire ça."
    
    dk "Pourquoi l'as-tu fait ?"

    hl "S'il te plaît, comprends-moi ! J'étais juste..."

    ### TODO : Peut-être développer l'argument

    am j_yell "Qu'est-ce qu'il y a à comprendre ? NE TOUCHE PAS À MES AFFAIRES, TU COMPRENDS ?"

    "Les larmes coulent sur tes joues."
    "Tu resserrez le [picked_from_the_bag]. C'est le dernier point d'ancrage de votre relation. La dernière chose qui tient debout pour vous deux."

    az "Accroches–y toi."

    dk "Quoi qu’il arrive, ne la lâche pas."

    am j_growl "J'ai tout essayé, je le jure, Howl. J'ai tout essayé pour que tu puisses arrêter de broyer du noir."
    am "J'ai été là pour toi, à chaque fois que tu as eu des moments difficiles."
    am "Et putain, avec toi, c'est tout le temps, c'est comme si je m'occupais d'un bébé, pas d'un adulte !"
    am "Avec Marie-Jil, on pourrait aussi bien être tes parents, avec la façon dont tu la laisses te garder."
    am "Vous êtes censés être un couple, tu te souviens ? Ce n'est pas ta mère !"
    am "Alors pour une fois, fais-toi pousser une paire et arrête de te morfondre."
    am "Tu ne fais même pas attention à elle. Elle n'est pas heureuse avec toi et ne le sera jamais."
    am "Avec toi dans les parages, nous ne le serons jamais tous les deux !"

    "Le déluge de critiques et de reproches te submerge. Tu as envie de rétorquer, de lui faire fermer la bouche."
    "Mais tu ne trouves rien à dire. Parce que..."
    "Il a raison, n'est-ce pas ?"

    am "Tu sais quoi ? Tu n'aurais jamais dû revenir."

    hl "... Quoi ?"

    am "Tu n'aurais pas dû revenir de ces bois."
    am j_yell "Je ne peux plus te supporter. Tu m'entraînes vers le bas. Tu m’empoisonnes !!!"
    am j_growl "Chaque fois que tu es là, ma vie est un putain de cauchemar."
    am right e_smug j_disgusted "Pourquoi t’es revenu ? Je ne comprends pas."
    am pupils_right "Pourquoi toi et pas lui ??"

    show ammon pupils_down
    
    "Il se tait."

    am pupils "... Je ne peux pas m'empêcher de penser que la vie est tout simplement injuste quand je te regarde."

    "Tu claudiques dans ton pantalon. Tu ne peux que marmonner ces mots."

    hl "Pourquoi... pourquoi tu dis ça ?..."
    hl "Qu'est-ce que j'ai fait pour mériter ça ?..."

    am front e_neutral "Je ne prendrai même pas la peine de te répondre. C’en vaut même pas la peine."
    am j_growl "Tu ne le mérites pas."

    am j_noway "Mais je vais te dire une chose. Pourquoi t’es pas venu pour mon anniversaire ?"

    hl "..."

    am j_growl "Je t'attendais. Je ne pouvais pas attendre une seconde de plus. Pour ce jour, je ne souhaitais qu'une chose, une seule chose !"
    am "Que tu sois là. Avec moi. C'était mon seul souhait."

    hl "Mais tu sais que je n'aurais pas pu, ce jour... Je me souviens de rien"
    hl "Ce n'est pas ma faute... Ce n'est pas juste..."

    am "..."
    am "... Tu n'as jamais disparu, n'est-ce pas ?"

    hl "huh-"

    am "Tu es allé dans la forêt tout seul."
    am "Enfin, pas tout seul, dis–moi ? "

    hl "Ce n'est pas vrai, c'est juste que je ne me souviens pas..."

    am "Ne t'inquiète pas. Je le sais, c'est tout. Tu n'as jamais été honnête de toute façon."
    am "C'est de ta faute... Je veux dire :"

    am "Est-ce que tu te regardes au moins parfois ! Tu es un putain de cadavre ambulant ! Un monstre !"
    am "Que tu sois revenu ou non n'a donc rien changé. Tu es peut-être en train de marcher..."
    am "Mais tu aurais dû rester mort. À l'époque. Dans les bois. Là où je n'aurais plus eu à regarder ta triste excuse pathétique de visage."
    am "Non..."
    am "Tu sais quoi ? Tu es déjà mort pour moi."
    am j_yell "Casse–toi."

    am j_growl "Non, attends. Rends-moi mes affaires et tu t'en iras."
    am "Je ne veux plus que tu me voies. Je ne veux plus te voir..."
    am "S'il te plaît, pars..."

    "Ammon se retourne vers la moto."
    
    hl "Attends ! S'il te plaît !..."

    "Tu lui tends la main."
    "Tu ne peux pas lui rendre son [picked_from_the_bag]. Il te quitterait pour de bon si tu le faisais."

    hl "S'il te plaît, ne pars pas... Où irai-je si tu t'en vas !..."
    hl "Je t'en supplie Ammon, reste s'il te plaît... Je ne suis rien sans toi !..."
    hl "Que veux-tu que je fasse ?"

    "Ammon se fige sur place. Il ne dit pas un mot pendant un temps angoissant."

    am "... Qu’est–ce que je veux que tu fasses."

    "Il fait demi-tour."

    am j_growl "Rends-le moi."

    hl "... Quoi-"

    ### TODO : Ajoute une expression où il a les yeux exorbités.

    am j_yell "Rends-moi ce que tu m'as volé."

    hide ammon with dissolve
    "Tout à coup, Ammon charge."

    "Ammon attrape le [picked_from_the_bag] mais l'enjeu est trop important pour le laisser partir alors tu lui serres la main"
    "Tu luttes pour ta vie afin de récupérer le [picked_from_the_bag]. C'est ta dernière chance d'arranger les choses alors tu le griffes, tu le siffles et tu le mords même."
    "D'un autre côté, Ammon ne veut pas lâcher prise non plus. Il t'aboie dessus, secoue la tête dans tous les sens. Plus tu tires sur ce [picked_from_the_bag], plus il te glisse entre les doigts."
    
    hl "S'il te plaît Ammon !!! Fais-moi confiance !!!"
    hl "S'il te plaît, crois-moi ! S'il te plaît, que quelqu'un me croie pour une fois !"
    hl "J'en ai marre de me répéter !"
    hl "S'il te plaît, crois-moi !"

    "Tu tends ta main vers lui, vers son épaule. Il te comprendra peut-être si tu t'agrippes à lui."

    am "{size=60}CASSE–TOI{/size}"

    play sound "audio/sounds/punch.mp3"
    
    
    show expression "#F00" at alpha_dissolve:
        easeout 1.5 alpha 0.7
    show parkinglot with sshake

    "L'instant d'après, son poing se connecte à ton arcade et tu exploses dans les airs sur sa moto."
    "Le [picked_from_the_bag] repose sur le sol, son contenu répandu dans l'herbe, dernière relique de votre amitié éphémère, piétinée"
    "Tu te cognes violemment la tête sur le cadre de la moto. Du sang s'en écoule goutte à goutte. Tu passes ta tête sur ta blessure. Juste du sang."

    am "PUTAIN, désolé, je n'ai pas fait exprès ! Laisse-moi t'aider..."

    hl "{size=60}JE TE DÉTESTE{/size}"

    show parkinglot with sshake

    scene black with dissolve

    "Tu te jettes sur Ammon. Vous vous roulez tous les deux dans l'herbe." 
    "Après ça, c'est un peu flou. Tu ne te souviens pas de tout."


    
    stop music fadeout 0.5
    play music "audio/music/uboa.mp3" loop

    show parking with dissolve
    show expression "#F00" at alpha_dissolve:
        easeout 1.5 alpha 0.7

    "Tout ce dont tu te souviens, c'est d'Ammon allongé dans l'herbe, sans défense, son visage se contorsionnant de douleur. Il est à bout de souffle, implorant de l'air."
    "Toi, de ton côté, tu es assis sur lui, à califourchon."
    "Tu déglutis."
    if azzy_score >= 2 :
        az "Pourquoi ça maintenant..."
    "Malheureusement, plus ta vue monte dans son corps, plus elle souhaites rester en bas."
    "Son t–shirt ébouriffée et déchirée et sa veste noire sale n'étaient pas différentes, mais ce qui te dérangeait, c’étaient tes bras qui comprimaient sa poitrine."
    "Ça doit lui faire mal, alors tu devrais arrêter, mais tes bras continuent à appuyer et ses cris de douleur remplissent tes oreilles. Mais tu continues à appuyer, peu importe à quel point il gémit."
    "Plus troublant encore, Ammon frappe tes bras de toutes ses forces mais cela se révèle en vain, tes bras plantés là comme des statues, inamovibles, quoi qu'il puisse arriver."
    "Malgré sa détermination et sa férocité, les poings se sont progressivement affaiblis jusqu'à ce que le vent te frappe aussi fort que lui."
    "Les coups de genoux, auparavant, aussi perçants que des lances, dans ton dos, te font plus rien."
    "Alors tu comprends. Tes mains s'enroulent autour du cou épais de ton ami qui s'affaiblit."
    "Tu serres et tu écrases sa gorge molle en écrasant toute chance sa respiration le sauve. Sa pomme d'Adam qui se convulse sous ton pouce te donne une vague de nausée. Cependant..."
    pause 1.0
    "Tu te surprends à aimer toucher sa peau flasque et sa texture rugueuse. Tu regrettes de ne pas l'avoir fait plus tôt."
    "Le visage d'Ammon devient pâle alors que tu lui arraches ses derniers fils d'énergie. De la bave jaillit de sa bouche, ses dents serrant pour garder le reste d'air dans sa bouche."
    "Un autre fil de bave tombe sur Ammon. Tes yeux sont exorbités par la rage. Tu es devenu un animal sauvage."
    "Tout à coup, tu sens un contact affectueux sur ton bras. Le molosse mourant partage un regard avec toi alors que ses dernières étincelles de vie sortent de ses yeux tristes."
    "Près de la mort, il dit :"

    am "S'il te plaît, arrêtez."

    "Tu réussis à entendre des mots du son grave et rauque qui sort de sa gorge"
    
    am "Je te crois, je te crois, d'a–accord ? Tu es mon ami et je ne te quitte–erai pas, ok ?"
    am "Je ne pensais pas ce que je disais. J’étais juste énervé."
    am "Je sais que tu vis des moments difficiles, alors je ne te tiendrai pas compte de ce que tu me fais là, je te le promets."
    
    "Sa poigne faiblit, toutes les couleurs se vident de son visage. Sa gorge avant, se contractant et bougeant, devient de plus en plus inerte."
    
    am "Tu n'es pas mort. Tu as toujours été le même chat que j'ai rencontré il y a des années."
    
    "Il te sourit, des larmes coulent au coin de ses lèvres"
    am "Je ne veux jamais te quitter."
    "Il tousse et de la bave coule sur tes mains. Tu ne bouges pas."
    am "Alors... je sais que ce n'est pas toi alors arrête de faire ça, je t'en supplie"
    am "Retire tes mains... S'il te plaît."

    "Ses mains tombent. Il ne respire plus beaucoup."
    if ammon_score == 0:
        "Mais tu t'en moques. Tout ce que tu veux, c'est continuer à étrangler sa petite gorge toute molle. Cela fait naître en toi des plaisirs interdits."
        "Tu as adoré chaque rictus de douleur sur son visage. Tu baves encore plus et ces cordes se mélangent aux siennes."
        "Ton plaisir est indiscernable de sa douleur. Tu le détestes. Tu le détestes et tu espères qu'il souffre suffisamment." 
        "Il va regretter d'avoir pensé à te quitter"
        stop music
        cl "Je te l'avais bien dit."
        cl "Tu l'aimes."
        cl "Tu as adoré."
        cl "Tu n'es pas du tout un être vivant."
        cl "Tu es une bête. {w} Tu es un monstre."

        "Tu enlèves tes mains."
        hl "... Pourquoi."

        "Une vague de nausée te submerge."
        "Tu vomis."
        "Il ne parle plus. Est-ce qu'il respire encore ?"
        "Ton mal de tête t'assaille avec plus d'intensité. Tu t'agrippes à ta tête."
        "Tu t'effondres."
    else:
        "Puis tu te souviens. Toutes les fois où Ammon t'a remonté le moral. Toutes les fois où tu as pleuré d'épuisement et où il était là pour toi."
        "Toutes les fois où il a pris ton yaourt au déjeuner au collège et a joué avec toi pendant des minutes. Sur l'instant, tu détestais ça mais à la fin, tu riais."
        "La fois où tu te sens nauséeuse à cette soirée nulle et qu'il est venu te raccompagner alors qu'il t'avait dit de ne pas le faire."
        "Les fois où il ne se sentait pas bien alors tu l'as veillé pendant des jours et des nuits pour qu'il aille mieux."
        "Tu grimaces. Tu ne pouvais pas avoir un meilleur ami que lui. Il était le seul capable de te comprendre pleinement. Puis tu réalises."
        "Tu es en train de l'étrangler. Tes mains entourent son cou. Qu'est-ce que tu fais ? Ce que tu fais est mauvais, interdit. Tu commets un crime."
        "Tu enlèves tes mains de son cou et tu te lèves si vite que tu es frappé par le vertige."
        "Ammon laisse échapper un souffle fulgurant, l'air remplissant enfin ses poumons. Cependant il reste au sol, trop chétif de ton assaut."
        am "Merci Howl..."
        am "Je t'aime {w} beaucoup, tu le sais ça."
        if ammon_score == 3:
            am "Non. Je t’–"
        
        "Tu attends ses prochains mots mais rien ne vient."
        "Après un long moment agonisant, tu baisses les yeux."
        "Il ne bouge plus. Il ne parle plus."
        "... Est–ce qu’il respire ?"
        "En panique, tu te précipites sur son visage, et tu colles ton oreilles sur sa bouche, pour vérifier que tu puisses entendre rien que, mais alors rien qu’une respiration..."
        "..."
        "Il ne respire plus."
    
    

    jump first_act_part_1
    