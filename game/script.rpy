define config.developer = True
define config.enable_steam = False
define config.console = True
define config_debug = False # Automatic Testing
define config_censored = False

define config.version = (1, 2, 11)

define config.steam_appid = 1463120
define config.load_failed_label = "load_failed"
define config.gl2 = True
define config.exception_handler = exception_handler
define config.label_callback = label_callback
define _quit_slot = "99-1"


label path_builder():
    $ setup()
    $ quick_menu = False
    call screen path_builder_starting_location
    return


# The game starts here.
label start:
    $ setup()

    call screen real_life_mode
