define config.enable_steam = False # Make sure you switch main_menu_background image to steam version.
define config.developer = False
define config.console = True
define config_debug = False
define config_censored = False

define config.steam_appid = 1463120

define _game_menu_screen = "ingmenu"

label splashscreen:
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

label before_main_menu:
    python:
        msgApp.img = "images/phone/messages/appAssets/messagesIcon.webp"
        statsApp.img = "images/phone/stats/appAssets/statsIcon.webp"
        achApp.img = "images/phone/achievements/appAssets/achievementsIcon.webp"
        kiwiiApp.img = "images/phone/kiwii/appAssets/kiwiiIcon.webp"

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
