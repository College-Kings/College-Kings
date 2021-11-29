screen achievements():
    tag phone_tag
    zorder 200
    
    use base_phone:
        add "phone_white_background" at truecenter

        text "Achievements":
            xalign 0.5
            ypos 200
            style "achievements_header"

        viewport:
            pos (780, 280)
            xysize (358, 600)
            mousewheel True
            draggable True

            vbox:
                spacing 10
                
                for ach in achievements:
                    if achievement.has(ach.achievement):
                        vbox:
                            spacing -10
                            background "#d4af37"

                            textbutton ach.display_name style "ach"
                            textbutton ach.text style "ach2"
                    else:
                        textbutton ach.display_name style "ach3"


style achievements_header is text:
    color "#000000"
    font "fonts/Freshman.ttf"
    size 45

style ach is button:
    background "#d4af37"
    xalign 0.5
    xsize 358

style ach_text is text:
    color "#ffffff"
    font "fonts/Freshman.ttf"
    size 30
    xoffset 10

style achievements_yellow is button:
    background "#d4af37"
    xalign 0.5
    xsize 358

style ach2_text is text:
    color "#ffffff"
    font "fonts/opensans.ttf"
    size 20
    xoffset 10

style achievements_grey is button:
    background "#dcdcdc"
    xalign 0.5
    xsize 358

style achievements_grey_text is text:
    color "#ffffff"
    font "fonts/Freshman.ttf"
    size 30
    xoffset 10