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

init python:
    time = 0 
    timer_range = 0 
    timer_jump = "timer_default"

screen countdown(show_c=False):
    timer 0.01 repeat True action If(time > 0, true=SetVariable("time", time - 0.01), false=[Hide("countdown"), Jump(timer_jump)])
    if show_c:
        bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

label timer_default:
    "No label to jump to"
    return