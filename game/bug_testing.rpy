screen bugTesting_Overlay():
    if config.developer:
        $ fileLine = renpy.get_filename_line()
        text "[fileLine!q]" xpos 10 color "#0f0"