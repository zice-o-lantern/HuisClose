label test_room:
    # show screen get_item(car_keys)

    # "You got the car keys"

    # hide screen get_item

    # "Anyway"
    scene bg test
    python:
        ga_inventory.append(notebook)
        ga_inventory.append(water_bottle)
        # ga_inventory.append(cigarette)
        ga_inventory.append(ammon_stuff)
    # python:
    #     ammon_talked = 0
    #     current_screen = "restarea"