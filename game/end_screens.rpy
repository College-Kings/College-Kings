screen end_screen(support_link="https://www.patreon.com/collegekings"):
    tag end_screen
    modal True
    style_prefix "end_screen"

    default image_path = "gui/end_screen/"

    add image_path + "end_screen_background.webp"

    vbox:
        xalign 0.5
        ypos 345

        text "ACT 4 PART 3" xalign 0.5
        text "Coming Soon!" color "#EA54E8" xalign 0.5

    if not config.enable_steam:
        hbox:
            xalign 0.5
            ypos 556
            spacing 20

            text "Exclusively on " size 40 yalign 0.5

            hbox:
                spacing 10

                imagebutton:
                    idle image_path + "patreon_logo.webp"
                    action OpenURL("https://www.patreon.com/collegekings")
                    yalign 0.5

                imagebutton:
                    idle image_path + "patreon_wordmark.webp"
                    action OpenURL("https://www.patreon.com/collegekings")
                    yalign 0.5

    hbox:
        xalign 0.5
        ypos 764
        spacing 100

        imagebutton:
            idle image_path + "menu_idle.webp"
            action MainMenu()
            yalign 0.5

        if not config.enable_steam:
            imagebutton:
                idle image_path + "get_access_idle.webp"
                action OpenURL(support_link)
                yalign 0.5

        imagebutton:
            idle image_path + "credits_idle.png"
            action Show("patreon_credits", None, support_link)
            yalign 0.5


screen patreon_credits(support_link="https://www.patreon.com/collegekings"):
    tag end_screen
    modal True
    style_prefix "patreon_credits"

    default image_path = "gui/end_screen/"

    add image_path + "patreon_credits_background.webp"

    vbox:
        align(0.5, 0.334)
        spacing 100

        add "patreon_credits"

    imagebutton:
        idle image_path + "support_development_idle.webp"
        action OpenURL(support_link)
        xalign 0.5
        ypos 765

    hbox:
        align (0.5, 1.0)
        yoffset -40
        spacing 60

        imagebutton:
            idle image_path + "main_menu_idle.webp"
            action MainMenu()

        imagebutton:
            idle image_path + "team_idle.webp"
            action Show("team_credits")

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    on "replace" action SetVariable("quick_menu", False)
    on "replaced" action SetVariable("quick_menu", True)


screen team_credits():
    tag end_screen
    modal True
    style_prefix "team_credits"

    default image_path = "gui/end_screen/"

    add image_path + "team_credits_background.webp"

    hbox:
        align (0.5, 0.5)
        yoffset -20
        spacing 150

        vbox:
            text "{b}UndergradSteve{/b} - Chief Executive Officer"
            text "{b}KingLui{/b} - Project Manager"
            text "{b}OscarSix{/b} - Technical Officer"
            null height 20
            text "{b}Cheexmarie{/b} - Lead Editor"
            text "{b}Condy{/b} - Senior Production Engineer"
            text "{b}Mozzart{/b} - Lead Artist & Coordinator"
            text "{b}Peace{/b} - Head Transcriber"
            null height 20
            text "{b}Jany{/b} - Community Manager"
            text "{b}Oskin{/b} - Community Manager"

            text "{b}MrSkeletor{/b} - Writer"

            text "{b}Jeffly{/b} - Transcriber"
            text "{b}MegaManX{/b} - Transcriber"
            text "{b}messy{/b} - Transcriber"
            text "{b}SystemFailed{/b} - Transcriber"

            text "{b}kaim{/b} - Animator"

        vbox:
            text "{b}xidcat{/b} - Animator"

            text "{b}3D4FUN{/b} - Renderer"
            text "{b}Bwonerart{/b} - Renderer"
            text "{b}François Gibon{/b} - Renderer"
            text "{b}ITtechnology{/b} - Renderer"
            text "{b}Oduvan{/b} - Renderer"
            text "{b}Meg{/b} - Renderer"
            
            text "{b}Stefan{/b} - Photoshopper"

            text "{b}ClearanceClarence{/b} - Gameplay Engineer"

            text "{b}Ana Paula Cunha{/b} - UI/UX Designer"
            text "{b}Danielrothier{/b} - UI/UX Designer"
            text "{b}Natalimartins{/b} - UI/UX Designer"

            text "{b}Ema9000{/b} - Human Resources Manager"

            text "{b}Sawsbucky{/b} - Gameplay Designer"

            text "{b}MimeFlayer{/b} - Assistant Editor"
            text "{b}slgeorge864{/b} - Assistant Editor"


    hbox:
        spacing 50
        align (0.5, 1.0)
        yoffset -40

        imagebutton:
            idle image_path + "main_menu_idle.webp"
            action MainMenu()

        imagebutton:
            idle image_path + "credits_small_idle.webp"
            action Show("patreon_credits")

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    on "replace" action SetVariable("quick_menu", False)
    on "replaced" action SetVariable("quick_menu", True)


style end_screen_text is montserrat_extra_bold_64

style team_credits_text is text:
    font "fonts/Montserrat-Regular.ttf"
    size 38
