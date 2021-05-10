screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100

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


    if renpy.loadable("/bugTesting/bugTesting.rpy") and config.developer:
        hbox:
            style_prefix "quick"
            align (1.0, 1.0)

            textbutton "Scene Select":
                action Show("bugTesting_SceneSelect")

            textbutton "Cheats":
                action Show("bugTesting_cheatMenu")

        use typoNotesOverlay