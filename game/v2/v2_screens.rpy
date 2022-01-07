screen costumes():
    add "images/v2/costumes.webp"

    imagebutton:
        idle "images/v2/try.webp"
        hover "images/v2/tryh.webp"
        pos (256, 802)
        if costumeaubrey and not v2_caughtpeeking:
            action Jump("try1")
        elif not costumeaubrey and not v2_caughtpeeking:
            action Jump("try1p")
                
    imagebutton:
        idle "images/v2/try.webp"
        hover "images/v2/tryh.webp"
        pos (738, 802)
        if costumeaubrey and not v2_caughtpeeking:
            action Jump("try2")
        elif not costumeaubrey and not v2_caughtpeeking:
            action Jump("try2p")

    imagebutton:
        idle "images/v2/try.webp"
        hover "images/v2/tryh.webp"
        pos (1219, 802)
        if costumeaubrey and not v2_caughtpeeking:
            action Jump("try3")
        elif not costumeaubrey and not v2_caughtpeeking:
            action Jump("try3p")

    imagebutton:
        idle "images/v2/try.webp"
        hover "images/v2/buyh.webp"
        pos (256, 935)
        action Show("confirm",
            message="Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?",
            yes_action=[Hide("confirm"), Jump("buy1{}".format("" if costumeaubrey else "p"))])

    imagebutton:
        idle "images/v2/try.webp"
        hover "images/v2/buyh.webp"
        pos (738, 935)
        action Show("confirm",
            message="Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?",
            yes_action=[Hide("confirm"), Jump("buy2{}".format("" if costumeaubrey else "p"))])

    imagebutton:
        idle "images/v2/try.webp"
        hover "images/v2/buyh.webp"
        pos (1219, 935)
        action Show("confirm",
            message="Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?",
            yes_action=[Hide("confirm"), Jump("buy3{}".format("" if costumeaubrey else "p"))])
