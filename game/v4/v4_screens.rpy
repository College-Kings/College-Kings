screen girls():

    default image_path = "gui/julia_call/"

    default girlLabels = [ 
            ["juchloe","Chloe"],
            ["juaubrey","Aubrey"],
            ["julauren","Lauren"],
            ["juriley","Riley"],
            ["juemily","Emily"],
            ["jupenelope","Penelope"],
        ]

    add image_path + "jc_background.webp"

    vpgrid:
        cols 3
        rows 2
        spacing 60
        xalign 0.5
        ypos 450

        for i in girlLabels:
            vbox:
                align (0.5, 0.5)

                imagebutton:
                    idle image_path + i[1] + "_idle.webp"
                    hover image_path + i[1] + ".webp"
                    action Jump(i[0])

                text i[1]:
                    yoffset -80
                    xoffset 30
                    xalign 0.5
                    size 30