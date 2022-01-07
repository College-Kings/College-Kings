screen v14s47_car():
    tag free_roam

    default finished_button_hover = False

    imagemap:
        idle "images/v14/Scene 47/v14s47_Screen.webp"
        hover "images/v14/Scene 47/v14s47_screen_hover.webp"

        hotspot (126, 253, 499, 570):
            if not "v14s47_hood_2.webp" in v14s47_car_pics and not "v14s47_hood_2b.webp" in v14s47_car_pics:
                action Jump("v14s47_hood")
        hotspot (633, 769, 1042, 135):
            if not "v14s47_driver_2c.webp" in v14s47_car_pics and not "v14s47_driver_2e.webp" in v14s47_car_pics:
                action Jump("v14s47_driver")
        hotspot (643, 197, 952, 83):
            if not ("v14s47_passenger_2b.webp" in v14s47_car_pics or "v14s47_passenger_2e.webp" in v14s47_car_pics) and not ("v14s47_passenger_2l.webp" in v14s47_car_pics or "v14s47_passenger_2f.webp" in v14s47_car_pics):
                action Jump("v14s47_passenger")
        hotspot (1620, 306, 190, 450):
            if not "v14s47_trunk_2b.webp" in v14s47_car_pics and not "v14s47_trunk_2c.webp" in v14s47_car_pics:
                action Jump("v14s47_trunk")

    if len(v14s47_car_pics) >= 1:
        button:
            xalign 0.5
            ypos 833
            minimum (500, 100)
            idle_background "choice_button_idle"
            hover_background "choice_button_hover"
            action Jump("v14s47_end")

            text "FINISH" align (0.5, 0.5)