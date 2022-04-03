transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

transform achievementShow:
    ypos -200
    linear 0.5 xpos 0 ypos 0
    2.0
    linear 0.5 xpos 0 ypos -200
    