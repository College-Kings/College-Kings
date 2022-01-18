screen relationship_screen():
    tag menu
    modal True

    add "darker_80"

    default image_path = "main_menu/path_builder/images/"

    add image_path + "path_builder_box_background.webp" align (0.5, 0.5)

    text "Your Relationships" xalign 0.5 ypos 300

    python:
        relationship_girls = ["chloe", "lindsey"]


    vbox:
        spacing 20
        align (0.5, 0.5)

        vpgrid:
            cols 4
            rows 3
            xspacing 10
            xalign 0.5
            yoffset 40

            for girl in relationship_girls:

                vbox:
                    xpos 120
                    yalign 0.5

                    add image_path + "girls/{}_idle.webp".format(girl):
                        yoffset 90

                    text girl:
                        size 30
                        color "#FFF"
                        xoffset 120

                    if girl.relationship.value < 0: #lindsey should be replaced by girl name
                        text "Complicated":
                            size 15
                            color "#FFD166"
                            xoffset 120
                    elif girl.relationship.value < 6: # Penelope needs an exception
                        text "Friends":
                            size 15
                            color "#FFD166"
                            xoffset 120

                    elif girl.relationship.value == 6:
                        text "Kissed":
                            size 15
                            color "#FFD166"
                            xoffset 120

                    elif girl.relationship.value == 7:
                        text "Friends with Benefits":
                            size 15
                            color "#FFD166"
                            xoffset 120
                    else:
                        text "Dating":
                            size 15
                            color "#FFD166"
                            xoffset 120

                    

