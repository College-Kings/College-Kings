label free_roam_spoken_too(background_image, return_screen, dialog="I should probably talk to someone else."):
    scene expression background_image
    u "[dialog]"
    scene black
    $ renpy.call_screen(return_screen)