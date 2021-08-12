screen v12s18_room1():
    tag freeRoam

    imagemap:
        if not v12s18_bottlespin_played:
            idle "images/v12/scene 18/Screens/v12s18Room1.webp"
            hover "images/v12/scene 18/Screens/v12s18Room1Hover.webp"

            hotspot (0, 0, 0, 0) action Jump("v12s18_riley") # Play spin the bottle with the girls sitting on the floor
            
            hotspot (0, 0, 0, 0) action Show("v12s18_room2") # Room 2

        else:
            idle "images/v12/scene 18/Screens/v12s18Room1a.webp" # Nora no longer sitting on the floor
            hover "images/v12/scene 18/Screens/v12s18Room1aHover.webp"

            hotspot (0, 0, 0, 0) action Call("freeRoamSpokenToo", backgroundImg="v12s18Room1a", returnScreen="v12s18_room1") # Already played with the girls

            hotspot (0, 0, 0, 0) action Show("v12s18_room2") # Room 2


screen v12s18_room2():
    tag freeRoam

    imagemap:
        idle "images/v12/scene 18/Screens/v12s18Room2.webp"
        hover "images/v12/scene 18/Screens/v12s18Room2Hover.webp"

        if not v12s18_fmk_played:
            hotspot (0, 0, 0, 0) action Jump("v12s18_fmk") # Play Fuck, Marry, Kill
        else:
            hotspot (0, 0, 0, 0) action Show("endFreeRoamConfirm", continueLabel="v12s18_bet") # End freeroam

        hotspot (246, 891, 1401, 188) action Show("v12s18_hallway1") # Room 1
