screen tutorial(tutorial_text, position=(1046, 73)):
    zorder 200
    tag tutorial
    style_prefix "tutorial"

    default image_path = "gui/tutorial/"
    default page_number = 1

    frame:
        pos position
        xysize (754, 271) 
        background "tutorial_background"

        fixed:
            ypos 42
            xysize (754, 223)
        
            text tutorial_text[page_number - 1] xsize 607 xalign 0.5 ypos 40

            imagebutton:
                yalign 0.5
                idle Transform(image_path + "left_button_idle.webp", zoom=0.6406)
                hover Transform(image_path + "left_button_hover.webp", zoom=0.6406)
                if page_number > 1:
                    action SetScreenVariable("page_number", page_number - 1)
                else:
                    action SetScreenVariable("page_number", len(tutorial_text))

            imagebutton:
                align (1.0, 0.5)
                idle Transform(image_path + "right_button_idle.webp", zoom=0.6406)
                hover Transform(image_path + "right_button_hover.webp", zoom=0.6406)
                if page_number < len(tutorial_text):
                    action SetScreenVariable("page_number", page_number + 1)
                else:
                    action SetScreenVariable("page_number", 1)

            text "{} of {}".format(page_number, len(tutorial_text)) style "tutorial_page_number" xalign 0.5 ypos 170


style tutorial_text is text:
    font "fonts/Effra-Regular.ttf"
    size 23
    text_align 0.5

style tutorial_page_number is syne_extra_bold_22
