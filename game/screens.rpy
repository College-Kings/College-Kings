## Initialization
################################################################################

init offset = -1
init python:
    yadjValue = float("inf")
    yadj = ui.adjustment()



##################

############ DEV TOOLS





################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")
    outlines [ (2, "#000000") ]

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
    color "#ffffff"
    outlines [ (2, "#000000") ]


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice


screen choice(items, time=3):
    image "gui/curves.png"
    style_prefix "choice"

    timer 0.001 action SetVariable("ischoice", True)

    default menuButtonsConfig = {
        0: {
            "background": "Left",
            "pos": (210, 907),
            "padding": (50, 21)
        },
        1: {
            "background": "Right",
            "pos": (1005, 907),
            "padding": (90, 21)
        },
        2: {
            "background": "Top",
            "pos": (600, 780),
            "padding": (0, 21) # Centered
        }
    }
    
    for count, item in enumerate(items):
        
        ### Requires menu disable function from jwt.rpy
        $ disabled = False
        if "(disabled)" in item.caption:
            $ disabled = True

        if count < len(menuButtonsConfig):
            textbutton item.caption.replace(" (disabled)", ""):
                if disabled:
                    background "gui/{}white.png".format(menuButtonsConfig[count]["background"])
                else:
                    idle_background "gui/{}blue.png".format(menuButtonsConfig[count]["background"])
                    action [item.action, SetVariable("ischoice", False)]
                hover_background "gui/{}white.png".format(menuButtonsConfig[count]["background"])
                pos menuButtonsConfig[count]["pos"]
                padding  menuButtonsConfig[count]["padding"]
                xysize (800, 104)
                text_size 40
                if count > 1:
                    text_xalign 0.5


    if realkcttut == 1:

        image "images/tutback.png":
            ypos 100 #+300
            xpos 1240 #+260

        imagebutton:
            idle "images/whitearrowleft.png"
            hover "images/whitearrowleft.png"
            ypos 720
            xpos 1260
            if kctpage > 1:
                action SetVariable("kctpage", kctpage -1)
            else:
                action SetVariable("kctpage", 5)

        imagebutton:
            idle "images/whitearrowright.png"
            hover "images/whitearrowright.png"
            ypos 720
            xpos 1740
            if kctpage < 5:
                action SetVariable("kctpage", kctpage +1)
            else:
                action SetVariable("kctpage", 1)

        text "Tutorial" style "choicetextnum" ypos 530 xpos 1490

        if kctpage == 1:
            text "Your decisions strongly influence the way the story progresses and how other characters perceive you." style "choicetuttext"
            text "1 of 5" style "choicetextnum"
        if kctpage == 2:
            text "With each choice you’ll either gain Bro, Boyfriend or Troublemaker points." style "choicetuttext"
            text "2 of 5" style "choicetextnum"
        if kctpage == 3:
            text "Bros put the squad first, boyfriends show strong affinity towards a few selected individuals and troublemakers seek thrills and take risks." style "choicetuttext"
            text "3 of 5" style "choicetextnum"
        if kctpage == 4:
            text "These points are then used to identify your Key Character Trait (KCT).  Each KCT will unlock different possibilities and choices, but you can only have one active at a time." style "choicetuttext"
            text "4 of 5" style "choicetextnum"
        if kctpage == 5:
            text "You can read more about each individual KCT in the Stats app on your phone." style "choicetuttext"
            text "5 of 5" style "choicetextnum"


    if influencetut == True:

        image "images/tutback.png":
            ypos 100 #+300
            xpos 1240 #+260

        imagebutton:
            idle "images/whitearrowleft.png"
            hover "images/whitearrowleft.png"
            ypos 720
            xpos 1260
            if itpage > 1:
                action SetVariable("itpage", itpage -1)
            else:
                action SetVariable("itpage", 4)

        imagebutton:
            idle "images/whitearrowright.png"
            hover "images/whitearrowright.png"
            ypos 720
            xpos 1740
            if itpage < 4:
                action SetVariable("itpage", itpage +1)
            else:
                action SetVariable("itpage", 1)

        text "Tutorial" style "choicetextnum" ypos 530 xpos 1490

        if itpage == 1:
            text "When people make important decisions on how they feel about you, they consider what kind of a person you are." style "choicetuttext"
            text "1 of 4" style "choicetextnum"
        if itpage == 2:
            text "Your Key Character Trait (Loyal, Popular or Confident) has a strong influence on how other characters react to your behavior." style "choicetuttext"
            text "2 of 4" style "choicetextnum"
        if itpage == 3:
            text "Some people value a popular leader, some care more about loyalty than status and some are drawn to confidence." style "choicetuttext"
            text "3 of 4" style "choicetextnum"
        if itpage == 4:
            text "Your decisions matter and have long time effects, as you can only have one KCT at a time. So think about what kind of person you want to be." style "choicetuttext"
            text "4 of 4" style "choicetextnum"


    if showkct == True:
        image "gui/kct.png"
        text "[kct]":
            ypos 18
            #xalign 0.975
            xpos 1700
            text_align 0.5
            font "fonts/Freshman.ttf"
            size 40
            if kct == "popular":
                color "#53d769"
            if kct == "loyal":
                color "#fecb2e"
            if kct == "confident":
                color "#fc3d39"

    if timed == True:

        timer time repeat False action [ Hide('countdown'), Jump("choicetimer") ]
        bar value AnimatedValue(0, time, time, time) at alpha_dissolve # assuming you're using the alpha_dissolve transform from the wiki

style choicetuttext is text:
    font "fonts/OpenSans.ttf"
    size 25
    color "#ffffff"
    text_align 0
    xpos 1310
    ypos 570
    xmaximum 500

style choicetextnum is text:
    font "fonts/Freshman.ttf"
    size 25
    color "#FFD166"
    text_align 0.5
    xpos 1530
    ypos 740


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

#######'INGAME Menu#############




screen ingmenu():

    add "gui/savepage.png"

    if realmode == True:

        if ischoice == False:

            default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

            fixed:


                ## This ensures the input will get the enter event before any of the
                ## buttons do.
                order_reverse True

                ## The page name, which can be edited by clicking on a button.
                text "In Real-life mode, you only get one save.":
                    size 50
                    yalign 0.1
                    xalign 0.5



                ## The grid of file slots.
                grid 1 1:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.5

                    spacing gui.slot_spacing

                    for i in range(1 * 1):

                        $ slot = 1

                        button:
                            action FileAction(slot)

                            has vbox

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)

                ## Buttons to access other pages.
                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign 0.85

                    spacing gui.page_spacing

                hbox:
                    xalign 0.5
                    yalign 0.02
                    text "Save name: "
                    frame:
                        ymaximum 50
                        xmaximum 750
                        add "#444" # You can add a background image here if you want to
                        input:
                            xoffset 5
                            yoffset 5
                            default "[save_name]"
                            value VariableInputValue("save_name")
                            length 35 # Maximum length of the save name
                            size 25
                            allow " .,_-0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM" # The characters that can be used in the save name



            style_prefix "navigation"
            hbox:
                style_prefix "navigation"

                xalign 0.5
                yalign 0.95

                spacing gui.navigation_spacing
                xsize gui.navigation_width


                textbutton _("Return") action Return()



                textbutton _("Load") action ShowMenu("load")

                textbutton _("Settings") action ShowMenu("preferences")

                textbutton _("Menu") action MainMenu()


                textbutton _("Quit") action Quit(confirm=not main_menu)




        else:

            text "You've enabled Real Life Mode and are therefore unable to use this menu whilst making a choice." yalign 0.5 xalign 0.5
            hbox:
                style_prefix "navigation"

                xalign 0.05
                yalign 0.95



    else:

        default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

        fixed:


            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 0.85

                spacing gui.page_spacing

                textbutton _("←") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _("→") action FilePageNext()

            hbox:
                xalign 0.5
                yalign 0.05
                text "Save name: "
                frame:
                    ymaximum 50
                    xmaximum 750
                    add "#444" # You can add a background image here if you want to
                    input:
                        xoffset 5
                        yoffset 5
                        default "[save_name]"
                        value VariableInputValue("save_name")
                        length 35 # Maximum length of the save name
                        size 25
                        allow " .,_-0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM" # The characters that can be used in the save name


        style_prefix "navigation"
        hbox:
            style_prefix "navigation"

            xalign 0.5
            yalign 0.95

            spacing gui.navigation_spacing
            xsize gui.navigation_width

            textbutton _("Return") action Return()



            textbutton _("Load") action ShowMenu("load")

            textbutton _("Settings") action ShowMenu("preferences")

            textbutton _("Menu") action MainMenu()


            textbutton _("Quit") action Quit(confirm=not main_menu)





## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if fantasy == 1:
        image "images/fantasyoverlay.png"

    if wton == True:

        if wt == 1:

            image "images/tutback.png":
                ypos -385
                xpos 20
            vbox xpos 30  ypos 40 spacing 20:

                text "Walkthrough" style "wttextnum" xoffset 180
                text "2. reply: +1 troublemaker (needed for Confident & Popular). Neither option cuts off Emily's path."  style "wttext" xoffset 10

        if wt == 2:

            image "images/tutback.png":
                ypos -385
                xpos 20
            vbox xpos 30  ypos 40 spacing 20:

                text "Walkthrough" style "wttextnum" xoffset 180
                text "Choice 1: +1 troublemaker (needed for Confident & Popular). Choice 2: +1 boyfriend (needed for Loyal & Confident)"  style "wttext" xoffset 10

        if wt == 3:

            image "images/tutback.png":
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
                    idle "images/phoneiconnot.png"
                else:
                    idle "images/phoneicon.png"
                yalign 0.05
                xalign 0.999
                action Jump ("homescreen")



        if freeroamtut == 1:

            image "images/tutback.png":
                ypos 100 #+300
                xpos 1240 #+260

            imagebutton:
                idle "images/whitearrowleft.png"
                hover "images/whitearrowleft.png"
                ypos 720
                xpos 1260
                if freeroamtutpage > 1:
                    action SetVariable("freeroamtutpage", freeroamtutpage -1)
                else:
                    action SetVariable("freeroamtutpage", 3)

            imagebutton:
                idle "images/whitearrowright.png"
                hover "images/whitearrowright.png"
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
            image "images/background.png"


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
                idle "images/jab.png"
                hover "images/jab.png"
                xalign 0.06
                yalign 0.5

            imagebutton:
                idle "images/hook.png"
                hover "images/hook.png"
                xalign 0.115
                yalign 0.4


            imagebutton:
                idle "images/kick.png"
                hover "images/kick.png"
                xalign 0.115
                yalign 0.61
        else:

            image "images/background.png"


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
                idle "images/jab.png"
                hover "images/jab.png"
                xalign 0.06
                yalign 0.5

            imagebutton:
                idle "images/hook.png"
                hover "images/hook.png"
                xalign 0.115
                yalign 0.4


            imagebutton:
                idle "images/kick.png"
                hover "images/kick.png"
                xalign 0.115
                yalign 0.61

            imagebutton:
                idle "images/body.png"
                hover "images/body.png"
                xalign 0.172
                yalign 0.5



    if stance == 2:
        if firstfight == True:
            image "images/background.png"

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
                idle "images/hookblock.png"
                hover "images/hookblock.png"
                xalign 0.06
                yalign 0.5

            imagebutton:
                idle "images/jabblock.png"
                hover "images/jabblock.png"
                xalign 0.115
                yalign 0.4

            imagebutton:
                idle "images/kickblock.png"
                hover "images/kickblock.png"
                xalign 0.115
                yalign 0.6
        else:
            image "images/background.png"

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
                idle "images/hookblock.png"
                hover "images/hookblock.png"
                xalign 0.06
                yalign 0.5

            imagebutton:
                idle "images/jabblock.png"
                hover "images/jabblock.png"
                xalign 0.115
                yalign 0.4

            imagebutton:
                idle "images/kickblock.png"
                hover "images/kickblock.png"
                xalign 0.115
                yalign 0.6
            imagebutton:
                idle "images/bodyblock.png"
                hover "images/bodyblock.png"
                xalign 0.172
                yalign 0.5


    if youdmg == 3:
        image "images/3 hits.png"
    if youdmg == 4:
        image "images/4 hits.png"
    if youdmg >= 5:
        image "images/5 hits.png"

style wttext is text:
    font "fonts/OpenSans.ttf"
    size 25
    color "#ffffff"
    text_align 0
    xmaximum 620

