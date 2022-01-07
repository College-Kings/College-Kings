init python:
    statsInfos = []

    class StatsInfo:
        def __init__(self, title, info, textColor):
            self.title = title
            self.info = info
            self.textColor = textColor

            statsInfos.append(self)

    StatsInfo("Popular", "Popular individuals are loved by the crowd and are often considered for important decisions. They prioritize their image and status over helping others.", "#53d769")
    StatsInfo("Loyal", "Loyal individuals care about other people and gain trust easily. They are known to be responsible, but can be a bit of a buzzkill when it comes to doing crazy stuff.", "#fecb2e")
    StatsInfo("Confident", "Confident individuals don’t rely on others to join them in their actions. They don’t crave their friends' approval, however they can be perceived as egotistical.", "#fc3d39")

screen stats():
    tag phone_tag
    zorder 200

    use base_phone:

        add "images/phone/white_background.webp" at truecenter

        text "This is your current Key Character Trait.\nIt's based on your choices & behavior.\nYou can only have one KCT at a time.":
            xpos 250
            ypos 150
            font "fonts/OpenSans.ttf"
            size 25
            color "#ffffff"

        add "images/phone/stats/appAssets/stats_circle.webp":
            xpos 520
            ypos 255

        add "images/phone/stats/appAssets/kct_diagram.webp":
            yalign 0.5
            xalign 0.05

        add "images/phone/stats/appAssets/tutback.webp":
            yalign 0.5
            xpos 1200

        text "KCT":
            xalign 0.5
            yalign 0.23
            font "fonts/Freshman.ttf"
            size 80
            color "#000000"

        ## Stats Info
        text statsInfos[statsPage - 1].title:
            style "statstitle"
            color statsInfos[statsPage - 1].textColor
            xalign 0.8

        text statsInfos[statsPage - 1].info style "statstext"

        fixed:
            xysize(650, 85)
            pos(1200, 550)

            hbox:
                align(0.5, 0.5)
                spacing 150

                imagebutton:
                    idle "images/whitearrowleft.webp"
                    if statsPage > 1:
                        action SetVariable("statsPage", statsPage - 1)
                    else:
                        action SetVariable("statsPage", 3)

                imagebutton:
                    idle "images/whitearrowright.webp"
                    if statsPage < 3:
                        action SetVariable("statsPage", statsPage + 1)
                    else:
                        action SetVariable("statsPage", 1)

        ## Current KCT
        vbox:
            pos (775, 380)
            spacing 80

            text "1.":
                font "fonts/Freshman.ttf"
                color "#000000"
                size 50
            text "2.":
                font "fonts/Freshman.ttf"
                size 50
                color "#000000"
            text "3.":
                font "fonts/Freshman.ttf"
                size 50
                color "#000000"

        vbox:
            align (0.5, 0.5)
            spacing 80

            text sortedKCT[0].capitalize():
                text_align 0.0
                font "fonts/Freshman.ttf"
                size 50
                if sortedKCT[0] == "popular":
                    color "#53d769" 
                elif sortedKCT[0] == "loyal":
                    color "#fecb2e"
                else:
                    color "#fc3d39"

            text sortedKCT[1].capitalize():
                text_align 0.0
                font "fonts/Freshman.ttf"
                size 50
                if sortedKCT[1] == "popular":
                    color "#53d769" 
                elif sortedKCT[1] == "loyal":
                    color "#fecb2e"
                else:
                    color "#fc3d39"

            text sortedKCT[2].capitalize():
                text_align 0.0
                font "fonts/Freshman.ttf"
                size 50
                if sortedKCT[2] == "popular":
                    color "#53d769" 
                elif sortedKCT[2] == "loyal":
                    color "#fecb2e"
                else:
                    color "#fc3d39"

style statstitle is text:
    font "fonts/Freshman.ttf"
    size 35
    text_align 0.5
    ypos 360

style statstext is text:
    font "fonts/OpenSans.ttf"
    size 25
    color "#ffffff"
    text_align 0.5
    xpos 1260
    ypos 400
    xmaximum 550

style statstextnum is text:
    font "fonts/Freshman.ttf"
    size 25
    color "#ffffff"
    text_align 0.5
    xpos 1490
    ypos 430
