label freeRoamSpokenToo(backgroundImg, returnScreen):
    scene expression backgroundImg
    u "I should probably talk to someone else."
    scene black
    $ renpy.call_screen(returnScreen)