python early:
    def get_short_git_sha():
        import os
        import subprocess

        cwd = os.getcwd()
        os.chdir(config.basedir)

        try:
            short_hash = subprocess.check_output([ "git", "rev-parse", "--short", "HEAD"]).strip()
            with open(os.path.join(config.basedir, "game", "version.txt"), "w") as file:
                file.write(str(short_hash))
        except subprocess.CalledProcessError:
            with open(os.path.join(config.basedir, "game", "version.txt"), "r") as file:
                short_hash = file.read().strip()

        os.chdir(cwd)
        return short_hash


    def get_version(major, minor, patch, development=False):
        act_1 = 7

        act = "DEVELOPMENT" if development else max(-((major - act_1) // -3) + 1, 1)    

        version = "{}.{}.{}".format(major, minor, patch)
        if config.enable_steam:
            version += "s"

        return "{} (Act: {}) (SHA: {})".format(version, act, get_short_git_sha())
