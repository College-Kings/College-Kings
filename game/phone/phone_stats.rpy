init python:
    statsInfos = []

    class StatsInfo:
        def __init__(self, title, info, textColor):
            self.title = title
            self.info = info
            self.textColor = textColor

            statsInfos.append(self)

    StatsInfo("Popular", "Popular individuals are loved by the crowd and are often considered for important decisions. They prioritize their image and status over helping others.", "#1C69B9")
    StatsInfo("Loyal", "Loyal individuals care about other people and gain trust easily. They are known to be responsible, but can be a bit of a buzzkill when it comes to doing crazy stuff.", "#DC9D05")
    StatsInfo("Confident", "Confident individuals don’t rely on others to join them in their actions. They don’t crave their friends' approval, however they can be perceived as egotistical.", "#be66a8")

screen stats():
    tag phone_tag
    zorder 200

    default image_path = "images/phone/stats/appAssets/"

    use base_phone:

        add Transform( image_path + "kct_background.webp" , zoom=0.25) at truecenter xoffset 2

        add Transform( image_path + "kct_diagram.webp", zoom=0.3334):
            yalign 0.5
            xalign 0.05

        add Transform(image_path + "kct_box.webp" , zoom=0.3334):
            xalign 0.975
            yalign 0.5

        ## Stats Info
        text statsInfos[statsPage - 1].title.upper():
            style "statstitle"
            if statsInfos[statsPage - 1].title == "Popular":
                xalign 0.8375
            elif statsInfos[statsPage - 1].title == "Confident":
                xalign 0.8525
            elif statsInfos[statsPage - 1].title == "Loyal":
                xalign 0.835

        text statsInfos[statsPage - 1].info style "statstext"

        fixed:
            xysize(650, 85)
            pos(1200, 525)

            hbox:
                align(0.5, 0.5)

                imagebutton:
                    idle Transform(image_path + "left_button_idle.webp", zoom=0.75)
                    hover Transform(image_path + "left_button_hover.webp", zoom=0.75)
                    if statsPage > 1:
                        action SetVariable("statsPage", statsPage - 1)
                    else:
                        action SetVariable("statsPage", 3)
                    xoffset -226

                imagebutton:
                    idle Transform(image_path + "right_button_idle.webp", zoom=0.75)
                    hover Transform(image_path + "right_button_hover.webp", zoom=0.75)
                    if statsPage < 3:
                        action SetVariable("statsPage", statsPage + 1)
                    else:
                        action SetVariable("statsPage", 1)
                    xoffset 294

        vbox:
            align (0.525, 0.30)
            spacing 40
                    

            if sortedKCT[0] == "popular":
                frame:
                    xsize 450
                    xoffset -15
                    padding (0, 10)
                    background Transform(image_path + "kct_popular.webp", xysize=(415, 125))

                    text "1. " + sortedKCT[0].upper() color "#fff" yoffset 30 xoffset 50

            elif sortedKCT[0] == "loyal":
                frame:
                    xsize 450
                    xoffset -15
                    padding (0, 10)
                    background Transform(image_path + "kct_loyal.webp", xysize=(415, 125))

                    text "1. " + sortedKCT[0].upper() color "#fff" yoffset 30 xoffset 50
            else:
                frame:
                    xsize 450
                    xoffset -15
                    padding (0, 10)
                    background Transform(image_path + "kct_confident.webp", xysize=(415, 125))

                    text "1. " + sortedKCT[0].upper() color "#fff" yoffset 30 xoffset 50

            if sortedKCT[1] == "popular":
                frame:
                    xsize 450
                    xoffset -15
                    padding (0, 10)
                    background Transform(image_path + "kct_disabled.webp", xysize=(415, 125))

                    text "2. " + sortedKCT[1].upper() color "#1C69B9" yoffset 30 xoffset 50

            elif sortedKCT[1] == "loyal":
                frame:
                    xsize 450
                    xoffset -15
                    padding (0, 10)
                    background Transform(image_path + "kct_disabled.webp", xysize=(415, 125))

                    text "2. " + sortedKCT[1].upper() color "#DC9D05" yoffset 30 xoffset 50
            else:
                frame:
                    xsize 450
                    xoffset -15
                    padding (0, 10)
                    background Transform(image_path + "kct_disabled.webp", xysize=(415, 125))

                    text "2. " + sortedKCT[1].upper() color "#be66a8" yoffset 30 xoffset 50

            if sortedKCT[2] == "popular":
                frame:
                    xsize 450
                    xoffset -15
                    padding (0, 10)
                    background Transform(image_path + "kct_disabled.webp", xysize=(415, 125))

                    text "3. " + sortedKCT[2].upper() color "#1C69B9" yoffset 30 xoffset 50

            elif sortedKCT[2] == "loyal":
                frame:
                    xsize 450
                    xoffset -15
                    padding (0, 10)
                    background Transform(image_path + "kct_disabled.webp", xysize=(415, 125))

                    text "3. " + sortedKCT[2].upper() color "#DC9D05" yoffset 30 xoffset 50
            else:
                frame:
                    xsize 450
                    xoffset -15
                    padding (0, 10)
                    background Transform(image_path + "kct_disabled.webp", xysize=(415, 125))

                    text "3. " + sortedKCT[2].upper() color "#be66a8" yoffset 30 xoffset 50

style statstitle is text:
    font "fonts/Syne-Bold.ttf"
    size 30
    text_align 0.5
    ypos 345
    color "#ffffff"

style statstext is text:
    font "fonts/Effra-Regular.ttf"
    size 25
    color "#ffffff"
    text_align 0.5
    xpos 1325
    ypos 485
    xmaximum 450
