screen v12s33_sneak_off_overlay(sneak_label):
    imagebutton:
        idle "images/v12/Scene 33/Buttons/Sneak.webp"
        hover "images/v12/Scene 33/Buttons/SneakHover.webp"
        action Jump(sneak_label)
        pos (20, 800)


screen v12s33_three_doors():
    tag freeRoam

    imagemap:
        idle "images/v12/Scene 33/Buttons/SaunaDoors.webp"
        hover "images/v12/Scene 33/Buttons/SaunaDoors_hover.webp"

        hotspot (219, 281, 265, 587) action Jump("v12s33_door1")
        hotspot (830, 283, 249, 583) action Jump("v12s33_door2")
        hotspot (1419, 284, 258, 580) action Jump("v12s33_door3")