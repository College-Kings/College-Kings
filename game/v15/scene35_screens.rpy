screen game_show_base(question):
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

        transclude


screen whos_most_likely_to(question):
    tag game_show
    style_prefix "game_show"

    use game_show_base(question):
        hbox:
            xalign 0.5

            for option in screen_options:
                button:
                    xysize (460, 297)
                    background Frame("images/v15/game_show/character_frame.png")
                    action NullAction()
                    style_prefix "game_show_character"

                    vbox:
                        align (0.5, 0.5)
                        spacing 20

                        add option["character"].profile_picture xalign 0.5

                        button:
                            xysize (324, 91)
                            idle_background "images/v15/game_show/button_idle.png"
                            hover_background "images/v15/game_show/button_idle.png"
                            action [SetDict(option, "votes", option["votes"] + [mc]), Show("whos_most_likely_to_answers", question=question)]

                            text option["character"].name.upper() align (0.5, 0.5)


screen would_you_rather(question):
    tag game_show
    style_prefix "game_show"

    use game_show_base(question):
        hbox:
            xalign 0.5

            for char, option in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", screen_options):
                button:
                    xysize (720, 293)
                    background Frame("images/v15/game_show/answer_frame.png")
                    sensitive mc not in option["votes"]
                    selected mc in option["votes"]
                    action [SetDict(option, "votes", option["votes"] + [mc]), Show("would_you_rather_answers", question=question)]

                    hbox:
                        align (0.5, 0.5)
                        spacing 20
                        xsize 500

                        text char + ":" yalign 0.5 style "game_show_char_text"

                        text option["option"].upper() yalign 0.5 style "game_show_option_text"


screen whos_most_likely_to_answers(question):
    tag game_show
    style_prefix "game_show"

    use game_show_base(question):
        hbox:
            xalign 0.5

            for option in screen_options:
                frame:
                    xysize (460, 297)
                    background Frame("images/v15/game_show/character_frame.png")

                    vbox:
                        align (0.5, 0.5)
                        spacing 20

                        text "{{color=#FFCC2B}{}{{/color}} VOTES".format(len(option["votes"])) style "game_show_vote_text" xalign 0.5

                        hbox:
                            xalign 0.5
                            spacing -20

                            for vote in option["votes"]:
                                add Transform(vote.profile_picture, size=(65, 65))

    button action Return()


screen would_you_rather_answers(question):
    tag game_show
    style_prefix "game_show"

    use game_show_base(question):
        hbox:
            xalign 0.5

            for char, option in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", screen_options):
                frame:
                    xysize (789, 293)
                    background Frame("images/v15/game_show/answer_frame.png")

                    hbox:
                        align (0.5, 0.5)
                        spacing 20
                        xsize 630

                        text char + ":" yalign 0.5 style "game_show_char_text"

                        text screen_options["option"].upper() yalign 0.5 style "game_show_option_text"

                        text "{{color=#FFCC2B}}{}{{/color}} VOTES".format(len(option["votes"])) yalign 0.5 style "game_show_vote_text"

    button action Return()


style game_show_question_text is text:
    font "fonts/Montserrat-Bold.ttf"
    size 30
    yoffset -5

style game_show_vote_text is game_show_question_text

style game_show_character_text is olympus_mount_30

style game_show_char_text is text:
    font "fonts/Montserrat-Bold.ttf"
    size 50
    color "#ffcc2b"

style game_show_option_text is text:
    font "fonts/Montserrat-Bold.ttf"
    size 40
    text_align 0.5