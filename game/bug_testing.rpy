init python:
    config.overlay_screens.append("bugTesting_Overlay")

screen bugTesting_Overlay():
    zorder 1000
    
    $ fileLine = renpy.get_filename_line()
    vbox:
        text "[fileLine!q]" xpos 10 color "#0f0"
        text "Stack Depth: {}".format(renpy.call_stack_depth())

