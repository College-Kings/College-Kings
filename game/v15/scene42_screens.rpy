screen detective_popup(type, message):
    tag detective
    
    default image_path = "images/v15/detective_board/"

    button:
        action Hide("detective")
        background Frame(image_path + "detective_popup_background.png")
        minimum (655, 108)
        pos(10, 10)

        vbox:
            pos (130, 15)
            spacing -2

            text type size 25 color "#FFD166"
            
            text message size 18

    timer 4 action Hide("detective", transition=dissolve)


screen detective_board():
    tag detective
    style_prefix "detective"

    default image_path = "images/v15/detective_board/"
    default clue_positions = {
        0: (263, 200),
        1: (460, 198),
        2: (657, 203),
        3: (240, 425),
        4: (440, 435),
        5: (640, 425),
        6: (220, 668),
        7: (420, 668),
        8: (620, 665),
    }

    add image_path + "background.png"
    button action Return()

    # Clues
    for i, clue in enumerate(v15_nora_clues):
        button:
            hovered Show("detective_board_description", card=clue)
            unhovered Hide("detective_board_description")
            action NullAction()
            pos clue_positions[i]
            xysize (212, 256)
            background image_path + "card_background.png"

            text clue.description align (0.5, 0.4) color "#fff" xsize 150
            text clue.informant xalign 0.5 ypos 190

    for i in range(len(v15_nora_clues), 9):
        frame:
            pos clue_positions[i]
            xysize (212, 256)
            background image_path + "card_background.png"

            add image_path + "unknown.png" align (0.5, 0.5)
            text "Unknown" xalign 0.5 ypos 195

    # Locations
    vpgrid:
        cols 3
        pos (1125, 480)
        spacing -10

        for location in v15_nora_locations:
            button:
                hovered Show("detective_board_description", card=location)
                unhovered Hide("detective_board_description")
                action NullAction()
                xysize (212, 256)
                background image_path + "card_background.png"

                add location.image xalign 0.5 ypos 22
                text location.name xalign 0.5 ypos 195 xsize 200

        for i in range(len(v15_nora_locations), 6):
            frame:
                xysize (212, 256)
                background image_path + "card_background.png"

                add image_path + "unknown.png" align (0.5, 0.5)
                text "Unknown" xalign 0.5 ypos 195

    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    on "replace" action SetVariable("quick_menu", False)
    on "replaced" action SetVariable("quick_menu", True)


screen detective_board_description(card):
    zorder 100

    frame:
        xysize (804, 337)
        align (0.5, 0.5)
        background "images/planning_boards/task_background.webp"

        vbox:
            spacing 20
            pos (50, 30)
            xsize 704

            text "Amber's opinion":
                color "#777777"
                size 30

            text card.opinion:
                color "#777777"
                size 22


style detective_text is text:
    font "fonts/RockSalt-Regular.ttf"
    size 16
    color "#191814"
    text_align 0.5
    line_spacing -22