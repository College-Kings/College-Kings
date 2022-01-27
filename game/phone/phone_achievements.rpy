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
                spacing 15
                
                for ach in achievements:

                    if achievement.has(ach.achievement):
                        frame:
                            xsize 450
                            xoffset -15
                            padding (0, 10)
                            background Transform(image_path + "ach_unlocked.webp", xysize=(415, 125))

                            vbox:
                                
                                text ach.display_name.upper() style "achievements_display_name" yoffset 25 xoffset 50
                                text ach.text.upper() style "achievements_text" yoffset 25 xoffset 50
                    else:
                        frame:
                            xsize 450 
                            xoffset -15
                            padding (0, 10)
                            background Transform(image_path + "ach_locked.webp", xysize=(415, 100))

                            text ach.display_name.upper() style "achievements_display_name_locked" yoffset 25 xoffset 50


style achievements_display_name is text:
    color "#ffffff"
    font "fonts/Montserrat-Bold.ttf"
    size 22

style achievements_display_name_locked is text:
    color "#777777"
    font "fonts/Montserrat-Bold.ttf"
    size 22

style achievements_text is text:
    color "#ffffff"
    font "fonts/Montserrat-SemiBold.ttf"
    size 16