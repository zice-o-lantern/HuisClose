## NOTE: Create a item class 
init python:
    class Item:
        def __init__(self, name, image, description, examine="default_examine"):
            self.name = name
            self.image = image
            self.description = description
            self.examine = examine

    
default ga_inventory = []
default columns_nb = 2
default rows_nb = 3
default selected_item = ""
default notebook = Item("Notebook", "notebook", "My beloved notebook. I bring it out with me everywhere.")
default water_bottle = Item("Water Bottle", "bottle", "A water bottle that rehydrates! To be honest, \nI’m pretty honest, I’m pretty thirsty.", "water_bottle_examine")
# default cigarette = Item("Cigarette", "cigarette", "I knew Ammon was hiding some from me.", "cigarette_examine")
default ammon_wallet = Item("Ammon’s Wallet", "portefeuille_clark", "Ammon’s wallet. You might find \nsome interesting informations about him", "ammon_wallet_examine")
default stick = Item("Stick", "stick", "This is a stick. Ammon might like it.")

default presented_item = ""

style item_inventory:
    align (.68, .3)
    spacing 30

style desc_inventory:
    pos (520, 200)
    spacing 30

style txt_butt:
    pos (600, 600)
    text_align (0.5, 0.5)
    spacing 40


## NOTE: custom inventory for game
screen inventory():
    tag menu

    add "inventory_bg"

    if selected_item == "" and ga_inventory != []:
        # on "show" action [SetVariable("inventory_desc", ga_inventory[0].description), SetVariable("inventory_image", ga_inventory[0].image), SetVariable("inventory_name", ga_inventory[0].name)]
        on "show" action SetVariable("selected_item", ga_inventory[0])
    
    elif selected_item != "":
        vbox:
            style 'desc_inventory'
            add selected_item.image size (256, 256)
            text selected_item.description size 20
        
        vbox:
            style 'txt_butt'
            if evidence_needed:
                textbutton "Present":
                    action Return()
            
            textbutton "Examine":
                action Call(selected_item.examine)

    grid columns_nb rows_nb:
        style 'item_inventory'
        $ item = ""
        for i in range(columns_nb*rows_nb):
            if i < len(ga_inventory):
                $ item = ga_inventory[i]

            imagebutton auto "inventory_slot_%s.png" action SetVariable("selected_item", item)
    
    grid columns_nb rows_nb:
        style 'item_inventory'
        for i in ga_inventory:
            add i.image size(128, 128)
        

screen get_item(item):
    tag menu

    frame:
        style 'item_inventory'

        hbox:
            spacing 10
            add item.image size (128, 128)

            vbox:
                spacing 20
                text item.name size 40
                text item.description size 40

label default_examine:
    n1 "Nothing special about it."
    call screen inventory
    return

label water_bottle_examine:
    "I should bring it to Ammon. {w}He might get impatient. I care no less if he’s pissed."
    "But I don’t have to deal his prick attitude, right now."
    call screen inventory
    return
label cigarette_examine:
    "You’d light one but you don’t have a lighter."
    "Seems like you’ll have to see Ammon anyway."
    call screen inventory
    return
label ammon_wallet_examine:
    ga "I should be able to find some informations on Ammon."
    "You search through his wallet"
    "There’s some money, gift cards and coupons for some groceries store. Not really interesting to you to be, honest."
    "Then you spot the thin you was searching for."

    show ammon_id
    pause 2.0
    "Well here his birthday, you should be able to open the padlock now"
    hide ammon_id
    call screen inventory
    return

label stick_examine:
    "This is a stick. Nothing more to it..."
    "Though it could interest Ammon." 
    "You know, how he’s a dog and all..."
    call screen inventory
    return