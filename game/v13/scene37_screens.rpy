screen v13s37_garden1():
    tag free_roam

    imagemap:
        idle "images/v13/Scene 37/Garden Free Roam.webp"
        hover "images/v13/Scene 37/garden_hover.webp"

        if "nora" in freeroam11 and "chris" in freeroam11:
            hotspot (218, 301, 226, 301) action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v13s37_end")])
        else:
            hotspot (218, 301, 226, 301) action Call("freeRoamSpokenToo", backgroundImg="images/v13/Scene 37/Garden Free Roam.webp", returnScreen="v13s37_garden1")

        if not "chris" in freeroam11:
            hotspot (531, 318, 309, 408) action Jump("v13s37_chris")

        if not "nora" in freeroam11:
            hotspot (1560, 209, 360, 453) action Jump("v13s37_nora")
