init offset = -5

# Declare images

image ruralRoad = "bg/ruralRoad.webp"
image parkingLot = "bg/bg restArea.jpg"
# image clearing = "bg/clearing.webp"

define dissolve = Dissolve(.5)
define fade = Fade(1., 1., 1.)

transform shiver_image(e=0.05, x=10,b=0):
    easein e xoffset b-x
    easein e xoffset b+x
    easein e xoffset b-x
    easein e xoffset b+x
    easein e xoffset b-x
    easein e xoffset b+x
    easein e xoffset b-x
    easein e xoffset b+x
    repeat

transform shiver_image_end(e=0.05, x=10):
    easein e xoffset -x
    easein e xoffset x
    easein e xoffset -x
    easein e xoffset x
    easein e xoffset -x
    easein e xoffset x
    easein e xoffset -x
    easein e xoffset 4
    easein e xoffset -4
    easein e xoffset 3
    easein e xoffset -3
    easein e xoffset 2
    easein e xoffset -2
    easein e xoffset 1
    easein e xoffset -1
    easein e xoffset 0

transform headright:
    linear 15 xalign 1.0

transform bounce:
    linear 0.5 xalign 1.0
    linear 100 xalign 0.0

transform move_right:
    linear 1 xpos -500

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0

    on hide:
        linear 0.5 alpha 0.0

transform zpos_bg:
    zoom 2.535
    align (0.5, 0.5)

transform zpos_camera:
    parallel:
        easein 1 zpos 1920
    parallel:
        easein 1 ypos 0

transform american_shot:
    xalign 0.5
    yalign 0.25

transform close_shot:
    parallel:
        ease 2 zpos 700
    parallel:
        ease 2 ypos -500

transform WiggleVision:
    xcenter 0.5
    ycenter 0.5
    zoom 1.5
    parallel:
        easein 2 xoffset 25
        easein 2 xoffset -25
        repeat
    parallel:
        easein 3 yoffset 50
        easein 3 yoffset -50
        repeat
    parallel:
        linear 2 blur(20)
        linear 2 blur(0)
        repeat

transform WiggleVisionAwake:
    xcenter 0.5
    ycenter 0.5
    zoom 1.3
    parallel:
        easein 2 xoffset 3
        easein 2 xoffset -3
        repeat
    parallel:
        easein 3 yoffset 2
        easein 3 yoffset -2
        repeat
    parallel:
        linear 2 blur(0)
        linear 2 blur(0)
        repeat

# transform zpos_black

    #############
    ## Effects ##
    #############

define blink_speed = 0.5
define rl_speed = 128
define dot_transition = ImageDissolve("Effects/dot_transition.png", 0.5, 320)
define blink_transition = ImageDissolve("Effects/eye_blink.png", blink_speed, ramplen=rl_speed)
define blink_reverse = ImageDissolve("Effects/eye_blink.png", blink_speed, ramplen=rl_speed, reverse=True)
define eye_lid = Image("Effects/eye_lid.png")