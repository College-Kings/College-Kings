screen end_screen():
    tag end_screen
    modal True
    style_prefix "end_screen"

    default image_path = "gui/end_screen/"

    add image_path + "end_screen_background.png"

    vbox:
        xalign 0.5
        ypos 345

        text "ACT 4 PART 2" xalign 0.5
        text "Coming this December!" xalign 0.5 color "EA54E8"

    hbox:
        xalign 0.5
        ypos 556
        spacing 20

        text "Exclusively on " yalign 0.5

        hbox:
            spacing 10

            add image_path + "patreon_logo.png" yalign 0.5
            add image_path + "patreon_wordmark.png" yalign 0.5

    hbox:
        xalign 0.5
        ypos 764
        spacing 100

        imagebutton:
            idle image_path + "menu_idle.png"
            action MainMenu()
            yalign 0.5

        imagebutton:
            idle image_path + "get_access_idle.png"
            action OpenURL("https://www.patreon.com/collegekings")
            yalign 0.5

        imagebutton:
            idle image_path + "credits_idle.png"
            action Show("patreon_credits")
            yalign 0.5
        


screen patreon_credits():
    tag end_screen
    modal True

    default image_path = "gui/end_screen/"

    add image_path + "patreon_credits_background.png"

    frame at credits_scroll(5.0):
        background None
        xalign 0.5

        vbox:
            label "Credits"

            null height 20

            hbox:
                text "Role 1"
                text "NAME 1"

            hbox:
                text "Role 2"
                text "NAME 2"

style credits_hbox:
    spacing 40
    ysize 30

style credits_label:
    xalign 0.5

style credits_text:
    xalign 0.5


screen team_credits():
    tag end_screen
    modal True
    style_prefix "team_credits"

    default image_path = "gui/end_screen/"

    add image_path + "team_credits_background.png"

    hbox:
        align (0.5, 0.5)
        spacing 150

        vbox:
            text "{b}UndergradSteve{/b} - Game Creator"
            text "{b}KingLui{/b} - Project Manager"
            text "{b}OscarSix{/b} - Technical Officer"
            null height 20
            text "{b}Oskin{/b} - Lead Enforcer"
            text "{b}Lucious Lordswill{/b} - Lead Writer"
            text "{b}Cheexmarie{/b} - Lead Editor"
            text "{b}Peace{/b} - Head Transcriber"
            text "{b}Condy{/b} - Quality Assurance Manager"
            text "{b}Jany{/b} - Translation Manager"
            text "{b}Mozzart{/b} - Lead Artist & Coordinator"
            null height 20
            text "{b}Maro{/b} - Marketing Specialist"
            text "{b}HugeBoiV2{/b} - Transcriber"
            text "{b}Jeffly{/b} - Transcriber"

        vbox:
            text "{b}MegaManX{/b} - Transcriber"
            text "{b}mstep17{/b} - Transcriber"
            text "{b}SystemFailed{/b} - Transcriber"
            text "{b}Wolf{/b} - Transcriber"
            text "{b}Dorkby{/b} - Animator"
            text "{b}Wiebley{/b} - Renderer"
            text "{b}Ranger{/b} - 3d Modeler"
            text "{b}François Gibon{/b} - Renderer"
            text "{b}3D4FUN{/b} - Renderer"
            text "{b}Bwonerart{/b} - Renderer"
            text "{b}Sznuk{/b} - Renderer"
            text "{b}Raystorm41{/b} - Render"
            text "{b}Stefan{/b} - Photoshopper"
            text "{b}Space-Storm{/b} - Tech Assistant"

    hbox:
        spacing 50
        align (0.5, 1.0)
        yoffset -40

        imagebutton:
            idle image_path + "main_menu_idle.png"
            action MainMenu()

        imagebutton:
            idle image_path + "credits_small_idle.png"
            action Show("patreon_credits")

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    on "replace" action SetVariable("quick_menu", False)
    on "replaced" action SetVariable("quick_menu", True)


style end_screen_text is montserrat_extra_bold_64

style team_credits_text is text:
    font "fonts/Montserrat-Regular.ttf"
    size 38
