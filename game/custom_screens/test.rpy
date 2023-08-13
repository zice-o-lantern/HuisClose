label test_room:
    # show screen get_item(car_keys)

    # "You got the car keys"

    # hide screen get_item

    # "Anyway"
    python:
        ammon_talked = 0
        current_screen = "restarea"

        
    jump pointnclick_interact_loop