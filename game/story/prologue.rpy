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
    cl "Je sais que ces deux feux follets avec lesquels tu m’épies, me scrutes ne sont qu’illusions.{w} Des leurres pour corrompre le peu qui reste de moi."
    cl "Je sais, cependant, que ton pouvoir, ta lumière, ton don..." 
    cl "Il peut les apprivoiser, les recueillir, ces monstres de l’au–delà{w}, au sein de ton phare au milieu de la mer déchaînée."
    cl "{cps=3}...{/cps}{w} Combler ce vide qui ronge cet être{w}——Mon être——{w}flétrissant."
    cl "C’est pour cela que,{w} jusqu’à présent,{w} et pour toujours..."
    cl "Je t’aime{w}, Charles"
    scene black
    stop sound
    pause 1.5
    # play sound 'audio/sounds/car_white_noise.ogg' loop
    jump little_road

label little_road:
    # show ruralRoad
    # with Fade(0.5, 4.0, 0.5)

    show ruralRoad
    with Fade(0.5, 4.0, 0.5)
    camera at zpos_camera

    "Tu te réveilles, au toucher glacial qui s’empare de ta nuque."

    hl "Ahhhh—"

    "???" "Je vois que je ne me trompais pas, au final."

    "Tu lèves les yeux et malgré le voile noire recouvrant ta vue, tu arrives toujours à distinguer les traits de la personne en face de toi."
    "Elle porte un casque et une veste de motard noirs. Impossible de voir son visage. Mais tu n’as pas vraiment besoin de le voir."
    "Tu sais qui elle est."
    "Elle reprend sa typique posture, croisant les bras, tapant du pied."
    show ammon at american_shot with dissolve
    
    "???" "En train de pioncer, n’est–ce pas ?"

    hl "Huh, de quoi ?"

    "Elle te laisse reprendre tes esprits à ton rythme."
    "Tu enlèves le casque, te compressant la tête. Ces fichues longues oreilles ne te facilitent pas la tâche."
    "Après avoir remué tes petites moustaches, et toute pilosité faciale qui te reste, tu retires tes lunettes de ton fin museau et tu te frottes les yeux."
    
    hl "Quelle heure il est ? Il est tard, non ?"

    "L’homme au casque pouffe."

    "Homme au casque" "Il est environ 18h, il est pas si tard."
    "Homme au casque" "Tu peux bien rester éveillé quelques heures de plus non ?"
    "Homme au casque" "Je voulais arriver à la Maison avant la tombée de la nuit mais c'est un peu tard pour ça"

    "Tu baisses les yeux et étonnamment, tu te trouves sur une moto, assis."
    "Sortant ton chiffon, tu essuies la buée qui obstrue les verres de tes lunettes." 
    "Tu aimes penser que tu n’as pas une si mauvaise vue mais tu ne peux qu’admettre que, sans elles, tu aurais dû mal à te concentrer, amplifiant la constante fatigue mentale sur tes épaules."
    "Une fois les lunettes posées sur ton visage, l’écriture en face de toi, auparavant trouble, devient clair, la mise en point moins laborieuse qu’avant."
    "Tu peux y lire la marque de la moto et tu ne retiens guère le nom, les automobiles ne faisant pas partie de tes intérêts."
    "Tu tournes ta tête pour observer les alentours. Des étendues de champs de tournesols. Une route déserte mal entretenue avec des crevasses à gauche et à droite."
    "Au loin, dans ton dos, tu aperçois des chaînes de montagnes survolant les horizons. Cela semble si loin de chez toi."
    

    hl "Ah oui c’est vrai..."

    "L’Homme au casque ricane."

    "Homme au casque" "T’es un peu long à la détente, tu le sais ça ?"

    hl "Arrête de dire ça, On me le dit bien trop souvent."

    "Homme au casque" "Comme tu veux mais si tu rêvassais moins souvent, je n'aurais sûrement pas te le dire aussi souvent." 
    "Tu ravales les remarques acerbes au fond de ta gorge et tu te contentes d’un claquement de langue."

    az "C’est vrai que t’es long à la détente, au fond."
    dk "Tu ne l’es pas ; tu considères toutes les options, plus que la moyenne, ce qui te prend plus de temps."

    "Homme au casque" "Par contre, je peux pas te laisser te rendormir."
    "Homme au casque" "Tu commençais à piquer du nez et je n’apprécie pas les gros objets lourds et froids qui me martèlent le dos pendant que je conduis."
    "Homme au casque" "Donc tu vas garder tes petites mirettes ouvertes le temps qu’on arrive à la Maison, compris ?"

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

            am "... Bref, faux ou pas, je peux pas faire grand-chose à ton problème."
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

    "Tu te retiens de lui hurler de garder ses commentaires pour lui."

    am "Bon tu veux savoir quoi sur \"La Maison\" ?"

    ## NOTE: Set up choices variables

    $ where_it_is = True
    $ why_there = False
    # $ work = False
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
            # $ work = True 

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

            "La brise du morne Automne reprend de plus belle. {w}Tu pondères la raison pour laquelle tu ne sais, au final, rien de la personne que tu appelais ton meilleur ami il y a des années."
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
            hl "Dis Ammon ?" 
 
            am "Oui ?" 
 
            hl "Tu es professeur d'Histoire à l'Université, non ?" 
 
            am "Pas exactement mais c'est l'idée, oui." 
 
            hl "Tu ne devrais pas être à l'université alors ?"

            "(pas fini d'écrire ce dialogue)"   

            jump destination_questions      
        "La vraie raison" if real_reason and not been_there and not why_there and not what_else: 
            $ real_reason = False 
            "Ammon, il n'y a pas une autre raison pour laquelle on y va ?"
            "(pas fini d'écrire ce dialogue)" 
            jump destination_questions 
         

        
    "Après toutes les questions, tu te sens épuisé."
    "La somnolence que tu avais contenu jusque-là, charge à pleine force à nouveau."
    "Bientôt tes paupières deviennent lourdes et la gravité jusque-là inoffensive t'arrache de la moto."
    "Ta tête se heurte au dos du grincheux chien."

    if ammon_score >= 1:
        am "Hé, fais attention !{w} Qu'est-ce qui te prend de frapper comme ça ?!"
        
        hl "Désolé... Je me suis laissé emporter par la fatigue."

        am "Tu es si fatigué que ça ?"

        "N'ayant plus d'énergie, tu hoches de la tête, savant pertinemment qu'il ne pourrait pas le voir."
        "Cependant il comprit——notamment grâce aux frottements du casque sur sa veste——et une pensée lui vient en tête."
        "Hésitant à le dire, il se décida subitement."

        am "Attrape-moi la queue."

        hl "... Hein ?"

        am "Attrape-moi la queue."

        "Même la deuxième fois, tu n'arrives pas à assimiler le sens de ce  qu'il vient de dire."

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

        # "Ça ne pose pas problème qu'on aille là-bas ?" if work:
        #     $ work = False

        #     hl "Ça ne pose pas problème ?"

        #     am "De quoi ?"

        #     "Tu n'as pas ton travail "
        #     jump destination_questions
        


