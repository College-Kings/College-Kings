screen bugTesting_Overlay():
    zorder 1000
    
    $ fileLine = renpy.get_filename_line()
    text "[fileLine!q]" xpos 10 color "#0f0"