screen achievements():
    tag phone_tag
    zorder 200

    default image_path = "images/phone/achievements/appAssets/"
    
    use base_phone:
        
        add Transform("images/phone/achievements/appAssets/ach_background.webp", zoom=0.25) at truecenter xoffset 2

        viewport:
            xysize (450, 640)
            pos (770, 246)
            mousewheel True
            draggable True

            vbox:
                spacing 20
                yminimum 100
                ymaximum 150
                
                for ach in achievements:

                    if achievement.has(ach.achievement):
                        frame:
                            xsize 450
                            xoffset -15
                            padding (10, 10)
                            background Transform(image_path + "ach_unlocked.webp", xysize=(415, 115))

                            vbox:
                                
                                text ach.display_name.upper() style "achievements_display_name" yoffset 25 xoffset 50
                                text ach.text.upper() style "achievements_text" yoffset 25 xoffset 50 xmaximum 310
                    else:
                        frame:
                            xsize 450 
                            xoffset -15
                            padding (10, 10)
                            background Transform(image_path + "ach_locked.webp", xysize=(415, 115))

                            vbox:

                                text ach.display_name.upper() style "achievements_display_name_locked" yoffset 25 xoffset 50
                                text "ACHIEVEMENT LOCKED" style "achievement_locked_text" yoffset 25 xoffset 50


style achievements_display_name is text:
    color "#ffffff"
    font "fonts/Montserrat-Bold.ttf"
    size 18

style achievements_display_name_locked is text:
    color "#555555"
    font "fonts/Montserrat-Bold.ttf"
    size 18

style achievements_text is text:
    color "#ffffff"
    font "fonts/Montserrat-SemiBold.ttf"
    size 14
style achievement_locked_text is text:
    color "#555555"
    font "fonts/Montserrat-SemiBold.ttf"
    size 14