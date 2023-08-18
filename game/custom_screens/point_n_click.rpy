label pointnclick_interact_loop:
    window hide
    $ renpy.call_screen(current_screen, _layer="master", screen_active=True)
    jump pointnclick_interact_loop

label present_evidence_loop:
    $ evidence_needed = True
    call screen inventory
    if selected_item.name == evidence_selected:
        $ evidence_needed = False
        jump evid_label_to_go
    else:
        "Wrong one"
        jump present_evidence_loop