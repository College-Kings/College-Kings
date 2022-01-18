screen relationship_screen():
    tag menu
    modal True

    add "darker_80"

    default image_path = "main_menu/path_builder/images/"
    default relationship_girls = [amber, aubrey, autumn, chloe, emily, jenny, lauren, lindsey, ms_rose, nora, penelope, samantha, riley]

    add image_path + "path_builder_box_background.webp" align (0.5, 0.5)

    text "Your Relationships" xalign 0.5 ypos 300


    vbox:
        spacing 20
        align (0.5, 0.5)

        vpgrid:
            #scrollbars "vertical"
            mousewheel True
            draggable True
            cols 4
            rows 5
            xspacing 30
            xalign 0.5
            yoffset 40
            ysize 500
            xsize 1550

            for girl in filter(lambda girl: girl._messenger is not None, relationship_girls):

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
                    elif girl.relationship < Relationship.KISS: # Penelope needs an exception
                        text "Friends":
                            size 15
                            color "#FFD166"
                            xoffset 120

                    elif girl.relationship == Relationship.KISS:
                        text "Kissed":
                            size 15
                            color "#FFD166"
                            xoffset 120

                    elif girl.relationship == Relationship.FWB:
                        text "Friends with Benefits":
                            size 15
                            color "#FFD166"
                            xoffset 120
                    else:
                        text "Dating":
                            size 15
                            color "#FFD166"
                            xoffset 120

                    

