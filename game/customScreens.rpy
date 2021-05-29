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

    add "images/censoredPopup/censoredPopup_background.webp"

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