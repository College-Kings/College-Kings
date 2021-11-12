screen v14s47_car():
    tag free_roam

    imagemap:
        idle "images/v14/Scene 47/v14s47_Screen.webp"
        hover "images/v14/Scene 47/v14s47_screen_hover.webp"

        hotspot (126, 253, 499, 570):
            if not v14s47_linds_hood and not v14s47_solo_hood:
                action Jump("v14s47_hood")
        hotspot (633, 769, 1042, 135):
            if not v14s47_linds_driver and not v14s47_solo_driver:
                action Jump("v14s47_driver")
        hotspot (643, 197, 952, 83):
            if not v14s47_linds_passenger and not v14s47_solo_passenger:
                action Jump("v14s47_passenger")
        hotspot (1620, 306, 190, 450):
            if v14_pics_no_linds and not v14s47_solo_trunk:
                action Jump("v14s47_trunk")
        if len(v14s47_car_pics) >= 1:
            button:
                align (0.5, 0.95)
                action Jump ("v14s47_end")
                maximum (707, 104)
                add "gui/center.webp"
                text "Finish" align (0.5, 0.5)