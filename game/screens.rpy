## Initialization
################################################################################

init python:
    yadjValue = float("inf")
    yadj = ui.adjustment()
    
    inf_adj = ui.adjustment()
    inf_adj.value = float("inf")

init offset = -1


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


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style say_window:
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

style input_window is say_window


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice


screen choice(items, seconds=3, fail_label=None):
    style_prefix "choice"
    # Show KCT
    if showkct and len(items) > 1:
        use kct_choice_hint
    
    hbox:
        xalign 0.5
        ypos 833
        spacing 25

        for item in items:
            button:
                idle_background "choice_button_idle"
                hover_background "choice_button_hover"
                action item.action
                minimum (550, 131)
                
                text item.caption.upper():
                    align (0.5, 0.5)

    if fail_label is not None:
        timer seconds:
            action Jump(fail_label)

        use timerBar(seconds)

    if config_debug:
        $ item = renpy.random.choice(items)
        on "show" action item.action


style choice_text is olympus_mount_30

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    zorder 100
    style_prefix "quick_menu"

    default image_path = "gui/quick_menu/"

    if quick_menu:
        hbox:
            align (0.5, 1.0)
            yoffset -40
            spacing 30

            if not realmode:
                imagebutton idle image_path + "rollback_idle.png" action Rollback()
            imagebutton idle image_path + "history_idle.png" action ShowMenu("history")
            imagebutton idle image_path + "skip_idle.png" action Skip() alternate Skip(fast=True, confirm=True)
            imagebutton idle image_path + "auto_forward_idle.png" action Preference("auto-forward", "toggle")
            imagebutton idle image_path + "save_idle.png" action ShowMenu("save")
            imagebutton idle image_path + "quick_save_idle.png" action QuickSave()
            imagebutton idle image_path + "quick_load_idle.png" action QuickLoad()
            # textbutton _("Prefs") action ShowMenu("preferences")

    if config.developer:
        hbox:
            align (1.0, 1.0)
            xoffset -20
            spacing 15

            textbutton "SCENE SELECT" action Show("bugTesting_SceneSelect")
            add "gui/common/arrow.png" yalign 0.5

            null width 10

            textbutton "CHEATS" action Show("bugTesting_cheatMenu")
            add "gui/common/arrow.png" yalign 0.5


style quick_menu_button:
    align (0.5, 0.5)

style quick_menu_button_text is olympus_mount_30


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    tag menu
    style_prefix "main_menu"

    default image_path = "gui/main_menu/"

    add image_path + "background.webp"

    # Patreon
    if not config.enable_steam:
        imagebutton:
            idle image_path + "patreon_idle.webp"
            hover Transform(image_path + "patreon_hover.webp", xpos=-28)
            action OpenURL("https://www.patreon.com/collegekings")
            pos (118, 36)

    # Discord
    imagebutton:
        idle image_path + "discord_idle.webp"
        hover Transform(image_path + "discord_hover.webp", xpos=-22)
        action OpenURL("https://discord.gg/collegekings")
        pos (1311, 30)

    # Scene Gallery
    imagebutton:
        pos (141, 811)
        idle image_path + "scene_gallery_idle.webp"
        hover Transform(image_path + "scene_gallery_hover.webp", pos=(-22, -22))
        action Show("confirm",
            message="Warning: The scene gallery contains spoilers for the story of the game. Are you sure you want to continue?",
            yes_action=[Hide("confirm"), ui.callsinnewcontext("scene_gallery_name_change"), ShowMenu("scene_gallery")],
            no_action=Hide("confirm"))


    # Path Builder
    imagebutton:
        idle image_path + "path_builder_idle.webp"
        hover Transform(image_path + "path_builder_hover.webp", pos=(-20, -20))
        action ShowMenu("path_builder_alert")
        pos (1454, 811)

    # Play Now
    imagebutton:
        idle image_path + "play_now_idle.webp"
        hover Transform(image_path + "play_now_hover.webp", pos=(-31, -31))
        action Start()
        pos (564, 880)

    # Load
    imagebutton:
        idle image_path + "load_idle.webp"
        hover Transform(image_path + "load_hover.webp", pos=(-27, -31))
        action ShowMenu("load")
        pos (1096, 880)

    # LEARN MORE
    imagebutton:
        idle image_path + "learn_more_idle.webp"
        hover Transform(image_path + "learn_more_hover.webp", pos=(-40, -33))
        action OpenURL("http://collegekingsgame.com")
        pos (303, 976)


    # SETTINGS
    imagebutton:
        idle "settings_idle"
        hover "settings_hover"
        action ShowMenu("preferences")
        pos (1439, 967)

    # QUIT
    imagebutton:
        idle "quit_idle"
        hover "quit_hover"
        action Quit()
        pos (1662, 971)


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

    if title == _("History"):
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

        label title

    else:
        transclude

    hbox:
        style_prefix "navigation"
        align (0.5, 0.95)
        spacing gui.navigation_spacing
        xsize gui.navigation_width

        textbutton _("Return") action Return()

        if title == _("Save"):
            textbutton _("Load") action ShowMenu("load")
        else:
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Settings") action ShowMenu("preferences")

        textbutton _("Menu") action MainMenu()

        textbutton _("Quit") action Quit(confirm=not main_menu)

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


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():
    tag menu

    use file_slots(_("Save"))


