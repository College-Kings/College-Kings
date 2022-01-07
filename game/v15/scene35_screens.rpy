screen whos_most_likely_to(question, characters):
    tag game_show
    style_prefix "game_show"

    vbox:
        align (0.5, 1.0)
        yoffset -50
        spacing -85

        frame:
            style_prefix "game_show_question"
            xalign 0.5
            xysize (1200, 224)
            background Frame("images/v15/game_show/question_frame.png")

            text question.upper() align (0.5, 0.5)

        hbox:
            xalign 0.5

            for character in characters:
                button:
                    xysize (460, 297)
                    background Frame("images/v15/game_show/character_frame.png")
                    action NullAction()
                    style_prefix "game_show_character"

                    vbox:
                        align (0.5, 0.5)
                        spacing 20

                        add character.profile_picture xalign 0.5

                        button:
                            xysize (324, 91)
                            idle_background "images/v15/game_show/button_idle.png"
                            hover_background "images/v15/game_show/button_idle.png"
                            action NullAction()

                            text character.name.upper() align (0.5, 0.5)


screen would_you_rather(question, options):
    tag game_show
    style_prefix "game_show"

    vbox:
        for char in options[0]["votes"]:
            text char.name

    vbox:
        align (0.5, 1.0)
        yoffset -50
        spacing -85

        frame:
            style_prefix "game_show_question"
            xalign 0.5
            xysize (1200, 224)
            background Frame("images/v15/game_show/question_frame.png")

            text question.upper() align (0.5, 0.5)

        hbox:
            xalign 0.5

            for char, option in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", options):
                button:
                    xysize (720, 293)
                    background Frame("images/v15/game_show/answer_frame.png")
                    sensitive mc not in option["votes"]
                    selected mc in option["votes"]
                    action SetDict(option, "votes", option["votes"] + [mc])

                    style_prefix "game_show_character"

                    hbox:
                        align (0.5, 0.5)
                        spacing 20
                        xsize 500

                        text char + ":" yalign 0.5 style "game_show_char_text"

                        text option["option"].upper() yalign 0.5 style "game_show_option_text"

style game_show_question_text is text:
    font "fonts/Montserrat-Bold.ttf"
    size 30
    yoffset -5

style game_show_character_text is olympus_mount_30

style game_show_char_text is text:
    font "fonts/Montserrat-Bold.ttf"
    size 50
    color "#ffcc2b"

style game_show_option_text is text:
    font "fonts/Montserrat-Bold.ttf"
    size 40
    text_align 0.5