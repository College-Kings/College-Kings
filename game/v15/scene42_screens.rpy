screen detective_board():
    tag detective
    style_prefix "detective"

    default image_path = "images/v15/detective_board/"
    default clue_positions = {
        4: (263, 200),
        7: (460, 198),
        5: (657, 203),
        3: (240, 425),
        8: (440, 430),
        2: (640, 425),
        1: (220, 668),
        6: (420, 668),
        0: (620, 665),
    }

    add image_path + "background.png"

    for i, clue in enumerate(v15_nora_clues):
        frame:
            pos clue_positions[i]
            xysize (212, 256)
            background image_path + "card_background.png"

            text clue.description align (0.5, 0.5) color "#fff"
            text clue.informant xalign 0.5 ypos 195

    for i in range(len(v15_nora_clues), 9):
        frame:
            pos clue_positions[i]
            xysize (212, 256)
            background image_path + "card_background.png"

            add image_path + "unknown.png" align (0.5, 0.5)
            text "Unknown" xalign 0.5 ypos 195



    vpgrid:
        cols 3
        pos (1125, 480)
        spacing -10

        for i in range(6):
            frame:
                xysize (212, 256)
                background image_path + "card_background.png"

                add image_path + "unknown.png" align (0.5, 0.5)
                text "Unknown" xalign 0.5 ypos 195

        # for location in v15_nora_locations:
        #     frame:
        #         xysize (212, 256)
        #         background image_path + "card_background.png"

        #         add location.image:
        #             xalign 0.5
        #             if location.image == "images/v15/detective_board/unknown.png":
        #                 yalign 0.5
        #             else:
        #                 ypos 22

        #         text location.name xalign 0.5 ypos 195 xsize 200

    button action Return()

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    on "replace" action SetVariable("quick_menu", False)
    on "replaced" action SetVariable("quick_menu", True)


style detective_text is text:
    font "fonts/RockSalt-Regular.ttf"
    size 16
    color "#191814"
    text_align 0.5
    line_spacing -22