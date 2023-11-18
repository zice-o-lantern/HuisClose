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