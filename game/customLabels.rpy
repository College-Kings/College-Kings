
label freeRoamSpokenToo(message="I should probably talk to someone else", backgroundImg, returnScreen):
    scene expression "[backgroundImg]"
    u "[message]"
    $ renpy.call_screen(returnScreen)