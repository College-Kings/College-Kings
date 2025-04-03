screen v11s23_entrance():
    tag free_roam

    if v11_pen_goes_europe:
        imagemap:
            idle "images/v11/scene 23/v11s23idle.webp"
            hover "images/v11/scene 23/v11s23entrancehover.webp"
            ground "images/v11/scene 23/v11s23entrance.webp"

            alpha False

            if not "riley" in freeroam8:
                hotspot (363, 403, 143, 367) action Jump("v11s23_riley1")# speak to riley
            else:
                hotspot (363, 403, 143, 367) action Call("free_roam_spoken_too", "v11s23entrance", "v11s23_entrance")
                
            hotspot (1593, 531, 231, 466) action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v11s23_freeroamend")]) # speak to Nora

            hotspot (287, 0, 1373, 186) action Show("v11s23_mid")
        
    else:
        imagemap:
            idle "images/v11/scene 23/v11s23idle.webp"
            hover "images/v11/scene 23/v11s23entrancehover.webp"
            ground "images/v11/scene 23/v11s23entrance_nopen.webp"

            alpha False

            if not "riley" in freeroam8:
                hotspot (363, 403, 143, 367) action Jump("v11s23_riley1")# speak to riley
            else:
                hotspot (363, 403, 143, 367) action Call("free_roam_spoken_too", "v11s23entrance", "v11s23_entrance")
                
            hotspot (1593, 531, 231, 466) action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v11s23_freeroamend")]) # speak to Nora

            hotspot (287, 0, 1373, 186) action Show("v11s23_mid")

    if config_debug:
        python:
            actions = []

            if v11_pen_goes_europe:
                if not "riley" in freeroam8:
                    actions.append(Jump("v11s23_riley1")) # speak to riley
                    
                actions.append(Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v11s23_freeroamend")])) # speak to Nora

                actions.append(Show("v11s23_mid"))
                
            else:
                if not "riley" in freeroam8:
                    actions.append(Jump("v11s23_riley1")) # speak to riley

                actions.append(Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v11s23_freeroamend")])) # speak to Nora

                actions.append(Show("v11s23_mid"))

        timer 0.1 action renpy.random.choice(actions)


screen v11s23_mid():
    tag free_roam

    imagemap:
        idle "images/v11/scene 23/v11s23idle.webp"
        hover "images/v11/scene 23/v11s23midhover.webp"
        ground "images/v11/scene 23/v11s23mid.webp"

        alpha False

        if not "chris" in freeroam8:
            hotspot (1118, 72, 135, 208) action Jump("v11s23_chris1")# speak to chris
        else:
            hotspot (1118, 72, 135, 208) action Call("free_roam_spoken_too", "v11s23mid", "v11s23_mid")
        if not "lee" in freeroam8:
            hotspot (117, 355, 213, 431) action Jump("v11s23_mrlee1")# speak to Mr. Lee
        else:
            hotspot (117, 355, 213, 431) action Call("free_roam_spoken_too", "v11s23mid", "v11s23_mid")

        hotspot (316, 879, 1243, 200) action Show("v11s23_entrance")

        if v11_pen_goes_europe:
            hotspot (1637, 171, 280, 846) action Show("v11s23_helm")

    if config_debug:
        python:
            actions = []

            if not "chris" in freeroam8:
                actions.append(Jump("v11s23_chris1")) # speak to chris

            if not "lee" in freeroam8:
                actions.append(Jump("v11s23_mrlee1")) # speak to Mr. Lee

            actions.append(Show("v11s23_entrance"))

            if v11_pen_goes_europe:
                actions.append(Show("v11s23_helm"))

        timer 0.1 action renpy.random.choice(actions)


screen v11s23_helm():
    tag free_roam

    imagemap:
        idle "images/v11/scene 23/v11s23idle.webp"
        hover "images/v11/scene 23/v11s23helmhover.webp"
        ground "images/v11/scene 23/v11s23helm.webp"

        alpha False

        if not "penelope" in freeroam8:
            hotspot (936, 342, 272, 585) action Jump("v11s23_penelope1")# speak to penelope
        else:
            hotspot (936, 342, 272, 585) action Call("free_roam_spoken_too", "v11s23helm", "v11s23_helm")

        hotspot (423, 958, 1096, 120) action Show("v11s23_mid")

    if config_debug:
        python:
            actions = []

            if not "penelope" in freeroam8:
                actions.append(Jump("v11s23_penelope1")) # speak to penelope

            actions.append(Show("v11s23_mid"))

        timer 0.1 action renpy.random.choice(actions)