screen enter_save_name(slot):
    tag menu
    style_prefix "save"

    use save

    text "SAVE NAME:" pos (270, 240)
    
    frame:
        xysize (1083, 99)
        pos (477, 210)
        background "gui/file_slots/save_name.png"

        input:
            align (0.5, 0.5)
            default save_name
            copypaste True
            value VariableInputValue("save_name")
            allow " .,_-0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

        imagebutton:
            idle "gui/file_slots/save_game_idle.png"
            action [Show("save"), FileAction(slot)]
            align (1.0, 0.5)


style save_text is file_slot_text
style save_input is text:
    font "fonts/Montserrat-Bold.ttf"
    size 36


screen load():
    tag menu

    use file_slots(_("Load"))


screen file_slots(title):
    style_prefix "file_slots"

    default page_name_value = FilePageNameInputValue(pattern=_("PAGE {}"), auto=_("AUTOMATIC SAVES"), quick=_("QUICK SAVES"))
    default image_path = "gui/file_slots/"

    python:
        incompatible_game_versions = {"12.0.0", "0.6.4"}
        incompatible_renpy_versions = {"7.4.8.1895", "7.4.7.1862"}

        game_version = FileJson(1, key="_version") or ""
        renpy_version = FileJson(1, key="_renpy_version") or ""
        renpy_version = '.'.join(str(i) for i in renpy_version)
        file_compatable = not (game_version in incompatible_game_versions or renpy_version in incompatible_renpy_versions)

    add image_path + "background.png"

    text "{} Game".format(title):
        xalign 0.5
        ypos 56
        style "file_slots_title"

    imagebutton:
        idle image_path + "return_idle.png"
        action Return()
        pos (129, 82)

    fixed:
        pos (243, 206)
        xysize (1430, 588)

        if not renpy.get_screen("enter_save_name"):
            button:
                xalign 0.5
                ypos 35
                action page_name_value.Toggle()
                key_events True

                input:
                    style "file_slots_page_name"
                    value page_name_value

        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            xalign 0.5
            ypos 110
            spacing 35

            for slot in range(1, gui.file_slot_cols * gui.file_slot_rows + 1):
                python:
                    game_version = FileJson(slot, key="_version") or ""
                    renpy_version = FileJson(slot, key="_renpy_version") or ""
                    renpy_version = '.'.join(str(i) for i in renpy_version)
                    file_compatable = not (game_version in incompatible_game_versions or renpy_version in incompatible_renpy_versions)


                button:
                    background Transform(FileScreenshot(slot), size=(config.thumbnail_width, config.thumbnail_height))
                    if title == _("Save"):
                        action Show("enter_save_name", slot=slot)
                    else:
                        action FileAction(slot)
                    xysize (config.thumbnail_width, config.thumbnail_height)

                    if file_compatable:
                        vbox:
                            align (0.5, 1.0)

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")).upper() xalign 0.5
                            text FileSaveName(slot).upper() xalign 0.5
                    else:
                        add image_path + "incompatible.png" xalign 0.5 yoffset -7

                    key "save_delete" action FileDelete(slot)

    # Buttons to access other pages.
    hbox:
        xalign 0.5
        ypos 803
        xysize (1100, 48)
        spacing 35
        xoffset 20

        imagebutton:
            idle image_path + "left_arrow.png"
            action FilePagePrevious()
            yalign 0.5

        if config.has_autosave:
            textbutton _("{#auto_page}A") action FilePage("auto") yalign 0.5

        if config.has_quicksave:
            textbutton _("{#quick_page}Q") action FilePage("quick") yalign 0.5

        for page in range(1, 10):
            textbutton str(page) action FilePage(page) yalign 0.5

        textbutton "99" action FilePage(99) yalign 0.5

        imagebutton:
            idle image_path + "right_arrow.png"
            action FilePageNext()
            yalign 0.5

    # Menu buttons
    if title == _("Save"):
        imagebutton:
            idle image_path + "load_idle.png"
            action ShowMenu("load")
            pos (129, 967)
    else:
        imagebutton:
            idle image_path + "save_idle.png"
            action ShowMenu("save")
            pos (129, 967)

    imagebutton:
        idle image_path + "menu_idle.png"
        action MainMenu()
        pos (314, 975)

    imagebutton:
        idle "settings_idle"
        hover "settings_hover"
        action ShowMenu("preferences")
        pos (1439, 967)

    imagebutton:
        idle "quit_idle"
        hover "quit_hover"
        action Quit(confirm=not main_menu)
        pos (1662, 971)


