## NOTE: Create a item class 
init python:
    class Item:
        def __init__(self, name, image, description):
            self.name = name
            self.image = image
            self.description = description

style item_inventory:
    yalign .3


## NOTE: custom inventory for game
screen inventory:
    tag menu

    frame:
        style 'item_inventory'
        hbox:
            for i in ga_inventory:
                frame:
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

            