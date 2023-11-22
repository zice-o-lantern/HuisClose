init offset = -5
# default car_keys = Item("Car Keys", "/images/gui/carKeys.webp", "The keys for turning on my car. \nIt should be able to unlock the trunk too.")
default current_screen = ""

default ammon_score = 0
default azzy_score = 0
default derek_score = 0

default got_notebook = False
default empty_inventory = True

# init python:
#     def check_inventory_empty():
#         if len(ga_inventory) > 0:
#             empty_inventory = False

default evidence_needed = False
default evidence_selected = ""
default evid_label_to_go = ""


init python:
    def narrator_noise(event, interact=True, **kwargs):
        if event == "show":
            renpy.sound.play("audio/sounds/beeps/cell_noise.ogg", channel="sound", loop=True)
        elif event == "slow_done":
            renpy.sound.play("audio/sounds/beeps/silence.wav", channel="sound", loop=True)
    
    def gap_noise(event, interact=True, **kwargs):
        if event == "show":
            renpy.sound.play("audio/sounds/beeps/howl_1_normal.ogg", channel="sound", loop=True)
        elif event == "slow_done":
            renpy.sound.play("audio/sounds/beeps/silence.wav", channel="sound", loop=True)
    
    def ammon_noise(event, interact=True, **kwargs):
        if event == "show":
            renpy.sound.play("audio/sounds/beeps/deep_1_normal.ogg", channel="sound", loop=True)
        elif event == "slow_done":
            renpy.sound.play("audio/sounds/beeps/silence.wav", channel="sound", loop=True)
    
    def clair_noise(event, interact=True, **kwargs):
        if event == "show":
            renpy.sound.play("audio/sounds/beeps/clair_1_normal.ogg", channel="sound", loop=True)
        elif event == "slow_done":
            renpy.sound.play("audio/sounds/beeps/silence.wav", channel="sound", loop=True)