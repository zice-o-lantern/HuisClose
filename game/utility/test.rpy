label test:
    "Hello testing timer"
    $ time = 5
    $ timer_range = 0
    $ timer_jump = "run_out_of_time"

    show screen countdown
    menu:
        "Test":
            "you made it"
        "Please":
            "ts’a.uirts"

label run_out_of_time:
    "well that’s bad"