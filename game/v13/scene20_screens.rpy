screen v13s20_room():
    tag free_roam

    imagemap:
        idle "images/v13/Scene 20/Screens/v13s20_room.webp"
        hover "images/v13/Scene 20/Screens/v13s20_room_hover.webp"

        hotspot (39, 81, 515, 773) action Show("v13s20_bathroom")

        hotspot (573, 434, 445, 420) action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v13s20_end")])

        if not "closet" in freeroam10:
            hotspot (1018, 103, 546, 711) action Jump("v13s20_closet")

    if config_debug:
        python:
            actions = []

            actions.append(Show("v13s20_bathroom"))
            actions.append(Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v13s20_end")]))

            if not "closet" in freeroam10:
                actions.append(Jump("v13s20_closet"))

        timer 0.1 action renpy.random.choice(actions)


screen v13s20_bathroom():
    tag free_roam

    imagemap:
        idle "images/v13/Scene 20/Screens/v13s20_bathroom.webp"
        hover "images/v13/Scene 20/Screens/v13s20_bathroom_hover.webp"
    
        if not "brush" in freeroam10:
            hotspot (1417, 303, 301, 224) action Jump("v13s20_toothbrush")

        if not "bleach" in freeroam10:
            hotspot (465, 630, 1103, 450) action Jump("v13s20_bleach")

        hotspot (307, 0, 1390, 284) action Show("v13s20_room")

    if config_debug:
        python:
            actions = []

            if not "brush" in freeroam10:
                actions.append(Jump("v13s20_toothbrush"))

            if not "bleach" in freeroam10:
                actions.append(Jump("v13s20_bleach"))

            actions.append(Show("v13s20_room"))

        timer 0.1 action renpy.random.choice(actions)