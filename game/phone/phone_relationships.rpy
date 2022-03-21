screen relationships_home():
    tag phone_tag

    default image_path = "images/phone/relationships/app-assets/"

    use base_phone_rotated:
        frame:
            background image_path + "background.webp"
            
            vpgrid:
                mousewheel True
                draggable True
                cols 3
                rows 6
                spacing 25
                pos (85, 85)
                xysize (765, 335)

                for girl in relationship_girls:
                    frame:
                        padding (10, 10)
                        xsize 238
                        background "relationships_frame_background"

                        hbox:
                            spacing 15

                            add Transform(girl.profile_picture, xysize=(65, 65)) yalign 0.5

                            vbox:
                                yalign 0.5

                                text girl.name

                                text girl.relationship.name.capitalize():
                                    size 20
                                    color "#FFD166"
