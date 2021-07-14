screen achievements():
    tag phoneTag
    zorder 200
    
    use phoneTemplate:

        add "images/phone/whiteBackground.webp" at truecenter

        text "achievements":
            color "#000000"
            font "fonts/Freshman.ttf"
            size 45
            ypos 200
            xalign 0.5

        viewport:
            pos (780, 280)
            xysize (358, 600)
            mousewheel True
            draggable True

            vbox:
                spacing 10
                
                for achievement in achievements:
                    if achievement.checkCondition():
                        vbox:
                            spacing -10
                            
                            textbutton achievement.achieve.replace("_", " ") style "ach"
                            textbutton achievement.text style "ach2"
                    else:
                        textbutton achievement.achieve.replace("_", " ") style "ach3"


style ach is button:
    background "#d4af37"
    xalign 0.5
    xsize 358
    ysize 50

style ach_text is text:
    color "#ffffff"
    font "fonts/Freshman.ttf"
    size 30
    xoffset 10

style ach2 is button:
    background "#d4af37"
    xalign 0.5
    xsize 358
    ysize 50

style ach2_text is text:
    color "#ffffff"
    font "fonts/opensans.ttf"
    size 20
    xoffset 10

style ach3 is button:
    background "#dcdcdc"
    xalign 0.5
    xsize 358
    ysize 50

style ach3_text is text:
    color "#ffffff"
    font "fonts/Freshman.ttf"
    size 30
    xoffset 10