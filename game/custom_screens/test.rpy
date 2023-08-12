label test_room:
    # show screen get_item(car_keys)

    # "You got the car keys"

    # hide screen get_item

    # "Anyway"
    $ ammon_talked = 0
    label restarea_interact_loop:
        window hide
        $ renpy.show_screen("restarea", _layer="master")
        $ ui.interact()
        jump restarea_interact_loop