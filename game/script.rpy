define config.enable_steam = True
define config.developer = False
define config.console = True
define config_debug = False # Automatic Playing
define config_censored = False

define config.version = get_version(13, 2, 2)

define config.steam_appid = 1463120
# define config.load_failed_label = "load_failed"
define config.gl2 = True
define _quit_slot = "99-1"


# The game starts here.
label start:
    $ setup()
    call screen real_life_mode

label gameEnd:
    stop music fadeout 3
    play music "music/vocal.mp3"

    call screen end_screen