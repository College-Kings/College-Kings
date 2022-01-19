screen girls():
    default girlLabels = ("juchloe", "juaubrey", "julauren", "juriley", "juemily", "jupenelope")

    add "images/v4/girls.webp"

    grid 3 2:
        pos (110, 360)
        spacing 50

        for l in girlLabels:
            imagebutton:
                idle "images/v4/girl.webp"
                hover "images/v4/girlhover.webp"
                action Jump(l)