init 999 python:
    try:
        import _renpysteam as steamAPI
    except ImportError:
        config.enable_steam = False


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
    
    add "images/endfr.webp"

    text "Are you sure you want to end free roam?" style "endfree"

    textbutton "Yes":
        style "endfr"
        action [Hide("endFreeRoamConfirm"), SetVariable("freeRoam", False), Jump(continueLabel)]
        text_align 0.5
        align (0.43, 0.58)

    textbutton "No":
        style "endfr"
        action Hide("endFreeRoamConfirm")
        text_align 0.5
        align (0.57, 0.58)


screen censoredPopup(continueLabel):
    modal True

    add "censoredPopup_background"

    vbox:
        xpos 15

        text "Censorship Mode: {}".format("{color=#0f0}Enabled" if config_censored else "{color=#f00}Disabled")
        text "You can disable censorship mode in the game settings":
            size 12

    vbox:
        xalign 0.5
        ypos 200
        spacing 165

        text "The following scenes have NSFW content.\nUse the \"Skip Scene\" button below to skip over this scene.":
            text_align 0.5

        hbox:
            spacing 250

            textbutton "Skip Scene":
                action Jump(continueLabel)

            textbutton "Continue":
                action Return()

        text "To get the full uncensored version head over to {a=https://www.patreon.com/collegekings}{color=#72bcef}College King's Patreon":
            size 24


screen kiwiiPopup():
    modal True

    add "images/endfr.webp"

    text "You've just unlocked the social media app Kiwii! Open it now from the homescreen." style "endfree"

    textbutton "OK":
        style "endfr"
        action [SetVariable("kiwii_firstTime", False), Hide("kiwiiPopup")]
        text_align 0.5
        align (0.5, 0.58)


screen fightPopup(fightMove):
    modal True
    add "images/endfr.webp"

    text "Congratulations! You have learned a new fighting move: {b}[fightMove]{/b}." style "endfree"

    textbutton "OK" style "endfr":
        action Return()
        text_align 0.5
        align (0.5, 0.58)


screen kctPopup():
    modal True
    zorder 300

    add "images/endfr.webp"

    text "Congratulations! Your Key Character Trait {b}[kct]{/b} has just changed the outcome of a decision someone was making." style "endfree"

    textbutton "OK":
        style "endfr"
        action Return()
        text_align 0.5
        align (0.5, 0.58)


screen steam_end(link="https://store.steampowered.com/app/1463120/College_Kings__Act_I/"):
    add "images/steam/steam_endscreen.webp"

    imagebutton:
        idle "images/steam/steam_wishlist.webp"
        hover "images/steam/steam_wishlistHover.webp"

        if steamAPI.is_overlay_enabled():
            action Function(steamAPI.activate_overlay_to_web_page, link)
        else:
            action OpenURL(link)
        align (0.5, 0.55)

    hbox:
        spacing 20
        xpos 20
        yalign 1.0

        textbutton "Menu":
            text_style "steam_endScreenTextButton"
            action MainMenu()

        textbutton "Credits":
            text_style "steam_endScreenTextButton"
            action Return()


screen credits():
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

    textbutton "Main Menu":
        text_underline True
        text_size 50
        text_font "fonts/Freshman.ttf"
        ypos 952
        xalign 0.5
        text_align 0.5
        action MainMenu()


screen teamCredits():
    modal True

    add "#000"

    hbox:
        xalign 0.5
        ypos 10
        spacing 200

        vbox:
            spacing 10

            text "Undergrad Steve - Game Leader" xalign 0.5
            text "OscarSix - Lead Coder" xalign 0.5
            text "Lew - Lead Artist" xalign 0.5
            text "KingLui - Project Manager" xalign 0.5
            null height 20
            text "Hive - Lead Transcriber" xalign 0.5
            text "Lucious Lordswill - Lead Writer" xalign 0.5
            text "Condy - Lead Beta Tester" xalign 0.5
            text "Oskin - Quality Assurance Manager" xalign 0.5
            text "Jany - Translation Manager" xalign 0.5
            null height 20
            text "Maro - Marketing Specialist" xalign 0.5
            text "OK-HAN - Marketing Specialist" xalign 0.5
            null height 20
            text "Grimlord - Assistant Writer" xalign 0.5
            text "Cheyenne Alexander - Editor" xalign 0.5
            text "RCS - Transcriber" xalign 0.5
            text "Peace - Transcriber" xalign 0.5
            text "Jeffly - Transcriber" xalign 0.5
            text "Dorkby - Animator" xalign 0.5
            text "Wiebley - Renderer" xalign 0.5

        vbox:
            spacing 10

            text "Ranger - 3d Modeler" xalign 0.5
            text "François Gibon - Renderer" xalign 0.5
            text "3D4FUN - Renderer" xalign 0.5
            text "Bwonerart - Renderer" xalign 0.5
            text "Sznuk - Renderer" xalign 0.5
            text "Stefan - Photoshopper" xalign 0.5
            text "Spacestorm - Assistant" xalign 0.5
            text "Gillzo - Intern" xalign 0.5
            text "Krispik - Translator" xalign 0.5
            text "Schcopeck - Translator" xalign 0.5
            text "KFar - Translator" xalign 0.5
            text "Peace - Translator" xalign 0.5
            text "Bibs - Translator" xalign 0.5
            text "Arkell - Translator" xalign 0.5
            text "Differ - Translator" xalign 0.5
            text "Marx Weber - Translator" xalign 0.5
            text "Rst - Translator" xalign 0.5
            text "Thyg - Translator" xalign 0.5
            text "Wolf - Beta Tester" xalign 0.5
            text "SamZwill - Beta Tester" xalign 0.5
        
        vbox:
            spacing 10

            text "Kass - Beta Tester" xalign 0.5
            text "Dikless - Idea Generator" xalign 0.5
