screen custom_quickbar:
    hbox:
        spacing 20
        if not empty_inventory:
            imagebutton:
                idle 'inventory'
                hover 'inventory_hover'
                action ShowMenu("inventory")

        if got_notebook:
            imagebutton:
                at custom_zoom
                idle "notebook"
                hover "notebook_hovered"
                action ShowMenu("notebook")