style wttextnum is text:
    font "fonts/Freshman.ttf"
    size 35
    color "#FFD166"
    text_align 0.5

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    style_prefix "navigation"

    if main_menu:

        imagebutton:
            idle "images/play2.png"
            hover "images/play3.png"
            action Start ()
            xpos 79
            ypos 147

        imagebutton:
            idle "images/load2.png"
            hover "images/load3.png"
            action ShowMenu("load")
            xpos 759
            ypos 147

        imagebutton:
            idle "images/patreon2.png"
            hover "images/patreon4.png"
            action OpenURL ("https://www.patreon.com/collegekings")
            xpos 1401
            ypos 147

        imagebutton:
            idle "images/patreon2.png"
            hover "images/discord2.png"
            action OpenURL ("http://discord.collegekingsgame.com")
            xpos 1401
            if steam == False:
                ypos 417
            else:
                ypos 147 #steam version


        imagebutton:
            idle "images/settings2.png"
            hover "images/settings3.png"
            action ShowMenu("preferences")
            xpos 79
            ypos 457

        imagebutton:
            idle "images/quit2.png"
            hover "images/quit3.png"
            action Quit(confirm= main_menu)
            xpos 531
            ypos 457

        imagebutton:
            idle "images/scene2.png"
            hover "images/scene1.png"
            action Jump ("scenegal")
            xpos 79
            ypos 346

        imagebutton:
            idle "images/patreon2.png"
            hover "images/website3.png"
            action OpenURL("http://collegekingsgame.com")
            xpos 1401
            if steam == False:
                ypos 687
            else:
                ypos 592 #steam version



    else:

        hbox:
            style_prefix "navigation"

            xpos 270
            yalign 0.95

            spacing gui.navigation_spacing
            xsize gui.navigation_width

            textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")

            textbutton _("Settings") action ShowMenu("preferences")

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("Quit") action Quit(confirm=not main_menu)



style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    outlines [ (3, "#000000") ]


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    text "v" + config.version:
        color "#4e628f"
        size 30
        xalign 0.99
        yalign 0.99


    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"
                outlines [ (3, "#000000") ]

            text "[config.version]":
                style "main_menu_version"
                outlines [ (3, "#000000") ]


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True


style main_menu_vbox:
    xalign 0.5
    xoffset 0
    xmaximum 1200
    yalign 0.1
    yoffset 0

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):


    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    vbox xalign 0.05 yalign 0.58 spacing 200:
        textbutton _("Return"):
            style "return_button"

            action Return()
        textbutton _("Main Menu"):
            style "return_button"

            action MainMenu()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text


style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 50
    ysize 180

style game_menu_label_text:
    size 100
    color gui.accent_color
    yalign 1

style return_button:
    xpos gui.navigation_xpos
    yalign 0.5
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    modal True

    add "gui/savepage.png"

    tag menu

    use file_slots(_("Save"))


screen load():

    modal True

    add "gui/loadpage.png"

    tag menu

    use file_slots(_("Load"))



screen file_slots(title):



    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))



    vbox xalign 0.05 yalign 0.95:
        textbutton _("Return"):
            style "return_button"

            action Return()

    fixed:


        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on a button.
        button:
            style "page_label"

            key_events True
            xalign 0.5
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        hbox:
            style_prefix "page"

            xalign 0.5
            yalign 0.85

            spacing gui.page_spacing

            textbutton _("←") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto")

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick")

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 10):
                textbutton "[page]" action FilePage(page)

            textbutton _("→") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    add "gui/settingspage.png"

    modal True

    tag menu


    hbox xalign 0.1645 yalign 0.265 spacing 136:
        style_prefix "check"

        textbutton _("window") action Preference("display", "window"):
            text_size 45
        textbutton _("fullscreen") action Preference("display", "fullscreen"):
            text_size 45

    hbox xalign 0.122 yalign 0.468 spacing 35:
        style_prefix "check"
        textbutton _("Unseen Text") action Preference("skip", "toggle"):
            text_size 28
        textbutton _("After Choices") action Preference("after choices", "toggle"):
            text_size 28
        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")):
            text_size 28


    hbox xalign 0.19 yalign 0.671 spacing 300:
        style_prefix "radio"
        if realmode == True:
            textbutton _("On") action Jump ("rmlon") text_color "#FFD166":
                text_size 45
            textbutton _("Off") action Jump ("rmloff"):
                text_size 45
        else:
            textbutton _("On") action Jump ("rmlon"):
                text_size 45
            textbutton _("Off") action Jump ("rmloff") text_color "#FFD166":
                text_size 45

    hbox xalign 0.19 yalign 0.874 spacing 300:
        style_prefix "radio"

        if showkct == True:
            textbutton _("On") action Jump ("showkcton") text_color "#FFD166":
                text_size 45
            textbutton _("Off") action Jump ("showkctoff"):
                text_size 45
        else:
            textbutton _("On") action Jump ("showkcton"):
                text_size 45
            textbutton _("Off") action Jump ("showkctoff") text_color "#FFD166":
                text_size 45




        #    hbox spacing 20:
        #        style_prefix "radio"
        #        label _("Allow Rollback")
        #        if config.rollback_enabled == True:
        #            textbutton _("True") action Jump ("rollbacktrue") text_color "#FFD166"
        #            textbutton _("False") action Jump ("rollbackfalse")
        #        else:
        #            textbutton _("True") action Jump ("rollbacktrue")
        #            textbutton _("False") action Jump ("rollbackfalse") text_color "#FFD166"

            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.




    style_prefix "slider"




    bar value Preference("text speed"):
        xpos 1020
        ypos 330


    bar value Preference("auto-forward time"):
        xpos 1020
        ypos 480


    if config.has_music:



        bar value Preference("music volume"):
            xpos 1020
            ypos 742

    if config.has_sound:



        bar value Preference("sound volume"):
            xpos 1020
            ypos 892


    hbox xpos 1500 ypos 1015:


        textbutton _("Return"):
            style "return_button"
            action Return ()

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            viewport:
                yoffset -200
                ysize 100

                ## This lays things out properly if history_height is None.

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text:
    size 50

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize 20

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "fonts/OpenSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"


style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900

#######################
screen stats():

        add "images/phonescreen.png" at truecenter

        add "images/stats.png" at truecenter
        if noexit == False:
            textbutton "Exit Phone" action Jump("exitphone") style"phonebutton"

        image "images/tutback.png":
            yalign 0.5
            xpos 1200

        image "images/KCTdiagram.png":
            yalign 0.5
            xalign 0.05

        imagebutton:
            idle "images/whitearrowleft.png"
            hover "images/whitearrowleft.png"
            yalign 0.55
            xpos 1220
            if statspage > 1:
                action SetVariable("statspage", statspage -1)
            else:
                action SetVariable("statspage", 3)

        imagebutton:
            idle "images/whitearrowright.png"
            hover "images/whitearrowright.png"
            yalign 0.55
            xpos 1700
            if statspage < 3:
                action SetVariable("statspage", statspage +1)
            else:
                action SetVariable("statspage", 1)

        text "KCT":
            xalign 0.5
            yalign 0.23
            font "fonts/Freshman.ttf"
            size 80
            color "#000000"

        text "This is your current Key Character Trait.\nIt's based on your choices & behavior.\nYou can only have one KCT at a time.":
            xpos 250
            ypos 150
            font "fonts/OpenSans.ttf"
            size 25
            color "#ffffff"

        image "images/statscircle.png":
            xpos 520
            ypos 273

        vbox:
            if statspage == 1:
                text "Popular" style "statstitle":
                    color "#53d769"
                    xpos 1417
                text "Popular individuals are loved by the crowd and are often considered for important decisions. They prioritize their image and status over helping others." style "statstext"
                text "1 of 3" style "statstextnum"

            if statspage == 2:
                text "Loyal" style "statstitle":
                    color "#fecb2e"
                    xpos 1442
                text "Loyal individuals care about other people and gain trust easily. They are known to be responsible, but can be a bit of a buzzkill when it comes to doing crazy stuff." style "statstext"
                text "2 of 3" style "statstextnum"

            if statspage == 3:
                text "Confident" style "statstitle":
                    color "#fc3d39"
                    xpos 1420
                text "Confident individuals don’t rely on others to join them in their actions. They don’t crave their friends' approval, however they can be perceived as egotistical." style "statstext"
                text "3 of 3" style "statstextnum"


        vbox xpos 780 ypos 400 spacing 80:
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

        vbox xalign 0.5 yalign 0.5 spacing 80:
            if [popular] >= [loyal] >= [confident]:
                text "Popular":
                    text_align 0.0
                    color "#53d769"
                    font "fonts/Freshman.ttf"
                    size 50

                text "Loyal":
                    text_align 0.0
                    color "#fecb2e"
                    font "fonts/Freshman.ttf"
                    size 50

                text "Confident":
                    text_align 0.0
                    color "#fc3d39"
                    font "fonts/Freshman.ttf"
                    size 50

            if [popular] >= [confident] > [loyal]:
                vbox xpos 25 ypos 17 spacing 80:

                    text "Popular":
                        text_align 0.0
                        color "#53d769"
                        font "fonts/Freshman.ttf"
                        size 50

                    text "Confident":
                        text_align 0.0
                        color "#fc3d39"
                        font "fonts/Freshman.ttf"
                        size 50

                    text "Loyal":
                        text_align 0.0
                        color "#fecb2e"
                        font "fonts/Freshman.ttf"
                        size 50

            if [loyal] > [popular] >= [confident]:
                vbox xpos 25 ypos 17 spacing 80:
                    text "Loyal":
                        text_align 0.0
                        color "#fecb2e"
                        font "fonts/Freshman.ttf"
                        size 50

                    text "Popular":
                        text_align 0.0
                        color "#53d769"
                        font "fonts/Freshman.ttf"
                        size 50

                    text "Confident":
                        text_align 0.0
                        color "#fc3d39"
                        font "fonts/Freshman.ttf"
                        size 50

            if [loyal] >= [confident] > [popular]:
                vbox xpos 25 ypos 17 spacing 80:
                    text "Loyal":
                        text_align 0.0
                        color "#fecb2e"
                        font "fonts/Freshman.ttf"
                        size 50

                    text "Confident":
                        text_align 0.0
                        color "#fc3d39"
                        font "fonts/Freshman.ttf"
                        size 50

                    text "Popular":
                        text_align 0.0
                        color "#53d769"
                        font "fonts/Freshman.ttf"
                        size 50



            if [confident] > [loyal] > [popular]:
                vbox xpos 25 ypos 17 spacing 80:

                    text "Confident":
                        text_align 0.0
                        color "#fc3d39"
                        font "fonts/Freshman.ttf"
                        size 50

                    text "Loyal":
                        text_align 0.0
                        color "#fecb2e"
                        font "fonts/Freshman.ttf"
                        size 50

                    text "Popular":
                        text_align 0.0
                        color "#53d769"
                        font "fonts/Freshman.ttf"
                        size 50

            if [confident] > [popular] >= [loyal]:
                vbox xpos 25 ypos 17 spacing 80:

                    text "Confident":
                        text_align 0.0
                        color "#fc3d39"
                        font "fonts/Freshman.ttf"
                        size 50

                    text "Popular":
                        text_align 0.0
                        color "#53d769"
                        font "fonts/Freshman.ttf"
                        size 50

                    text "Loyal":
                        text_align 0.0
                        color "#fecb2e"
                        font "fonts/Freshman.ttf"
                        size 50


style statstitle is text:
    font "fonts/Freshman.ttf"
    size 35
    text_align 0.5
    ypos 380

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


screen freeroam1a():
    add "images/s50.jpg"
    imagebutton:
        yalign 0.12
        xalign 0.86
        idle "images/fr1riley.png"
        hover "images/fr1rileyhover.png"

        if fr1riley == 0:
            action Jump ("fr1riley1")

        else:
            action Jump ("fr1riley2")
    imagebutton:
        yalign 0.195
        xalign 0.335
        idle "images/fr1elijah.png"
        hover "images/fr1elijahoverh.png"

        if fr1elijah == 0:
            action Jump ("fr1elijah1")

        else:
            action Jump ("fr1elijah2")

    imagebutton:
        yalign 0.07
        xalign 0.65
        idle "images/fr1b.png"
        hover "images/fr1bhover.png"
        action Jump ("fr1b")

screen freeroam1b():
    add "images/s55.jpg"
    imagebutton:
        yalign 0.5
        xalign 0.685
        idle "images/fr1chris.png"
        hover "images/fr1chrishover.png"
        action Jump ("fr1chris1")

    imagebutton:
        yalign 0.38
        xalign 0.21
        idle "images/fr1c.png"
        hover "images/fr1chover.png"
        action Jump ("fr1c")

    imagebutton:
        yalign 1.0
        xalign 0.23
        idle "images/backchris.png"
        hover "images/backchrishover.png"
        action Jump ("fr1a1")

screen freeroam1b2():
    add "images/s56.jpg"
    imagebutton:
        yalign 0.53
        xalign 0.74
        idle "images/fr1nora.png"
        hover "images/fr1norahover.png"
        if fr1nora == 0:
            action Jump ("fr1nora1")

        else:
            action Jump ("fr1nora2")

    imagebutton:
        yalign 0.38
        xalign 0.21
        idle "images/fr1c.png"
        hover "images/fr1chover.png"
        action Jump ("fr1c")

    imagebutton:
        yalign 1.0
        xalign 0.23
        idle "images/backchris.png"
        hover "images/backchrishover.png"
        action Jump ("fr1a1")


screen freeroam1c():
    add "images/s58.jpg"
    imagebutton:
        yalign 0.025
        xalign 0.26
        idle "images/fr1dorm.png"
        hover "images/fr1dormhover.png"
        if fr1adam == 0:
            action Jump ("fr1adam1")

        else:
            action Jump ("fr1adam2")

    imagebutton:
        yalign 0.05
        xalign 0.82
        idle "images/fr1yours.png"
        hover "images/fr1yourshover.png"
        action Jump ("fr1end")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/dormback.png"
        hover "images/dormbackhover.png"
        action Jump ("fr1b2")

screen endfreeroam():
    add "images/endfr.png"
    text "Are you sure you want to end free roam?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("frcontinue")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("frgoback")
        text_align 0.5
        xalign 0.43
        yalign 0.58


