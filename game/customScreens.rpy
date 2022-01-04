screen alert_template(message):
    zorder 200
    modal True
    style_prefix "alert"

    python:
        message = message.upper()
        message = message.replace("{B}", "{b}")
        message = message.replace("{/B}", "{/b}")

    frame:
        align (0.5, 0.5)
        minimum (758, 363)
        background "alert_background"

        vbox:
            align (0.5, 0.5)
            spacing 45

            text _(message) xalign 0.5 xsize 650

            hbox:
                xalign 0.5
                spacing 20

                transclude


style alert_text is olympus_mount_30


screen warning_template(message, style="blue"):
    zorder 200
    modal True
    style_prefix "warning"

    frame:
        align (0.5, 0.5)
        yoffset -42
        minimum (758, 363)
        background "warning_background_{}".format(style)

        vbox:
            align (0.5, 0.5)
            spacing 45

            null height 50

            text _(message.upper()) xalign 0.5 xsize 650

            hbox:
                xalign 0.5
                spacing 20
                
                transclude

            null height 50


style warning_text is olympus_mount_30


screen real_life_mode():
    modal True

    add "images/start/real_life_mode_background.png"

    use warning_template("THIS MODE PROHIBITS you from saving during important choices, meaning all choices are final. this can't be disabled without starting a new game."):

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action [SetVariable("realmode", True), SetVariable("config.rollback_enabled", False), SetVariable("showkct", False), Show("phone_icon"), Jump("v1start")]
            xysize (215, 55)

            text "ENABLE" align (0.5, 0.5)

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action [SetVariable("realmode", False), SetVariable("config.rollback_enabled", True), SetVariable("showkct", True), Show("phone_icon"), Jump("v1start")]
            xysize (215, 55)

            text "DISABLE" align (0.5, 0.5)


screen fantasyOverlay():
    add "images/fantasyoverlay.webp"


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

    use alert_template("You've just unlocked the social media app Kiwii! Open it now from the homescreen."):

        textbutton "OK":
            xalign 0.5
            action [Function(kiwii_firstTimeMessages), SetVariable("kiwii_firstTime", False), Hide("kiwiiPopup")]


# Fight Screens
screen fightPopup(fightMove):
    modal True
    
    use alert_template("Congratulations! You have learned a new fighting move: {{b}}{}{{/b}}.".format(fightMove)):

        textbutton "OK":
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