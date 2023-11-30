init python:
    def button_available(screen_active):
        return screen_active and not renpy.get_screen("inventory") and not renpy.get_screen("notebook")


label pointnclick_interact_loop:
    window hide
    $ renpy.call_screen(current_screen, _layer="master", screen_active=True)
    if current_screen != "":
        jump pointnclick_interact_loop

label present_evidence_loop:
    $ evidence_needed = True
    call screen inventory
    if selected_item.name == evidence_selected:
        $ evidence_needed = False
        $ renpy.jump(evid_label_to_go)
    else:
        "Wrong one"
        jump present_evidence_loop

label pointnclick_screen:
    if renpy.get_screen(current_screen):
        $ renpy.show_screen(current_screen, _layer="master",screen_active=False)
    return