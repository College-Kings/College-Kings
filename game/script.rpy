define config.enable_steam = False
define config.developer = True
define config.console = True
define config_debug = False
define config_censored = False

define config.version = "14.9.0{} - ({})".format('s' if config.enable_steam else "", date.today())

define config.steam_appid = 1463120

define config.gl2 = True
define _quit_slot = "99-1"

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

# The game starts here.
label start:
    
    # Get Animation/Transform List
    show no_hard_feelings at achievementShow
    $ achievementAtList = renpy.get_at_list("no_hard_feelings")
    hide no_hard_feelings

    if config.developer:
        show screen bugTesting_Overlay
        
    show screen fightDamage

    call screen realmode

label end_credits: # for compatibility
label gameEnd:
    stop music fadeout 3
    play music "music/vocal.mp3"

    if not config.enable_steam:
        call screen getaccess

label credits:
    show credits:
        ypos 50
        xalign 0.5

    call screen credits
