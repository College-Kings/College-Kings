screen savenow():
    tag save_now
    modal True
    style_prefix "save_now"

    default music_file = "music/horror2.mp3"
    default image_path = "gui/end_screen/"

    on "show" action Play("music", music_file)

    add image_path + "end_screen_background.webp"

    vbox:
        align (0.5, 0.5)
        spacing 25

        text "WARNING\n" color "#FF0000" xalign 0.5 size 105
        text "END OF CURRENT VERSION" color "#FFFFFF" xalign 0.5 size 70
        text "SAVE HERE TO KEEP PROGRESS\n" color "#FFFFFF" xalign 0.5 size 70
        text "DO NOT CLICK CONTINUE UNTIL YOU HAVE SAVED!" color "#FFFFFF" xalign 0.5 size 50

        imagebutton:
            idle image_path + "continue_idle.webp"
            hover image_path + "continue_hover.webp"
            action Show("patreon_credits")
            xalign 0.5

    text "v" + config.version.split(" ")[0] align (1.0, 1.0) xoffset -20 color "#4e628f" size 30


style save_now_text is text:
    font "fonts/Freshman.ttf"