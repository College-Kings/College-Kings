screen girls():
    default girlLabels = [ 
            ["juchloe","CHLOE"],
            ["juaubrey","AUBREY"],
            ["julauren","LAUREN"],
            ["juriley","RILEY"],
            ["juemily","EMILY"],
            ["jupenelope","PENELOPE"],
        ]

    add "images/v4/julia_call/girls.webp"

    hbox:
        pos (175, 120)

        text "WHICH GIRL DO YOU WANT TO TELL JULIA ABOUT?":
            size 55

    grid 3 2:
        ypos 360
        xspacing 25
        yspacing 50
        xalign 0.5

        for i in girlLabels:
            vbox:
                align (0.5, 0.5)

                imagebutton:
                    idle Transform("images/v4/julia_call/" + i[0] + ".webp", zoom=.8)
                    action Jump(i[0])

                text i[1] xalign 0.5