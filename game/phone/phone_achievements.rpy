screen achievements_home():
    tag phone_tag

    default image_path = "images/phone/achievements/app-assets/"
    
    use base_phone:
        frame:
            background image_path + "achievement-background.webp"

            viewport:
                ysize 710
                ypos 134
                mousewheel True
                draggable True

                vbox:
                    xalign 0.5
                    spacing -40

                    for ach in achievements:
                        frame:
                            xsize 415
                            ypadding 35
                            xalign 0.5

                            if achievement.has(ach.achievement):
                                background "achievement_unlocked"

                                vbox:
                                    pos (50, -2)

                                    text ach.display_name.upper() style "achievement_name"
                                    text ach.text style "achievement_text"
                                
                            else:
                                background "achievement_locked"

                                text ach.display_name.upper() style "achievement_locked_name" pos (50, -2)


style achievement_name is text:
    color "#fff"
    font "fonts/Montserrat-ExtraBold.ttf"
    size 18

style achievement_text is text:
    color "#fff"
    font "fonts/Montserrat-SemiBold.ttf"
    size 15

style achievement_locked_name is text:
    color "#777"
    font "fonts/Montserrat-ExtraBold.ttf"
    size 18
