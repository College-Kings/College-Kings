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
    left_bar Frame("gui/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.webp"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.webp", gui.frame_borders, tile=gui.frame_tile)



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

    background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
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
    image "gui/curves.webp"
    style_prefix "choice"

    timer 0.001 action SetVariable("ischoice", True)

    default menuButtonsConfig = {
        0: {
            "background": "Left",
            "pos": (210, 907),
            "xoffset": 0
        },
        1: {
            "background": "Right",
            "pos": (1005, 907),
            "xoffset": 50
        },
        2: {
            "background": "Top",
            "pos": (600, 780),
            "xoffset": 0 # Centered
        }
    }
    
    for count, item in enumerate(items):
        
        ### Requires menu disable function from jwt.rpy
        $ disabled = False
        if "(disabled)" in item.caption:
            $ disabled = True

        if count < len(menuButtonsConfig):
            fixed:
                xysize (660, 104)
                pos menuButtonsConfig[count]["pos"]

                imagebutton:
                    if disabled:
                        idle "gui/{}white.webp".format(menuButtonsConfig[count]["background"])
                    else:
                        idle "gui/{}blue.webp".format(menuButtonsConfig[count]["background"])
                        action [item.action, SetVariable("ischoice", False)]
                    hover "gui/{}white.webp".format(menuButtonsConfig[count]["background"])

                text item.caption.replace(" (disabled)", ""):
                    align(0.5, 0.5)
                    xoffset menuButtonsConfig[count]["xoffset"]
                    yalign 0.5
                    size 40
                    if count > 1:
                        xalign 0.5

    if showkct == True:
        image "gui/kct.webp"
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

        timer time repeat False action [ SetVariable("timed", False), Hide('countdown'), Jump("choicetimer") ]
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

    add "gui/savepage.webp"

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

    if youDamage == 3:
        image "images/3 hits.webp"
    if youDamage == 4:
        image "images/4 hits.webp"
    if youDamage >= 5:
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
            idle "images/play2.webp"
            hover "images/play3.webp"
            action Start()
            xpos 79
            ypos 147

        imagebutton:
            idle "images/load2.webp"
            hover "images/load3.webp"
            action ShowMenu("load")
            xpos 759
            ypos 147

        imagebutton:
            idle "images/patreon2.webp"
            hover "images/patreon4.webp"
            action OpenURL ("https://www.patreon.com/collegekings")
            xpos 1401
            ypos 147

        imagebutton:
            idle "images/patreon2.webp"
            hover "images/discord2.webp"
            action OpenURL ("http://discord.collegekingsgame.com")
            xpos 1401
            if not config.enable_steam:
                ypos 417
            else:
                ypos 147 # steam version


        imagebutton:
            idle "images/settings2.webp"
            hover "images/settings3.webp"
            action ShowMenu("preferences")
            xpos 79
            ypos 457

        imagebutton:
            idle "images/quit2.webp"
            hover "images/quit3.webp"
            action Quit(confirm= main_menu)
            xpos 531
            ypos 457

        imagebutton:
            idle "images/scene2.webp"
            hover "images/scene1.webp"
            action Show("spoiler")
            xpos 79
            ypos 346

        imagebutton:
            idle "images/patreon2.webp"
            hover "images/website3.webp"
            action OpenURL("http://collegekingsgame.com")
            xpos 1401
            if not config.enable_steam:
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

    add "gui/savepage.webp"

    tag menu

    use file_slots(_("Save"))


screen load():

    modal True

    add "gui/loadpage.webp"

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
    tag menu
    modal True

    add "gui/settingspage.webp"

    # Display settings
    hbox:
        align (0.1645, 0.265)
        spacing 136
        style_prefix "check"

        textbutton _("window"):
            action Preference("display", "window")
            text_size 45
        textbutton _("fullscreen"):
            action Preference("display", "fullscreen")
            text_size 45

    # Skip settings
    hbox:
        align (0.122, 0.468)
        spacing 35
        style_prefix "check"

        textbutton _("Unseen Text"):
            action Preference("skip", "toggle")
            text_size 28
        textbutton _("After Choices"):
            action Preference("after choices", "toggle")
            text_size 28
        textbutton _("Transitions"):
            action InvertSelected(Preference("transitions", "toggle"))
            text_size 28

    # Real Life settings
    hbox:
        align (0.195, 0.671)
        spacing 300

        if realmode:
            textbutton _("On"):
                action [SetVariable("realmode", True), SetVariable("config.rollback_enabled", False), SetVariable("showkct", False)]
                text_color "#FFD166"
                text_size 45
            textbutton _("Off"):
                action [SetVariable("realmode", False), SetVariable("config.rollback_enabled", True)]
                text_size 45
        else:
            textbutton _("On"):
                action [SetVariable("realmode", True), SetVariable("config.rollback_enabled", False), SetVariable("showkct", False)]
                text_size 45
            textbutton _("Off"):
                action [SetVariable("realmode", False), SetVariable("config.rollback_enabled", True)]
                text_color "#FFD166"
                text_size 45

    # KCT settings
    hbox:
        align (0.195, 0.874)
        spacing 300

        if showkct:
            textbutton _("On"):
                action SetVariable("showkct", True)
                text_color "#FFD166"
                text_size 45
            textbutton _("Off"):
                action SetVariable("showkct", False)
                text_size 45
        else:
            textbutton _("On"):
                action SetVariable("showkct", True)
                text_size 45
            textbutton _("Off"):
                action SetVariable("showkct", False)
                text_color "#FFD166"
                text_size 45

    # Sliders
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

    textbutton _("Return"):
        style "return_button"
        pos (1500, 1050)
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

    add "gui/overlay/confirm.webp"

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
    background Frame([ "gui/confirm_frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=gui.frame_tile)
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
    background Frame("gui/skip.webp", gui.skip_frame_borders, tile=gui.frame_tile)
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

    background Frame("gui/notify.webp", gui.notify_frame_borders, tile=gui.frame_tile)
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

    background "gui/nvl.webp"
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
    background "gui/phone/textbox.webp"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.webp"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.webp"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.webp"

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
    left_bar Frame("gui/phone/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.webp"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900

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

######## General fighting screens.

screen ft1():
    image "images/fightchoice.webp"

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
    image "images/fightchoice.webp"

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
    image "images/fightchoice.webp"

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

screen surebuy1():
    add "images/endfr.webp"
    text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("buy1")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("v1_gocostumes")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen surebuy2():
    add "images/endfr.webp"
    text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("buy2")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("v1_gocostumes")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen surebuy3():
    add "images/endfr.webp"
    text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("buy3")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("v1_gocostumes")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen surebuy1p():
    add "images/endfr.webp"
    text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("buy1p")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("v1_gocostumes")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen surebuy2p():
    add "images/endfr.webp"
    text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("buy2p")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("v1_gocostumes")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen surebuy3p():
    add "images/endfr.webp"
    text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump ("buy3p")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("v1_gocostumes")
        text_align 0.5
        xalign 0.43
        yalign 0.58

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

screen aubsex():

    image "images/sexpos.webp"

    imagebutton:
        idle "images/sexposbutton.webp"
        hover "images/sexposbutton.webp"
        ypos 150
        xpos 36
        action Jump ("amiss")

    imagebutton:
        idle "images/sexposbutton.webp"
        hover "images/sexposbutton.webp"
        ypos 335
        xpos 36
        action Jump ("acow")

    imagebutton:
        idle "images/sexposbutton.webp"
        hover "images/sexposbutton.webp"
        ypos 531
        xpos 36
        action Jump ("abj")

    imagebutton:
        idle "images/sexposbutton.webp"
        hover "images/sexposbutton.webp"
        ypos 727
        xpos 36
        action Jump ("acream")

screen skiptut():
    add "images/endfr.webp"
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

    add "images/earlyaccess2.webp"


    imagebutton:
        ypos 770
        xpos 540
        idle "images/get2.webp"
        hover "images/get.webp"
        action OpenURL ("https://www.patreon.com/collegekings")

screen texta():

    add "images/darker.webp"
    add "images/text1big.webp" at truecenter

    imagebutton:
        idle "images/bigbutton.webp"
        hover "images/bigbutton.webp"
        action Hide ("texta")

screen textb():

    add "images/darker.webp"
    add "images/text2big.webp" at truecenter

    imagebutton:
        idle "images/bigbutton.webp"
        hover "images/bigbutton.webp"
        action Hide ("textb")

screen textc():

    add "images/darker.webp"
    add "images/text3big.webp" at truecenter

    imagebutton:
        idle "images/bigbutton.webp"
        hover "images/bigbutton.webp"
        action Hide ("textc")

screen trolleyskip():
    add "images/endfr.webp"
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

screen trolleya(time=3): # I set a default reaction time of 5 seconds

    image "images/trolleylever.webp"

    imagebutton:
        idle "images/leverno.webp"
        hover "images/lever.webp"
        ypos 150
        xpos 125
        action Jump ("trolleyab")


    timer time repeat False action [ Hide('countdown'), Jump("trolleyaa") ]
    bar value AnimatedValue(0, time, time, time) at alpha_dissolve # assuming you're using the alpha_dissolve transform from the wiki

screen trolleyb(time=3): # I set a default reaction time of 5 seconds

    image "images/trolleylever.webp"

    imagebutton:
        idle "images/leverno.webp"
        hover "images/lever.webp"
        ypos 150
        xpos 125
        action Jump ("trolleybb")


    timer time repeat False action [ Hide('countdown'), Jump("trolleyba") ]
    bar value AnimatedValue(0, time, time, time) at alpha_dissolve # assuming you're using the alpha_dissolve transform from the wiki


screen trolleyc(time=3): # I set a default reaction time of 5 seconds

    image "images/trolleylever.webp"

    imagebutton:
        idle "images/leverno.webp"
        hover "images/lever.webp"
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
            idle "images/emhead.webp"
            hover "images/emhead.webp"
            action Jump ("emhead")

        imagebutton:
            idle "images/emfacefuck.webp"
            hover "images/emfacefuck.webp"
            action Jump ("emfacefuck")

        imagebutton:
            idle "images/embehind.webp"
            hover "images/embehind.webp"
            action Jump ("embehind")

        imagebutton:
            idle "images/embutterfly.webp"
            hover "images/embutterfly.webp"
            action Jump ("embutterfly")

        imagebutton:
            idle "images/emclimax.webp"
            hover "images/emclimax.webp"
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
            idle "images/naubblowjob.webp"
            hover "images/naubblowjob.webp"
            action Jump ("naubblowjob")

        imagebutton:
            idle "images/naub69.webp"
            hover "images/naub69.webp"
            action Jump ("naub69")

        imagebutton:
            idle "images/naubfingering.webp"
            hover "images/naubfingering.webp"
            action Jump ("naubfingering")

        imagebutton:
            idle "images/naubmissionary.webp"
            hover "images/naubmissionary.webp"
            action Jump ("naubmissionary")

        imagebutton:
            idle "images/naubbehind.webp"
            hover "images/naubbehind.webp"
            action Jump ("naubbehind")

        imagebutton:
            idle "images/naubclimax.webp"
            hover "images/naubclimax.webp"
            action Jump ("naubclimax")

screen letter1():
    add "images/darker.webp"
    add Transform("images/emilyletter.webp", size=(764, 1080))


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
    add "images/homecomingchoice.webp"
    use hc_info()

    vpgrid:
        cols 4
        rows 2
        spacing 40
        xalign 0.5
        ypos 285

        if "amber" not in hcAsked and not laurenrs:
            imagebutton:
                idle "images/HCAmber.webp"
                hover "images/HCAmber2.webp"
                hovered SetVariable("tmpGirl", "amber")
                ypos # 1
                xpos # 1
                action Jump("hc_asking_amber")
        else:
            imagebutton:
                idle "images/HCAmber3.webp"
                hover "images/HCAmber23.webp"
                hovered SetVariable("tmpGirl", "amber")
                ypos # 1
                xpos # 1
                action NullAction()

        if "aubrey" not in hcAsked and not laurenrs:
            imagebutton:
                idle "images/HCAubrey.webp"
                hover "images/HCAubrey2.webp"
                hovered SetVariable("tmpGirl", "aubrey")
                ypos # 1
                xpos # 2
                action Jump("hc_asking_aubrey")
        else:
            imagebutton:
                idle "images/HCAubrey3.webp"
                hover "images/HCAubrey23.webp"
                hovered SetVariable("tmpGirl", "aubrey")
                ypos # 1
                xpos # 2
                action NullAction()

        if "autumn" not in hcAsked and not laurenrs and not autumnmad:
            imagebutton:
                idle "images/HCAutumn.webp"
                hover "images/HCAutumn2.webp"
                hovered SetVariable("tmpGirl", "autumn")
                ypos # 1
                xpos # 3
                action Jump("hc_asking_autumn")
        else:
            imagebutton:
                idle "images/HCAutumn3.webp"
                hover "images/HCAutumn23.webp"
                hovered SetVariable("tmpGirl", "autumn")
                ypos # 1
                xpos # 3
                action NullAction()

        if "chloe" not in hcAsked and not laurenrs and not chloemad:
            imagebutton:
                idle "images/HCChloe.webp"
                hover "images/HCChloe2.webp"
                hovered SetVariable("tmpGirl", "chloe")
                ypos # 2
                xpos # 1
                action Jump("hc_asking_chloe")
        else:
            imagebutton:
                idle "images/HCChloe3.webp"
                hover "images/HCChloe23.webp"
                hovered SetVariable("tmpGirl", "chloe")
                ypos # 2
                xpos # 1
                action NullAction()

        if "emily" not in hcAsked and not laurenrs and forgiveemily:
            imagebutton:
                idle "images/HCEmily.webp"
                hover "images/HCEmily2.webp"
                hovered SetVariable("tmpGirl", "emily")
                ypos # 2
                xpos # 2
                action Jump("hc_asking_emily")
        else:
            imagebutton:
                idle "images/HCEmily3.webp"
                hover "images/HCEmily23.webp"
                hovered SetVariable("tmpGirl", "emily")
                ypos # 2
                xpos # 2
                action NullAction()

        if "lauren" not in hcAsked and not laurenemily == 3: # Can ask her if she did not break up for suggesting an open relationship
            imagebutton:
                idle "images/HCLauren.webp"
                hover "images/HCLauren2.webp"
                hovered SetVariable("tmpGirl", "lauren")
                ypos # 2
                xpos # 3
                action Jump("hc_asking_lauren")
        else:
            imagebutton:
                idle "images/HCLauren3.webp"
                hover "images/HCLauren23.webp"
                hovered SetVariable("tmpGirl", "lauren")
                ypos # 2
                xpos # 3
                action NullAction()

        if "penelope" not in hcAsked and not laurenrs:
            imagebutton:
                idle "images/HCPenelope.webp"
                hover "images/HCPenelope2.webp"
                hovered SetVariable("tmpGirl", "penelope")
                ypos # 3
                xpos # 1
                action Jump("hc_asking_penelope")
        else:
            imagebutton:
                idle "images/HCPenelope3.webp"
                hover "images/HCPenelope23.webp"
                hovered SetVariable("tmpGirl", "penelope")
                ypos # 3
                xpos # 1
                action NullAction()

        if "riley" not in hcAsked and not laurenrs:
            imagebutton:
                idle "images/HCRiley.webp"
                hover "images/HCRiley2.webp"
                hovered SetVariable("tmpGirl", "riley")
                ypos # 3
                xpos # 2
                action Jump("hc_asking_riley")
        else:
            imagebutton:
                idle "images/HCRiley3.webp"
                hover "images/HCRiley23.webp"
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
                $ tmpMsg += "Autumn and I aren’t really close, but I’ll never know if she’d say yes if I don’t try."
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
    add "images/endfr.webp"
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
            add "images/fr4dancefloorchloedatenonora.webp"
        else:
            add "images/fr4dancefloorchloedate.webp"

    elif hcGirl == "emily":
        if fr4nora and not fr4nora2:
            add "images/fr4danceflooremilydatenonora.webp"
        else:
            add "images/fr4danceflooremilydate.webp"

    elif hcGirl == "lauren":
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloorlaurendatenonora.webp"
        else:
            add "images/fr4dancefloorlaurendate.webp"

    elif hcGirl == "penelope":
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloorpenelopedatenonora.webp"
        else:
            add "images/fr4dancefloorpenelopedate.webp"

    elif hcGirl == "riley":
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloorrileydatenonora.webp"
        else:
            add "images/fr4dancefloorrileydate.webp"

    else:
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloornodatenonora.webp"
        else:
            add "images/fr4dancefloornodate.webp"

    if not fr4nora or fr4nora2:
        imagebutton:
            ypos 0
            xpos 0
            idle "images/fr4dancefloornora.webp"
            hover "images/fr4dancefloornorahover.webp"
            if fr4nora2:

                action Jump ("fr4nora3")

            else:
                action Jump ("fr4nora1")
    else:
        imagebutton:
            ypos 0
            xpos 150
            idle "images/fr4dancefloorchris.webp"
            hover "images/fr4dancefloorchrishover.webp"
            action Jump ("fr4chris1")



    imagebutton:
        ypos 50
        xpos 1100
        idle "images/fr4dancefloorelijah.webp"
        hover "images/fr4dancefloorelijahhover.webp"
        if not fr4elijah:
            action Jump ("fr4elijah1")
        else:
            action Jump ("fr4elijah2")

    imagebutton:
        ypos 85
        xpos 905
        idle "images/fr4dancefloormason.webp"
        hover "images/fr4dancefloormasonhover.webp"
        if not fr4mason:
            action Jump ("fr4mason1")
        else:
            action Jump ("fr4mason2")


    if hcGirl == "chloe":

        imagebutton:
            ypos 30
            xpos 645
            idle "images/fr4dancefloorchloe.webp"
            hover "images/fr4dancefloorchloehover.webp"
            action Jump ("fr4chloedate")

    elif hcGirl == "emily":

        imagebutton:
            ypos 0
            xpos 615
            idle "images/fr4danceflooremily.webp"
            hover "images/fr4danceflooremilyhover.webp"
            action Jump ("fr4emilydate")

    elif hcGirl == "lauren":

        imagebutton:
            ypos 0
            xpos 617
            idle "images/fr4dancefloorlauren.webp"
            hover "images/fr4dancefloorlaurenhover.webp"
            action Jump ("fr4laurendate")

    elif hcGirl == "penelope":

        imagebutton:
            ypos 0
            xpos 655
            idle "images/fr4dancefloorpenelope.webp"
            hover "images/fr4dancefloorpenelopehover.webp"
            action Jump ("fr4penelopedate")

    elif hcGirl == "riley":
        imagebutton:
            ypos 25
            xpos 675
            idle "images/fr4dancefloorriley.webp"
            hover "images/fr4dancefloorrileyhover.webp"
            action Jump ("fr4rileydate")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump ("labelfr4gymentrance")

    imagebutton:
        yalign 0.5
        xalign 0
        idle "images/fr4left.webp"
        hover "images/fr4lefthover.webp"
        action Jump ("labelfr4gymleft")

    imagebutton:
        yalign 0.5
        xalign 1.0
        idle "images/fr4right.webp"
        hover "images/fr4righthover.webp"
        action Jump ("labelfr4gymright")


screen fr4gymleft():

    if hcGirl == "chloe":
        if fr4riley:
            add "images/fr4gymleftnochloenoriley.webp"
        else:
            add "images/fr4gymleftnochloe.webp"

    elif hcGirl == "riley":

        if fr4chloe:
            add "images/fr4gymleftnochloenoriley.webp"
        else:
            add "images/fr4gymleftnoriley.webp"

    else:
        if fr4riley and fr4chloe:
            add "images/fr4gymleftnochloenoriley.webp"
        elif fr4riley:
            add "images/fr4gymleftnoriley.webp"
        elif fr4chloe:
            add "images/fr4gymleftnochloe.webp"
        else:
            add "images/fr4gymleft.webp"

    if not hcGirl == "chloe":
        if not fr4chloe:
            imagebutton:
                ypos 190
                xpos 375
                idle "images/fr4gymleftchloe.webp"
                hover "images/fr4gymleftchloehover.webp"
                action Jump ("fr4chloe1")
        else:
            imagebutton:
                ypos 195
                xpos 63
                idle "images/fr4gymleftryan.webp"
                hover "images/fr4gymleftryanhover.webp"
                action Jump ("fr4ryan3")

    else:
        imagebutton:
            ypos 195
            xpos 63
            idle "images/fr4gymleftryan.webp"
            hover "images/fr4gymleftryanhover.webp"
            action Jump ("fr4ryan1")

    if not hcGirl == "riley" and not fr4riley:

        imagebutton:
            ypos 215
            xpos 1485
            idle "images/fr4gymleftriley.webp"
            hover "images/fr4gymleftrileyhover.webp"
            action Jump ("fr4riley1")

    else:

        imagebutton:
            ypos 225
            xpos 1520
            idle "images/fr4gymleftaubrey.webp"
            hover "images/fr4gymleftaubreyhover.webp"
            if not fr4aubrey:
                action Jump ("fr4aubrey1")
            else:
                action Jump ("fr4aubrey2")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump ("labelfr4dancefloor")

screen fr4gymright():

    if hcGirl == "lauren":
        add "images/fr4gymrightnolauren.webp"
    else:
        add "images/fr4gymright.webp"


    if not hcGirl == "lauren":
        imagebutton:
            ypos 355
            xpos 1492
            idle "images/fr4gymrightlauren.webp"
            hover "images/fr4gymrightlaurenhover.webp"
            if not fr4lauren:
                action Jump ("fr4lauren1")
            else:
                action Jump ("fr4lauren2")
    else:
        imagebutton:
            ypos 335
            xpos 1775
            idle "images/fr4gymrightmsrose.webp"
            hover "images/fr4gymrightmsrosehover.webp"
            if not fr4msrose:
                action Jump ("fr4msrose1")
            else:
                action Jump ("fr4msrose2")

    imagebutton:
        ypos 360
        xpos 0
        idle "images/fr4gymrightcameron.webp"
        hover "images/fr4gymrightcameronhover.webp"
        if not fr4cameron:
            action Jump ("fr4cameron1")
        else:
            action Jump ("fr4cameron2")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump ("labelfr4dancefloor")

screen fr4gymentrance():

    if fr4riley and not fr4noriley and fr4nora and not fr4nora2:
        add "images/fr4gymentrancerileynora.webp"
    elif fr4riley and not fr4noriley:
        add "images/fr4gymentranceriley.webp"
    elif fr4nora and not fr4nora2:
        add "images/fr4gymentrancenora.webp"
    else:
        add "images/fr4gymentrance.webp"

    if fr4riley and not fr4noriley:
        imagebutton:
            ypos 318
            xpos 365
            idle "images/fr4gymentrancerileyidle.webp"
            hover "images/fr4gymentrancerileyhover.webp"
            action Jump ("fr4riley2")

    if fr4nora and not fr4nora2:
        imagebutton:
            ypos 315
            xpos 0
            idle "images/fr4gymentrancenoraidle.webp"
            hover "images/fr4gymentrancenorahover.webp"
            action Jump ("fr4nora2")

    imagebutton:
        ypos 440
        xpos 1235
        idle "images/fr4gymentranceaaron.webp"
        hover "images/fr4gymentranceaaronhover.webp"
        if not fr4aaron:
            action Jump ("fr4aaron1")
        else:
            action Jump ("fr4aaron2")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump ("labelfr4dancefloor")

    imagebutton:
        ypos 285
        xpos 710
        idle "images/fr4gymentrancedoor.webp"
        hover "images/fr4gymentrancedoorhover.webp"
        action Jump ("labelfr4hallwaygymexit")

### Hallway ###

screen fr4hallwaygymexit():

    add "images/fr4hallwaygymexit.webp"

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump ("labelfr4gymentrance")

    imagebutton:
        yalign 0.5
        xalign 1.0
        idle "images/fr4right.webp"
        hover "images/fr4righthover.webp"
        action Jump ("labelfr4hallwaybathroom")

    imagebutton:
        yalign 0.5
        xalign 0
        idle "images/fr4left.webp"
        hover "images/fr4lefthover.webp"
        action Jump ("labelfr4hallway")

screen fr4hallwaybathroom():

    add "images/fr4hallwaybathroom.webp"

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump ("labelfr4hallwaygymexit")

    imagebutton:
        ypos 130
        xpos 737
        idle "images/fr4hallwaybathroomdoor.webp"
        hover "images/fr4hallwaybathroomdoorhover.webp"
        if not fr4imre:
            action Jump ("fr4imre1")
        else:
            action Jump ("fr4imre2")


screen fr4hallway():

    if not hcGirl == "penelope":
        if fr4chloe and preventgrayson:
            add "images/fr4hallwaychloe.webp"
        else:
            add "images/fr4hallway.webp"
    else:
        if fr4chloe and preventgrayson:
            add "images/fr4hallwaynopenelopechloe.webp"
        else:
            add "images/fr4hallwaynopenelope.webp"

    if fr4chloe and preventgrayson:
        imagebutton:
            ypos 175
            xpos 1035
            idle "images/fr4hallwaychloeidle.webp"
            hover "images/fr4hallwaychloehover.webp"
            if not fr4chloe2:
                action Jump ("fr4chloe2")
            else:
                action Jump ("fr4chloe3")

    if not hcGirl == "penelope":
        imagebutton:
            ypos 105
            xpos 535
            idle "images/fr4hallwaypenelope.webp"
            hover "images/fr4hallwaypenelopehover.webp"
            if not fr4penelope:
                action Jump ("fr4penelope1")
            else:
                action Jump ("fr4penelope2")

    imagebutton:
        ypos 70
        xpos 770
        idle "images/fr4hallwaycornerpath.webp"
        hover "images/fr4hallwaycornerpathhover.webp"
        action Jump ("labelfr4hallwaycorner")

    imagebutton:
        ypos 160
        xpos 835
        idle "images/fr4hallwaydoor.webp"
        hover "images/fr4hallwaydoorhover.webp"
        action Jump ("labelfr4outsidestairs")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump ("labelfr4hallwaygymexit")

screen fr4hallwaycorner():

    if not fr4grayson:
        add "images/fr4hallwaycorner.webp"
    elif preventgrayson:
        add "images/fr4hallwaycornernumber.webp"
    else:
        add "images/fr4hallwaycornernograyson.webp"

    imagebutton:
        ypos 205
        xpos 875
        idle "images/fr4hallwaycornerdoor.webp"
        hover "images/fr4hallwaycornerdoorhover.webp"
        if fr4chloe and not preventgrayson:
            action Jump ("fr4lockerroomchloe")
        else:
            action Jump ("fr4lockerroom")

    if not fr4grayson:
        imagebutton:
            ypos 395
            xpos 320
            idle "images/fr4hallwaycornergrayson.webp"
            hover "images/fr4hallwaycornergraysonhover.webp"
            action Jump ("fr4grayson1")


    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump ("labelfr4hallway")

### Outside ###

screen fr4outsidestairs():

    if not hcGirl == "emily":
        add "images/fr4outsidestairs.webp"
    else:
        add "images/fr4outsidestairsnoemily.webp"

    if not hcGirl == "emily":
        imagebutton:
            ypos 295
            xpos 520
            idle "images/fr4outsidestairsemily.webp"
            hover "images/fr4outsidestairsemilyhover.webp"
            if not fr4emily:
                action Jump ("fr4emily1")
            else:
                action Jump ("fr4emily2")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump ("labelfr4hallway")

    imagebutton:
        yalign 0.5
        xalign 1.0
        idle "images/fr4right.webp"
        hover "images/fr4righthover.webp"
        action Jump ("labelfr4outsidestreet")

screen fr4outsidestreet():

    add "images/fr4outsidestreet.webp"

    imagebutton:
        ypos 340
        xpos 830
        idle "images/fr4outsidestreetidle.webp"
        hover "images/fr4outsidestreethover.webp"
        if not fr4samantha:
            action Jump ("fr4samantha1")
        else:
            action Jump ("fr4samantha2")

    imagebutton:
        yalign 1.0
        xalign 0.5
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump ("labelfr4outsidestairs")

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
            idle "images/riblowjob.webp"
            hover "images/riblowjob.webp"
            action Jump ("riblowjob")

        imagebutton:
            idle "images/rifingering.webp"
            hover "images/rifingering.webp"
            action Jump ("rifingering")

        imagebutton:
            idle "images/rimissionary.webp"
            hover "images/rimissionary.webp"
            action Jump ("rimissionary")

        imagebutton:
            idle "images/riclimax.webp"
            hover "images/riclimax.webp"
            action Jump ("riclimax")
