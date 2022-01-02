screen v9s7_lakeFull(): ###### LAKE ZOOM OUT SCREEN
    tag free_roam

    add "images/v9/scene 7/fr5lakefull.webp"

    imagebutton: #switch to zoomed in view
        pos (550, 540)
        idle "images/v9/scene 7/fr5zoomin.webp"
        hover "images/v9/scene 7/fr5zoominhover.webp"
        action Show("v9s7_lakeZoomIn")

    imagebutton: # RYAN
        pos (935, 506)
        idle "images/v9/scene 7/fr5ryan.webp"
        hover "images/v9/scene 7/fr5ryanhover.webp"
        if not "ryan" in freeroam5:
            action Jump("fr5ryan1")
        else:
            action Show("confirm", message="Are you sure you want to end free roam?", yes_action=[Hide("confirm"), Jump("fr5ryan3")])

    imagebutton: # DOGWALKER
        pos (1590, 576)
        idle "images/v9/scene 7/fr5dogwalker.webp"
        hover "images/v9/scene 7/fr5dogwalkerhover.webp"
        if not "dogwalker" in freeroam5:
            action Jump("fr5dogwalker1")
        else:
            action Jump("fr5dogwalker2")

    imagebutton: # TREEGUY
        pos (75, 540)
        idle "images/v9/scene 7/fr5treeguy.webp"
        hover "images/v9/scene 7/fr5treeguyhover.webp"
        if not "treeguy" in freeroam5:
            action Jump("fr5treeguy1")
        else:
            action Jump("fr5treeguy2")


screen v9s7_lakeZoomIn(): ###### LAKE ZOOM OUT SCREEN
    tag free_roam

    add "images/v9/scene 7/fr5lakezoomin.webp"

    imagebutton: #switch to zoomed out view
        pos (350, 900)
        idle "images/v9/scene 7/fr5zoomout.webp"
        hover "images/v9/scene 7/fr5zoomouthover.webp"
        action Show("v9s7_lakeFull")

    imagebutton: # AUBREY
        pos (244, 567)
        idle "images/v9/scene 7/fr5aubrey.webp"
        hover "images/v9/scene 7/fr5aubreyhover.webp"
        if not "aubrey" in freeroam5:
            action Jump("fr5aubrey1")
        else:
            action Jump("fr5aubrey2")

    imagebutton: # RILEY
        pos (1523, 329)
        idle "images/v9/scene 7/fr5riley.webp"
        hover "images/v9/scene 7/fr5rileyhover.webp"
        if not "riley" in freeroam5:
            action Jump("fr5riley1")
        else:
            action Jump("fr5riley2")