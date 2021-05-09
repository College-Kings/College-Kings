screen costumes():
    add "images/costumes.webp"

    imagebutton:
        idle "images/try.webp"
        hover "images/tryh.webp"
        pos (256, 802)
        if costumeaubrey and not caughtpeekingaubrey:
            action Jump ("try1")
        elif not costumeaubrey and not caughtpeekingpenelope:
            action Jump ("try1p")
                
    imagebutton:
        idle "images/try.webp"
        hover "images/tryh.webp"
        pos (738, 802)
        if costumeaubrey and not caughtpeekingaubrey:
            action Jump ("try2")
        elif not costumeaubrey and not caughtpeekingpenelope:
            action Jump ("try2p")

    imagebutton:
        idle "images/try.webp"
        hover "images/tryh.webp"
        pos (1219, 802)
        if costumeaubrey and not caughtpeekingaubrey:
            action Jump ("try3")
        elif not costumeaubrey and not caughtpeekingpenelope:
            action Jump ("try3p")

    imagebutton:
        idle "images/try.webp"
        hover "images/buyh.webp"
        pos (256, 935)
        if costumeaubrey and auboutfits <= 3:
            action Jump ("surebuy1")
        elif costumeaubrey:
            action Jump ("buy1")
        elif penoutfits <= 3:
            action Jump ("surebuy1p")
        else:
            action Jump ("buy1p")

    imagebutton:
        idle "images/try.webp"
        hover "images/buyh.webp"
        pos (738, 935)
        if costumeaubrey and auboutfits <= 3:
            action Jump ("surebuy2")
        elif costumeaubrey:
            action Jump ("buy2")
        elif penoutfits <= 3:
            action Jump ("surebuy2p")
        else:
            action Jump ("buy2p")

    imagebutton:
        idle "images/try.webp"
        hover "images/buyh.webp"
        pos (1219, 935)
        if costumeaubrey and auboutfits <= 3:
            action Jump ("surebuy3")
        elif costumeaubrey:
            action Jump ("buy3")
        elif penoutfits <= 3:
            action Jump ("surebuy3p")
        else:
            action Jump ("buy3p")