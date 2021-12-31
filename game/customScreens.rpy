screen endfrTemplate():

    window:
        align (0.5, 0.5)
        padding (25, 50)
        xysize (746, 384)

        background "images/endfr.webp"

        transclude


screen changeLanguage():
    tag menu

    text _("Select Language") align (0.5, 0.01) size 72
    vpgrid:
        cols 1
        draggable True
        mousewheel True
        align (0.5, 0.9)
        ysize 950
        xfill True
        style_prefix "radio"
        spacing 10

        textbutton "English" text_font "DejaVuSans.ttf" action Language(None) xalign 0.5 text_size 32
        if renpy.loadable("tl/chineses/script.rpy"):
            textbutton "Chineses" text_font "DejaVuSans.ttf" action Language("chineses") xalign 0.5 text_size 32
        if renpy.loadable("tl/chineset/script.rpy"):
            textbutton "Chineset" text_font "DejaVuSans.ttf" action Language("chineset") xalign 0.5 text_size 32
        if renpy.loadable("tl/czech/script.rpy"):
            textbutton "Czech" text_font "DejaVuSans.ttf" action Language("czech") xalign 0.5 text_size 32
        if renpy.loadable("tl/francais/script.rpy"):
            textbutton "Francais" text_font "DejaVuSans.ttf" action Language("francais") xalign 0.5 text_size 32
        if renpy.loadable("tl/german/script.rpy"):
            textbutton "German" text_font "DejaVuSans.ttf" action Language("german") xalign 0.5 text_size 32
        if renpy.loadable("tl/greek/script.rpy"):
            textbutton "Greek" text_font "DejaVuSans.ttf" action Language("greek") xalign 0.5 text_size 32
        if renpy.loadable("tl/hindi/script.rpy"):
            textbutton "Hindi" text_font "DejaVuSans.ttf" action Language("hindi") xalign 0.5 text_size 32
        if renpy.loadable("tl/hungarian/script.rpy"):
            textbutton "Hungarian" text_font "DejaVuSans.ttf" action Language("hungarian") xalign 0.5 text_size 32
        if renpy.loadable("tl/italian/script.rpy"):
            textbutton "Italian" text_font "DejaVuSans.ttf" action Language("italian") xalign 0.5 text_size 32
        if renpy.loadable("tl/japanese/script.rpy"):
            textbutton "Japanese" text_font "DejaVuSans.ttf" action Language("japanese") xalign 0.5 text_size 32
        if renpy.loadable("tl/polish/script.rpy"):
            textbutton "Polish" text_font "DejaVuSans.ttf" action Language("polish") xalign 0.5 text_size 32
        if renpy.loadable("tl/portuguese/script.rpy"):
            textbutton "Portuguese" text_font "DejaVuSans.ttf" action Language("portuguese") xalign 0.5 text_size 32
        if renpy.loadable("tl/russian/script.rpy"):
            textbutton "Russian" text_font "DejaVuSans.ttf" action Language("russian") xalign 0.5 text_size 32
        if renpy.loadable("tl/spanish/script.rpy"):
            textbutton "Spanish" text_font "DejaVuSans.ttf" action Language("spanish") xalign 0.5 text_size 32
        if renpy.loadable("tl/thai/script.rpy"):
            textbutton "Thai" text_font "DejaVuSans.ttf" action Language("thai") xalign 0.5 text_size 32
        if renpy.loadable("tl/turkish/script.rpy"):
            textbutton "Turkish" text_font "DejaVuSans.ttf" action Language("turkish") xalign 0.5 text_size 32
        if renpy.loadable("tl/vietnamese/script.rpy"):
            textbutton "Vietnamese" text_font "DejaVuSans.ttf" action Language("vietnamese") xalign 0.5 text_size 32

    textbutton _("Return"):
        align (0.99, 0.99)
        action ShowMenu("settings")