style endfr is button:
        xpos 1260
        ypos 400
        xmaximum 550

style endfr_text is text:
        font "fonts/Freshman.ttf"
        size 40
        color "#ffffff"
        hover_color "#ffffff"

style endfree is text:
        font "fonts/Freshman.ttf"
        size 40
        color "#ffffff"
        text_align 0.5
        xalign 0.5
        yalign 0.42
        xmaximum 600


screen freeroam2a(): #outside

    if samtalk == 0:
        add "images/s100.jpg"
    else:
        add "images/s100a.jpg"

    imagebutton:
        yalign 1.0
        xalign 0.43
        idle "images/fr2sam.png"
        hover "images/fr2samh.png"
        if samtalk == 0:
            action Jump ("fr2sam")
        else:
            action Jump ("fr2sam2")

    imagebutton:
        yalign 0
        xalign 0.482
        idle "images/fr2door.png" #inside
        hover "images/fr2doorh.png"
        if fr2door == 0:
            action Jump ("fr2door")
        else:
            action Jump ("fr2door2")


screen freeroam2b():

    add "images/s102.jpg"

    imagebutton:
        yalign 1.0
        xalign 0.515
        idle "images/fr2josh.png"
        hover "images/fr2joshh.png"
        if joshtalk == 0:
            action Jump ("fr2josh")
        else:
            action Jump ("fr2josh2")

    imagebutton:
        yalign 1.0
        xalign 1.0
        idle "images/fr2pool.png" #pool room
        hover "images/fr2poolh.png"
        action Jump ("fr2pool")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr2outside.png" ### back outside
        hover "images/fr2outsideh.png"
        action Jump ("fr2outside")

    imagebutton:
        yalign 0.4
        xalign 0.242
        idle "images/fr2courtney.png"
        hover "images/fr2courtneyh.png"
        if courtneytalk == 0:
            action Jump ("fr2courtney")
        else:
            action Jump ("fr2courtney2")

    imagebutton:
        yalign 1.0
        xalign 0
        idle "images/fr2camp.png"
        hover "images/fr2camph.png"
        action Jump ("fr2camp")

    imagebutton:
        yalign 0
        xalign 0.42
        idle "images/fr2stairs.png"
        hover "images/fr2stairsh.png"
        action Jump ("fr2stairs")

screen freeroam2c(): ###pool room

    add "images/s104.jpg"

    imagebutton:
        yalign 1.0
        xalign 1.0
        idle "images/fr2mason.png"
        hover "images/fr2masonh.png"
        if masontalk == 1:
            action Jump ("fr2mason2")
        else:
            action Jump ("fr2mason")

    imagebutton:
        yalign 0.38
        xalign 0.52
        idle "images/fr2katy.png"
        hover "images/fr2katyh.png"
        if katytalk == 1:
            action Jump ("fr2katy2")
        else:
            action Jump ("fr2katy")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/backpool.png"
        hover "images/backpoolh.png"
        action Jump ("fr2poolback")

screen freeroam2d(): ###camp room

    add "images/s106.jpg"

    imagebutton:
        yalign 1.0
        xalign 0.21
        idle "images/fr2chloe.png"
        hover "images/fr2chloeh.png"
        action Jump ("fr2chloe")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr2campback.png"
        hover "images/fr2campbackh.png"
        action Jump ("fr2campback")

screen freeroam2e(): ###stairs

    add "images/s105.jpg"

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr2grayson.png"
        hover "images/fr2graysonh.png"
        if graysontalk == 1:
            action Jump ("fr2grayson2")
        else:
            action Jump ("fr2grayson")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr2down.png"
        hover "images/fr2downh.png"
        action Jump ("fr2down")

screen endfreeroam2():
    add "images/endfr.png"
    text "Are you sure you want to end free roam?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("fr2end")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("fr2dontend")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen thx():
    if steam == False:
        add "images/newthx.png"
    else:
        add "images/newsteamend.jpg" # steam

    if steam == False:
        imagebutton:
            ypos 677
            xpos 394
            idle "images/supportdevelopmentblank.png"
            hover "images/supportdevelopment.png"
            action OpenURL ("https://www.patreon.com/collegekings")

    else:
        imagebutton:# steam
            ypos 700
            xalign 0.5
            idle "images/discordbutton1.png"
            hover "images/discordbutton2.png"
            action OpenURL ("http://discord.collegekingsgame.com")

    textbutton "Main Menu":
        text_underline True
        text_size 50
        text_font "fonts/Freshman.ttf"
        ypos 952
        xalign 0.5
        text_align 0.5
        action MainMenu()

######## General fighting screens.

screen ft1():
    image "images/fightchoice.png"

    text "Fighting":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5
    text "Fighting is big part of College Kings, however you can simulate all fights if you'd like to.":
        xalign 0.5
        yalign 0.42
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5


    textbutton "Play Fight":
        text_size 40
        xalign 0.5
        yalign 0.6
        action Jump ("playf1")

    textbutton "Simulate: realistic":
        text_size 40
        xalign 0.5
        yalign 0.7
        action Jump ("simtomfight")

    textbutton "Simulate: auto-win":
        text_size 40
        xalign 0.5
        yalign 0.8
        action Jump ("autowin")

screen ft2():
    image "images/fightchoice.png"

    text "Difficulty":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5
    text "Higher difficulties require quicker reactions. You can change this at any time in the settings.":
        xalign 0.5
        yalign 0.42
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5

    vbox xalign 0.45 yalign 0.75 spacing 30:
        textbutton "Easy":
            text_size 40
            action Jump ("easy")

        textbutton "Moderate":
            text_size 40
            action Jump ("moderate")

        textbutton "Hard":
            text_size 40
            action Jump ("hard")

screen ft3():
    image "images/fightchoice.png"

    text "Keybinding":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5
    text "The current keybindings are:\n[q] = Jab / Block Head\n[w] = Hook / Block Face\n[r] = Kick / Block Leg":
        xalign 0.5
        yalign 0.42
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5

    vbox xalign 0.45 yalign 0.75 spacing 30:
        textbutton "Change Keys":
            text_size 40
            action Jump ("changekeys")

        textbutton "Start Fight":
            text_size 40
            action Jump ("letsgo")


screen realmode():
    image "images/REALLIFEMODE.jpg"

    imagebutton:
        ypos 683
        xpos 417
        idle "images/rlmt.png"
        hover "images/enable.jpg"
        action Jump ("rme")

    imagebutton:
        ypos 683
        xpos 1016
        idle "images/rlmt.png"
        hover "images/disable.jpg"
        action Jump ("rmd")



######## POPUP

screen popup1():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Loyal{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup1")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup2():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Popular{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup2")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup3():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Confident{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup3")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup4():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Confident{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup4")
        text_align 0.5
        xalign 0.5
        yalign 0.58


