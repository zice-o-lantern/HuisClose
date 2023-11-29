init offset = -5

init python:
    
    import math

    class Shaker(object):
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                    time,
                    child,
                    add_sizes=True,
                    **properties)

    Shake = renpy.curry(_Shake)

define sshake = Shake((0, 0, 0, 0), 1.0, dist=50)

init python:
    renpy.register_shader('drunk', variables="""
    uniform sampler2D tex0;
    uniform vec2 u_model_size;
    varying vec2 v_uv;
    uniform float u_blur_radius;
    uniform float u_dark_radius;
""", vertex_300="""
    v_uv = a_position.xy / u_model_size;
""", fragment_300="""
    vec4 col = texture2D(tex0, v_uv);
    col += texture2D(tex0, v_uv + vec2(.0, -u_blur_radius) / u_model_size);
    col += texture2D(tex0, v_uv + vec2(.0, u_blur_radius) / u_model_size);
    col += texture2D(tex0, v_uv + vec2(-u_blur_radius, .0) / u_model_size);
    col += texture2D(tex0, v_uv + vec2(u_blur_radius, .0) / u_model_size);
    col /= 5.0;
    gl_FragColor = vec4(mix(col.rgb, vec3(0,0,0), max(distance(v_uv, vec2(.5,.5)) / sqrt(.5) - u_dark_radius, .0)), col.a);
""")

transform shaking:
    linear 0.05 xoffset -50 yoffset 50 
    linear 0.05 xoffset 100 yoffset -100 
    linear 0.05 xoffset 50 yoffset -50
    linear 0.05 xoffset -100 yoffset 100
    linear 0.05 xoffset 0 yoffset 0
    repeat

transform drunk:
    # parallel:
    #     parallax()
    # parallel:
        shader 'drunk'
        u_blur_radius .0 u_dark_radius 1.0
        easein .5 u_blur_radius persistent.blur u_dark_radius .5
        .1
        easeout .5 u_blur_radius .0 u_dark_radius 1.0

# Declare images

image ruralRoad = "bg/ruralRoad.webp"
image parkingLot = "bg/bg restArea.jpg"
# image clearing = "bg/clearing.webp"

define dissolve = Dissolve(.5)
define fade = Fade(1., 1., 1.)

label spawn_fireflies:
    ##NOTE: Spawning fireflies
    
    $ xpo = renpy.random.randint(500, 1300)
    $ ypo = renpy.random.randint(200, 640)
    $ margin = 10

    show firefly:
        alpha 0.0
        xpos xpo
        ypos ypo

        easein 1.0 alpha 1.0
    show firefly:
        parallel:
            ease 1.0 alpha 0.0
            ease 1.0 alpha 1.0
        parallel:
            ease 1 xpos xpo-margin
            ease 1 xpos xpo+margin
            ease 1 xpos xpo-margin
            # ease 1 xpos xpo+margin
        
        parallel:
            ease 1 ypos ypo-margin
            ease 1 ypos ypo+margin

        repeat
        
    $ xpo = renpy.random.randint(500, 1300)
    $ ypo = renpy.random.randint(200, 640)

    show firefly as firefly1:
        alpha 0.0
        linear 2 alpha 0.0
        xpos xpo
        ypos ypo

        easein 1.0 alpha 1.0
    
    show firefly as firefly1:
        linear 2 alpha 0.0
        parallel:
            ease 1.0 alpha 0.0
            ease 1.0 alpha 1.0
        parallel:
            ease 1 xpos xpo-margin
            ease 1 xpos xpo+margin
            ease 1 xpos xpo-margin
            # ease 1 xpos xpo+margin
        
        parallel:
            ease 1 ypos ypo-margin
            ease 1 ypos ypo+margin

        repeat
    
    $ xpo = renpy.random.randint(500, 1300)
    $ ypo = renpy.random.randint(200, 640)

    show firefly as firefly2:
        alpha 0.0
        linear 4 alpha 0.0
        xpos xpo
        ypos ypo

        easein 1.0 alpha 1.0
    
    show firefly as firefly2:
        linear 4 alpha 0.0
        parallel:
            ease 1.0 alpha 0.0
            ease 1.0 alpha 1.0
        parallel:
            ease 1 xpos xpo-margin
            ease 3 xpos xpo+margin
            ease 1 xpos xpo-margin
            # ease 1 xpos xpo+margin
        
        parallel:
            ease 3 ypos ypo-margin
            ease 1.4 ypos ypo+margin

        repeat
    
    $ xpo = renpy.random.randint(500, 1300)
    $ ypo = renpy.random.randint(200, 640)

    show firefly as firefly3:
        alpha 0.0
        linear 7 alpha 0.0
        xpos xpo
        ypos ypo

        easein 1.0 alpha 1.0
    
    show firefly as firefly3:
        linear 7 alpha 0.0
        parallel:
            ease 1.0 alpha 0.0
            ease 1.0 alpha 1.0
        parallel:
            ease 1 xpos xpo-margin
            ease 1 xpos xpo+margin
            ease 1 xpos xpo-margin
            # ease 1 xpos xpo+margin
        
        parallel:
            ease 1.4 ypos ypo-margin
            ease .9 ypos ypo+margin

        repeat
    
    $ xpo = renpy.random.randint(500, 1300)
    $ ypo = renpy.random.randint(200, 640)

    show firefly as firefly4:
        alpha 0.0
        linear 9 alpha 0.0
        xpos xpo
        ypos ypo

        easein 6.2 alpha 1.0
    
    show firefly as firefly4:
        linear 9 alpha 0.0
        parallel:
            ease 1.0 alpha 0.0
            ease 1.0 alpha 1.0
        parallel:
            ease 1 xpos xpo-margin
            ease 1 xpos xpo+margin
            ease 1 xpos xpo-margin
            # ease 1 xpos xpo+margin
        
        parallel:
            ease 2 ypos ypo-margin
            ease 2 ypos ypo+margin

        repeat
    return

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