label rest_area_1:
    # "Eventually, Ammon, who had stripped away his helmet since a long time ago, notices you."

    show ammon right at american_shot

    am "Do you want some help? You look like you're having a hard time."

    menu let_ammon_help_you:
        "Please, yes, can you help?":
            $ ammon_score += 1 
            "Usually, it would’ve been the time where you deflect any sort of assistance. But..."
            hl "Alright, go on."
            "You didn’t have the strength to struggle nor protest so you give in to Ammon."

            show ammon front

            "His bulky hands grab the base of your helmet and his nails brush the tip of your neck hair, surprising you, not liking being touched."
            "Your hair stands on edge, imploring to get it done the sooner you can. You don’t disagree. The sooner the helmet removed, the better you’ll be"
            "Nonetheless, he gets trouble too to rid your feline head of the helmet. He pulls harder and harder on you and the pain gradually increases and you can't see the end of it."
            hl "Oh my god, Ammon, be softer!! Less harder! You're going to hurt me!"
            
            am "If you weren't so such tight!"
            
            hl "What did you say?!"

            am "I said, if you didn't have a such tight helmet... And such a big head!"
            
            hl "You can talk with your long big snout!"
            
            am "If you don't stop talking right now, I'll pull your helmet in any way possible,"
            show ammon right e_smug
            extend " with or without your head."
            
            hl "Stop talking with your long snout and just do what you just said, we'll both be better off!"
            
            "For a moment Ammon still struggles to remove your helmet. The pain is really insufferable and you both pull like idiots trying to pull out Excalibur." 
            "You yell and he apologises hoarsely."
            "At some point, you feel with your united combined effort, the helmet is ready to give in. Suddenly there's a pop and you fly out of the helmet on the grass rolling for a considerate amount of time."
            "When your frenetic charge comes to stop, you cough out the dirt and the blades of grasses stuck in your mouth."
            show ammon front e_happy j_noway
            "You shake up your head so your blood flows back in it. When you come back to your senses, you are met with a laughing dog unable to stop."
            "His piercing laughter overwhelm your space and you get red of embarrassment irresistibly, despite you. You clutch the grass."

            menu:
                "Throw some grass at him.":
                    $ ammon_score += 1 
                    "You pluck out some grass and you throw some at him to make him shut its long snout trap that serves him as a mouth."
                    hl "Fucking moron !! I told you you shouldn't pull that hard! I'm all scratched and dirty now. I hate you, you hear me??"

                    show ammon j_neutral
                    "Ammon wipes out his tears of laughter and approaches, triumphing, over you. His wicked smile pierces his helmet as he hands you your helmet and reach a hand to you."
        
                    am e_neutral  "Okay you cry kitten, keep whining all you want. But if you stay on the ground, you won't get anywhere, will you?"

                    "You grit your teeth as you clutch his hand. He carries you off the ground that you find yourself levitating. You often forget his undogly force."
                
                "Stay calm": 
                    "You clutch the grass harder and harder. You want to unleash your rage on him, to throw grass and dirt at him."
                    "But you can't. You're too weak for that. He'd only laugh at you harder. {w}You hate him."

                    show ammon j_neutral
                    "Ammon wipes out his tears of laughter and approaches, triumphing, over you. His wicked smile pierces his helmet as he looks at you."

                    am e_noway "Hum, are you alright? Were you hurt? You look tense."

                    show ammon e_neutral
                    "He rushes towards you."
                    "Once close to you, he reaches a hand out at you."

                    "But you swat it off."

                    show ammon e_noway j_disgusted
                    hl "I am fine, you don’t need to worry over me."

                    "You stand up and you quickly brush your clothes of the dust and the green blades."

        
        "I can do it on my own, no thanks":
            "You don't need the help of that prick."
            hl "I don't need your help. I can deal with it on my own."
            
            am pupils_right "Alright... Suit yourself."
            
            "You don't wait for his signal."
            "However something's wrong: It really is stuck. No matter how much you pull or the angle you use, your ears won't budge so it won't come off."
            "As you panic, you wiggle out in every directions possible, almost rushing in the motorcycle or Ammon."

            am pupils "Are you sure you don't need any help? you sure look like so."

            hl "I'm fine! I don't need your help or anyone's help!"
            
            am pupils_left "Um, ok... I guess?"

            show ammon pupils 

            "In your wrestle against the helmet, you keep spinning around until you get nauseated from the all over experience."
            "By a thread of luck or misfortune, you manage to get rid of your helmet. However with all your dances and twirling, you lost sense of directions and you lose balance making you fall into the grass."
            "When your frenetic charge comes to stop, you cough out the dirt and the blades of grasses caught in your mouth. As you come back to your senses, you are met with a laughing dog unable to stop."
        
            am pupils_left j_smug "Deserved it, jackass."

            hl "What did you say?"

            am pupils j_neutral "You heard me. Just get up. You won't get anywhere like this."
            
            "You get up. You rub your head out of pain and you can feel a nasty bump on your head. Maybe you should've asked for Ammon."

    hide ammon with dissolve

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
    "The capillaries running through your blue sapphire eyes sclera pulse a like a living entity."
    
    "You are annoyed at them and even more you are scared of them."
    "The next moment, they disappear and you are then alone with your no better thoughts, still uncomfortable that someone might be watching you." 
    cl "Just a wrong step and you're done for. Don't ever misstep, you hear me? Not ever. {w}You are a deviant and you know it."

    am "Hum Gap, what are you looking at? You've been staring for quite some time now."

    show ammon at american_shot
    with dissolve

    "Ammon tilts his head from the other side of the motorcycle to look at your reflection in the mirror"

    am "You've got to stop looking at yourself like that. You look like you are on the brink of murdering someone."

    "With this disturbing statement, Ammon goes on to get rid of his helmet." 
    "Realising he has got some points, you cut off your sight from your other you and you look at him inquisitively, wondering where he might have had this idea."
    "You weren't that unhinged, were you?"
    
    hl "Do you need help with your helmet, Ammon? You may use some given.. your head shape..."
    
    am right "It's alright, pal. I can deal with it on my own. I'm used to."

    "The cocky dog removes his helmet elegantly without any issues nor events whatsoever." 
    "He wiggles his head finally free from his protective plastic jail."

    show ammon pupils_right 
    "What a show–off. But a good show–off."
    camera at close_shot
    show parkingLot:
        parallel:
            easeout 1 blur 64
    "The thing that always catches your attention in him is his eyes. His priceless golden eyes shining more than any sun you've seen." 
    "You find yourself mesmerising in these luxurious jewels."
    show ammon pupils 
    "These piercing cruel eyes look through your soul"
    show ammon pupils_right 
    extend "and you are read like a dirty open book." 
    "At any time, if he feels like so, he can pick an excerpt from it and study it attentively to your expense" 
    dk "He can guess who you are from it alone."
    "He is objectively better than you in every domain possible."
    camera:
        easeout 15 ypos 400
    "He is handsome, he is charming, he is charismatic, he has a sense a sense of style you will never have." 
    "He also wears golden face piercing. It really amplifies his rebel attitude."
    "You may want to say that to him but he’d say that you’re being too emotional so you always shut yourself."
    "He often wears biker suits because that fits his life style he told you." 
    "You wish you could be as extravagant as him and take crazy risks" 
    "You are not as bold as him so you keep to your little classic shirt with your tie."
    "You hope, one day, you’ll break the ties that roots you to your plain life and take the chance to be as free, as lifeful as liberated as him."

    am "What are you staring at?"

    pause 0.5

    camera:
        easein .5 ypos -200
    
    show ammon pupils e_smug

    am "Do I have something funny down there?"

    hl "Huh not at all ahah"

    "You cringe, rubbing your neck with your hand."

    hl "I just really like your cloches ahah."

    am "{cps=3}...{/cps} ok, thanks, I guess?"
    am pupils_right "{size=20} you weirdo"
    
    camera:
        parallel:
            ease 2 zpos 0
        parallel:
            ease 2 ypos 0

    pause 1.0

    hide ammon with dissolve
    "Despite your fixation on Ammon, you come to notice the deserted rest area you just stop in." 
    "Dead leaves piled up on the border of the roads, signaling the fall has come and taken his toll on Nature." 
    "The brownish orangey landscape contrasted with the bright green of Summer." 
    "The mourning trees stand there, waiting for better times"
    "Sooner or later, even their melancholic colours will be replaced by scarce branches and the glacial white tucking them to their warm sleep." 
    "Tall grasses remain nonetheless undefeated by the time passing. Some sunflowers still resist, searching for their lead."
    "The usual restrooms stick out of the surrounding nature. They are not at all well–maintained..."
    "A tall metallic structure stand out with all this misery, a shine, a beacon of what lies ahead. You have seen them a handful of times. A phone booth." 
    "You rarely see phone booths out in city so to find one in a rest area is even more incredible. Technology goes fast, you think, nowadays."

    hl "Hey look, Ammon! They have a phone booth around here. Isn’t that wonderful?"

    show ammon right pupils_right e_smug at american_shot with dissolve

    am "Huh?"
    show ammon pupils 
    extend "Oh yeah... sure."

    "Ammon doesn’t seem very interested in these incredible structure. You lower your gaze and notice his hand pressing his crotch, clutching his fist at a gradually faster pace." 
    "This explains his lack of interest, you guess."

    am "So you’re going to use it, right? Who you gonna call?"

    "You mull over the question, even though you don’t know a lot of people who owns a phone at home. Only two persons comes to mind."

    am j_noway "Is it gonna be you mom?.. Or..." 
    show ammon pupils_left
    extend " MJ?"

    show ammon pupils j_neutral

    "He says the last word with a lot of emphasis as it was only obvious from both of them you’re going to pick." 
    "A annoyed tone comes with and that disturbs you, as Ammon being genuinely annoyed is rare."

    hl "Yes I’m going to call her."

    am "Ok, suit yourself."
    am "I’m going to pee. Wait for me and don’t go far ok?"

    "Ammon quickly deflects the topic of discussion and comes back to the pressing matter at hand." 
    "You watch him waddling in place, jumping like a late hare and you find yourself hard to not comply with his request."

    hl "Ok, don’t lose yourself on the way!"

    am "Don’t worry. See ya."

    hide ammon with dissolve

    "As soon as he finishes his sentence, you see him sprint towards the forsaken restroom and you chuckle." 
    "As he disappears from your vision, you are now alone... Not quite... There's the phone booth. It attracts, implore you to come."
    "So you stare at it longingly. For a moment, you can only stand there, in front of the cubicle, as your eyes runs through it, intrigued."


    
    jump phone_booth