screen realmode():
    modal True
    
    add "images/REALLIFEMODE.webp"

    imagebutton:
        pos (417, 683)
        idle "images/rlmt.webp"
        hover "images/enable.webp"
        action [SetVariable("realmode", True), SetVariable("config.rollback_enabled", False), SetVariable("showkct", False), Show("phone_icon"), Jump("v1start")]

    imagebutton:
        pos (1016, 683)
        idle "images/rlmt.webp"
        hover "images/disable.webp"
        action [SetVariable("realmode", False), SetVariable("config.rollback_enabled", True), SetVariable("showkct", True), Show("phone_icon"), Jump("v1start")]


screen fantasyOverlay():
    add "images/fantasyoverlay.webp"


screen endFreeRoamConfirm(continueLabel):
    modal True
    
    use endfrTemplate:

        text "Are you sure you want to end free roam?":
            style "endfree"
            xalign 0.5

        hbox:
            align (0.5, 1.0)
            spacing 200

            textbutton "Yes":
                action [Hide("endFreeRoamConfirm"), Jump(continueLabel)]
                
            textbutton "No":
                action Hide("endFreeRoamConfirm")


screen censoredPopup(continueLabel):
    modal True

    add "gui/censoredPopup/censoredBackground.webp"

    vbox:
        pos (365, 566)
        spacing 148

        if config_censored:
            imagebutton:
                idle "gui/censoredPopup/censoredSettings.webp"
                hover "gui/censoredPopup/censoredSettingsHover.webp"
                action ShowMenu("settings")
        else:
            imagebutton:
                idle "gui/censoredPopup/censoredContinue.webp"
                hover "gui/censoredPopup/censoredContinueHover.webp"
                action Return()

        imagebutton:
            idle "gui/censoredPopup/censoredSkipScene.webp"
            hover "gui/censoredPopup/censoredSkipSceneHover.webp"
            action Jump(continueLabel)


screen timerBar(seconds=3):
    bar value AnimatedValue(0, seconds, seconds, seconds) at alpha_dissolve


# Kiwii Screens
screen kiwiiPopup():
    modal True
    zorder 200

    use endfrTemplate:

        text "You've just unlocked the social media app Kiwii! Open it now from the homescreen.":
            style "endfree"
            xalign 0.5

        textbutton "OK":
            align (0.5, 1.0)
            action [Function(kiwii_firstTimeMessages), SetVariable("kiwii_firstTime", False), Hide("kiwiiPopup")]


# Fight Screens
screen fightPopup(fightMove):
    modal True
    
    use endfrTemplate:

        text "Congratulations! You have learned a new fighting move: {b}[fightMove]{/b}.":
            style "endfree"
            xalign 0.5

        textbutton "OK":
            align (0.5, 1.0)
            action Return()


screen fightDamage():
    if youDamage == 3:
        add "images/3 hits.webp"
    elif youDamage == 4:
        add "images/4 hits.webp"
    elif youDamage >= 5:
        add "images/5 hits.webp"


# Steam Screens
screen steam_end(link="https://store.steampowered.com/app/1463120/College_Kings__Act_I/"):
    tag credits
    modal True
    zorder 100

    add "images/steam/end_screen.webp"

    imagebutton:
        idle "images/steam/playNow.webp"
        hover "images/steam/playNowHover.webp"

        if achievement.steam.dlc_installed(1624520):
            action Function(renpy.quit, relaunch=True, save=True)
        elif achievement.steam.is_overlay_enabled():
            action Function(achievement.steam.activate_overlay_to_web_page, link)
        else:
            action OpenURL(link)
        align (0.5, 0.55)

    hbox:
        spacing 50
        xpos 20
        yalign 1.0

        textbutton "Main Menu":
            text_style "steam_endScreenTextButton"
            action MainMenu()

        textbutton "Credits":
            text_style "steam_endScreenTextButton"
            action Jump("gameEnd")

        textbutton "The Team":
            text_style "steam_endScreenTextButton"
            action Show("teamCredits")


