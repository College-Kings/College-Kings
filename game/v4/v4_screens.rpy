screen girls():
    modal True

    # character, label
    default girl_labels = [
            ["Chloe", "juchloe"],
            ["Aubrey", "juaubrey"],
            ["Lauren", "julauren"],
            ["Riley", "juriley"],
            ["Emily", "juemily"],
            ["Penelope", "jupenelope"],
        ]
        
    default image_path = "gui/julia_call/"

    add image_path + "jc_background.webp"

    vpgrid:
        cols 3
        rows 2
        spacing 60
        xalign 0.5
        ypos 450

        for character, l in girl_labels:
            vbox:
                align (0.5, 0.5)

                imagebutton:
                    idle image_path + character + "_idle.webp"
                    hover image_path + character + ".webp"
                    action Jump(l)

                text character:
                    yoffset -80
                    xoffset 30
                    xalign 0.5
                    size 30