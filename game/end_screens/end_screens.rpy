screen end_screen():
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

                text "{b}UndergradSteve{/b} - Game Creator"
                text "{b}DomG{/b} - Producer"
                text "{b}KingLui{/b} - Head of Operations"
                text "{b}OscarSix{/b} - Technical Lead"

                null height 50

                text "{b}Condy{/b} - Senior Production Engineer"
                text "{b}Messy17{/b} - Head Transcriber, Renderer"
                text "{b}Mozzart{/b} - Lead Artist & Coordinator"

                null height 50

                text "{b}Vain{/b} - Marketing Director"

                null height 25

                text "{b}Nicki5617{/b} - Editor"

                null height 25

                text "{b}Jeffly{/b} - Transcriber"
                text "{b}MegaManX{/b} - Transcriber"

                null height 25

                # text "{b}Shark Hug{/b} - Animator, Renderer"
                text "{b}TheFatLebowski{/b} - Animator"

                null height 25

                text "{b}Bwonerart{/b} - Renderer"
                text "{b}François Gibon{/b} - Renderer"
                text "{b}Infrank{/b} - Renderer"
                text "{b}Mugi{/b} - Renderer"
                text "{b}Oduvan{/b} - Renderer"
                text "{b}RogueRoach{/b} - Renderer"
                text "{b}sznuk{/b} - Renderer"
                text "{b}Tr4sh P4nda{/b} - Renderer"

                null height 25

                text "{b}Stefan{/b} - Photoshopper"

                null height 25

                text "{b}ClearanceClarence{/b} - Gameplay Engineer"

                null height 25

                text "{b}spacestorm{/b} - General Assistant"

                null height 25

                text "{b}Jany{/b} - Community Liaison"

                null height 25

                text "{b}Rev{/b} - Quality Assurance Specialist"
                text "{b}RyanMK666{/b} - Quality Assurance Specialist"
                text "{b}Skepticalz{/b} - Quality Assurance Specialist"

                null height 25

                text "{b}Ana Paula Cunha{/b} - UI/UX Designer"
                text "{b}Daisa Biancalana{/b} - UI/UX Designer"
                text "{b}danielrothier{/b} - UI/UX Designer"
                text "{b}Luiza Nis{/b} - UI/UX Designer"
                text "{b}natalimartins{/b} - UI/UX Designer"

                null height 25

                text "{b}Ema9000{/b} - Human Resources Manager"

                null height 25

                text "{b}Mobi{/b} - Amendments Lead"

                null height 25

                text "{b}Sawsbucky{/b} - Assistant Game Designer"

                null height 25

                text "{b}MimeFlayer{/b} - Assistant Editor"

                null height 100

                text "Special thanks to all the community members and players who have made this possible"

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
