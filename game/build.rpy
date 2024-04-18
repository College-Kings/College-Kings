define build.name = "CollegeKings"
define build.directory_name = "CollegeKings{}".format("" if config.enable_steam else f"-{config.version}")
define build.destination = "{}-dists".format(build.name)
define build.include_old_themes = False
define build.include_i686 = False

init python:
    ## Classify files as None to exclude them from the built distributions.

    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("README.md", None)
    build.classify("game/**.md", None)
    build.classify("audio/music/ck1/**", None)

    build.classify('game/**.py', 'archive')
    build.classify('game/**.rpy', "archive")
    build.classify("game/**.rpyc", "archive")