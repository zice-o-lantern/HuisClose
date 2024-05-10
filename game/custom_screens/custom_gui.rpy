screen custom_quickbar:
    $ screen_active = renpy.get_screen("inventory")
    hbox:
        spacing 20
        if not empty_inventory:
            imagebutton auto "gui/inventory_%s.png":
                action Show("inventory")
                sensitive not screen_active

        if got_notebook:
            imagebutton:
                at custom_zoom
                idle "notebook_idle"
                hover "notebook_hover"
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

label hide_customgui:
    hide screen inventory
    hide screen notebook

style return_butt:
    align (1.0, 0.0)