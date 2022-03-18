screen relationship_app():
    tag phone_tag

    use base_phone_rotated:

        default image_path = "images/phone/relationships/appAssets/"

        add Transform(image_path + "rela_bg.webp", zoom=0.40) at truecenter yoffset 3 xoffset 1
            
        vpgrid:
            mousewheel True
            draggable True
            cols 3
            rows 6
            xspacing 30
            yspacing 30
            xoffset 50
            xysize (1230, 490)
            pos (410, 340)

            for girl in relationship_girls:

                frame:
                    padding(10, 10)
                    xsize 350
                    background Transform(image_path + "button_bg.webp".format(girl.name), xysize=(350,125))

                    vbox:
                        text girl.name yoffset 15 xoffset 50 size 30

                        if girl.relationship < Relationship.FRIEND: #lindsey should be replaced by girl name
                            text "Complicated":
                                size 20
                                color "#FFD166"
                                yoffset 10 xoffset 50
                        elif girl.relationship < Relationship.KISS: # Penelope needs an exception
                            if girl == "penelope" and girl.relationship < Relationship.LIKES:
                                text "Kissed":
                                    size 20
                                    color "#FFD166"
                                    yoffset 10 xoffset 50                      
                            else:
                                text "Friends":
                                    size 20
                                    color "#FFD166"
                                    yoffset 10 xoffset 50

                        elif girl.relationship == Relationship.KISS:
                            text "Kissed":
                                size 20
                                color "#FFD166"
                                yoffset 10 xoffset 50

                        elif girl.relationship == Relationship.FWB:
                            text "Friends with Benefits":
                                size 20
                                color "#FFD166"
                                yoffset 10 xoffset 50
                        elif girl.relationship == Relationship.LOYAL and girl == "autumn":
                            text "Trust":
                                size 20
                                color "#FFD166"
                                yoffset 10 xoffset 50
                        else:
                            text "Dating":
                                size 20
                                color "#FFD166" 
                                yoffset 10 xoffset 50 