style file_slots_title is text:
    font "fonts/Montserrat-ExtraBold.ttf"
    size 64

style file_slots_page_name is olympus_mount_30

style file_slots_text is olympus_mount_30:
    size 22
    yoffset 2

style file_slots_button_text is druk_wide_bold_22


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    tag menu
    style_prefix "settings"

    default image_path = "gui/settings/"

    add image_path + "background.webp"

    # Display
    hbox:
        pos (171, 278)
        spacing 22

        fixed:
            xysize (339, 61)

            imagebutton:
                idle "blue_button_idle"
                hover "blue_button_hover"
                selected_idle "blue_button_hover"
                action Preference("display", "window")
            text "Window" align (0.5, 0.5)

        fixed:
            xysize (339, 61)

            imagebutton:
                idle "blue_button_idle"
                hover "blue_button_hover"
                selected_idle "blue_button_hover"
                action Preference("display", "fullscreen")
            text "Full Screen" align (0.5, 0.5)

    # Skip
    hbox:
        pos (171, 452)
        spacing 22

        fixed:
            xysize (339, 61)

            imagebutton:
                idle "blue_button_idle"
                hover "blue_button_hover"
                selected_idle "blue_button_hover"
                action Preference("skip", "toggle")
            text "Unseen Text" align (0.5, 0.5)

        fixed:
            xysize (339, 61)

            imagebutton:
                idle "blue_button_idle"
                hover "blue_button_hover"
                selected_idle "blue_button_hover"
                action Preference("after choices", "toggle")
            text "After Choices" align (0.5, 0.5)

    # Other Settings
    vbox:
        pos (618, 663)
        spacing 22

        for variable in ("config_censored", "voice_acted", "showkct"):
            hbox:
                spacing 6

                fixed:
                    xysize (137, 61)

                    imagebutton:
                        idle "blue_button_idle"
                        hover "blue_button_hover"
                        selected_idle "blue_button_hover"
                        action SetVariable(variable, True)
                    text "On" align (0.5, 0.5)

                fixed:
                    xysize (137, 61)

                    imagebutton:
                        idle "blue_button_idle"
                        hover "blue_button_hover"
                        selected_idle "blue_button_hover"
                        action SetVariable(variable, False)
                    text "Off" align (0.5, 0.5)

        # REAL LIFE MODE
        hbox:
            spacing 6

            fixed:
                xysize (137, 61)

                imagebutton:
                    idle "blue_button_idle"
                    hover "blue_button_hover"
                    selected_idle "blue_button_hover"
                    selected realmode
                    action [SetVariable("realmode", True), SetVariable("config.rollback_enabled", False), SetVariable("showkct", False)]
                text "On" align (0.5, 0.5)

            fixed:
                xysize (137, 61)

                imagebutton:
                    idle "blue_button_idle"
                    hover "blue_button_hover"
                    selected_idle "blue_button_hover"
                    selected not realmode
                    action [SetVariable("realmode", False), SetVariable("config.rollback_enabled", True)]
                text "Off" align (0.5, 0.5)

    bar value Preference("text speed"):
        pos (1022, 353)
        xysize (725, 37)
        left_bar "settings_bar_left"
        right_bar "settings_bar_right"
        thumb "settings_bar_thumb"
        thumb_offset 20

    bar value Preference("auto-forward time"):
        pos (1022, 490)
        xysize (725, 37)
        left_bar "settings_bar_left"
        right_bar "settings_bar_right"
        thumb "settings_bar_thumb"
        thumb_offset 20

    bar value Preference("music volume"):
        pos (1022, 791)
        xysize (725, 37)
        left_bar "settings_bar_left"
        right_bar "settings_bar_right"
        thumb "settings_bar_thumb"
        thumb_offset 20

    bar value Preference("sound volume"):
        pos (1022, 928)
        xysize (725, 37)
        left_bar "settings_bar_left"
        right_bar "settings_bar_right"
        thumb "settings_bar_thumb"
        thumb_offset 20

    imagebutton:
        idle "gui/settings/return_idle.webp"
        action Return()
        pos (129, 82)

# style settings_imagebutton:
#     idle "blue_button_idle"
#     hover "blue_button_hover"
#     selected_idle "blue_button_hover"


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
    xsize 755

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

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

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


################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action=Hide("confirm")):
    zorder 200
    modal True
    style_prefix "confirm"

    use alert_template(message):

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action yes_action
            xysize (215, 55)

            text "YES" align (0.5, 0.5)

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action no_action
            xysize (215, 55)

            text "NO" align (0.5, 0.5)

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_text is olympus_mount_30


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
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

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

# for compatibility
screen ingmenu():
    use save 