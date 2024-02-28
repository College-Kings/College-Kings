define config.enable_steam = False
define config_debug = False # Automatic Testing

define config.version = "1.4.5"

label path_builder:
    $ quick_menu = False
    
    call screen path_builder_starting_location
    return


# The game starts here.
label start:
    if config.developer:
        show screen debug_overlay

    call screen real_life_mode