label phone_booth: 
    stop music fadeout 0.5
    stop sound
    scene phone_booth with fade

    play music "audio/music/night_sky.mp3" fadein 1.0 loop

    "You jog towards the deserted phone booth. You hurry yourself to talk to her, to get it done." 
    "Dragging yourself the door, you grab with a grand difficulty the handle, not being able to find the motivation to penetrate into the dark cubicle."
    "You turn an inconsiderate amount of times the handle, at last, the door opens when you shove into it." 
    "You mustn’t be in the right mindset to not notice that pulling a thousand times a door will not work on the 1001th time."
    "But you couldn’t give more than a care, your gloominess crashing down at its lowest as you finally set paw in the somber void, pierced by rays of declining sunlight."
    "Blind, by the low current luminosity of the place, you put some time to even find the phone."
    "On the phone box, on a little sign at the bottom of it, it is written \"10 francs for 10 minutes!\" You think the sign bargains a fair deal to you."
    "You get a coin from your pocket and you slid it into the coin slot. Soon after, the phone screen lits up awaiting your input." 
    "You observe carefully as some features disturb you: they never had a screen before."
    "With slowness, you press the phone number on the keypad, with petite–size buttons but you manage to input it on your first try."
    "You pick up the phone and wait for the ringing to come and let it resonate in the booth soothing the emptiness of the place. You liked the music tone and you daydream a bit of time."
    "You’ve wandered in your head for a undefined span of time, the ringing going on and on, the sound receding away in the dark void."
    "You wonder why she puts this much amount of time to respond. Must it be the hour? Or is she’s not home right now? Maybe she has got an extended work shift and wasn’t still able to come this evening."
    "Whatever the reason, it has to be a valid one. You mull over it a bit. She wouldn’t ignore you, would she? Perhaps she is ignoring you and is looking at the phone ringing right now."
    "Suddenly a click travels from the other side of the line as to prove you wrong. You hear an inquisitive, quite sly, feminine voice answering the call."
    
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
    
    "For an enigmatic reason, your passion for latest high-tech overhauled your usual gloominess." 
    "You find yourself very eager to indulge yourself in this pit of wonders, dreaming for the future of all living beings."

    hl "Imagine for a second, how the americans reached the moon, {cps=120.0}how we will in the future be able to travel to space {cps=150.0}and also how we will be able to even eat without opening the mouth."
    hl "{cps=200}don’tyouthinkit’sfantasticsometimesyouthinkwowtechnolgyandallh\nowrapiditwillreachveryhighstandads??it’sreallywonderfulwhenyouthinkaboutitIwanttoneverdietowitnessthis{nw}"

    "You couldn’t hold your excitation anymore. The words leaving from your mouth were forming before your brain could even process the information you were spilling out at her. Your speaking functions were not functioning anymore."

    mj "Howl, Calm down! Calm down, for god's sake. You’re going to choke on your own words. Take a breath ok? Breathe with me, alright? At the count of three you’ll breathe out, ok?"

    "You follow Marie—Jil’s instructions and soon enough, you manage to calm yourself down and in the end you are able to talk at steady pace."
    "Once calmed down, your lungs stops contorting and burning the air within is able to bring you tranquility to you. Her voice helps you catch back and stand on your two paws."
    "You’re finally able to talk normally now."

    hl "Ahah, sorry, MJ. It’s been so long that I haven’t talked to you! It’s been like what? a week?"

    mj "You’ve talked to me this morning, Honey. But I don’t mind, I love it when you get all worked up over me, little kitten."
    mj "I didn’t think that you’ll be missing me so much. You’ll only stay 3 day over there and you’re already panting your insides out"
    mj "You didn't even reach the hotel."
    mj "You’re lucky that I was the one answering the phone." 
    mj "Had it been Dad or Mom, they would have teased the heck out of you. Don’t thank me huh? I almost didn’t answer given the hour."

    hl "It’s not that late..."

    mj "It’s like fifty to eight, at least it’s starting to get late, don’t you think? I don’t think I’ll answer later in the evening. Or my parents will. I don’t think you want to talk to them that late, huh?"

    "She’s got a point. As much as you like her parents, the situation you would find yourself, head–to–head with them, not knowing what to say would be very akward."
    "So you agree with her, not very much a lot you can do more to talk to her later."

    hl "Yeah you are right..."
    hl "Hey, you should’ve come too, to the trip with us! I really miss you!"

    mj "Me? You’re doing great without me, don’t worry. And I wanted to come but you know I can’t, I’ve got to work tomorrow. Have to help out Mom with her restaurant."
    
    hl "You could’ve explained the situation to her. I’m sure she would have let you come."

    mj "It’s not like that, Howl. She just opened her restaurant. I can’t let her down like that. She really needs me, I don’t have the time to travel to a luxuous hotel unfortunately."

    hl "Alright... but next time, you gotta come!"

    "She softly chuckles at your liveliness."

    mj "You know, your attitude earlier reminded me of the time where we first–{nw}"

    az "There she goes. On her rant like always."
    
    dk "Well it'd be rude to interrupt her don't you think?"

    az "Then don't"
    az "Think of something else."

    menu:
        "Listen to her":
            $ derek_score += 1
            "You decide that you should at least listen a tad before declaring it boring."
            mj "-we first went to the beach?"

            hl "Yes... I think so..."

            mj "Well Ammon always liked acting like a goofball to tease you; and I must agree with him that your reactions were worth it."
            mj "This day, Ammon decided that he was going to dance on rocks and provoke you to come and get him..."
            mj "That was at least what it looked from afar."
            mj "Anyway I think at some point it worked and you charged him. He got so scared that he fell of the rock and sprained his ankle. I don’t think the pebbles helped."
            mj "Fortunately your dad that drove us to the beach was around because he was able to provide first medical care before getting to a doctor."
            mj "Well it kind of ruined our little outing but thinking back then, Ammon and you were always at each others’ throats but you went everything though thick and thin."
            mj "It’s fascinating how you managed to stay together."

            az "His misbehaviours only made him more interesting."
            az "Why ditch him."

            dk "He has a way to get on your nerves."

            mj "Oh by the way, do you remember when we first got together?"

        "Think of something else":
            $ azzy_score += 1
            "You let your mind wander elsewhere. You’ve already been there. Listening to her unending rants. You never were able to focus more than a minute."
            "So this time, you give up instantly, too tired to fight against your boredom."
            "That didn’t mean you didn’t appreciate her."
            "You liked her, she’s a wonderful girl" 
            "You are childhood friends and you were stuck together like hand in glove and never you has been separated from her." 
            "She lived in your birth village, so you used to play together every day."
            "For some reason, she could stand your presence, contrary to most of your peers of your age. That made her a precious friend." 
            "She was always fond of your fantasies and your games, you had a lot of them when you were young."
            "You would read a book about a boy in a green tunic going for adventures and you would pretend that you are this same boy reenacting the events of the book." 
            "Most kids would take you for a social case and most have."
            "But not Marie–Jil. Marie–Jil played with you in your little pretend games." 

            mj "So um Howl, Howl, are you listening?"

            "You wake up from your daydreaming, all of these memories have had left you groggy"

            hl "Yeah, MJ, you were saying?"

            mj "... I was saying, do you remember when we first got together? Your enthusiasm didn't die down since. It's warming to the heart to witness it."
    
    show canteen at zpos_bg with dissolve
    show canteen:
        ease 1 blur 16
    "When you first got together, huh? Yes you do remember, how could you not? It was a very special day after all."
    "You weren't expecting it. One day, you were eating at the cafeteria of your high school." 
    "The usual crowd of the cafeteria flew away for an event you surely were not interested in so there were not a lot of people left here."
    "You tapped weakly at the food in front of you, not really hungry." 
    "The unusual quietness, although, helped you focus and take some bites into your plate, but no matter how much you tried, your plate remained, for the most part, untouched."
    "At your left, Ammon was laying on his chair, his tummy hurting him. He defied you earlier to an eating contest." 
    "You had accepted meekly, by principle, you’d never refuse any challenge thrown at you by your favorite troublemaker."
    "But you didn’t have the heart—nor the stomach—to follow him up on the challenge." 
    "You had been surprised at his dedication, this day you had been fed hachis parmentier and you both had taken double rations so it weighed a lot on his stomach."
    "He was so full, his shirt couldn't hold his belly any more, so you could admire his belly button and the lump the food had formed in his insides." 
    "Trying to cheer him up, you rubbed his abdomen and you were met with a pleasant slushiness."
    "You couldn’t stop so you kept on rubbing, hoping to appease him. To your disbelief, Ammon didn’t mind and he even let out some squeak of laughter and satisfaction."

    hl "Heheh, what do you think it’s gonna be?"

    "Confusion roses on Ammon’s face, still contorted by pain mixed with softness."

    am "I–I thiiiink it’s go– gonna be what?"

    "I look at his tummy."

    hl "A boy or a girl?"

    am "A–A gir– *Buuuurrurp* oh shut u–up man."

    "Ammon continued to burp uncontrollably so you remove your hand off of him, disgusted." 
    "You were less eager than before to finish your food so you mulled on the table, leaned on it, disturbed."
    "It started to worry you: Marie–Jil still had not come to the cafeteria, today. You three always ate together for lunch so you wondered where she could be." 
    "Usually, she was never late, so her absence left you concerned about her whereabouts."
    "Perhaps, she went to the match happening during lunch but she wasn’t really into the high school sports and she would have told you, if she were." 
    "Then her class might take longer than expected. But again, you didn’t think that was it."

    hl "I wonder where she is..."
    "Said out loud, you were expecting that Ammon was going to answer you, or at least say something, but no response as Ammon laid now seemingly unconscious on his chair."
    "All of the sudden, Marie–Jil approached you, bringing in no food but an tense air on her way. As she got closer to you, you started shivering from stress."
    "Marie–Jil stood shut fast on the floor, very anxious, not knowing where to place herself. Her tail couldn’t stop shaking; the nervosity of the situation got you making your tail moving out of your own."
    ## TODO: add Marie–Jil sprite?
    mj "Hi Howl..."

    hl "Hi MJ... Why are you late, what’s going on? Do you want to tell me something?"

    "Marie–Jil raised her head, shocked, like she had been unmasked, as the end grew nearer with every second passing."

    mj "Huh, what do you mean?"

    hl "You’re all nervous. I never saw you like that. Did you break my stuff?"

    mj "No I did not!! {w}Oh hi Ammon..."
    mj "Ammon could you leave Howl and I alo–"

    "She finally noticed Ammon and his thick tummy. Hopeless at the scenery she was beholding, she ignored him and returned her attention to you."

    mj "Please let me finish, Howl."

    "Sensing the seriousness of the situation, you put down your tableware and looked at her in the eyes. You estimated that she needed your full attention"
    "The disheartened deer clasped her hands together, breathing in, trying to gather all the courage needed for the tremendous act she was about to do." 
    "She lingers here for a time whether she had made the right choice." 
    "Not able to help her at this moment, you let her be. She had a lot on her mind and you see strands of doubt, confusion and determination twitching at the corner of her long snout."
    "She rubs her eyelids one last time and Resolve rosed in her eyes, determined to get done with it."
    
    mj "You know, how we have been friend for a very long time, now, Howl?"

    hl "Yes I do?"

    mj "Well I am really happy with our friendship right now, how you always have been there for me."

    hl "And you always have been there for me! No need to sweat it o–"

    mj "Just a second please...{w} What I meant to say is that you are a wonderful person and I enjoy every moment I spent with you."

    "Ammon slowly raised from the dead, lending an interested ear to where the discussion was leading. In your heart, you knew where it was going and he knew too. You gaze at Marie–Jil."

    mj "But lately, I have felt a change inside me. I want to spend more time with you, I want to be closer to you. Closer than our current bond."
    mj "Those last years, I’ve come to want for a change in our relationship, something Friendship can’t offer. Those last months, I’ve been pondering the question."
    mj "Is it really right? Do I need a closer relationship than what we have right now. Then I realised."

    "While she pronounced all of that, she teared her dress down nervously, helping her to stay calm. But her composure broke once her eyes met yours."
    "Her face began to turn pinkish so she turned around, breaking the eye contact with you, making you unable to observe her facial features anymore." 
    "Your piercing gaze caused her to get embarrassed and she turned to prevent your gaze to reach her."
    "Ammon at this point, was fully alert, listening on her every words, every sounds leaving her mouth, every finger movement, every anxious tics."
    "You must have had put too much pressure on her because she yelled the next sentence."

    mj "Stop staring at me!! You’re making me anxious. Fine! What I mean is..."
    mj "I can’t go like this any longer. I need to know. I’m sure that, if I don’t have the response I want, we will be able to go back at how things were."
    mj "So... I wanted to know, if those feelings are reciprocal and if you want to explore and figure out those feelings with me then I’d be really happy... What I really mean is:–"

    "She clenched her dress hard, not wanting to let go her only last support. Ammon and you were both suspended at her lips waiting for her next words."

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

    show canteen at zpos_bg with dissolve

    "Howl + Marie–Jil" "Of course, I’ll be your boyfriend! Why did we not do that sooner!"

    am "I think I’m going to vomit..."

    "Ammon abruptly stood up and rushed to the toilets."

    # scene phone_booth with dissolve
    hide canteen with dissolve

    hl "I had to check up on him that day too... He shouldn’t have eaten that much."

    mj "Actually Howly... I am the one who went check up on him, I made you stay at the table to keep watch of our stuff."

    "A sense of discomfort and awkwardness emanates from Marie—Jil’s words like opening matriochka dolls. She had to witness him bathing in his vomit after all. You wouldn’t want to be the one that had go that day."
    
    mj "By the way, while we are talking about him, is everything alright with Ammon?"

    hl "What do you mean by that?"

    mj "I know he can be exhausting, sometimes. You didn’t do anything reckless with him, did you?"
    
    "A concerned voice comes out out of the receiver. You always become bold with the jackass dog around."

    hl "No, nothing of the sort, thankfully."

    "Silence fills the air. Marie–Jil returns you an doubting laugh, with multiple layers of sarcasm, suspicion and reservation. She was, with a lack of better words, able to see right through you."

    mj "Sure Howl."
    mj "Anything worthy telling me about him?"
    
    menu:
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

    mj "I–I wanted to talk about your behavior lately."

    "Unsettled, she struggles to find words on her thoughts. Her overall attitude disturbs you."
    "She grows impatient. You let her explain herself."

    mj "Are you alright?"

    hl "What do you mean? You’re making me confused."

    mj "With you trip, were you able to think back, clear your thoughts, to reflect on what happened recently."

    "She sounds concerned. Irritated. Have you been that out of it lately?" 
    "At most, you felt a bit tired from the pressure but that’s all."
    "She waits for your answer, expecting a thorough justification. You don’t have one. You’re utterly confused." 
    "You scratch the back of your head, hoping something will come out, but nothing. Only oblivion and the dark void."

    hl "I genuinely don’t know what you’re talking about. I don’t recall anything noteworthy that happened earlier. Everything’s fine, alr–"

    stop music
    play music "audio/music/anger.mp3" 

    mj "Oh my god, for Jesus Christ." 
    mj "Are you for real, Howl??? You’ve been pretending for a month everything’s fine and you expect me to believe you!??"
    
    hl "Huh..."

    show phone_booth:
        ease 1 blur 32
        ease 1 blur 16
        repeat
    "Confusion roses into you."
    "A burst of voice surges through the phone and you almost drop it." 
    "You panic. What happened, for Jesus’ sake? You dig through you mind."
    "You’re in the void, your head absent, beholding a black box. You try to open it. You can’t. You’re afraid. You shouldn’t go deeper"
    "You hands are wet. Every second, you are to the point of letting it slip." 
    "You sweat profusely. Your throat tightens."
    "You fall silent."

    mj "Hurle! please answer to me!" 
    mj "Your mom is dead sick worried for you!"
    mj "So please, help me, Hurle... Please Howl, will you let me help you? Will you tell me what happened last month"
    
    hl "Last... Month?"
    
    "You asked confused. Everything she says, You can't hear it. More accurately, you can hear her perfectly but you refuse to hear it. The black box should never be opened and every attempt sends a throb trough your brain." 
    "You head hurts. You seethe. Please stop. Please stop, you can't take it anymore."
    
    menu:
        "Make her stop":
            hl "Please.... stop."
            mj " ... I won't stop. I {w=1.0}am {w}fed up. I won't stop until I'm finished." 
        
        "Try to change the subject":
            hl "Can’t... we talk about something else?"
            mj "no we won’t. I am fed up. You let me finish."

    
    mj "You will answer to my questions, Hurle and you won't be able to escape forever."
    mj "We never asked any questions, we didn't want to put pressure on you. We let you breathe, rest, mourn, or even hell, agonize." 
    mj "But I’m sick of it."
    mj "But one day or sooner, you'll have to tell us what happened and I'm sick of not knowing the truth."
    mj "So tell me Hurle. What happened, last month, the day you went missing in the forest?"
    mj "We were waiting for you that day."
    
    "You panic even more. Went missing, it hits a bell. You realise. The box tightens even more. What happened that day must remain secret at all cost." 
    "She mustn't go further in her crusade of questioning. You ought to make her shut or you don't know what may become of you."
    "She represents a menace to your tranquility. Your Apathy."
    
    hl "I told you and told you, I don't know! How many times do I have to tell you?!! I don't know, I don't know and I still don't know! How that goes for you!"
    
    mj "I am sick of you with your \"I don't know\" \"I don't know\"! You lie to me as you breathe! You know and I will get the truth about that day."

    "The deluge of your body flows down on your sweaty palms. Your shaky hands tremble like a sinner to Judgment day."
    "The phone slips out out of your hands and falls down; thus, its thud echoes heavily in the booth. You pick it up hastily and shove it into your ear by fear to annoy the Bringer of your Retributions." 
    "You are scared of it, you are scared of your Judgment, you are scared of the Truth."
    
    mj "Don't you dare to try and slip away. If not today, I'll make you spill out on way or another, just wait for it. That could be today, but that could be tomorrow or after tomorrow or a week or a year, just wait for me."
    mj "I mean, for fuck’s sake, you were gone missing for a week?? A whole week and you weren’t even hurt."
    mj "It never happens! Do you understand that??? We all thought you were fucking dead."
    mj "Ammon couldn’t sleep a night, your mom cried all day non–stop, and I searched everywhere for you in this god damn forest."
    mj "I just couldn’t stop.{w} Just the thought of you, maybe alive, in the dark, alone, in the woods was driving me mad."
    mj "But no matter how much we searched, we never found you. The whole village searched for you!"
    mj "I could almost believe you didn’t exist anymore..."
    mj "Then out of nowhere, you reappear like nothing happened??"
    mj "Not 
    injured, with no consequences, whatsoever! It’s like you never disappeared??"
    mj "Do you know how much it’s fucking strange??"
    mj "You had nothing on you, do you expect me that you didn’t drink or eat for a whole fucking week??"
    mj "How did you survive??"
    "You didn’t need to drink."
    "Nor eat.{w} For that matter..."

    mj "You know that day, you weren’t the only one gone missing. Well I’m sure you are aware of it, after all."
    mj "Not everyone was lucky..."
    pause 1.0
    mj "So please, tell me what happened. We still can find him. Perhaps we can still save him!"

    hl "I don’t know..."

    mj "I’m sure you wouldn’t know. You’re glad that he’s not there anymore, aren’t you? Well I am not."

    mj "So please answer me..."

    hl "I don’t know... I don’t know, I swear... I can’t remember."

    mj "Ok let me rephrase it more clearly so you can remember..."

    "Please. She shouldn’t. Why is she always like that."
    "Everyone would fare much better if she just minded her own business..."
    "Some things are best left forgotten."

    hl "Please... Don’t do that."
    
    mj "What were you doing September the 13th?{w} Were you with him,"
    stop music
    extend "with ×××××××××××××××××××××××{nw}"

    "It hits you like a truck. This date. You didn’t want to hear it."

    dk "This is starting to get out of hands...{w} Like always."

    az "The box is getting loose."
    
    menu:
        "Let loose.":
            jump you_dont_understand
        "Keep it contained at all costs":
            jump you_dont_understand
    
    label you_dont_understand:
            az "I don’t think you understand."
            
            dk "You’re not the one who decides around here"
    
    "You look down. You’re holding the box. You let it slip. The box opens."
    "You are beholding the hill. He was expecting you. You brought someone. He is pleased."
    "You’re pleased too. You’ve done what He asked."
    "He brushes your cheek. A surge of adrenaline rushes through you. You want His hand forever, that It never leaves your skin."
    "You want His embrace more than anything. You’re willing to do anything for It. He knows how to fill your sick heart. Your deviant heart."
    "You know that you’re already a forsaken case so you let Him corrupt you even further. What were good in you to begin with anyway."
    "You present Him your partner. He gladly accepts the offering."
    "You take a step back to admire fully the demonstration he’s going to put for you."
    "He wraps his hands around his neck. {w} You like it.{nw}"

    hl "No."

    "You liked it."
    
    hl "No..."

    "You liked it."

    hl "No................."

    "You liked it."
    
    hl "No......................................"

    "You liked it."

    hl "NO I DIDN’T."
    hl "I DIDN’T LIKE IT."

    "Yes you did"

    mj "Wait, Howl, what’s going on?? What are you on about???"

    hl "I DIDN’T LIKE IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIT."

    "..." 
    cl "You loved it."

    play music "audio/music/uboa.mp3"

    show phone_booth at shaking
    
    hl "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH"
    show phone_booth:
        xoffset 0
        yoffset 0

    hl "SHUT UP I’M NOT A MONSTER"

    show phone_booth:
        easein 0.5 blur 96
        easein 0.5 blur 128
        repeat

    mj "What’s going on, Hurle, I don’t understand."
    mj "You are rambling like a mad man!!"
    mj "Are you insane??"

    hl "I’m not a monster, I am not a monster I am not a monster."
    hl "i’m just going to breathe in and out and everything’s going to be fine"
    hl "friendly fleas and fireflies friendly fleas and fireflies"
    hl "friendly fleas and fireflies friendly fireflies and fleas"
    hl "friendly fireflies and fleas friendly fireflies and fleasfriendly fireflies and fleas fireflies fleas and friendly"
    hl "friendly fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas fleas"


    mj "What are you even saying???"
    mj "Just listen to me{nw}"

    hl "{size=60}SHUT THE FUCK UP{/size}"
    stop music

    pause 2.0

    play sound "audio/sounds/glass_breaking.ogg"
    ### TODO: Drunk effect
    show phone_booth:
        ease 2 blur 128
    with sshake
    
    play sfx "audio/sounds/ear_ringing.ogg" fadein 0.5 volume 0.3
    
    show expression "#F00":
        alpha 0.0
        zoom 2.535
        align (0.5, 0.5)
        ease 2 alpha 0.5
    pause 2.0
    
    "A loud crash echoes and resonates within the phone booth." 
    "Slumped down, you don’t move anymore." 
    "Your head’s empty but a shrill and piercing white noise in your ears. You’re clawed to the ground and won’t get up anymore."
    show phone_booth:
        ease 1 blur 32
    "When your bloodied vision sets back into focus, you observe with a dead eye the destroyed–to—thousand—pieces receiver on the ground, you come to wonder what has guided you to this point." 
    "You rise your hands at eye–level sight to watch the blood spill out of your hands." 
    "What happened that has come to you to bloody them. {w}What happened September Friday the 13th."



    jump rest_area_2

