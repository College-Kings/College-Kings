init python:
    persistent.ep = 10

define steam = False
define developer = True
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