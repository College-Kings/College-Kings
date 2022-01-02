screen v13s37_garden1():
    tag free_roam

    imagemap:
        idle "images/v13/Scene 37/Garden Free Roam.webp"
        hover "images/v13/Scene 37/garden_hover.webp"

        hotspot (218, 301, 226, 301) action Show("endFreeRoamConfirm", continueLabel="v13s37_end")

        if not "chris" in freeroam11:
            hotspot (531, 318, 309, 408) action Jump("v13s37_chris")

        if not "nora" in freeroam11:
            hotspot (1560, 209, 360, 453) action Jump("v13s37_nora")
