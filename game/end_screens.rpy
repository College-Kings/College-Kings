screen save_now(next_version):
    tag save_now
    modal True
    style_prefix "save_now"

    default music_file = "music/horror2.mp3"
    default image_path = "gui/end_screen/"

    add image_path + "end_screen_background.webp"

    vbox:
        align (0.5, 0.5)
        spacing 25

        text "WARNING" color "#FF0000" xalign 0.5 size 105
        null height 100
        text "END OF CURRENT VERSION" xalign 0.5
        text "SAVE HERE TO KEEP PROGRESS" xalign 0.5
        null height 50
        text "DO NOT CLICK CONTINUE UNTIL YOU HAVE SAVED!" xalign 0.5 size 50
            
        imagebutton:
            xalign 0.5
            idle image_path + "continue_idle.webp"
            hover image_path + "continue_hover.webp"
            if renpy.loadable("v{}/scene1.rpy".format(next_version)):
                action Return()
            else:
                action Show("patreon_credits")

    text "v" + config.version.split(" ")[0] align (1.0, 1.0) xoffset -20 color "#4e628f" size 30
    
    on "show" action Play("music", music_file)

style save_now_text is text:
    font "fonts/Freshman.ttf"
    color "#FFFFFF"
    size 70


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
        hover image_path + "support_development_hover.webp"
        action OpenURL(support_link)
        xalign 0.5
        ypos 735

    hbox:
        align (0.5, 1.0)

        imagebutton:
            idle image_path + "main_menu_idle.webp"
            hover image_path + "main_menu_hover.webp"
            action MainMenu()
            yalign 0.5

        imagebutton:
            idle image_path + "team_idle.webp"
            hover image_path + "team_hover.webp"
            action Show("team_credits")
            yalign 0.5

    on "show" action [SetVariable("quick_menu", False), Play("music", "music/vocal.mp3")]
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
        spacing 100

        vbox:
            align (0.5, 0.5)

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
            text "{b}Oskin{/b} - Product Enforcer"

            text "{b}MrSkeletor{/b} - Writer"

            text "{b}Jeffly{/b} - Transcriber"
            text "{b}MegaManX{/b} - Transcriber"
            text "{b}messy{/b} - Transcriber"
            text "{b}SystemFailed{/b} - Transcriber"

            text "{b}kaim{/b} - Animator"
            text "{b}xidcat{/b} - Animator"

        vbox:
            align (0.5, 0.5)

            text "{b}3D4FUN{/b} - Renderer"
            text "{b}Bwonerart{/b} - Renderer"
            text "{b}François Gibon{/b} - Renderer"
            text "{b}ITtechnology{/b} - Renderer"
            text "{b}Oduvan{/b} - Renderer"
            text "{b}sznuk{/b} - Renderer"
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
