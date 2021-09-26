screen v13s37_garden1():
    tag free_roam

    imagemap:
        idle "images/v13/Scene37/Garden Free Roam.webp"
        hover "images/v13/Scene37/garden_hover.webp"

        hotspot (218, 301, 226, 301) action Show("endFreeRoamConfirm", continueLabel="v13s37_end")

        if not v13s37_frchris:
            hotspot (531, 318, 309, 408) action Jump("v13s37_chris")

        if not v13s37_frnora:
            hotspot (1560, 209, 360, 453) action Jump("v13s37_nora")
