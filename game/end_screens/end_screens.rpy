screen end_screen(support_link="https://store.steampowered.com/app/1924480/College_Kings_2__Episode_1/"):
    tag end_screen
    modal True
    style_prefix "end_screen"

    default image_path = "gui/end_screen/"

    if config.enable_steam:
        add image_path + "end_screen_background_steam.webp"
        default support_link = "https://store.steampowered.com/app/1924480/College_Kings_2__Act_I/"

    else:
        add image_path + "end_screen_background.webp"
        default support_link = "https://www.patreon.com/collegekings"

    hbox:
        xalign 0.5
        ypos 800
        spacing 50

        imagebutton:
            idle image_path + "menu_idle.webp"
            hover image_path + "menu_hover.webp"
            action MainMenu()
            yalign 0.5

        imagebutton:
            idle image_path + "get_access_idle.webp"
            hover image_path + "get_access_hover.webp"
            action OpenURL(support_link)
            yalign 0.5

        imagebutton:
            idle "gui/common/credits_idle.webp"
            hover "gui/common/credits_hover.webp"
            action Show("patreon_credits", None, support_link)
            yalign 0.5

    on "show" action Hide("phone_icon")
    on "hide" action Show("phone_icon")
    on "replace" action Hide("phone_icon")
    on "replaced" action Show("phone_icon")


screen team_credits():
    tag end_screen
    modal True
    style_prefix "team_credits"

    default image_path = "gui/end_screen/"

    add image_path + "team_credits_background.webp"

    fixed:
        ysize 890
        ypos 125

        viewport:
            mousewheel True
            ysize 850
            yalign 0.5

            vbox:
                xfill True

                text _("{b}UndergradSteve{/b} - Game Creator")
                text _("{b}DomG{/b} - Producer")
                text _("{b}KingLui{/b} - Head of Operations")
                text _("{b}OscarSix{/b} - Chief Technology Officer")

                null height 50

                text _("{b}Condy{/b} - Senior Production Engineer")
                text _("{b}Messy17{/b} - Head Transcriber, Renderer")
                text _("{b}Mozzart{/b} - Lead Artist & Coordinator")

                null height 50

                text _("{b}Vain{/b} - Marketing Director")

                null height 25

                text _("{b}Nicki5617{/b} - Editor")

                null height 25

                text _("{b}Jeffly{/b} - Transcriber")
                text _("{b}MegaManX{/b} - Transcriber")

                null height 25

                text _("{b}TheFatLebowski{/b} - Animator")

                null height 25

                text _("{b}Bwonerart{/b} - Renderer")
                text _("{b}François Gibon{/b} - Renderer")
                text _("{b}Infrank{/b} - Renderer")
                text _("{b}Mugi{/b} - Renderer")
                text _("{b}Oduvan{/b} - Renderer")
                text _("{b}RogueRoach{/b} - Renderer")
                text _("{b}sznuk{/b} - Renderer")
                text _("{b}Tr4sh P4nda{/b} - Renderer")

                null height 25

                text _("{b}Stefan{/b} - Photoshopper")

                null height 25

                text _("{b}ClearanceClarence{/b} - Gameplay Engineer")

                null height 25

                text _("{b}spacestorm{/b} - General Assistant")

                null height 25

                text _("{b}Jany{/b} - Community Liaison")

                null height 25

                text _("{b}Rev{/b} - Quality Assurance Specialist")
                text _("{b}RyanMK666{/b} - Quality Assurance Specialist")
                text _("{b}Skepticalz{/b} - Quality Assurance Specialist")

                null height 25

                text _("{b}Ana Paula Cunha{/b} - UI/UX Designer")
                text _("{b}Daisa Biancalana{/b} - UI/UX Designer")
                text _("{b}danielrothier{/b} - UI/UX Designer")
                text _("{b}Luiza Nis{/b} - UI/UX Designer")
                text _("{b}natalimartins{/b} - UI/UX Designer")

                null height 25

                text _("{b}Ema9000{/b} - Human Resources Manager")

                null height 25

                text _("{b}Mobi{/b} - Amendments Lead")

                null height 25

                text _("{b}Sawsbucky{/b} - Assistant Game Designer")

                null height 25

                text _("{b}MimeFlayer{/b} - Assistant Editor")

                null height 100

                text _("Special thanks to all the community members and players who have made this possible")

    hbox:
        align (0.5, 1.0)

        imagebutton:
            idle image_path + "main_menu_idle.webp"
            hover image_path + "main_menu_hover.webp"
            action MainMenu()
            yalign 0.5

        imagebutton:
            idle Transform("gui/common/credits_idle.webp", zoom=0.72)
            hover Transform("gui/common/credits_hover.webp", zoom=0.72)
            action Show("patreon_credits")
            yalign 0.5

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    on "replace" action SetVariable("quick_menu", False)
    on "replaced" action SetVariable("quick_menu", True)


style end_screen_text is montserrat_extra_bold_64

style team_credits_text is text:
    font "fonts/Montserrat-Regular.ttf"
    size 36
    xalign 0.5
