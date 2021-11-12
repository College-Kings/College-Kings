screen v14s47_car():
    tag free_roam

    imagemap:
        idle "images/v14/Scene 47/v14s47_Screen.webp"
        hover "images/v14/Scene 47/v14s47_screen_hover.webp"

        hotspot (126, 253, 499, 570) action Jump("v14s47_hood")
        hotspot (633, 769, 1042, 135) action Jump("v14s47_driver")
        hotspot (643, 197, 952, 83) action Jump("v14s47_passenger")
        hotspot (1620, 306, 190, 450) action Jump("v14s47_trunk")

        ## NEED TO ADD A CONTINUE/END BUTTON ##