## NOTE: Create a item class 
init python:
    class Item:
        def __init__(self, name, image, description, examine="default_examine"):
            self.name = name
            # self.image = Image("Environment Items/{}_idle".fornat(image))
            self.image = image
            self.description = description
            self.examine = examine

    
default ga_inventory = []
default columns_nb = 2
default rows_nb = 3
default selected_item = ""
default notebook = Item("Notebook", "notebook", _("Ton carnet bien-aimé. Tu l'emportes partout avec toi."), "notebook_examine")
default water_bottle = Item("Water Bottle", "water-bottle", _("Une bouteille d'eau qui réhydrate ! Pour être honnête, \ntu as plutôt soif.."), "water_bottle_examine")
# default cigarette = Item("Cigarette", "cigarette", "I knew Ammon was hiding some from me.", "cigarette_examine")
default ammon_wallet = Item("Ammon’s Wallet", "wallet", _("Ammon’s wallet. You might find \nsome interesting information about him"), "ammon_wallet_examine")
default stick = Item("Stick", "stick", _("C'est un bâton. Ammon pourrait aimer ça."), "stick_examine")

default presented_item = ""


## NOTE: custom inventory for game
screen inventory():
    tag dialogue

    frame:
        at inventory_move_in
        style 'inventory_frame'
        background "gui/inventory_bg.png"

        if selected_item == "" and ga_inventory != []:
            $ selected_item = ga_inventory[0]
        #     # on "show" action [SetVariable("inventory_desc", ga_inventory[0].description), SetVariable("inventory_image", ga_inventory[0].image), SetVariable("inventory_name", ga_inventory[0].name)]
        #     on "show" action SetVariable("selected_item", ga_inventory[0])
        
        # elif selected_item != "":
        #     vbox:
        #         style 'desc_inventory'
        #         add "Environment Items/"+selected_item.image+"_idle.png" size (256, 256)
        #         text selected_item.description size 20
            
        #     vbox:
        #         style 'txt_butt'
        #         if evidence_needed:
        #             textbutton "Present":
        #                 action Return()
                
        #         textbutton "Examine":
        #             action Call(selected_item.examine)

        # grid columns_nb rows_nb:
        #     style 'item_inventory'
        #     $ item = ""
        #     for i in range(columns_nb*rows_nb):
        #         if i < len(ga_inventory):
        #             $ item = ga_inventory[i]

        #         imagebutton auto "gui/inventory_slot_%s.png" action SetVariable("selected_item", item)
        #         # imagebutton auto "Environment Items/{}_%s.png".format(item.image) action SetVariable("selected_item", item):
        
        grid columns_nb rows_nb:
            style 'grid_inventory'
            for item in ga_inventory:
                imagebutton auto "Environment Items/{}_%s.png".format(item.image) action SetVariable("selected_item", item):
                    style 'item_inventory'  
                    at custom_zoom

        imagebutton auto "gui/backbutton_%s.png" action Hide("inventory"):
            style 'return_inventory_butt'
            at custom_zoom
        
        imagebutton auto "gui/button/examine_%s.png":
            pos (67, 660)
            action Call(selected_item.examine)
    
    
        

style inventory_frame:
    anchor (0.0, 0.0)

style item_inventory:
    anchor (0.5, 0.5)

style grid_inventory:
    xpos 100 
    ypos 200
    spacing 30

style desc_inventory:
    # pos (520, 200)
    spacing 30

style txt_butt:
    # pos (600, 600)
    text_align (0.5, 0.5)
    spacing 40

style return_inventory_butt:
    xpos -100

        

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
    hide screen inventory 
    # call pointnclick_screen from _call_pointnclick_screen
    "Rien de particulier sur ça."
    show screen inventory
    return

label water_bottle_examine:
    # call pointnclick_screen from _call_pointnclick_screen_1
    "De l’eau, cool"
    call screen inventory
    return
label cigarette_examine:
    # call pointnclick_screen from _call_pointnclick_screen_2
    "You’d light one but you don’t have a lighter."
    "Seems like you’ll have to see Ammon anyway."
    show screen inventory
    return
label ammon_wallet_examine:
    # call pointnclick_screen from _call_pointnclick_screen_3
    hl "Tu devrais pouvoir trouver des informations sur Ammon."
    "Tu fouilles dans son portefeuille"
    "Il y a un peu d'argent, des cartes cadeaux et des coupons pour des magasins. Ce n'est pas vraiment intéressant pour toi, honnêtement."
    "Puis tu repères la chose que tu cherchais."

    show ammon_id
    pause 2.0
    "Eh bien voici son anniversaire, tu devrais pouvoir ouvrir le cadenas maintenant."
    hide ammon_id
    show screen inventory
    return

label stick_examine:
    # call pointnclick_screen from _call_pointnclick_screen_4
    "C'est un bâton. Il n'y a rien de plus..."
    "Mais ça pourrait intéresser Ammon." 
    "Tu sais, comme il est un chien et tout ça..."
    show screen inventory
    return

label notebook_examine:
    show screen notebook
    return