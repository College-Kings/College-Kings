screen aubsex():
    add "images/v3/sexpos.webp"

    vbox:
        pos (36, 150)
        
        imagebutton:
            idle "images/v3/sexposbutton.webp"
            hover "images/v3/sexposbutton.webp"
            action Jump("amiss")

        imagebutton:
            idle "images/v3/sexposbutton.webp"
            hover "images/v3/sexposbutton.webp"
            action Jump("acow")

        imagebutton:
            idle "images/v3/sexposbutton.webp"
            hover "images/v3/sexposbutton.webp"
            action Jump("abj")

        imagebutton:
            idle "images/v3/sexposbutton.webp"
            hover "images/v3/sexposbutton.webp"
            action Jump("acream")

    if config_debug:
        timer 0.1 action Jump(renpy.random.choice(("amiss", "acow", "abj", "acream")))