screen popup5():
    image "images/endfr.png"

    text "Congratulations! You have learned a new fighting move: {b}Body Hook{/b}." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup5")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup6():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Loyal{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup6")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup7():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Loyal{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup7")
        text_align 0.5
        xalign 0.5
        yalign 0.58


screen popup8():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Confident{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup8")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup9():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Loyal{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup9")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup10():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Loyal{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup10")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup11():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Loyal{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup11")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup12():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Popular{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup12")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup13():
    image "images/endfr.png"

    text "Congratulations! You have learned a new fighting move: {b}Uppercut{/b}." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup13")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup14():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Confident{/b} has just changed the way your actions were perceived." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup14")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup15():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Popular{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup15")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup16():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Popular{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup16")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup17():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Confident{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup17")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup18():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Confident{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup18")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup19():
    image "images/endfr.png"

    text "You've just unlocked the social media app Kiwii! Open it now from the homescreen." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup19")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup20():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Loyal{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup20")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup21():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Loyal{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup21")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup22():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Loyal{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup22")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup23():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Confident{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup23")
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen popup24():
    image "images/endfr.png"

    text "Congratulations! Your Key Character Trait {b}Popular{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK" style "endfr":
        action Jump ("popup24")
        text_align 0.5
        xalign 0.5
        yalign 0.58



########### FIGHT with Tom

screen tomtut1():

    image "images/tomstancekick.jpg"


    key w:
        action Jump ("tomtut1hook")
    key q:
        action Jump ("tomtut1jab")
    key r:
        action Jump ("tomtut1kick")

    imagebutton:
        idle "images/jab.png"
        hover "images/jab.png"
        xalign 0.06
        yalign 0.5
        action Jump ("tomtut1jab")

    imagebutton:
        idle "images/hook.png"
        hover "images/hook.png"
        xalign 0.115
        yalign 0.4
        action Jump ("tomtut1hook")


    imagebutton:
        idle "images/kick.png"
        hover "images/kick.png"
        xalign 0.115
        yalign 0.61
        action Jump ("tomtut1kick")


screen kickcounter():

    image "images/tomhook.jpg"

    key q:
        action Jump ("tuthookblock")
    key w:
        action Jump ("tuthookhit1")
    key r:
        action Jump ("tuthookhit2")

    imagebutton:
        idle "images/hookblock.png"
        hover "images/hookblock.png"
        xalign 0.06
        yalign 0.5
        action Jump ("tuthookblock")

    imagebutton:
        idle "images/jabblock.png"
        hover "images/jabblock.png"
        xalign 0.115
        yalign 0.4
        action Jump ("tuthookhit1")

    imagebutton:
        idle "images/kickblock.png"
        hover "images/kickblock.png"
        xalign 0.115
        yalign 0.6
        action Jump ("tuthookhit2")


screen hookcounter():

    image "images/hookcounter.jpg"


    key q:
        action Jump ("tutjabhit")
    key w:
        action Jump ("tutjabblock")
    key r:
        action Jump ("tutjabhit2")

    imagebutton:
        idle "images/hookblock.png"
        hover "images/hookblock.png"
        xalign 0.06
        yalign 0.5
        action Jump ("tutjabhit")

    imagebutton:
        idle "images/jabblock.png"
        hover "images/jabblock.png"
        xalign 0.115
        yalign 0.4
        action Jump ("tutjabblock")

    imagebutton:
        idle "images/kickblock.png"
        hover "images/kickblock.png"
        xalign 0.115
        yalign 0.6
        action Jump ("tutjabhit2")

screen jabcounter():

    image "images/jabcounter.jpg"


    key q:
        action Jump ("tuthookblock2")
    key w:
        action Jump ("tuthookhit3")
    key r:
        action Jump ("tuthookhit4")

    imagebutton:
        idle "images/hookblock.png"
        hover "images/hookblock.png"
        xalign 0.06
        yalign 0.5
        action Jump ("tuthookblock2")

    imagebutton:
        idle "images/jabblock.png"
        hover "images/jabblock.png"
        xalign 0.115
        yalign 0.4
        action Jump ("tuthookhit3")

    imagebutton:
        idle "images/kickblock.png"
        hover "images/kickblock.png"
        xalign 0.115
        yalign 0.6
        action Jump ("tuthookhit4")




screen youattack():

    if tomstance == 1:


        image "images/tomstancekick.jpg"

        key r:
            action Jump ("tomkick1")
        key w:
            action Jump ("tomkick2")
        key q:
            action Jump ("tomkick3")

        imagebutton:
            idle "images/jab.png"
            hover "images/jab.png"
            xalign 0.06
            yalign 0.5
            action Jump ("tomkick3")

        imagebutton:
            idle "images/hook.png"
            hover "images/hook.png"
            xalign 0.115
            yalign 0.4
            action Jump ("tomkick2")


        imagebutton:
            idle "images/kick.png"
            hover "images/kick.png"
            xalign 0.115
            yalign 0.61
            action Jump ("tomkick1")

        timer reactiona action Jump("timer1")



    if tomstance == 2:
        image "images/tomstancehook.jpg"

        key w:
            action Jump ("tomhook1")
        key q:
            action Jump ("tomhook2")
        key r:
            action Jump ("tomhook3")

        imagebutton:
            idle "images/jab.png"
            hover "images/jab.png"
            xalign 0.06
            yalign 0.5
            action Jump ("tomhook2")

        imagebutton:
            idle "images/hook.png"
            hover "images/hook.png"
            xalign 0.115
            yalign 0.4
            action Jump ("tomhook1")


        imagebutton:
            idle "images/kick.png"
            hover "images/kick.png"
            xalign 0.115
            yalign 0.61
            action Jump ("tomhook3")

        timer reactiona action Jump("timer2")



    if tomstance == 3:
        image "images/tomstancejab.jpg"

        key q:
            action Jump ("tomjab1")
        key w:
            action Jump ("tomjab2")
        key r:
            action Jump ("tomjab3")

        imagebutton:
            idle "images/jab.png"
            hover "images/jab.png"
            xalign 0.06
            yalign 0.5
            action Jump ("tomjab1")

        imagebutton:
            idle "images/hook.png"
            hover "images/hook.png"
            xalign 0.115
            yalign 0.4
            action Jump ("tomjab2")


        imagebutton:
            idle "images/kick.png"
            hover "images/kick.png"
            xalign 0.115
            yalign 0.61
            action Jump ("tomjab3")


        timer reactiona action Jump("timer3")


screen tomattack():

    if tomattack == 1:
        image "images/tomhook.jpg"

        key r:
            action Jump ("tomhookhit")
        key q:
            action Jump ("tomhookblocked")
        key w:
            action Jump ("tomhookhit2")

        imagebutton:
            idle "images/hookblock.png"
            hover "images/hookblock.png"
            xalign 0.06
            yalign 0.5
            action Jump ("tomhookblocked")

        imagebutton:
            idle "images/jabblock.png"
            hover "images/jabblock.png"
            xalign 0.115
            yalign 0.4
            action Jump ("tomhookhit")

        imagebutton:
            idle "images/kickblock.png"
            hover "images/kickblock.png"
            xalign 0.115
            yalign 0.6
            action Jump ("tomhookhit2")

        timer reaction action Jump("timer4")


    if tomattack == 2:
        image "images/tomjab.jpg"

        key q:
            action Jump ("tomjabhit")
        key w:
            action Jump ("tomjabblocked")
        key r:
            action Jump ("tomjabhit2")

        imagebutton:
            idle "images/hookblock.png"
            hover "images/hookblock.png"
            xalign 0.06
            yalign 0.5
            action Jump ("tomjabhit")

        imagebutton:
            idle "images/jabblock.png"
            hover "images/jabblock.png"
            xalign 0.115
            yalign 0.4
            action Jump ("tomjabblocked")

        imagebutton:
            idle "images/kickblock.png"
            hover "images/kickblock.png"
            xalign 0.115
            yalign 0.6
            action Jump ("tomjabhit2")

        timer reaction action Jump("timer5")

    if tomattack == 3:
        image "images/tomkick.jpg"

        key w:
            action Jump ("tomkickhit")
        key q:
            action Jump ("tomkickhit2")
        key r:
            action Jump ("tomkickblocked")


        imagebutton:
            idle "images/hookblock.png"
            hover "images/hookblock.png"
            xalign 0.06
            yalign 0.5
            action Jump ("tomkickhit")

        imagebutton:
            idle "images/jabblock.png"
            hover "images/jabblock.png"
            xalign 0.115
            yalign 0.4
            action Jump ("tomkickhit2")

        imagebutton:
            idle "images/kickblock.png"
            hover "images/kickblock.png"
            xalign 0.115
            yalign 0.6
            action Jump ("tomkickblocked")

        timer reaction action Jump("timer6")


screen costumes():

    image "images/costumes.png"

    imagebutton:
        idle "images/try.png"
        hover "images/tryh.png"
        ypos 802
        xpos 256
        if costumeaubrey == True:
            if caughtpeekingaubrey == False:
                action Jump ("try1")

        else:
            if caughtpeekingpenelope == False:
                action Jump ("try1p")
    imagebutton:
        idle "images/try.png"
        hover "images/tryh.png"
        ypos 802
        xpos 738
        if costumeaubrey == True:
            if caughtpeekingaubrey == False:
                action Jump ("try2")
        else:
            if caughtpeekingpenelope == False:
                action Jump ("try2p")
    imagebutton:
        idle "images/try.png"
        hover "images/tryh.png"
        ypos 802
        xpos 1219
        if costumeaubrey == True:
            if caughtpeekingaubrey == False:
                action Jump ("try3")
        else:
            if caughtpeekingpenelope == False:
                action Jump ("try3p")
    imagebutton:
        idle "images/try.png"
        hover "images/buyh.png"
        ypos 935
        xpos 256
        if costumeaubrey == True:
            if auboutfits <= 3:
                action Jump ("surebuy1")
            else:
                action Jump ("buy1")
        else:
            if penoutfits <= 3:
                action Jump ("surebuy1p")
            else:
                action Jump ("buy1p")
    imagebutton:
        idle "images/try.png"
        hover "images/buyh.png"
        ypos 935
        xpos 738
        if costumeaubrey == True:
            if auboutfits <= 3:
                action Jump ("surebuy2")
            else:
                action Jump ("buy2")
        else:
            if penoutfits <= 3:
                action Jump ("surebuy2p")
            else:
                action Jump ("buy2p")
    imagebutton:
        idle "images/try.png"
        hover "images/buyh.png"
        ypos 935
        xpos 1219
        if costumeaubrey == True:
            if auboutfits <= 3:
                action Jump ("surebuy3")
            else:
                action Jump ("buy3")
        else:
            if penoutfits <= 3:
                action Jump ("surebuy3p")
            else:
                action Jump ("buy3p")



screen surebuy1():
    add "images/endfr.png"
    text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("buy1")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("gocostumes1")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen surebuy2():
    add "images/endfr.png"
    text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("buy2")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("gocostumes2")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen surebuy3():
    add "images/endfr.png"
    text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("buy3")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("gocostumes3")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen surebuy1p():
    add "images/endfr.png"
    text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("buy1p")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("gocostumes4")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen surebuy2p():
    add "images/endfr.png"
    text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("buy2p")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("gocostumes5")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen surebuy3p():
    add "images/endfr.png"
    text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("buy3p")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("gocostumes6")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen achievements():

        add "images/phonescreen.png" at truecenter

        add "images/stats.png" at truecenter
        if noexit == False:
            textbutton "Exit Phone" action Jump("exitphone") style"phonebutton"

        text "achievements":
            color "#000000"
            font "fonts/Freshman.ttf"
            size 45
            ypos 200
            xalign 0.5

        viewport:
            mousewheel True
            xanchor -780
            yanchor -280
            xmaximum 358
            ymaximum 600

    ########### copy paste messages here
            vbox spacing 10:

                if openwound == True:
                    vbox spacing -10:
                        textbutton "open wound" style "ach"

                        textbutton "Tell off Emily" style "ach2"

                else:
                    vbox:
                        textbutton "open wound" style "ach3"

                if nohardfeelings == True:
                    vbox spacing -10:
                        textbutton "no hard feelings" style "ach"

                        textbutton "Play nice with Emily" style "ach2"

                else:
                    vbox:
                        textbutton "no hard feelings" style "ach3"


                if keepitmoving == True:
                    vbox spacing -10:
                        textbutton "keep it moving" style "ach"

                        textbutton "Hit on Nora" style "ach2"

                else:
                    vbox:
                        textbutton "keep it moving" style "ach3"

                if romeo == True:
                    vbox spacing -10:
                        textbutton "romeo" style "ach"

                        textbutton "Kiss Lauren" style "ach2"

                else:
                    vbox:
                        textbutton "romeo" style "ach3"

                if bigmouth == True:
                    vbox spacing -10:
                        textbutton "big mouth" style "ach"

                        textbutton "Threaten Cameron" style "ach2"

                else:
                    vbox:
                        textbutton "big mouth" style "ach3"

                if mixedfeelings == True:
                    vbox spacing -10:
                        textbutton "mixed feelings" style "ach"

                        textbutton "Decline Lauren" style "ach2"

                else:
                    vbox:
                        textbutton "mixed feelings" style "ach3"

                if thenotorious == True:
                    vbox spacing -10:
                        textbutton "the notorious" style "ach"

                        textbutton "Win your first fight" style "ach2"

                else:
                    vbox:
                        textbutton "the notorious" style "ach3"

                if anewbeginning == True:
                    vbox spacing -10:
                        textbutton "a new beginning" style "ach"

                        textbutton "Lauren likes you" style "ach2"

                else:
                    vbox:
                        textbutton "a new beginning" style "ach3"

                if overit == True:
                    vbox spacing -10:
                        textbutton "over it" style "ach"

                        textbutton "Let Benjamin make a move" style "ach2"

                else:
                    vbox:
                        textbutton "over it" style "ach3"


                if notnowmom == True:
                    vbox spacing -10:
                        textbutton "not now, mom" style "ach"

                        textbutton "Decline Julia's call" style "ach2"

                else:
                    vbox:
                        textbutton "not now, mom" style "ach3"

                if lipsdontlie == True:
                    vbox spacing -10:
                        textbutton "lips don't lie" style "ach"

                        textbutton "Kiss Riley in the Park" style "ach2"

                else:
                    vbox:
                        textbutton "lips don't lie" style "ach3"

                if truthhurts == True:
                    vbox spacing -10:
                        textbutton "truth hurts" style "ach"

                        textbutton "Tell Lauren about Aubrey" style "ach2"

                else:
                    vbox:
                        textbutton "truth hurts" style "ach3"

                if relightthefire == True:
                    vbox spacing -10:
                        textbutton "relight the fire" style "ach"

                        textbutton "Tell Julia about Emily" style "ach2"

                else:
                    vbox:
                        textbutton "relight the fire" style "ach3"

                if rematch == True:
                    vbox spacing -10:
                        textbutton "rematch" style "ach"

                        textbutton "Buy Chloe the volleyball" style "ach2"

                else:
                    vbox:
                        textbutton "rematch" style "ach3"

                if keeneye == True:
                    vbox spacing -10:
                        textbutton "keen eye" style "ach"

                        textbutton "Pick the muffin" style "ach2"

                else:
                    vbox:
                        textbutton "keen eye" style "ach3"
                if onthelow == True:
                    vbox spacing -10:
                        textbutton "on the low" style "ach"

                        textbutton "Deny PDA with Lauren" style "ach2"

                else:
                    vbox:
                        textbutton "on the low" style "ach3"

                if petapublicenemy == True:
                    vbox spacing -10:
                        textbutton "peta public enemy" style "ach"

                        textbutton "Kill dog as animal lover" style "ach2"

                else:
                    vbox:
                        textbutton "peta public enemy" style "ach3"

                if snitch == True:
                    vbox spacing -10:
                        textbutton "snitch" style "ach"

                        textbutton "Tell the school" style "ach2"

                else:
                    vbox:
                        textbutton "snitch" style "ach3"

                if brosbeforehoes == True:
                    vbox spacing -10:
                        textbutton "bros before hoes" style "ach"

                        textbutton "Help Imre" style "ach2"

                else:
                    vbox:
                        textbutton "bros before hoes" style "ach3"

                if monkeybusiness == True:
                    vbox spacing -10:
                        textbutton "monkey business" style "ach"

                        textbutton "Join the Apes" style "ach2"

                else:
                    vbox:
                        textbutton "monkey business" style "ach3"

                if notmybusiness == True:
                    vbox spacing -10:
                        textbutton "not my business" style "ach"

                        textbutton "Don't disturb Ms.Rose" style "ach2"

                else:
                    vbox:
                        textbutton "not my business" style "ach3"

                if reignition == True:
                    vbox spacing -10:
                        textbutton "reignition" style "ach"

                        textbutton "Kiss Emily back" style "ach2"

                else:
                    vbox:
                        textbutton "reignition" style "ach3"

                if credulous == True:
                    vbox spacing -10:
                        textbutton "credulous" style "ach"

                        textbutton "Trust Chloe" style "ach2"

                else:
                    vbox:
                        textbutton "credulous" style "ach3"

                if seemsfishy == True:
                    vbox spacing -10:
                        textbutton "seems fishy" style "ach"

                        textbutton "Don't meet Grayson" style "ach2"

                else:
                    vbox:
                        textbutton "seems fishy" style "ach3"

                if strike == True:
                    vbox spacing -10:
                        textbutton "strike" style "ach"

                        textbutton "Kiss Penelope" style "ach2"

                else:
                    vbox:
                        textbutton "strike" style "ach3"

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


screen girls():

    image "images/girls.jpg"

    imagebutton:
        idle "images/girl.png"
        hover "images/girlhover.png"
        ypos 360
        xpos 110
        action Jump ("juchloe")

    imagebutton:
        idle "images/girl.png"
        hover "images/girlhover.png"
        ypos 360
        xpos 693
        action Jump ("juaubrey")

    imagebutton:
        idle "images/girl.png"
        hover "images/girlhover.png"
        ypos 360
        xpos 1277
        action Jump ("julauren")

    imagebutton:
        idle "images/girl.png"
        hover "images/girlhover.png"
        ypos 670
        xpos 110
        action Jump ("juriley")

    imagebutton:
        idle "images/girl.png"
        hover "images/girlhover.png"
        ypos 670
        xpos 693
        action Jump ("juemily")

    imagebutton:
        idle "images/girl.png"
        hover "images/girlhover.png"
        ypos 670
        xpos 1277
        action Jump ("jupenelope")

screen aubsex():

    image "images/sexpos.png"

    imagebutton:
        idle "images/sexposbutton.png"
        hover "images/sexposbutton.png"
        ypos 150
        xpos 36
        action Jump ("amiss")

    imagebutton:
        idle "images/sexposbutton.png"
        hover "images/sexposbutton.png"
        ypos 335
        xpos 36
        action Jump ("acow")

    imagebutton:
        idle "images/sexposbutton.png"
        hover "images/sexposbutton.png"
        ypos 531
        xpos 36
        action Jump ("abj")

    imagebutton:
        idle "images/sexposbutton.png"
        hover "images/sexposbutton.png"
        ypos 727
        xpos 36
        action Jump ("acream")


screen spoiler():

    if steam == False:
        add "images/menu4.jpg"
    else:
        add "images/menu4steam.jpg"
    add "images/darker.png"

    add "images/endfr.png"
    text "Warning: The scene gallery contains spoilers for the story of the game. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("spoilergo")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        text_align 0.5
        xalign 0.43
        yalign 0.58
        action Return ()

    tag menu

screen scenegal():

    tag menu

    add "Images/scenegalleryblank.jpg"

    imagebutton:
        idle "images/backtransp.png"
        hover "images/back.png"
        ypos 933
        xpos 79
        action Return()

    vpgrid:
        cols 4
        spacing 40
        xpos 78
        ypos 200

        imagebutton:
            idle "images/gallery1new.png"
            hover "images/gallery1.png"
            action Replay ("ga", locked = False)

        imagebutton:
            idle "images/gallery2new.png"
            hover "images/gallery2.png"
            action Replay ("gb", locked = False)

        imagebutton:
            idle "images/gallery3new.png"
            hover "images/gallery3.png"
            action Replay ("gc", locked = False)

        imagebutton:
            idle "images/gallery4new.png"
            hover "images/gallery4.png"
            action Replay ("fkcon", locked = False)

        imagebutton:
            idle "images/gallery6.png"
            hover "images/gallery6outline.png"
            action Replay ("ge", locked = False)

        imagebutton:
            idle "images/gallery5.png"
            hover "images/gallery5outline.png"
            action Replay ("gf", locked = False)

        imagebutton:
            idle "images/gallery7.png"
            hover "images/gallery7outline.png"
            action Replay ("rileysexscene", locked = False)

        imagebutton:
            idle "images/gallery8.png"
            hover "images/gallery8outline.png"
            action Replay ("brbj", locked = False)



screen skiptut():
    add "images/endfr.png"
    text "Would you like to play the fighting tutorial?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("sta")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("stb")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen getaccess():

    add "images/earlyaccess2.jpg"


    imagebutton:
        ypos 770
        xpos 540
        idle "images/get2.png"
        hover "images/get.png"
        action OpenURL ("https://www.patreon.com/collegekings")

screen texta():

    add "images/darker.png"
    add "images/text1big.jpg" at truecenter

    imagebutton:
        idle "images/bigbutton.png"
        hover "images/bigbutton.png"
        action Hide ("texta")

screen textb():

    add "images/darker.png"
    add "images/text2big.jpg" at truecenter

    imagebutton:
        idle "images/bigbutton.png"
        hover "images/bigbutton.png"
        action Hide ("textb")

screen textc():

    add "images/darker.png"
    add "images/text3big.jpg" at truecenter

    imagebutton:
        idle "images/bigbutton.png"
        hover "images/bigbutton.png"
        action Hide ("textc")

screen trolleyskip():
    add "images/endfr.png"
    text "The trolley problem involves hypothetical people and/or animals being run over by a train and can be a lot to handle. The following scene might make you feel uncomfortable or uneasy. If you prefer to skip the trolley problem scene, you can click skip right now.":
        style "endfree"
        yoffset 20
        size 30
    textbutton "Continue" style "endfr":
        action Jump ("continuetrolley")
        text_align 0.5
        xalign 0.57
        yalign 0.62

    textbutton "Skip" style "endfr":
        action Jump ("skiptrolley")
        text_align 0.5
        xalign 0.43
        yalign 0.62


screen skiptut2():
    add "images/endfr.png"
    text "Since this is your first fight, would you like to play the fighting tutorial?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("gb")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("fkcon")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen af():
    image "images/fightchoice.png"

    text "Fighting":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5
    text "Fighting is big part of College Kings, however you can simulate all fights if you'd like to.":
        xalign 0.5
        yalign 0.42
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5


    textbutton "Play Fight":
        text_size 40
        xalign 0.5
        yalign 0.6
        action Jump ("playf2")

    textbutton "Simulate: realistic":
        text_size 40
        xalign 0.5
        yalign 0.7
        action Jump ("simadamfight")

    textbutton "Simulate: auto-win":
        text_size 40
        xalign 0.5
        yalign 0.8
        action Jump ("autowinadam")


screen af2():
    image "images/fightchoice.png"

    text "Difficulty":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5
    text "Higher difficulties require quicker reactions. You can change this at any time in the settings.":
        xalign 0.5
        yalign 0.42
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5

    text "Warning: This fight is particularly difficult as your opponent is significantly more skilled than you.":
        xalign 0.5
        yalign 0.53
        font "fonts/OpenSans-Italic.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5
        size 20

    vbox xalign 0.45 yalign 0.75 spacing 30:
        textbutton "Easy":
            text_size 40
            action Jump ("easy2")

        textbutton "Moderate":
            text_size 40
            action Jump ("moderate2")

        textbutton "Hard":
            text_size 40
            action Jump ("hard2")

screen af3():
    image "images/fightchoice.png"

    text "Keybinding":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5

    text "If you change keybindings, you will need to delete the previous binding (the letter shown after pressing \"change keys\") first by pressing backspace. Only use lowercase letters / numbers unless you want to hold shift all fight.":
        xalign 0.5
        yalign 0.42
        font "fonts/OpenSans.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5
        size 20


    vbox xalign 0.45 yalign 0.75 spacing 30:
        textbutton "Change Keys":
            text_size 40
            action Jump ("keys1")

        textbutton "Start Fight":
            text_size 40
            action Jump ("letsgoadam")

screen keys1():
    image "images/fightchoice.png"

    text "Keybinding":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5

    vbox yalign 0.5 xalign 0.49:

        vbox:
            text "Jab / Block Head = ":
                size 40
            input at truecenter:
                size 100
                value VariableInputValue("q")
                length 1


    vbox xalign 0.45 yalign 0.75 spacing 30:
        textbutton "Next":
            text_size 40
            action Jump ("keys2")

        textbutton "Start Fight":
            text_size 40
            action Jump ("letsgoadam")

screen keys2():
    image "images/fightchoice.png"

    text "Keybinding":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5

    vbox yalign 0.5 xalign 0.49:

        vbox:
            text "Hook / Block Face = ":
                size 40
            input at truecenter:
                size 100
                value VariableInputValue("w")
                length 1


    vbox xalign 0.45 yalign 0.75 spacing 30:
        textbutton "Next":
            text_size 40
            action Jump ("keys3")

        textbutton "Start Fight":
            text_size 40
            action Jump ("letsgoadam")

screen keys3():
    image "images/fightchoice.png"

    text "Keybinding":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5

    vbox yalign 0.5 xalign 0.49:

        vbox:
            text "Body Hook / Block Body = ":
                size 40
            input at truecenter:
                size 100
                value VariableInputValue("e")
                length 1


    vbox xalign 0.45 yalign 0.75 spacing 30:
        textbutton "Next":
            text_size 40
            action Jump ("keys4")

        textbutton "Start Fight":
            text_size 40
            action Jump ("letsgoadam")

screen keys4():
    image "images/fightchoice.png"

    text "Keybinding":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5

    vbox yalign 0.5 xalign 0.49:

        vbox:
            text "Kick / Block Leg = ":
                size 40
            input at truecenter:
                size 100
                value VariableInputValue("r")
                length 1


    vbox xalign 0.45 yalign 0.75 spacing 30:

        textbutton "Redo Keybindings":
            text_size 40
            action Jump ("keys1")


        textbutton "Start Fight":
            text_size 40
            action Jump ("letsgoadam")



########### FIGHT with Adam

screen youattack2():

    if adamstance == 1:
        image "images/afstancejab.jpg"

        key q:
            action Jump ("adamjab1")
        key w:
            action Jump ("adamhook2")
        key e:
            action Jump ("adambody2")
        key r:
            action Jump ("adamkick2")

        imagebutton:
            idle "images/jab.png"
            hover "images/jab.png"
            xalign 0.06
            yalign 0.5
            action Jump ("adamjab1")

        imagebutton:
            idle "images/hook.png"
            hover "images/hook.png"
            xalign 0.115
            yalign 0.4
            action Jump ("adamhook2")

        imagebutton:
            idle "images/body.png"
            hover "images/body.png"
            xalign 0.172
            yalign 0.5
            action Jump ("adambody2")

        imagebutton:
            idle "images/kick.png"
            hover "images/kick.png"
            xalign 0.115
            yalign 0.61
            action Jump ("adamkick2")


        timer reactiona action Jump("adamattack")


    if adamstance == 2:
        image "images/afstancehook.jpg"

        key q:
            action Jump ("adamjab2")
        key w:
            action Jump ("adamhook1")
        key e:
            action Jump ("adambody2")
        key r:
            action Jump ("adamkick2")

        imagebutton:
            idle "images/jab.png"
            hover "images/jab.png"
            xalign 0.06
            yalign 0.5
            action Jump ("adamjab2")

        imagebutton:
            idle "images/hook.png"
            hover "images/hook.png"
            xalign 0.115
            yalign 0.4
            action Jump ("adamhook1")

        imagebutton:
            idle "images/body.png"
            hover "images/body.png"
            xalign 0.172
            yalign 0.5
            action Jump ("adambody2")

        imagebutton:
            idle "images/kick.png"
            hover "images/kick.png"
            xalign 0.115
            yalign 0.61
            action Jump ("adamkick2")



        timer reactiona action Jump("adamattack")


    if adamstance == 3:
        image "images/afstancebody.jpg"

        key q:
            action Jump ("adamjab2")
        key w:
            action Jump ("adamhook2")
        key e:
            action Jump ("adambody1")
        key r:
            action Jump ("adamkick2")

        imagebutton:
            idle "images/jab.png"
            hover "images/jab.png"
            xalign 0.06
            yalign 0.5
            action Jump ("adamjab2")

        imagebutton:
            idle "images/hook.png"
            hover "images/hook.png"
            xalign 0.115
            yalign 0.4
            action Jump ("adamhook2")

        imagebutton:
            idle "images/body.png"
            hover "images/body.png"
            xalign 0.172
            yalign 0.5
            action Jump ("adambody1")

        imagebutton:
            idle "images/kick.png"
            hover "images/kick.png"
            xalign 0.115
            yalign 0.61
            action Jump ("adamkick2")

        timer reactiona action Jump("adamattack")

    if adamstance == 4:


        image "images/afstancekick.jpg"

        key q:
            action Jump ("adamjab2")
        key w:
            action Jump ("adamhook2")
        key e:
            action Jump ("adambody2")
        key r:
            action Jump ("adamkick1")

        imagebutton:
            idle "images/jab.png"
            hover "images/jab.png"
            xalign 0.06
            yalign 0.5
            action Jump ("adamjab2")

        imagebutton:
            idle "images/hook.png"
            hover "images/hook.png"
            xalign 0.115
            yalign 0.4
            action Jump ("adamhook2")

        imagebutton:
            idle "images/body.png"
            hover "images/body.png"
            xalign 0.172
            yalign 0.5
            action Jump ("adambody2")

        imagebutton:
            idle "images/kick.png"
            hover "images/kick.png"
            xalign 0.115
            yalign 0.61
            action Jump ("adamkick1")

        timer reactiona action Jump("adamattack")





screen adamattack():

    if adamattack == 1:
        image "images/af13pic.jpg"

        key q:
            action Jump ("adamhookblocked")
        key w:
            action Jump ("adamhookhit")
        key e:
            action Jump ("adamhookhit")
        key r:
            action Jump ("adamhookhit")

        imagebutton:
            idle "images/hookblock.png"
            hover "images/hookblock.png"
            xalign 0.06
            yalign 0.5
            action Jump ("adamhookblocked")

        imagebutton:
            idle "images/jabblock.png"
            hover "images/jabblock.png"
            xalign 0.115
            yalign 0.4
            action Jump ("adamhookhit")

        imagebutton:
            idle "images/bodyblock.png"
            hover "images/bodyblock.png"
            xalign 0.172
            yalign 0.5
            action Jump ("adamhookhit")

        imagebutton:
            idle "images/kickblock.png"
            hover "images/kickblock.png"
            xalign 0.115
            yalign 0.6
            action Jump ("adamhookhit")


        timer reaction action Jump("adamhookhit")


    if adamattack == 2:
        image "images/af14pic.jpg"

        key q:
            action Jump ("adamjabhit")
        key w:
            action Jump ("adamjabblocked")
        key e:
            action Jump ("adamjabhit")
        key r:
            action Jump ("adamjabhit")

        imagebutton:
            idle "images/hookblock.png"
            hover "images/hookblock.png"
            xalign 0.06
            yalign 0.5
            action Jump ("adamjabhit")

        imagebutton:
            idle "images/jabblock.png"
            hover "images/jabblock.png"
            xalign 0.115
            yalign 0.4
            action Jump ("adamjabblocked")

        imagebutton:
            idle "images/bodyblock.png"
            hover "images/bodyblock.png"
            xalign 0.172
            yalign 0.5
            action Jump ("adamjabhit")

        imagebutton:
            idle "images/kickblock.png"
            hover "images/kickblock.png"
            xalign 0.115
            yalign 0.6
            action Jump ("adamjabhit")

        timer reaction action Jump("adamjabhit")

    if adamattack == 3:
        image "images/af15pic.jpg"

        key q:
            action Jump ("adambodyhit")
        key w:
            action Jump ("adambodyhit")
        key e:
            action Jump ("adambodyblocked")
        key r:
            action Jump ("adambodyhit")

        imagebutton:
            idle "images/hookblock.png"
            hover "images/hookblock.png"
            xalign 0.06
            yalign 0.5
            action Jump ("adambodyhit")

        imagebutton:
            idle "images/jabblock.png"
            hover "images/jabblock.png"
            xalign 0.115
            yalign 0.4
            action Jump ("adambodyhit")

        imagebutton:
            idle "images/bodyblock.png"
            hover "images/bodyblock.png"
            xalign 0.172
            yalign 0.5
            action Jump ("adambodyblocked")

        imagebutton:
            idle "images/kickblock.png"
            hover "images/kickblock.png"
            xalign 0.115
            yalign 0.6
            action Jump ("adambodyhit")

        timer reaction action Jump("adambodyhit")

    if adamattack == 4:
        image "images/af16pic.jpg"

        key q:
            action Jump ("adamkickhit")
        key w:
            action Jump ("adamkickhit")
        key e:
            action Jump ("adamkickhit")
        key r:
            action Jump ("adamkickblocked")

        timer reaction action Jump("adamkickhit")

        imagebutton:
            idle "images/hookblock.png"
            hover "images/hookblock.png"
            xalign 0.06
            yalign 0.5
            action Jump ("adamkickhit")

        imagebutton:
            idle "images/jabblock.png"
            hover "images/jabblock.png"
            xalign 0.115
            yalign 0.4
            action Jump ("adamkickhit")

        imagebutton:
            idle "images/bodyblock.png"
            hover "images/bodyblock.png"
            xalign 0.172
            yalign 0.5
            action Jump ("adamkickhit")

        imagebutton:
            idle "images/kickblock.png"
            hover "images/kickblock.png"
            xalign 0.115
            yalign 0.6
            action Jump ("adamkickblocked")

screen trolleya(time=3): # I set a default reaction time of 5 seconds

    image "images/trolleylever.jpg"

    imagebutton:
        idle "images/leverno.png"
        hover "images/lever.png"
        ypos 150
        xpos 125
        action Jump ("trolleyab")


    timer time repeat False action [ Hide('countdown'), Jump("trolleyaa") ]
    bar value AnimatedValue(0, time, time, time) at alpha_dissolve # assuming you're using the alpha_dissolve transform from the wiki

screen trolleyb(time=3): # I set a default reaction time of 5 seconds

    image "images/trolleylever.jpg"

    imagebutton:
        idle "images/leverno.png"
        hover "images/lever.png"
        ypos 150
        xpos 125
        action Jump ("trolleybb")


    timer time repeat False action [ Hide('countdown'), Jump("trolleyba") ]
    bar value AnimatedValue(0, time, time, time) at alpha_dissolve # assuming you're using the alpha_dissolve transform from the wiki


screen trolleyc(time=3): # I set a default reaction time of 5 seconds

    image "images/trolleylever.jpg"

    imagebutton:
        idle "images/leverno.png"
        hover "images/lever.png"
        ypos 150
        xpos 125
        action Jump ("trolleycb")


    timer time repeat False action [ Hide('countdown'), Jump("trolleyca") ]
    bar value AnimatedValue(0, time, time, time) at alpha_dissolve # assuming you're using the alpha_dissolve transform from the wiki

style phonebutton is button:
    yalign 0.95
    xalign 0.05

style phonebutton_text is text:
    font "fonts/Freshman.ttf"
    size 100
    hover_color "#FFD166"
    color "#ffffff"

style tutorialtext is text:
    font "fonts/OpenSans.ttf"
    size 25
    color "#ffffff"
    text_align 0
    xpos 1270
    ypos 400
    xmaximum 500

style tutorialtextnum is text:
    font "fonts/Freshman.ttf"
    size 25
    color "#FFD166"
    text_align 0.5
    xpos 1490
    ypos 580

style applabels is text:
    font "fonts/OpenSans.ttf"
    size 15
    color "#ffffff"
    text_align 0.5
    xalign 0.5

style phonehome is button:
    color "#000000"
    xsize 300
    ysize 50

style phonetext is text:
    font "fonts/OpenSans-Bold.ttf"
    size 40
    color "#000000"

style nametext is text:
    font "fonts/OpenSans-Bold.ttf"
    size 25
    color "#000000"


style msgleft is button:
    background "#CECECE"
    xpadding 15
    ypadding 5
    xmaximum 350
    ymargin 15

style msgleft_text is text:
    color "#000000"
    font "fonts/OpenSans.ttf"
    size 20

style msgright is button:
    background "#147efb"
    xpadding 15
    ypadding 5
    xalign 1.0
    xoffset 14
    xmaximum 350

style msgright_text is text:
    color "#ffffff"
    font "fonts/OpenSans.ttf"
    size 20

style replybox is button:
    background "#ffffff"
    xsize 250
    ysize 40

style replybox_text is text:
    color "#000000"
    font "fonts/OpenSans.ttf"

    size 20
    xalign 0.5
    yalign 0.5

style replies_style is button:
    background "#147efb"
    xpadding 15
    ypadding 5
    xmaximum 350

style replies_style_text is text:
    color "#ffffff"
    font "fonts/OpenSans.ttf"
    size 20

style imgright is button:
    background "#147efb"
    xpadding 15
    ypadding 5
    xalign 1.0
    xoffset 14
    xmaximum 350


########################## FREEROAM 3 : WOLVES RUSH PARTY

screen endfreeroam3():
    add "images/endfr.png"
    text "Are you sure you want to end free roam?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("fr3chris3")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("fr3stay")
        text_align 0.5
        xalign 0.43
        yalign 0.58


screen fr3garden():
    if kimpuke == False:
        add "images/fr3garden.jpg" # location picture

        imagebutton: #Josh button
            ypos 430
            xpos 1195
            idle "images/fr3gardenjoshblank.png"
            hover "images/fr3gardenjosh.png"

            if fr3josh == False:
                action Jump ("fr3josh1")

            else:
                if relics >= 5 and upstairs == "nobody" and askedkim == False: #Asking people for upstairs
                    action Jump ("fr3josh3")
                else:
                    action Jump ("fr3josh2")

    else:

        add "images/fr3garden2.jpg"

    imagebutton: #Go inside
        ypos 190
        xpos 485
        idle "images/fr3gardendoorblank.png"
        hover "images/fr3gardendoor.png"
        action Jump ("labelfr3downstairs")


screen fr3downstairs():

    add "images/fr3downstairs.jpg" # location picture

    imagebutton: #Go outside
        ypos 900
        xpos 440
        idle "images/fr3downstairsbackblank.png"
        hover "images/fr3downstairsback.png"
        action Jump ("labelfr3garden")

    imagebutton: #Go upstairs
        ypos 0
        xpos 940
        idle "images/fr3downstairsstairsblank.png"
        hover "images/fr3downstairsstairs.png"
        action Jump ("labelfr3upstairs")

    imagebutton: #Go living room
        ypos 70
        xpos 360
        idle "images/fr3downstairsdoorblank.png"
        hover "images/fr3downstairsdoor.png"
        action Jump ("labelfr3livingroom")

    imagebutton: #Go kitchen
        ypos 368
        xpos 1486
        idle "images/fr3downstairsrightblank.png"
        hover "images/fr3downstairsright.png"
        action Jump ("labelfr3kitchen2")

screen fr3livingroom():

    add "images/fr3livingroom.jpg" # location picture

    imagebutton: #guy1 button
        ypos 392
        xpos 760
        idle "images/fr3livingroomsofablank.png"
        hover "images/fr3livingroomsofa.png"

        if fr3guy == False:
            action Jump ("fr3guy1")

        else:
            action Jump ("fr3guy2")

    imagebutton: #Aubrey button
        ypos 254
        xpos 804
        idle "images/fr3livingroomaubreyblank.png"
        hover "images/fr3livingroomaubrey.png"

        if fr3aubrey == False:
            action Jump ("fr3aubrey1")

        else:
            if relics >= 5 and upstairs == "nobody":#Asking people for upstairs
                if askedemily == True and askedaubrey == True:
                    action Jump ("fr3aubrey2")
                else:
                    action Jump ("fr3aubrey3")
            else:
                action Jump ("fr3aubrey2")


    imagebutton: #Go back
        ypos 915
        xpos 432
        idle "images/fr3livingroombackblank.png"
        hover "images/fr3livingroomback.png"
        action Jump ("labelfr3downstairs")

    imagebutton: #Go kitchen
        ypos 106
        xpos 1700
        idle "images/fr3livingroomdoorblank.png"
        hover "images/fr3livingroomdoor.png"
        action Jump ("labelfr3kitchen")

screen fr3kitchen():

    add "images/fr3kitchen.jpg" # location picture

    imagebutton: #chris button
        ypos 60
        xpos 1147
        idle "images/fr3kitchenchrisblank.png"
        hover "images/fr3kitchenchrisn.png"

        if fr3chris == False:
            action Jump ("fr3chris1")

        else:
            action Jump ("fr3chris2")

    imagebutton: #Matt button
        ypos 139
        xpos 1048
        idle "images/fr3kitchenmattblank.png"
        hover "images/fr3kitchenmatt.png"

        if fr3matt == False:
            action Jump ("fr3matt1")

        else:
            action Jump ("fr3matt2")

    imagebutton: # Go Kitchen 2
        ypos 99
        xpos 0
        idle "images/fr3kitchenleftblank.png"
        hover "images/fr3kitchenleft.png"
        action Jump ("labelfr3kitchen2")

    imagebutton: # Go Living room
        ypos 100
        xpos 0
        idle "images/fr3kitchenlivingdoorblank.png"
        hover "images/fr3kitchenlivingdoor.png"
        action Jump ("labelfr3livingroom")

    imagebutton: #Riley button
        ypos 270
        xpos 328
        idle "images/fr3kitchenrileyblank.png"
        hover "images/fr3kitchenriley.png"

        if fr3riley == False:
            action Jump ("fr3riley1")

        else:
            if relics >= 5 and upstairs == "nobody" and askedriley == False:#Asking people for upstairs
                action Jump ("fr3riley3")
            else:
                action Jump ("fr3riley2")

screen fr3kitchen2():

    add "images/fr3kitchen2.jpg" # location picture

    imagebutton: # Go Ktichen
        ypos 836
        xpos 358
        idle "images/fr3kitchen2backblank.png"
        hover "images/fr3kitchen2back.png"
        action Jump ("labelfr3kitchen")

    imagebutton: # Go Middleroom
        ypos 65
        xpos 0
        idle "images/fr3kitchen2doorblank.png"
        hover "images/fr3kitchen2door.png"
        action Jump ("labelfr3middleroom")

    imagebutton: # Go downstairs hallway
        ypos 245
        xpos 1364
        idle "images/fr3kitchen2rightblank.png"
        hover "images/fr3kitchen2right.png"
        action Jump ("labelfr3downstairs")


screen fr3middleroom():

    add "images/fr3middleroom.jpg" # location picture

    imagebutton: # Go Kitchen2
        ypos 0
        xpos 50
        idle "images/fr3middleroomleftblank.png"
        hover "images/fr3middleroomleft.png"
        action Jump ("labelfr3kitchen2")

    imagebutton: # Downstairs bathroom
        ypos 106
        xpos 700
        idle "images/fr3middleroommiddleblank.png"
        hover "images/fr3middleroommiddle.png"
        action Jump ("fr3dsbathroom")

    imagebutton: # Go garage
        ypos 0
        xpos 1210
        idle "images/fr3middleroomrightblank.png"
        hover "images/fr3middleroomright.png"
        action Jump ("labelfr3garage")


screen fr3garage():
    if kimpuke == False:
        add "images/fr3garage.jpg" # location picture

        imagebutton: #Amber button
            ypos 235
            xpos 345
            idle "images/fr3garageamberblank.png"
            hover "images/fr3garageamber.png"

            if fr3amber == False:
                action Jump ("fr3amber1")

            else:
                if relics >= 5 and upstairs == "nobody" and askedamber == False: #Asking people for upstairs
                    action Jump ("fr3amber3")
                else:
                    action Jump ("fr3amber2")

    else:
        add "images/fr3garage2.jpg"

    imagebutton: #sebastian button
        ypos 168
        xpos 1338
        idle "images/fr3garagefightblank.png"
        hover "images/fr3garagefight.png"

        if fr3sebastian == False:
            action Jump ("fr3sebastian1")

        else:
            action Jump ("fr3sebastian2")


    imagebutton: # Go back to middleroom
        ypos 877
        xpos 473
        idle "images/fr3garagebackblank.png"
        hover "images/fr3garageback.png"
        action Jump ("labelfr3middleroom")


screen fr3upstairs():

    add "images/fr3upstairs.jpg" # location picture

    imagebutton: # Go backdownstairs
        yalign 1.0
        xalign 0.5
        idle "images/fr3upstairsbackblank.png"
        hover "images/fr3upstairsback.png"
        action Jump ("labelfr3downstairs")

    imagebutton: # go office
        ypos 140
        xpos 1125
        idle "images/fr3upstairsrightblank.png"
        hover "images/fr3upstairsright.png"
        action Jump ("fr3office")

    imagebutton: # Go roofroom
        ypos 115
        xpos 922
        idle "images/fr3upstairsmiddleblank.png"
        hover "images/fr3upstairsmiddle.png"
        action Jump ("labelfr3roofroom")

    imagebutton: #chloe button
        ypos 25
        xpos 490
        idle "images/fr3upstairsleftblank.png"
        hover "images/fr3upstairsleft.png"

        if fr3chloe == False:
            action Jump ("fr3chloe1")

        else:
            action Jump ("fr3chloe2")

screen fr3office():

    add "images/fr3office.jpg" # location picture

    imagebutton: # Go back out of office
        ypos 847
        xpos 440
        idle "images/fr3officebackblank.png"
        hover "images/fr3officeback.png"
        action Jump ("labelfr3upstairs")

    imagebutton: # picture
        ypos 115
        xpos 100
        idle "images/fr3officephotoblank.png"
        hover "images/fr3officephoto.png"
        action Jump ("fr3picture")

    imagebutton: # certificate
        ypos 212
        xpos 1240
        idle "images/fr3officecertificateblank.png"
        hover "images/fr3officecertificate.png"
        action Jump ("fr3certificate")

    imagebutton: # books
        ypos 593
        xpos 1382
        idle "images/fr3officebooksblank.png"
        hover "images/fr3officebooks.png"
        action Jump ("fr3books")

    imagebutton: # trophies
        yalign 1.0
        xpos 1480
        idle "images/fr3officetrophyblank.png"
        hover "images/fr3officetrophy.png"
        action Jump ("fr3trophies")



screen fr3roofroom():

    add "images/fr3roofroom.jpg" # location picture

    imagebutton: # Go back
        yalign 1.0
        xpos 500
        idle "images/fr3roofroombackblank.png"
        hover "images/fr3roofroomback.png"
        action Jump ("labelfr3upstairs")

    imagebutton: #Window (Nora) button
        ypos 50
        xpos 327
        idle "images/fr3roofroomwindowblank.png"
        hover "images/fr3roofroomwindow.png"

        if fr3nora == False:
            action Jump ("fr3nora1")

        else:
            action Jump ("fr3nora2")

screen emilysexoverlaybutton():

    if renpy.get_screen("emilysexoverlay"):
        textbutton "hide overlay":
            xpos 250
            action Hide("emilysexoverlay")
    else:
        textbutton "show overlay":
            xpos 10
            action Show("emilysexoverlay")

screen emilysexoverlay():

    vpgrid:
        rows 5
        spacing 10
        xpos 10
        ypos 10

        imagebutton:
            idle "images/emhead.png"
            hover "images/emhead.png"
            action Jump ("emhead")

        imagebutton:
            idle "images/emfacefuck.png"
            hover "images/emfacefuck.png"
            action Jump ("emfacefuck")

        imagebutton:
            idle "images/embehind.png"
            hover "images/embehind.png"
            action Jump ("embehind")

        imagebutton:
            idle "images/embutterfly.png"
            hover "images/embutterfly.png"
            action Jump ("embutterfly")

        imagebutton:
            idle "images/emclimax.png"
            hover "images/emclimax.png"
            action Jump ("emclimax")

screen aubreysexoverlaybutton():

    if renpy.get_screen("aubreysexoverlay"):
        textbutton "hide overlay":
            xpos 420
            action Hide("aubreysexoverlay")
    else:
        textbutton "show overlay":
            xpos 10
            action Show("aubreysexoverlay")

screen aubreysexoverlay():

    vpgrid:
        rows 5
        spacing 10
        xpos 10
        ypos 10

        imagebutton:
            idle "images/naubblowjob.png"
            hover "images/naubblowjob.png"
            action Jump ("naubblowjob")

        imagebutton:
            idle "images/naub69.png"
            hover "images/naub69.png"
            action Jump ("naub69")

        imagebutton:
            idle "images/naubfingering.png"
            hover "images/naubfingering.png"
            action Jump ("naubfingering")

        imagebutton:
            idle "images/naubmissionary.png"
            hover "images/naubmissionary.png"
            action Jump ("naubmissionary")

        imagebutton:
            idle "images/naubbehind.png"
            hover "images/naubbehind.png"
            action Jump ("naubbehind")

        imagebutton:
            idle "images/naubclimax.png"
            hover "images/naubclimax.png"
            action Jump ("naubclimax")

screen letter1():

    add "images/darker.png"
    add "images/emilyletter.png"

    button:
        xsize 1920
        ysize 1080
        action Hide ("letter1")

    #---------- Images description -----------#
    # hc_girls - Full screen image consisting Amber, Aubrey, Autumn, Chloe, Emily, Lauren, Penelope, Riley, Alone in a 3x3 layout. Leave space on right side to show some stuff about the girls when hovered on them (?)
    # hc_girlidle - just a blank image
    # hc_girlaccept - white frame around the girls to show when hovered if they are available
    # hc_girlreject - a semi-transparent red "X" mark with a semi-transparent grey background to show when hovered on girls when they cannot be asked or have already been asked
default tmpGirl = "none"
screen hc_select():
    add "images/homecomingchoice.jpg"
    use hc_info()

    vpgrid:
        cols 4
        rows 2
        spacing 40
        xalign 0.5
        ypos 285

        if "amber" not in hcAsked and not laurenrs:
            imagebutton:
                idle "images/HCAmber.png"
                hover "images/HCAmber2.png"
                hovered SetVariable("tmpGirl", "amber")
                ypos # 1
                xpos # 1
                action Jump("hc_asking_amber")
        else:
            imagebutton:
                idle "images/HCAmber3.png"
                hover "images/HCAmber23.png"
                hovered SetVariable("tmpGirl", "amber")
                ypos # 1
                xpos # 1
                action NullAction()

        if "aubrey" not in hcAsked and not laurenrs:
            imagebutton:
                idle "images/HCAubrey.png"
                hover "images/HCAubrey2.png"
                hovered SetVariable("tmpGirl", "aubrey")
                ypos # 1
                xpos # 2
                action Jump("hc_asking_aubrey")
        else:
            imagebutton:
                idle "images/HCAubrey3.png"
                hover "images/HCAubrey23.png"
                hovered SetVariable("tmpGirl", "aubrey")
                ypos # 1
                xpos # 2
                action NullAction()

        if "autumn" not in hcAsked and not laurenrs and not autumnmad:
            imagebutton:
                idle "images/HCAutumn.png"
                hover "images/HCAutumn2.png"
                hovered SetVariable("tmpGirl", "autumn")
                ypos # 1
                xpos # 3
                action Jump("hc_asking_autumn")
        else:
            imagebutton:
                idle "images/HCAutumn3.png"
                hover "images/HCAutumn23.png"
                hovered SetVariable("tmpGirl", "autumn")
                ypos # 1
                xpos # 3
                action NullAction()

        if "chloe" not in hcAsked and not laurenrs and not chloemad:
            imagebutton:
                idle "images/HCChloe.png"
                hover "images/HCChloe2.png"
                hovered SetVariable("tmpGirl", "chloe")
                ypos # 2
                xpos # 1
                action Jump("hc_asking_chloe")
        else:
            imagebutton:
                idle "images/HCChloe3.png"
                hover "images/HCChloe23.png"
                hovered SetVariable("tmpGirl", "chloe")
                ypos # 2
                xpos # 1
                action NullAction()

        if "emily" not in hcAsked and not laurenrs and forgiveemily:
            imagebutton:
                idle "images/HCEmily.png"
                hover "images/HCEmily2.png"
                hovered SetVariable("tmpGirl", "emily")
                ypos # 2
                xpos # 2
                action Jump("hc_asking_emily")
        else:
            imagebutton:
                idle "images/HCEmily3.png"
                hover "images/HCEmily23.png"
                hovered SetVariable("tmpGirl", "emily")
                ypos # 2
                xpos # 2
                action NullAction()

        if "lauren" not in hcAsked and not laurenemily == 3: # Can ask her if she did not break up for suggesting an open relationship
            imagebutton:
                idle "images/HCLauren.png"
                hover "images/HCLauren2.png"
                hovered SetVariable("tmpGirl", "lauren")
                ypos # 2
                xpos # 3
                action Jump("hc_asking_lauren")
        else:
            imagebutton:
                idle "images/HCLauren3.png"
                hover "images/HCLauren23.png"
                hovered SetVariable("tmpGirl", "lauren")
                ypos # 2
                xpos # 3
                action NullAction()

        if "penelope" not in hcAsked and not laurenrs:
            imagebutton:
                idle "images/HCPenelope.png"
                hover "images/HCPenelope2.png"
                hovered SetVariable("tmpGirl", "penelope")
                ypos # 3
                xpos # 1
                action Jump("hc_asking_penelope")
        else:
            imagebutton:
                idle "images/HCPenelope3.png"
                hover "images/HCPenelope23.png"
                hovered SetVariable("tmpGirl", "penelope")
                ypos # 3
                xpos # 1
                action NullAction()

        if "riley" not in hcAsked and not laurenrs:
            imagebutton:
                idle "images/HCRiley.png"
                hover "images/HCRiley2.png"
                hovered SetVariable("tmpGirl", "riley")
                ypos # 3
                xpos # 2
                action Jump("hc_asking_riley")
        else:
            imagebutton:
                idle "images/HCRiley3.png"
                hover "images/HCRiley23.png"
                hovered SetVariable("tmpGirl", "riley")
                ypos # 3
                xpos # 2
                action NullAction()

    textbutton "Go Alone":
        ypos 100
        xpos 1500
        action Jump("hc_no_girl")


# Info screen that is shown on the right side of 3x3 girl grid
screen hc_info():
    $ tmpMsg = ""
    if tmpGirl == "none":
        $ tmpMsg += "I could always go alone..."
    elif tmpGirl == "amber":
        if laurenrs:
            $ tmpMsg += "Lauren would kill me if I asked someone other than her."
        else:
            $ tmpMsg += "I’m not that close with Amber but she does seem quite flirty around me."
    elif tmpGirl == "aubrey":
        if laurenrs:
            $ tmpMsg += "Lauren would kill me if I asked someone other than her."
        else:
            if aubreyrs:
                $ tmpMsg += "I’m pretty sure that Aubrey would go with me and that would probably lead to a pretty hot night afterwards..."
            else:
                $ tmpMsg += "Aubrey and I get along well, she might be down to go with me."
    elif tmpGirl == "autumn":
        if laurenrs:
            $ tmpMsg += "Lauren would kill me if I asked someone other than her."
        else:
            if autumnmad:
                $ tmpMsg += "I think Autumn might be mad at me, so I probably shouldn’t ask her."
            else:
                $ tmpMsg += "Autumn and aren’t really close, but I’ll never know if she’d say yes if I don’t try."
    elif tmpGirl == "chloe":
        if laurenrs:
            $ tmpMsg += "Lauren would kill me if I asked someone other than her."
        else:
            if chloemad:
                $ tmpMsg += "I think Chloe is mad at me, so I probably shouldn’t ask her."
            else:
                $ tmpMsg += "Chloe and I have been getting closer recently. Who knows, I might have a shot."
    elif tmpGirl == "emily":
        if laurenrs:
            $ tmpMsg += "Lauren would kill me if I asked someone other than her."
        else:
            if not forgiveemily:
                $ tmpMsg += "I don't think asking Emily is the right call."
            else:
                $ tmpMsg += "I could take Emily. She definitely still has a thing for me."
    elif tmpGirl == "lauren":
        if laurenrs:
            $ tmpMsg += "Lauren thinks we’re dating so I definitely have to ask her."
        else:
            if laurenmad:
                $ tmpMsg += "It’s kinda weird between Lauren and me, I probably should ask someone else."
            else:
                $ tmpMsg += "I’m not sure Lauren sees me as more than a friend, but we have been getting closer."
    elif tmpGirl == "penelope":
        if laurenrs:
            $ tmpMsg += "Lauren would kill me if I asked someone other than her."
        else:
            if bowling:
                if emilyrs:
                    $ tmpMsg += "Penelope didn’t seem too eager to talk to me today, I better ask someone else."
                else:
                    $ tmpMsg += "Penelope and I got along really well when we went bowling together, I think she could say yes."
            else:
                $ tmpMsg += "I haven’t done that much with Penelope so far, but maybe she’ll yes."
    elif tmpGirl == "riley":
        if laurenrs:
            $ tmpMsg += "Lauren would kill me if I asked someone other than her."
        else:
            if rileyrs:
                $ tmpMsg += "Riley seems to really like me so I think she’ll say yes."
            else:
                $ tmpMsg += "Riley and I are good friends. She might say yes if I ask her."

    text tmpMsg:
        color "#000"
        xmaximum 700
        xalign 0.5
        yalign 0.88

########################## FREEROAM 4 : HOMECOMING

screen endfr4(labelYes, labelNo, girl):
    add "images/endfr.png"
    text "Are you sure you want to end the free roam with [girl]?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump (labelYes)
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump (labelNo)
        text_align 0.5
        xalign 0.43
        yalign 0.58

### GYM ###

screen fr4dancefloor():

    if hcGirl == "chloe":
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloorchloedatenonora.jpg"
        else:
            add "images/fr4dancefloorchloedate.jpg"

    elif hcGirl == "emily":
        if fr4nora and not fr4nora2:
            add "images/fr4danceflooremilydatenonora.jpg"
        else:
            add "images/fr4danceflooremilydate.jpg"

    elif hcGirl == "lauren":
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloorlaurendatenonora.jpg"
        else:
            add "images/fr4dancefloorlaurendate.jpg"

    elif hcGirl == "penelope":
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloorpenelopedatenonora.jpg"
        else:
            add "images/fr4dancefloorpenelopedate.jpg"

    elif hcGirl == "riley":
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloorrileydatenonora.jpg"
        else:
            add "images/fr4dancefloorrileydate.jpg"

    else:
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloornodatenonora.jpg"
        else:
            add "images/fr4dancefloornodate.jpg"

    if not fr4nora or fr4nora2:
        imagebutton:
            ypos 0
            xpos 0
            idle "images/fr4dancefloornora.png"
            hover "images/fr4dancefloornorahover.png"
            if fr4nora2:

                action Jump ("fr4nora3")

            else:
                action Jump ("fr4nora1")
    else:
        imagebutton:
            ypos 0
            xpos 150
            idle "images/fr4dancefloorchris.png"
            hover "images/fr4dancefloorchrishover.png"
            action Jump ("fr4chris1")



    imagebutton:
        ypos 50
        xpos 1100
        idle "images/fr4dancefloorelijah.png"
        hover "images/fr4dancefloorelijahhover.png"
        if not fr4elijah:
            action Jump ("fr4elijah1")
        else:
            action Jump ("fr4elijah2")

    imagebutton:
        ypos 85
        xpos 905
        idle "images/fr4dancefloormason.png"
        hover "images/fr4dancefloormasonhover.png"
        if not fr4mason:
            action Jump ("fr4mason1")
        else:
            action Jump ("fr4mason2")


    if hcGirl == "chloe":

        imagebutton:
            ypos 30
            xpos 645
            idle "images/fr4dancefloorchloe.png"
            hover "images/fr4dancefloorchloehover.png"
            action Jump ("fr4chloedate")

    elif hcGirl == "emily":

        imagebutton:
            ypos 0
            xpos 615
            idle "images/fr4danceflooremily.png"
            hover "images/fr4danceflooremilyhover.png"
            action Jump ("fr4emilydate")

    elif hcGirl == "lauren":

        imagebutton:
            ypos 0
            xpos 617
            idle "images/fr4dancefloorlauren.png"
            hover "images/fr4dancefloorlaurenhover.png"
            action Jump ("fr4laurendate")

    elif hcGirl == "penelope":

        imagebutton:
            ypos 0
            xpos 655
            idle "images/fr4dancefloorpenelope.png"
            hover "images/fr4dancefloorpenelopehover.png"
            action Jump ("fr4penelopedate")

    elif hcGirl == "riley":
        imagebutton:
            ypos 25
            xpos 675
            idle "images/fr4dancefloorriley.png"
            hover "images/fr4dancefloorrileyhover.png"
            action Jump ("fr4rileydate")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.png"
        hover "images/fr4bottomhover.png"
        action Jump ("labelfr4gymentrance")

    imagebutton:
        yalign 0.5
        xalign 0
        idle "images/fr4left.png"
        hover "images/fr4lefthover.png"
        action Jump ("labelfr4gymleft")

    imagebutton:
        yalign 0.5
        xalign 1.0
        idle "images/fr4right.png"
        hover "images/fr4righthover.png"
        action Jump ("labelfr4gymright")


screen fr4gymleft():

    if hcGirl == "chloe":
        if fr4riley:
            add "images/fr4gymleftnochloenoriley.jpg"
        else:
            add "images/fr4gymleftnochloe.jpg"

    elif hcGirl == "riley":

        if fr4chloe:
            add "images/fr4gymleftnochloenoriley.jpg"
        else:
            add "images/fr4gymleftnoriley.jpg"

    else:
        if fr4riley and fr4chloe:
            add "images/fr4gymleftnochloenoriley.jpg"
        elif fr4riley:
            add "images/fr4gymleftnoriley.jpg"
        elif fr4chloe:
            add "images/fr4gymleftnochloe.jpg"
        else:
            add "images/fr4gymleft.jpg"

    if not hcGirl == "chloe":
        if not fr4chloe:
            imagebutton:
                ypos 190
                xpos 375
                idle "images/fr4gymleftchloe.png"
                hover "images/fr4gymleftchloehover.png"
                action Jump ("fr4chloe1")
        else:
            imagebutton:
                ypos 195
                xpos 63
                idle "images/fr4gymleftryan.png"
                hover "images/fr4gymleftryanhover.png"
                action Jump ("fr4ryan3")

    else:
        imagebutton:
            ypos 195
            xpos 63
            idle "images/fr4gymleftryan.png"
            hover "images/fr4gymleftryanhover.png"
            action Jump ("fr4ryan1")

    if not hcGirl == "riley" and not fr4riley:

        imagebutton:
            ypos 215
            xpos 1485
            idle "images/fr4gymleftriley.png"
            hover "images/fr4gymleftrileyhover.png"
            action Jump ("fr4riley1")

    else:

        imagebutton:
            ypos 225
            xpos 1520
            idle "images/fr4gymleftaubrey.png"
            hover "images/fr4gymleftaubreyhover.png"
            if not fr4aubrey:
                action Jump ("fr4aubrey1")
            else:
                action Jump ("fr4aubrey2")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.png"
        hover "images/fr4bottomhover.png"
        action Jump ("labelfr4dancefloor")

screen fr4gymright():

    if hcGirl == "lauren":
        add "images/fr4gymrightnolauren.jpg"
    else:
        add "images/fr4gymright.jpg"


    if not hcGirl == "lauren":
        imagebutton:
            ypos 355
            xpos 1492
            idle "images/fr4gymrightlauren.png"
            hover "images/fr4gymrightlaurenhover.png"
            if not fr4lauren:
                action Jump ("fr4lauren1")
            else:
                action Jump ("fr4lauren2")
    else:
        imagebutton:
            ypos 335
            xpos 1775
            idle "images/fr4gymrightmsrose.png"
            hover "images/fr4gymrightmsrosehover.png"
            if not fr4msrose:
                action Jump ("fr4msrose1")
            else:
                action Jump ("fr4msrose2")

    imagebutton:
        ypos 360
        xpos 0
        idle "images/fr4gymrightcameron.png"
        hover "images/fr4gymrightcameronhover.png"
        if not fr4cameron:
            action Jump ("fr4cameron1")
        else:
            action Jump ("fr4cameron2")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.png"
        hover "images/fr4bottomhover.png"
        action Jump ("labelfr4dancefloor")

screen fr4gymentrance():

    if fr4riley and not fr4noriley and fr4nora and not fr4nora2:
        add "images/fr4gymentrancerileynora.jpg"
    elif fr4riley and not fr4noriley:
        add "images/fr4gymentranceriley.jpg"
    elif fr4nora and not fr4nora2:
        add "images/fr4gymentrancenora.jpg"
    else:
        add "images/fr4gymentrance.jpg"

    if fr4riley and not fr4noriley:
        imagebutton:
            ypos 318
            xpos 365
            idle "images/fr4gymentranceriley.png"
            hover "images/fr4gymentrancerileyhover.png"
            action Jump ("fr4riley2")

    if fr4nora and not fr4nora2:
        imagebutton:
            ypos 315
            xpos 0
            idle "images/fr4gymentrancenora.png"
            hover "images/fr4gymentrancenorahover.png"
            action Jump ("fr4nora2")

    imagebutton:
        ypos 440
        xpos 1235
        idle "images/fr4gymentranceaaron.png"
        hover "images/fr4gymentranceaaronhover.png"
        if not fr4aaron:
            action Jump ("fr4aaron1")
        else:
            action Jump ("fr4aaron2")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.png"
        hover "images/fr4bottomhover.png"
        action Jump ("labelfr4dancefloor")

    imagebutton:
        ypos 285
        xpos 710
        idle "images/fr4gymentrancedoor.png"
        hover "images/fr4gymentrancedoorhover.png"
        action Jump ("labelfr4hallwaygymexit")

### Hallway ###

screen fr4hallwaygymexit():

    add "images/fr4hallwaygymexit.jpg"

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.png"
        hover "images/fr4bottomhover.png"
        action Jump ("labelfr4gymentrance")

    imagebutton:
        yalign 0.5
        xalign 1.0
        idle "images/fr4right.png"
        hover "images/fr4righthover.png"
        action Jump ("labelfr4hallwaybathroom")

    imagebutton:
        yalign 0.5
        xalign 0
        idle "images/fr4left.png"
        hover "images/fr4lefthover.png"
        action Jump ("labelfr4hallway")

screen fr4hallwaybathroom():

    add "images/fr4hallwaybathroom.jpg"

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.png"
        hover "images/fr4bottomhover.png"
        action Jump ("labelfr4hallwaygymexit")

    imagebutton:
        ypos 130
        xpos 737
        idle "images/fr4hallwaybathroomdoor.png"
        hover "images/fr4hallwaybathroomdoorhover.png"
        if not fr4imre:
            action Jump ("fr4imre1")
        else:
            action Jump ("fr4imre2")


screen fr4hallway():

    if not hcGirl == "penelope":
        if fr4chloe and preventgrayson:
            add "images/fr4hallwaychloe.jpg"
        else:
            add "images/fr4hallway.jpg"
    else:
        if fr4chloe and preventgrayson:
            add "images/fr4hallwaynopenelopechloe.jpg"
        else:
            add "images/fr4hallwaynopenelope.jpg"

    if fr4chloe and preventgrayson:
        imagebutton:
            ypos 175
            xpos 1035
            idle "images/fr4hallwaychloe.png"
            hover "images/fr4hallwaychloehover.png"
            if not fr4chloe2:
                action Jump ("fr4chloe2")
            else:
                action Jump ("fr4chloe3")

    if not hcGirl == "penelope":
        imagebutton:
            ypos 105
            xpos 535
            idle "images/fr4hallwaypenelope.png"
            hover "images/fr4hallwaypenelopehover.png"
            if not fr4penelope:
                action Jump ("fr4penelope1")
            else:
                action Jump ("fr4penelope2")

    imagebutton:
        ypos 70
        xpos 770
        idle "images/fr4hallwaycornerpath.png"
        hover "images/fr4hallwaycornerpathhover.png"
        action Jump ("labelfr4hallwaycorner")

    imagebutton:
        ypos 160
        xpos 835
        idle "images/fr4hallwaydoor.png"
        hover "images/fr4hallwaydoorhover.png"
        action Jump ("labelfr4outsidestairs")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.png"
        hover "images/fr4bottomhover.png"
        action Jump ("labelfr4hallwaygymexit")

screen fr4hallwaycorner():

    if not fr4grayson:
        add "images/fr4hallwaycorner.jpg"
    elif preventgrayson:
        add "images/fr4hallwaycornernumber.jpg"
    else:
        add "images/fr4hallwaycornernograyson.jpg"

    imagebutton:
        ypos 205
        xpos 875
        idle "images/fr4hallwaycornerdoor.png"
        hover "images/fr4hallwaycornerdoorhover.png"
        if fr4chloe and not preventgrayson:
            action Jump ("fr4lockerroomchloe")
        else:
            action Jump ("fr4lockerroom")

    if not fr4grayson:
        imagebutton:
            ypos 395
            xpos 320
            idle "images/fr4hallwaycornergrayson.png"
            hover "images/fr4hallwaycornergraysonhover.png"
            action Jump ("fr4grayson1")


    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.png"
        hover "images/fr4bottomhover.png"
        action Jump ("labelfr4hallway")

### Outside ###

screen fr4outsidestairs():

    if not hcGirl == "emily":
        add "images/fr4outsidestairs.jpg"
    else:
        add "images/fr4outsidestairsnoemily.jpg"

    if not hcGirl == "emily":
        imagebutton:
            ypos 295
            xpos 520
            idle "images/fr4outsidestairsemily.png"
            hover "images/fr4outsidestairsemilyhover.png"
            if not fr4emily:
                action Jump ("fr4emily1")
            else:
                action Jump ("fr4emily2")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.png"
        hover "images/fr4bottomhover.png"
        action Jump ("labelfr4hallway")

    imagebutton:
        yalign 0.5
        xalign 1.0
        idle "images/fr4right.png"
        hover "images/fr4righthover.png"
        action Jump ("labelfr4outsidestreet")

screen fr4outsidestreet():

    add "images/fr4outsidestreet.jpg"

    imagebutton:
        ypos 340
        xpos 830
        idle "images/fr4outsidestreet.png"
        hover "images/fr4outsidestreethover.png"
        if not fr4samantha:
            action Jump ("fr4samantha1")
        else:
            action Jump ("fr4samantha2")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.png"
        hover "images/fr4bottomhover.png"
        action Jump ("labelfr4outsidestairs")

# Generic screen for showing KCT popups
screen kctpopup(labelname):
    image "images/endfr.png"
    text "Congratulations! Your Key Character Trait {b}[kct!c]{/b} has just changed the outcome of a decision someone was making." style "endfree"
    textbutton "OK" style "endfr":
        action Jump(labelname)
        text_align 0.5
        xalign 0.5
        yalign 0.58

screen rileysexoverlaybutton():

    if renpy.get_screen("rileysexoverlay"):
        textbutton "hide overlay":
            xpos 250
            action Hide("rileysexoverlay")
    else:
        textbutton "show overlay":
            xpos 10
            action Show("rileysexoverlay")

screen rileysexoverlay():

    vpgrid:
        rows 5
        spacing 10
        xpos 10
        ypos 10

        imagebutton:
            idle "images/riblowjob.png"
            hover "images/riblowjob.png"
            action Jump ("riblowjob")

        imagebutton:
            idle "images/rifingering.png"
            hover "images/rifingering.png"
            action Jump ("rifingering")

        imagebutton:
            idle "images/rimissionary.png"
            hover "images/rimissionary.png"
            action Jump ("rimissionary")

        imagebutton:
            idle "images/riclimax.png"
            hover "images/riclimax.png"
            action Jump ("riclimax")
