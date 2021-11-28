screen tutorial(tutorial_text):
    zorder 200
    tag tutorial

    default page_number = 1

    add "images/tutback.webp" pos (1240, 100)

    text "Tutorial" style "choicetextnum" pos (1490, 530)

    text tutorial_text[page_number -1] style "choicetuttext"

    fixed:
        xysize(650, 85)
        pos(1240, 720)

        hbox:
            align(0.5, 0.5)
            spacing 150

            imagebutton:
                idle "images/whitearrowleft.webp"
                if page_number > 1:
                    action SetScreenVariable("page_number", page_number - 1)
                else:
                    action SetScreenVariable("page_number", len(tutorial_text))

            text "{} of {}".format(page_number, len(tutorial_text)) style "choicetextnum" yalign 0.5

            imagebutton:
                idle "images/whitearrowright.webp"
                if page_number < len(tutorial_text):
                    action SetScreenVariable("page_number", page_number + 1)
                else:
                    action SetScreenVariable("page_number", 1)


style choicetuttext is text:
    font "fonts/OpenSans.ttf"
    size 25
    color "#ffffff"
    text_align 0
    xpos 1310
    ypos 570
    xmaximum 500

style choicetextnum is text:
    font "fonts/Freshman.ttf"
    size 25
    color "#FFD166"
    text_align 0.5

style tutorialtext is text:
    font "fonts/OpenSans.ttf"
    size 25
    color "#ffffff"
    text_align 0
    xpos 1270
    ypos 400
    xmaximum 500

style tutorialtextnum is text:
    font "fonts/Freshman.ttf"
    size 25
    color "#FFD166"