screen murderButtonOverlay(character):
    if v12s7_seenList:
        add "images/v12/Scene 7/gui/eye_open.webp"
    else:
        add "images/v12/Scene 7/gui/eye_closed.webp"

    imagebutton:
        align (0.9, 0.9)
        idle "images/v12/Scene 7/gui/gun.webp"
        hover "images/v12/Scene 7/gui/gun_hover.webp"
        if v12s7_seenList:
            action Jump("MurderFail") # Check Label after transcribing review
        else:
            action [ Function(character.kill), Jump("MurderSuccess") ] # Check Label after transcribing review