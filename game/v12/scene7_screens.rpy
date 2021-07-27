screen murderButtonOverlay(character):
    if v12s7_seenList:
        add "openEyeImage"
    else:
        add "closedEyeImage"

    textbutton "Murder!":
        align (0.9, 0.9)
        if v12s7_seenList:
            action Jump("MurderFail") # Check Label after transcribing review
        else:
            action [ Function(character.kill), Jump("MurderSuccess") ] # Check Label after transcribing review