label rest_area_2:
    stop music
    stop sfx fadeout 10.0

    scene parkingLot:
        zoom 1.25
    with Fade(0.5, 6.0, 0.5)

    "You lay down onto the frame of the bike. You can’t stand. Dragging yourself here from the booth was already hard enough as it is."
    "The tiredness and your recent agitated behaviour set you into a second state — there but quite not there."
    "You rub your eyes. If you were feeling sleepy, you don’t anymore. You’re just nauseated and want to get home as soon as possible."
    "But you won’t. So you just comatose around. Waiting for Ammon."
    
    am "Huh you alright Howl?"

    show ammon at american_shot with dissolve

    "You feel a hand on your shoulder. You’re about to raise your head"
    camera at close_shot
    extend " but a the dog crouches to eye–level."
    "Having his face close to yours sets you uncomfortable but you gulp and stare him back."

    am "You don’t look fine. Were you able to sleep? Well surely not."
    am "I’m sorry I took so much time. I had some matters to take care of. I didn’t think it would take that long."
    am "Maybe we need to take a longer break. Just go take a nap, ok?"

    "You swat his hand away."

    hl "I’m fine, I’m fine, just let me breathe."

    am e_noway "... What happened" 
    
    hl "Nothing."
    
    # angry
    am right e_angry "Your hands are full of blood."

    show ammon e_neutral pupils_right
    
    "He looks at the phone booth."

    am "Did you smash the glass???"

    hl "No... I did not."

    am e_smug pupils "Say it with less enthusiasm next time.{w} I almost didn’t believe you."
    am j_noway "Seriously. What the hell???"

    hl "Right. Anyway I am fine."

    show ammon front e_neutral j_disgusted
    "Ammon’s mouth twists. He gives you his usual stare."

    am j_noway "No you’re not."
    am j_disgusted "Trust me, you look like shit. You should at least rest."

    "Ammon’s sudden attention for you gets on your nerves. He has been cold to you all ride long. Why care about you now."

    hl "Ammon I swear I am fine."

    "You stand up. Proving a point to Ammon, you forgot your weak state and latent nausea, the world spins gradually around you."

    ### TODO: Drunk

    "The dusk sky, who was empty until now, fills with stars all of colours, it reminds you of the strange colour artifacts that you can find on low–quality photographs."
    "A sudden headache takes hold of your head like a vice tightening it."
    show ammon e_noway j_disgusted
    "Your stomach churns. Your legs tremble and can’t support your weight any longer. They give out."

    am j_noway "Howl!"

    "He catches you before you hit the ground."

    am "I told you you were not fine. Don’t do stuff like that on me, alright?"

    show ammon e_neutral pupils_right j_neutral

    "His muscled arms wrap around you. A smell of lavender spread through your nose."
    
    if azzy_score >= 1:
        az "You should pass out more often"
        az "Or break grass"

    show ammon pupils

    "He helps you sit on the grass. He crouches yet again and take you with both hands."

    am "What’s going on!?"

    hl "My head hurts."

    am "Maybe the blood loss doing that to you. Well I’m not sure you’ve lost that much blood but it’s better to patch it up."

    "You brush your forehead and your pulsating skull heats up your hand."

    am "Let me see."

    "He puts his hand on your forehead too."

    am j_disgusted pupils_left "Ok I don’t feel like you have a fever but we’ve got to treat your headache and your hands."
    am "I think I have some aspirins and bandages in my stuff, let me get it."

    hide ammon with dissolve

    "Ammon stands up and walks towards the top box of the motorbike."
    "Still nauseated, you can’t much more than sit back and watch."
    "He opens the top—box and get his traveling bag. It is of medium—size, large enough for a 3—day trip."
    "However, you can’t but notice something familiar with one of his belongings."
    "Something cylindrical, something blue."
    "Finally, Ammon pulls out a box of medicines and bandages of his bag and gives it to you."

    show ammon at american_shot with dissolve

    am "Here, with that, your head will hurt a bit less than before."

    hl "Thanks."

    "You grab the little box."

    am "And now let me patch that."

    "He takes your hand one by one and starts to roll the tissue around the wounds."
    "He knows what he’s doing. It’s like he’s already done that before."

    am "I don’t have any antiseptic solutions but I couldn’t let that bleed."

    am "Wait you’ll surely need some water. Let me fetch some for you."

    "He starts walking to the top—box then stops midway."
    "He ponders for some moment, for a strange amount of time then turns around."

    am "I just remembered I don’t have any water. There are some faucets in the restrooms, let me you get—"

    hl "That’s alright you’ve already done enough for me."

    "You swallow down the aspirin in one fell swoop."

    if azzy_score >= 2:
        az "Show off"
    
    hl "I’m used to take them without water..."

    am "Huh I see... Well that’s great. No need to get to the restroom then."
    am "Well take your time then... We’ll leave when you’re ready."

    "The discussion drops silent. You’re too tired to get it alive anyway."
    "You try to rest a bit, but gradually something’s starting to bother you."
    "You’ve already seen this thing that Ammon had in his bag."
    "It shouldn’t catch your attention like that. After all, it’s just his bag. Nonetheless..."
    "You bite your lip. The more you look at it, the more it doesn’t make sense. Your world revolves, no, distorts around it."
    "It mesmerizes you. You are drawn to it. You can’t let the bag out of your sight anymore. The moth within has to follow this firefly."

    "You need to check this bag."
    camera at zpos_camera
    "Still quite dizzy, you manage to get up. You have to use the bike as a support. You shouldn’t push yourself too much."
    "But you still get up."

    hl "Hey you know what? I’m thirsty. I think I have some water left in my bag."

    am "Are you sure, you don’t want me to get it for you. You don’t look like you can stand up in your state."

    hl "I feel better now. I’ll feel even better when I’ll drink water, won’t I?"

    am "Sure..."

    hl "Look, I can stand! I’m a big boy aren’t I."

    show ammon j_disgusted

    "Ammon looks at you, unamused. Your attempts at teasing him fall on deaf ears. You roll your eyes."
    "You sigh and you pinch the bridge between your eyes."

    hl "Ok, I’ll just get the water."

    am "Right."

    label restarea_pointnclick_start:
        "Ammon is definitely hiding something to you."
        "Your interest has only grown bigger."
        python:
            ammon_talked = 0
            current_screen = "restarea"
            trunk_explored = False

            padlock_code = [6, 1, 5, 3]
            checked_padlock = 0 
            
            got_stick = False
            got_notebook = False
            good_code = ""

        
        # show screen custom_quickbarç
        camera:
            # perspective False
            zpos 0
            perspective False
        hide ammon
        scene black
        stop music
        play music "audio/music/moment_orange.mp3" loop fadein 1.0
        jump pointnclick_interact_loop