screen steam_join_discord():
    tag credits
    modal True
    zorder 100

    add "images/steam/end_screen_discord.webp"

    imagebutton:
        idle "images/discordbutton1.webp"
        hover "images/discordbutton2.webp"
        action OpenURL("https://discord.gg/collegekings")
        align (0.5, 0.65)

    hbox:
        spacing 50
        xpos 20
        yalign 1.0

        textbutton "Main Menu":
            text_style "steam_endScreenTextButton"
            action MainMenu()

        textbutton "Credits":
            text_style "steam_endScreenTextButton"
            action Jump("gameEnd")

        textbutton "The Team":
            text_style "steam_endScreenTextButton"
            action Show("teamCredits")


# End Screens
screen getaccess():
    tag endScreen

    add "images/end_screen.webp"

    hbox:
        align (0.5, 0.9)
        spacing 100

        textbutton "MENU":
            action MainMenu()
            yalign 0.5
            text_size 100

        imagebutton:
            idle "images/get.webp"
            hover "images/get.webp"
            action OpenURL("https://www.patreon.com/collegekings")
            align (0.5, 0.65)

        textbutton "Credits":
            action Jump("credits")
            yalign 0.5
            text_size 100


screen credits():
    tag endScreen
    modal True
    zorder 100

    if config.enable_steam:
        add "images/steamCredits.webp"
    else:
        add "images/patreonCredits.webp"

    if config.enable_steam:
        imagebutton:
            xalign 0.5
            ypos 675
            idle "images/discordbutton1.webp"
            hover "images/discordbutton2.webp"
            action OpenURL ("http://discord.collegekingsgame.com")
    else:
        imagebutton:
            pos (394, 677)
            idle "images/supportdevelopmentblank.webp"
            hover "images/supportdevelopment.webp"
            action OpenURL ("https://www.patreon.com/collegekings")

    hbox:
        xalign 0.5
        ypos 950
        spacing 50

        textbutton "Main Menu":
            text_style "steam_endScreenTextButton"
            action MainMenu()

        textbutton "The Team":
            text_style "steam_endScreenTextButton"
            action Show("teamCredits")


screen teamCredits():
    tag endScreen
    modal True
    zorder 100

    add "images/stockBackgrounds/eveningSunshine.webp"

    text "Team Credits":
        xalign 0.5
        ypos 15
        size 72

    hbox:
        align (0.5, 0.5)
        spacing 300

        vbox:
            spacing 10

            text "UndergradSteve - Game Creator"
            text "KingLui - Project Manager"
            text "OscarSix - Chief Technical Officer"
            null height 20
            text "Oskin - Lead Enforcer"
            text "Lucious Lordswill - Lead Writer"
            text "Cheexmarie - Lead Editor"
            text "Peace - Head Transcriber"
            text "Condy - Quality Assurance Manager"
            text "Jany - Translation Manager"
            text "Mozzart - Lead Artist & Coordinator"
            null height 20
            text "Maro - Marketing Specialist"
            text "HugeBoiV2 - Transcriber"
            text "Jeffly - Transcriber"

        vbox:
            spacing 10

            text "MegaManX - Transcriber"
            text "mstep17 - Transcriber"
            text "SystemFailed - Transcriber"
            text "Wolf - Transcriber"
            text "Dorkby - Animator"
            text "Wiebley - Renderer"
            text "Ranger - 3d Modeler"
            text "François Gibon - Renderer"
            text "3D4FUN - Renderer"
            text "Bwonerart - Renderer"
            text "Sznuk - Renderer"
            text "Raystorm41 - Render"
            text "Stefan - Photoshopper"
            text "Space-Storm - Tech Assistant"

    text "Special thanks to all the community members and players who have made this project possible :)":
        align (0.5, 0.9)
        size 24

    hbox:
        spacing 50
        xpos 20
        yalign 1.0

        textbutton "Main Menu":
            text_style "steam_endScreenTextButton"
            action MainMenu()

        textbutton "Credits":
            text_style "steam_endScreenTextButton"
            action Jump("credits")