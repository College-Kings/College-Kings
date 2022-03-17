screen bugTesting_Overlay():
    zorder 1000
    
    if config.developer:
        $ fileLine = renpy.get_filename_line()
        vbox:
            text "[fileLine!q]" xpos 10 color "#0f0"
            text "Stack Depth: {}".format(renpy.call_stack_depth())
            