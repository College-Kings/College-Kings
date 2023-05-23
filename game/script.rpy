define config.enable_steam = True
define config.console = True
define config_debug = False # Automatic Testing

define config.version = "1.3.10"

define config.steam_appid = 1463120
define config.image_cache_size_mb = 520
define config.load_failed_label = "load_failed"
define config.exception_handler = exception_handler
define config.label_callback = label_callback
define _quit_slot = "99-1"


label path_builder:
    $ quick_menu = False
    
    call screen path_builder_starting_location
    return


# The game starts here.
label start:
    if config.developer:
        show screen debug_overlay

    call screen real_life_mode
