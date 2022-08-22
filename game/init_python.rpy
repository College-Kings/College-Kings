init python:
    # Helper functions
    
    def get_file_contents(file_path: str):
        with open(file_path, "r") as f:
            return f.read()


    def write_console(data: Any):
        with open("console.txt", "w") as f:
            f.write(str(data))


    def exception_handler(
        short_traceback: str, long_traceback: str, path_to_traceback_file: str
    ) -> bool:
        if not config_debug:
            return False

        if "ScriptError: could not find label" in short_traceback:
            renpy.jump("v1_start")

        return False


    def label_callback(label_name: str, is_reached_from_jump: bool):
        try:
            label_history.add(label_name)
        except NameError: pass
    

    def write_scene_lines_to_file():
        file_line = renpy.get_filename_line()
        with open(os.path.join(config.basedir, "game_log.txt"), "a") as f:
            f.write(f"{file_line}\n")


init 100 python:
    if config_debug:
        config.interact_callbacks.append(write_scene_lines_to_file)