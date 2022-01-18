screen relationship_screen():
    tag menu
    modal True

    add "darker_80"

    default image_path = "main_menu/path_builder/images/"
    default relationship_girls = [chloe, lindsey]

    add image_path + "path_builder_box_background.webp" align (0.5, 0.5)

    text "Your Relationships" xalign 0.5 ypos 300


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

                    add image_path + "girls/{}_idle.webp".format(girl.name):
                        yoffset 90

                    text girl.name:
                        size 30
                        color "#FFF"
                        xoffset 120

                    if girl.relationship < Relationship.FRIEND: #lindsey should be replaced by girl name
                        text "Complicated":
                            size 15
                            color "#FFD166"
                            xoffset 120
                    elif girl.relationship.value < Relationship.KISS: # Penelope needs an exception
                        text "Friends":
                            size 15
                            color "#FFD166"
                            xoffset 120

                    elif girl.relationship.value == Relationships.KISS:
                        text "Kissed":
                            size 15
                            color "#FFD166"
                            xoffset 120

                    elif girl.relationship.value == Relationship.FWB:
                        text "Friends with Benefits":
                            size 15
                            color "#FFD166"
                            xoffset 120
                    else:
                        text "Dating":
                            size 15
                            color "#FFD166"
                            xoffset 120

                    

