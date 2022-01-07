transform credits_scroll(speed):
    ypos 720
    linear speed ypos -720

screen end_screen():
    tag end_screen
    modal True

    default image_path = "gui/end_screen/"

    add image_path + "end_screen_background.png"

    hbox:
        align (0.5, 0.9)
        spacing 100

        textbutton "MENU":
            action MainMenu()
            yalign 0.5
            text_size 100


        textbutton "Credits":
            action Jump("credits")
            yalign 0.5
            text_size 100


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

    default image_path = "gui/end_screen/"

    add image_path + "team_credits_background.png"

    text "TEAM CREDITS":
        xalign 0.5
        ypos 45
        size 68

    hbox:
        align (0.5, 0.5)
        spacing 150

        vbox:
            spacing 10

            text "{=credits_bold}UndergradSteve{/=credits_bold}{=credits_regular} - Game Creator{/=credits_regular}"
            text "{=credits_bold}KingLui{/=credits_bold}{=credits_regular} - Project Manager{/=credits_regular}"
            text "{=credits_bold}OscarSix{/=credits_bold}{=credits_regular} - Technical Officer{/=credits_regular}"
            null height 20
            text "{=credits_bold}Oskin{/=credits_bold}{=credits_regular} - Lead Enforcer{/=credits_regular}"
            text "{=credits_bold}Lucious Lordswill{/=credits_bold}{=credits_regular} - Lead Writer{/=credits_regular}"
            text "{=credits_bold}Cheexmarie{/=credits_bold}{=credits_regular} - Lead Editor{/=credits_regular}"
            text "{=credits_bold}Peace{/=credits_bold}{=credits_regular} - Head Transcriber{/=credits_regular}"
            text "{=credits_bold}Condy{/=credits_bold}{=credits_regular} - Quality Assurance Manager{/=credits_regular}"
            text "{=credits_bold}Jany{/=credits_bold}{=credits_regular} - Translation Manager{/=credits_regular}"
            text "{=credits_bold}Mozzart{/=credits_bold}{=credits_regular} - Lead Artist & Coordinator{/=credits_regular}"
            null height 20
            text "{=credits_bold}Maro{/=credits_bold}{=credits_regular} - Marketing Specialist{/=credits_regular}"
            text "{=credits_bold}HugeBoiV2{/=credits_bold}{=credits_regular} - Transcriber{/=credits_regular}"
            text "{=credits_bold}Jeffly{/=credits_bold}{=credits_regular} - Transcriber{/=credits_regular}"

        vbox:
            spacing 10

            text "{=credits_bold}MegaManX{/=credits_bold}{=credits_regular} - Transcriber{/=credits_regular}"
            text "{=credits_bold}mstep17{/=credits_bold}{=credits_regular} - Transcriber{/=credits_regular}"
            text "{=credits_bold}SystemFailed{/=credits_bold}{=credits_regular} - Transcriber{/=credits_regular}"
            text "{=credits_bold}Wolf{/=credits_bold}{=credits_regular} - Transcriber{/=credits_regular}"
            text "{=credits_bold}Dorkby{/=credits_bold}{=credits_regular} - Animator{/=credits_regular}"
            text "{=credits_bold}Wiebley{/=credits_bold}{=credits_regular} - Renderer{/=credits_regular}"
            text "{=credits_bold}Ranger{/=credits_bold}{=credits_regular} - 3d Modeler{/=credits_regular}"
            text "{=credits_bold}François Gibon{/=credits_bold}{=credits_regular} - Renderer{/=credits_regular}"
            text "{=credits_bold}3D4FUN{/=credits_bold}{=credits_regular} - Renderer{/=credits_regular}"
            text "{=credits_bold}Bwonerart{/=credits_bold}{=credits_regular} - Renderer{/=credits_regular}"
            text "{=credits_bold}Sznuk{/=credits_bold}{=credits_regular} - Renderer{/=credits_regular}"
            text "{=credits_bold}Raystorm41{/=credits_bold}{=credits_regular} - Render{/=credits_regular}"
            text "{=credits_bold}Stefan{/=credits_bold}{=credits_regular} - Photoshopper{/=credits_regular}"
            text "{=credits_bold}Space-Storm{/=credits_bold}{=credits_regular} - Tech Assistant{/=credits_regular}"

    text "{=credits_thank_you}Special thanks to all the community members and players who have made this project possible :){/=credits_thank_you}":
        align (0.5, 0.88)

    hbox:
        spacing 50
        align (0.5, 0.96)

        imagebutton:
            idle image_path + "main_menu_icon.png"
            action MainMenu()

        imagebutton:
            idle image_path + "credits_button.png"
            action Show("patreon_credits")