screen endfrTemplate():

    window:
        align (0.5, 0.5)
        padding (25, 50)
        xysize (746, 384)

        background "images/endfr.webp"

        # add "#00ff0080"
        transclude

screen realmode():
    modal True
    
    add "images/REALLIFEMODE.webp"

    imagebutton:
        pos (417, 683)
        idle "images/rlmt.webp"
        hover "images/enable.webp"
        action [SetVariable("realmode", True), SetVariable("config.rollback_enabled", False), SetVariable("showkct", False), Show("phoneIcon"), Jump("v1start")]

    imagebutton:
        pos (1016, 683)
        idle "images/rlmt.webp"
        hover "images/disable.webp"
        action [SetVariable("realmode", False), SetVariable("config.rollback_enabled", True), SetVariable("showkct", True), Show("phoneIcon"), Jump("v1start")]


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
                action [Hide("endFreeRoamConfirm"), SetVariable("freeRoam", False), Jump(continueLabel)]
                
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
                action ShowMenu("preferences")
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
            action [SetVariable("kiwii_firstTime", False), Hide("kiwiiPopup")]

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


# KCT Screens
screen kctChoice():
    fixed:
        xysize (298, 76)
        xalign 1.0

        add "gui/kct.webp"
        text kct:
            align (0.5, 0.5)
            font "fonts/Freshman.ttf"
            size 40
            if kct == "popular":
                color "#53d769"
            if kct == "loyal":
                color "#fecb2e"
            if kct == "confident":
                color "#fc3d39"


screen kctPopup():
    modal True
    zorder 300

    use endfrTemplate:

        text "Congratulations! Your Key Character Trait {b}[kct]{/b} has just changed the outcome of a decision someone was making.":
            style "endfree"
            xalign 0.5

        textbutton "OK":
            align (0.5, 1.0)
            action Return()

# Steam Screens
screen steam_end(link="https://store.steampowered.com/app/1463120/College_Kings__Act_I/"):
    tag credits
    modal True
    zorder 100

    add "images/steam/endScreen.webp"

    imagebutton:
        idle "images/steam/playNow.webp"
        hover "images/steam/playNowHover.webp"

        if achievement.steam.dlc_installed(1624520):
            action [Function(renpy.quit, relaunch=True, save=True)]
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

# End Screens
screen getaccess():
    tag endScreen

    add "images/endscreen.webp"

    hbox:
        align (0.5, 0.9)
        spacing 100

        textbutton "MENU":
            action MainMenu()
            yalign 0.5
            text_size 100

        imagebutton:
            idle "images/get.webp"

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

            text "UndergradSteve - Game Designer"
            text "KingLui - Project Manager"
            text "OscarSix - Lead Programmer"
            text "Lew - Lead Artist"
            null height 20
            text "Oskin - Lead Enforcer"
            text "Lucious Lordswill - Lead Writer"
            text "Hive - Lead Transcriber"
            text "Condy - Quality Assurance Manager"
            text "Jany - Translation Manager"
            null height 20
            text "Maro - Marketing Specialist"
            text "Cheyenne Alexander - Editor"

        vbox:
            spacing 10

            text "Peace - Transcriber"
            text "Wolf - Transcriber"
            text "Jeffly - Transcriber"
            text "Dorkby - Animator"
            text "Wiebley - Renderer"
            text "Ranger - 3d Modeler"
            text "François Gibon - Renderer"
            text "3D4FUN - Renderer"
            text "Bwonerart - Renderer"
            text "Sznuk - Renderer"
            text "Raystorm41 - Render"
            text "Stefan - Photoshopper"

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