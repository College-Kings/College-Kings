screen archetype_selection():
    add "images/v15/detective_board/archetype_background.webp"

    text "You've watched enough crime shows to know what questions need to be asked. You've got the mind of a true detective.":
        pos (190,700)
        xsize 400
        text_align 0.5
        font "fonts/Effra-Regular.ttf"
        size 23

    text "Why do people do the things they do? What are the obvious signs of a liar? You're perceptive, mindful, and thorough.":
        pos (787,700)
        xsize 400
        text_align 0.5
        font "fonts/Effra-Regular.ttf"
        size 23

    text "The bad cop approach. It doesn't always make sense, but you're angry, and that can be useful... sometimes.":
        pos (1345,700)
        xsize 400
        text_align 0.5
        font "fonts/Effra-Regular.ttf"
        size 23


    imagebutton:
        pos (176, 850)
        idle "images/v15/detective_board/archetype_blue_button.png"
        hover "images/v15/detective_board/archetype_blue_button_hover.png"
        action [SetField(mc, "detective", Detective.PROFESSIONAL), Return()]

    imagebutton:
        pos (755, 850)
        idle "images/v15/detective_board/archetype_yellow_button.png"
        hover "images/v15/detective_board/archetype_yellow_button_hover.png"
        action [SetField(mc, "detective", Detective.PSYCHOLOGIST), Return()]
    
    imagebutton:
        pos (1334, 850)
        idle "images/v15/detective_board/archetype_pink_button.png"
        hover "images/v15/detective_board/archetype_pink_button_hover.png"
        action [SetField(mc, "detective", Detective.LOOSE_CANNON), Return()]


screen detective_icon():
    zorder 90

    imagebutton:
        idle "images/v15/detective_board/detective_icon.webp"
        action [ToggleScreen("detective_board")]


screen detective_popup(type, message):
    tag detective
    
    default image_path = "images/v15/detective_board/"

    button:
        action Hide("detective")
        background Frame(image_path + "detective_popup_background.webp")
        minimum (655, 108)
        pos(10, 10)

        vbox:
            pos (130, 15)
            spacing -2

            text type size 25 color "#FFD166"
            
            text message size 18

    timer 4 action Hide("detective", transition=dissolve)


screen detective_board():
    zorder 1
    
    tag detective
    style_prefix "detective"

    modal True

    default image_path = "images/v15/detective_board/"
    default clue_positions = {
        0: (657, 203),
        1: (420, 668),
        2: (220, 668),
        3: (263, 200),
        4: (460, 198),
        5: (440, 435),
        6: (640, 425),
        7: (620, 665),
        8: (240, 425),
    }

    add image_path + "background.webp"
    #button action Return()
    button action Hide("detective_board")

    # Clues
    for i, clue in enumerate(v15_nora_clues):
        button:
            hovered Show("detective_board_description", card=clue)
            unhovered Hide("detective_board_description")
            action NullAction()
            pos clue_positions[i]
            xysize (212, 256)
            background image_path + "card_background.webp"

            text clue.description align (0.5, 0.4) color "#fff" xsize 150
            text clue.informant xalign 0.5 ypos 190

    for i in range(len(v15_nora_clues), 9):
        frame:
            pos clue_positions[i]
            xysize (212, 256)
            background image_path + "card_background.webp"

            add image_path + "unknown.webp" align (0.5, 0.5)
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
                background image_path + "card_background.webp"

                add location.image xalign 0.5 ypos 22
                text location.name xalign 0.5 ypos 195 xsize 200

        for i in range(len(v15_nora_locations), 6):
            frame:
                xysize (212, 256)
                background image_path + "card_background.webp"

                add image_path + "unknown.webp" align (0.5, 0.5)
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