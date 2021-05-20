init python:
    persistent.ep = 7

define config.enable_steam = True
define config.developer = True
define config.console = True


define config.steam_appid = 1463120

define _game_menu_screen = "ingmenu"

label splashscreen:
    # Get Animation/Transform List
    show nohardfeelings at achievementShow
    $ achievementAtList = renpy.get_at_list("nohardfeelings")
    hide nohardfeelings

    # Splashscreen
    scene black
    with Pause(1)

    show splashone
    with dissolve
    with Pause(2)

    show splashtwo
    with dissolve
    with Pause(2)

    show splashthree
    with dissolve
    with Pause(2)

    scene black
    with dissolve
    with Pause(1)

    return

# The game starts here.
label start:
    # Get Animation/Transform List
    show nohardfeelings at achievementShow
    $ achievementAtList = renpy.get_at_list("nohardfeelings")
    hide nohardfeelings

    call screen realmode


label end_credits:
    stop music fadeout 2.0
    play music "music/vocal.mp3"

    if not config.enable_steam:
        show screen getaccess
        with dissolve
        " "
        hide screen getaccess

    show credits:
        ypos 50
        xalign 0.5

    call screen credits
