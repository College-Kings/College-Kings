screen v12s18_room1():
    tag free_roam

    imagemap:
        if not "bottle" in v12_slumberparty:
            idle "images/v12/scene 18/Screens/v12s18Room1.webp"
            hover "images/v12/scene 18/Screens/v12s18Room1Hover.webp"

            hotspot (182, 174, 1495, 906) action Jump("v12s18_bottlespin") # Play spin the bottle with the girls sitting on the floor
            
        else:
            idle "images/v12/scene 18/Screens/v12s18Room1a.webp" # Nora no longer sitting on the floor
            hover "images/v12/scene 18/Screens/v12s18Room1aHover.webp"

            hotspot (182, 174, 1495, 691) action Call("free_roam_spoken_too", "v12/scene 18/Screens/v12s18Room1a.webp", "v12s18_room1") # Already played with the girls

        hotspot (0, 30, 126, 1020) action Show("v12s18_room2") # Room 2


screen v12s18_room2():
    tag free_roam

    imagemap:
        idle "images/v12/scene 18/Screens/v12s18Room2.webp"
        hover "images/v12/scene 18/Screens/v12s18Room2Hover.webp"

        if not "fmk" in v12_slumberparty:
            hotspot (849, 70, 477, 759) action Jump("v12s18_fmk") # Play Fuck, Marry, Kill
        else:
            hotspot (849, 70, 477, 759) action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v12s18_bet")]) # End freeroam

        hotspot (1793, 30, 126, 1020) action Show("v12s18_room1") # Room 1