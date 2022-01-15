screen savenow():
    tag save_now
    modal True
    style_prefix "save_now"

    default music_file ="music/horror2.mp3"

    on "show" action Play("music", music_file)

    default image_path   = "gui/end_screen/"

    add image_path + "end_screen_background.webp"

    vbox:
        align (0.5, 0.5)
        spacing 25

        text "WARNING\n" color "#FF0000" xalign 0.5 size 120
        text "END OF CURRENT VERSION" color "#FFFFFF" xalign 0.5 size 80
        text "SAVE HERE TO KEEP PROGRESS\n" color "#FFFFFF" xalign 0.5 size 80
        text "DO NOT CLICK CONTINUE UNTIL YOU HAVE SAVED!\n" color "#FFFFFF" xalign 0.5 size 60

        textbutton "Continue" action Show("patreon_credits") xalign 0.5 text_style "save_now_textbutton"


style save_now_text is text:
    font "fonts/Freshman.ttf"

style save_now_textbutton:
    font "fonts/Freshman.ttf"
    size 50