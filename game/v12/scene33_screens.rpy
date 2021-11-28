screen v12s33_sneak_off_overlay(sneak_label):
    imagebutton:
        idle "images/v12/Scene 33/Buttons/Sneak.webp"
        hover "images/v12/Scene 33/Buttons/SneakHover.webp"
        action Jump(sneak_label)
        pos (20, 800)


screen v12s33_three_doors():
    tag free_roam

    imagemap:
        idle "images/v12/Scene 33/Buttons/SaunaDoors.webp"
        hover "images/v12/Scene 33/Buttons/SaunaDoors_hover.webp"

        if not "door1" in v12_saunadoors:
            hotspot (219, 281, 265, 587) action Jump("v12s33_door1")
        
        if not "door2" in v12_saunadoors:
            hotspot (830, 283, 249, 583) action Jump("v12s33_door2")
        
        if not "door3" in v12_saunadoors:
            hotspot (1419, 284, 258, 580) action Jump("v12s33_door3")