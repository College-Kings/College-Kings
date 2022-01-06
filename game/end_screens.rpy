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
