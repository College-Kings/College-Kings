screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if fantasy == 1:
        image "images/fantasyoverlay.webp"

    if wton == True:

        if wt == 1:

            image "images/tutback.webp":
                ypos -385
                xpos 20
            vbox xpos 30  ypos 40 spacing 20:

                text "Walkthrough" style "wttextnum" xoffset 180
                text "2. reply: +1 troublemaker (needed for Confident & Popular). Neither option cuts off Emily's path."  style "wttext" xoffset 10

        if wt == 2:

            image "images/tutback.webp":
                ypos -385
                xpos 20
            vbox xpos 30  ypos 40 spacing 20:

                text "Walkthrough" style "wttextnum" xoffset 180
                text "Choice 1: +1 troublemaker (needed for Confident & Popular). Choice 2: +1 boyfriend (needed for Loyal & Confident)"  style "wttext" xoffset 10

        if wt == 3:

            image "images/tutback.webp":
                ypos -385
                xpos 20
            vbox xpos 30  ypos 40 spacing 20:

                text "Walkthrough" style "wttextnum" xoffset 180
                text "Open your phone to get a detailed breakdown of the stats system in the stats app."  style "wttext" xoffset 10



    if quick_menu:

        
        if realmode == True:
            if ischoice == False:
                hbox:
                    style_prefix "quick"

                    xalign 0.5
                    yalign 1.0

                    textbutton _("History") action ShowMenu('history')
                    textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                    textbutton _("Auto") action Preference("auto-forward", "toggle")
                    textbutton _("Save") action ShowMenu('save')
                    textbutton _("Q.Save") action QuickSave()
                    textbutton _("Q.Load") action QuickLoad()
                    textbutton _("Prefs") action ShowMenu('preferences')



        else:

            if quick_menu:
                hbox:
                    style_prefix "quick"

                    xalign 0.5
                    yalign 1.0
                    textbutton _("Back") action Rollback()
                    textbutton _("History") action ShowMenu('history')
                    textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                    textbutton _("Auto") action Preference("auto-forward", "toggle")
                    textbutton _("Save") action ShowMenu('save')
                    textbutton _("Q.Save") action QuickSave()
                    textbutton _("Q.Load") action QuickLoad()
                    textbutton _("Prefs") action ShowMenu('preferences')



        if showphone: # Edited
            imagebutton:
                if any([application.notification for application in applications]):
                    idle "images/phoneiconnot.webp"
                else:
                    idle "images/phoneicon.webp"
                yalign 0.05
                xalign 0.999
                action Jump ("homescreen")



        if freeroamtut == 1:

            image "images/tutback.webp":
                ypos 100 #+300
                xpos 1240 #+260

            imagebutton:
                idle "images/whitearrowleft.webp"
                hover "images/whitearrowleft.webp"
                ypos 720
                xpos 1260
                if freeroamtutpage > 1:
                    action SetVariable("freeroamtutpage", freeroamtutpage -1)
                else:
                    action SetVariable("freeroamtutpage", 3)

            imagebutton:
                idle "images/whitearrowright.webp"
                hover "images/whitearrowright.webp"
                ypos 720
                xpos 1740
                if freeroamtutpage < 3:
                    action SetVariable("freeroamtutpage", freeroamtutpage +1)
                else:
                    action SetVariable("freeroamtutpage", 1)

            text "Tutorial" style "choicetextnum" ypos 530 xpos 1490

            if freeroamtutpage == 1:
                text "At certain parts of the game, you’ll unlock free roam."  style "choicetuttext"
                text "1 of 3" style "choicetextnum"
            if freeroamtutpage == 2:
                text "During free roam, you choose where you go and who you want to talk to next." style "choicetuttext"
                text "2 of 3" style "choicetextnum"
            if freeroamtutpage == 3:
                text "You will also be able to use your phone and you might just find some hidden content." style "choicetuttext"
                text "3 of 3" style "choicetextnum"

    if stance == 1:

        if firstfight == True:
            image "images/background.webp"


            text "[w]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 2:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.122
                yalign 0.3
            text "[q]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 1:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.02
                yalign 0.5
            text "[e]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 3:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.235
                yalign 0.5
            text "[r]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 4:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.122
                yalign 0.7

            imagebutton:
                idle "images/jab.webp"
                hover "images/jab.webp"
                xalign 0.06
                yalign 0.5

            imagebutton:
                idle "images/hook.webp"
                hover "images/hook.webp"
                xalign 0.115
                yalign 0.4


            imagebutton:
                idle "images/kick.webp"
                hover "images/kick.webp"
                xalign 0.115
                yalign 0.61
        else:

            image "images/background.webp"


            text "[w]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 2:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.122
                yalign 0.3
            text "[q]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 1:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.02
                yalign 0.5
            text "[e]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 3:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.235
                yalign 0.5
            text "[r]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 4:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.122
                yalign 0.7

            imagebutton:
                idle "images/jab.webp"
                hover "images/jab.webp"
                xalign 0.06
                yalign 0.5

            imagebutton:
                idle "images/hook.webp"
                hover "images/hook.webp"
                xalign 0.115
                yalign 0.4


            imagebutton:
                idle "images/kick.webp"
                hover "images/kick.webp"
                xalign 0.115
                yalign 0.61

            imagebutton:
                idle "images/body.webp"
                hover "images/body.webp"
                xalign 0.172
                yalign 0.5



    if stance == 2:
        if firstfight == True:
            image "images/background.webp"

            text "[w]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 2:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.122
                yalign 0.3
            text "[q]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 1:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.02
                yalign 0.5
            text "[e]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 3:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.235
                yalign 0.5
            text "[r]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 4:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.122
                yalign 0.7

            imagebutton:
                idle "images/hookblock.webp"
                hover "images/hookblock.webp"
                xalign 0.06
                yalign 0.5

            imagebutton:
                idle "images/jabblock.webp"
                hover "images/jabblock.webp"
                xalign 0.115
                yalign 0.4

            imagebutton:
                idle "images/kickblock.webp"
                hover "images/kickblock.webp"
                xalign 0.115
                yalign 0.6
        else:
            image "images/background.webp"

            text "[w]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 2:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.122
                yalign 0.3
            text "[q]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 1:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.02
                yalign 0.5
            text "[e]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 3:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.235
                yalign 0.5
            text "[r]":
                font "fonts/freshman.ttf"
                size 100
                if hl == 4:
                    color "#d10000"
                else:
                    color "#FFD166"
                xalign 0.122
                yalign 0.7

            imagebutton:
                idle "images/hookblock.webp"
                hover "images/hookblock.webp"
                xalign 0.06
                yalign 0.5

            imagebutton:
                idle "images/jabblock.webp"
                hover "images/jabblock.webp"
                xalign 0.115
                yalign 0.4

            imagebutton:
                idle "images/kickblock.webp"
                hover "images/kickblock.webp"
                xalign 0.115
                yalign 0.6
            imagebutton:
                idle "images/bodyblock.webp"
                hover "images/bodyblock.webp"
                xalign 0.172
                yalign 0.5


    if youdmg == 3:
        image "images/3 hits.webp"
    if youdmg == 4:
        image "images/4 hits.webp"
    if youdmg >= 5:
        image "images/5 hits.webp"


    if renpy.loadable("/bugTesting/bugTesting.rpy") and developer:
        hbox:
            style_prefix "quick"
            align (1.0, 1.0)

            textbutton "Scene Select":
                action Show("bugTesting_SceneSelect")

            textbutton "Cheats":
                action Show("bugTesting_cheatMenu")

        use typoNotesOverlay
