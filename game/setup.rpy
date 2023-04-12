init python:
    def setup():
        path_builder_setup()
        
        nonplayable_character_setup()

        if config_debug:
            # Clear the contents of "game_log.txt"
            open(os.path.join(config.basedir, "game_log.txt"), "w").close()