screen costumes():
    add "images/v2/costumes.webp"

    imagebutton:
        idle "images/v2/try.webp"
        hover "images/v2/tryh.webp"
        pos (256, 802)
        if costumeaubrey and not caughtpeekingaubrey:
            action Jump("try1")
        elif not costumeaubrey and not caughtpeekingpenelope:
            action Jump("try1p")
                
    imagebutton:
        idle "images/v2/try.webp"
        hover "images/v2/tryh.webp"
        pos (738, 802)
        if costumeaubrey and not caughtpeekingaubrey:
            action Jump("try2")
        elif not costumeaubrey and not caughtpeekingpenelope:
            action Jump("try2p")

    imagebutton:
        idle "images/v2/try.webp"
        hover "images/v2/tryh.webp"
        pos (1219, 802)
        if costumeaubrey and not caughtpeekingaubrey:
            action Jump("try3")
        elif not costumeaubrey and not caughtpeekingpenelope:
            action Jump("try3p")

    imagebutton:
        idle "images/v2/try.webp"
        hover "images/v2/buyh.webp"
        pos (256, 935)
        if costumeaubrey and v2_outfits <= 3:
            action Show("confirmBuy", exit="buy1")
        elif costumeaubrey:
            action Jump("buy1")
        elif penoutfits <= 3:
            action Show("confirmBuy", exit="buy1p")
        else:
            action Jump("buy1p")

    imagebutton:
        idle "images/v2/try.webp"
        hover "images/v2/buyh.webp"
        pos (738, 935)
        if costumeaubrey and v2_outfits <= 3:
            action Show("confirmBuy", exit="buy2")
        elif costumeaubrey:
            action Jump("buy2")
        elif penoutfits <= 3:
            action Show("confirmBuy", exit="buy2p")
        else:
            action Jump("buy2p")

    imagebutton:
        idle "images/v2/try.webp"
        hover "images/v2/buyh.webp"
        pos (1219, 935)
        if costumeaubrey and v2_outfits <= 3:
            action Show("confirmBuy", exit="buy3")
        elif costumeaubrey:
            action Jump("buy3")
        elif penoutfits <= 3:
            action Show("confirmBuy", exit="buy3p")
        else:
            action Jump("buy3p")


screen confirmBuy(exit):
    modal True

    use endfrTemplate:

        text "Once you decide which outfit to buy, you will no longer be able to play through all of the \"Try\" scenes. Are you sure you want to continue?":
            style "endfree"
            xalign 0.5
        
        hbox:
            align (0.5, 1.0)
            spacing 200

            textbutton "Yes":
                action [Hide("confirmBuy"), Jump(exit)]

            textbutton "No":
                action Hide("confirmBuy")
