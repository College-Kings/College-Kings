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
                    frame:
                        xsize 358
                        padding (15, 5)

                        if achievement.has(ach.achievement):
                            background "#d4af37"

                            vbox:
                                text ach.display_name style "achievements_display_name"
                                text ach.text style "achievements_text"
                        else:
                            background "#dcdcdc"

                            text ach.display_name style "achievements_display_name"


style achievements_header is text:
    color "#000000"
    font "fonts/Freshman.ttf"
    size 45

style achievements_display_name is text:
    color "#ffffff"
    font "fonts/Freshman.ttf"
    size 30

style achievements_text is text:
    color "#ffffff"
    font "fonts/opensans.ttf"
    size 20