init python:
    def setup():
        if config_debug:
            # Clear the contents of "game_log.txt"
            open(os.path.join(config.basedir, "game_log.txt"), "w").close()