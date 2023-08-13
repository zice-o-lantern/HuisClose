label pointnclick_interact_loop:
    window hide
    $ renpy.show_screen(current_screen, _layer="master", screen_active=True)
    $ ui.interact()
    jump pointnclick_interact_loop