label confront_him:
    # python:
    #     del ammon_talked
    #     del trunk_explored
    #     del padlock_code
    #     del good_code
    #     del checked_padlock  
    #     del got_stick

    #     current_screen = "" 
    stop music fadeout 1.5
    am "Can I help you?"

    
    show parkingLot:
        xpos -2144
    show ammon at american_shot:
        xpos -1073
    
    pause 0.5

    camera:
        perspective True
        easeout 3 xpos -2032

    pause 1.5
    
    
    play music "audio/music/anger.mp3" loop fadein 0.5
    "There stands an angry dog"
    camera:
        perspective False 
        xpos 0
    
    scene black
    show parkingLot
    show ammon at american_shot
    am "May I know what are you doing with my bag?"

    "You shiver out of fear. Why did he have to see you do this. If only you could fly very far away from here."

    hl "That’s... not what you think, Ammon..."

    ### TODO: Expand the conditions with picked objects

    am j_growl "Then what are you doing with my [picked_from_the_bag] in your hand?"

    hl "I don’t know I just took it, I swear!"

    "Ammon yells at you."

    am j_yell "You just took it??? The padlock just disappeared then??? That’s what you’re going to tell me?"
    am j_disgusted "Because, if you are, don’t even show your shitty face to me anymore."
    am j_growl "You fucking cracked the padlock, you asshole."
    am "Well I’m glad you remember my birthday now, bastard. Hope it helped you crack the code."
    am "I would’ve prefered you remember a fucking month ago??? Don’t you think?!"
    am "Why did you even do that?? You can’t trust me that much??"
    am "You’ve pissed me off enough times that you possibly could{w} and even then, I’ve tried everything to set you comfortable, even comforting when you were bitching and doing one of your too many whims."
    am pupils_down j_disgusted "Bandaged you up..."
    am pupils "I went along with your hysteric behaviour all day long."
    am j_yell "And that’s how you thank me back?? By snooping my stuff??"

    show ammon j_growl

    "You stay shut. Tears overflow your eyes. You didn’t want to do that."
    
    dk "Why did you even do it."

    hl "Please understand me! I was just–"

    ### TODO: Maybe expand the argument

    am j_yell "What is there to understand?? DON’T FUCKING TOUCH MY STUFF YOU UNDERSTAND??"

    "Tears stream down your cheeks."
    "You tighten the [picked_from_the_bag]. This is your last anchor of your relationship. The last thing standing for both of you."

    az "Cling onto it."

    dk "Do not let it go."

    am j_growl "I’ve tried everything I swear, Howl. I’ve tried everything so you could stop brooding."
    am "I’ve been there for you, everytime you were having hard time."
    am "And fucking God, with you, it’s all the time, it’s like I’m caretaking a baby, not a grown man!"
    am "With Marie–Jil, we might as well be your surrogate parents, with how you let her babysit you."
    am "You’re supposed to be a couple, remember?? She’s not your mom!"
    am "So for once, just grow a pair and stop moping around."
    am "You won’t even look at her. She’s not happy with you and never will be."
    am "With you around, we both won’t ever be! You life—energy vaccuum."

    "The deluge of critiscm and reproach overwhelm you. You want to retort, to make him shut his mouth."
    "But you can’t find anything to say. Because..."
    "He’s right, isn’t he?"

    am "You know what? You should have never come back, then."

    hl "... What?"

    am "You shouldn’t have come back from those woods."
    am j_yell "I can’t deal with you anymore. You’re dragging me down. You’re intoxicating!!"
    am j_growl "Everytime you’re around my life is a fucking nightmare."
    am right e_smug j_disgusted "Why did you come back? I can’t understand why."
    am pupils_right "Why you and not him??"

    show ammon pupils_down
    
    "He falls silent."

    am pupils "... I can’t help but think Life is simply unfair when I look at you."

    "You cluch your pants. You can only mutter those words."

    hl "Why... why would you say that?.."
    hl "What did I do to deserve that?.."

    am front e_neutral "I won’t even bother with answering you. It isn’t even worth it."
    am j_growl "You don’t deserve it. You’re insufferable."

    am j_noway "But I will say one thing. Why didn’t you come for my birthday?"

    hl "..."

    am j_growl "I was expecting you. I couldn’t wait one more second. For this day, I only wished for one thing, only one thing!"
    am "That you were there. With me. That was my only wish."
    am "I wanted to give you one last chance..."

    hl "But you know I couldn’t have, this day..."
    hl "This is not my fault... That’s not fair..."

    am "..."
    am "... You never went missing didn’t you?"

    hl "huh–"

    am "You went in the forest by yourself, didn’t you?"
    am "Well, not by yourself right?"

    hl "That’s not true, I just can’t rememb–"

    am "Don’t bother. I just know it. You were never honest anyway."
    am "This is your fault... I mean:"

    am "Do you even look at yourself sometimes! You’re a fucking walking corpse! A Monster!"
    am "So that you came back or not made no difference. You may be walking..."
    am "But you should’ve stayed dead. Back then. In the woods.{w} Where I wouldn’t have to watch your sad pathetic excuse of a face anymore."
    am "No..."
    am "You know what? You’re already dead to me."
    am j_yell "Scram."

    am j_growl "No wait. Give me back my stuff then you’ll scram."
    am "I don’t want you to see me anymore. I don’t want to see you anymore..."
    am "Please just leave..."

    "Ammon turns around towards the bike."
    
    hl "Wait! Please!.."

    "You reach a hand out to him."
    "You can’t give his [picked_from_the_bag] back. He’d leave you for good if you did."

    hl "Please don’t leave... Where will I go if you leave!.."
    hl "I beg you Ammon, please stay... I am nothing without you!.."
    hl "What do you want me to do?"

    "Ammon freezes in place. He doesn’t say a word for an agonising amount of time."

    am "... I am fed up with you."

    "He turns back."

    am j_growl "Give it back to me."

    hl "... What–"

    ### TODO: Add an expression where he has exorbitated eyes

    am j_yell "GIVE BACK WHAT YOU STOLE FROM ME."

    hide ammon with dissolve
    "All of the sudden, Ammon charges."

    "Ammon grabs the [picked_from_the_bag] but there is too much at stake to let it go so you clutch his hand"
    "You wrestle for your life to get the [picked_from_the_bag] back. This is your last chance to set things right so you scratch at him, hiss at him, and even bites him."
    "On the other hand, Ammon won’t let go either. He barks at you, jerks his head in all directions. He’s slipping through your fingers the more you pull that [picked_from_the_bag]."
    
    hl "Please Ammon!! Trust me!!!"
    hl "Please believe me!{w} Please that someone believes me for once!"
    hl "I’m tired of repeating myself!"
    hl "Please believe me!"

    "You put you hand out to him, to his shoulder. He might understand if you can grab a hold of him."

    am "{size=60}BACK OFF{/size}"

    play sound "audio/sounds/punch.mp3"
    
    
    show expression "#F00" at alpha_dissolve:
        easeout 1.5 alpha 0.7
    show parkingLot with sshake

    "The next moment, his fist connects to your eyebrows arch and you blast through the air on his motorcycle."
    "The [picked_from_the_bag] sits on the floor, its contents spilled in the grass, last relic of your fleeting friendship, trampled"
    "You hit your head hard on the frame of the motorcycle. Blood trickles down from it. You pass your head on your wound. Just blood."

    am "FUCK, sorry, I didn’t mean to! Let me hel–"

    hl "{size=60}YOU FUCKING BASTARD{/size}"

    show parkingLot with sshake

    scene black with dissolve

    "You spring on Ammon. You both roll on the grass. After that it’s a bit of a blur. You don’t remember everything."


    
    stop music fadeout 0.5
    play music "audio/music/uboa.mp3" loop

    show parkingLot with dissolve
    show expression "#F00" at alpha_dissolve:
        easeout 1.5 alpha 0.7

    "All you remember, is Ammon laid down in the grass, defenseless, his face contorting in pain. He’s out of breath, imploring for air."
    "You, on the other hand, sits on top of him, astride. You watch his unbeckled belt and you can see the tip of his underpants though his fly."
    "You gulp."
    if azzy_score >= 2:
        az "Why that now..."
    "Unfortunately, the more you go up though his body, the more you wish you stayed down there."
    "His disheveled, torn down, shirt and his black dirty jacket were no different, no the thing that disturbs you were your arms compressing his chest down."
    "This must hurt him so you should stop but your arms keep pressing down and his cries of pain fill your ears. But you keep pressing down, no matter how much he seethes."
    "Even more disturbing, Ammon hits your arms with all his strength but that reveals in vain, your arms planted there like statues, unmovable, whatever may happened."
    "Despite his determination and his fierceness, the fists grew gradually weaker to the point where the wind hits you as hard as him."
    "The knee strikes, beforehand, as piercing as spears, in your back, became bumps comparable to tickles."
    "Then you understand. Your hands are wrapped around the thick neck of your weakening friend."
    "You squeeze and squeeze his squishy throat crushing every chance that air revigorates him. His adam apple convulsing under your thumb gives you a wave of nausea. However..."
    pause 1.0
    "You find yourself loving touching his flim skin, and its rough texture. You wished you had done it sooner."
    "Ammon’s face turns pale as you writhe him of his last strands of energy. Drool bubbles out of his mouth, his teeth gritted to keep the remaining air in his mouth."
    "Another thread of drool drops on Ammon. Your eyes are exorbitated from rage. You have become a feral animal."
    "All of the sudden, you feel a loving touch on your arm. The dying hound shares a gaze with you as his last sparkles of life exit those sad eyes."
    "Close to Death, he says:"

    am "Pl–please stop."

    "You succeed to make up words from the low raspy sound coming out of his throat."
    
    am "I believ–believe you, ok? You are my friend and I won’t leave you, ok?"
    am "I know you’re having hard times, so I won’t hold you to what you’re doing right now, I promise."
    
    "His grip weakens, all colours drain out of his face. His throat before, contracting and moving, goes more and more inert."
    
    am "You’re n–not dea–dead. You always ha–have been the s–same cat I met years ago."
    
    "He grins at you, tears streaming down the corner of his lips."
    am "I don’t want to ever leave you."
    am "I’ve said a—ll"
    "He coughs and drool leaks on your hands. You don’t budge."
    am "a–all those horri—horrible things to you, but I never thought them."
    am "You’re one of my favourite persons"
    am "So... I know it’s not you so stop doing that, I beg you."
    am "Re—remove your h—hands... Please."

    "His hands fall down, unmoving. He doesn’t breathe a lot anymore."
    if ammon_score == 0:
        "But you didn’t care. All you want it to keep strangling his squishy little throat. It brings within you forbidden pleasures."
        "You loved every rictus of pain on his face. You drool even more and these strings mix with his."
        "Your pleasure is indiscernible from his pain. You hate him. You hate him and you hope he suffers enough." 
        "He’s going to regret ever thinking about leaving you."
        stop music
        cl "Told you so."
        cl "You love it."
        cl "You loved it."
        cl "You’re not at all a living being."
        cl "You’re a beast. {w}You are a Monster."

        "You remove your hands."
        hl "... Why."

        "A wave of nausea overflows you."
        "You puke."
    
    # else:
    #     "Then you remenmber. All the times Ammon bring up your spirits. All the times you cried out of exhaustion and he was there for you."
    #     "All the times, he took your yogurt at lunch at middle school and toyed with you for minutes. In the instant, you hated it but in the end, you’d laugh."
    #     "The time you feel nauseated at this lame party and he came take you home even though he told you not to."
    #     "The times where he didn’t feel good so you watched over him for day and nights so he’d go better."
    #     "You grin. You couldn’t have a better friend than him. He was the only one able to fully understand you. Then you realise."
    #     "You’re strangling him. Your hands are wrapped his neck. What are you doing. What you’re doing is bad, forbidden. You’re committing a crime."
    #     "You remove you hands of his neck and you stand up so fast, you’re striked with the vertigo."
    #     "Ammon let out a seething gasp, finally air filling his lungs. However he stays on the ground, too puny of your assault."
        
    #     if ammon_score >= 1:
    #         am "Thanks Gap..."
    #         am "I like you {w}a lot."
    #         if ammon_score == 3:
    #             am "No. I lo–"
        
        "He doesn’t talk anymore. Does he breathe anymore?"
    
    "Your headache assaults you with greater intensity. You clutch you head. You lose your balance."
    "You collapse."

    jump first_act_part_1
    