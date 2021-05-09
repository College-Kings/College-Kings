screen girls():
    default girlLabels = [ "juchloe", "juaubrey", "julauren", "juriley", "juemily", "jupenelope" ]

    add "images/girls.webp"

    grid 3 2:
        pos (110, 360)
        spacing 50

        for i in girlLabels:
            imagebutton:
                idle "images/girl.webp"
                hover "images/girlhover.webp"
                action Jump(i)