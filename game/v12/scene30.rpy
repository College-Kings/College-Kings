# SCENE 30: MC sneaks into his room
# Locations: Hotel Room
# Characters: MC (Outfit: 3), CHLOE (Outfit: 6), RILEY (Outfit: 5)
# Time: Night
# Phone Images: NONE

label v12_room_sneak:
    scene v12rs1 # TPP. Show MC quietly entering the room while closing the door behind him, MC slight smile, mouth closed
    with dissolve

    pause 0.75

    play music "music/v12/Track Scene 30.mp3" fadein 2

    if not v11_riley_roomate:
        if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
            scene v12rs2 # FPP. MC standing in front of Chloe's bed, looking at her as she sleeps
            with dissolve

            u "(So beautiful.)"

            play sound "sounds/kiss.mp3"

            scene v12rs3 # TPP. Show MC giving Chloe a quick kiss on the cheek, Chloe still sleeping
            with dissolve

            pause 0.75

        else:
            scene v12rs2
            with dissolve

            u "(Must've been really tired if she didn't wait up.)"

    else:
        scene v12rs2a # FPP. Same as v12rs2, but show Riley sleeping instead
        with dissolve
        
        u "(Surprised she doesn't have company.)"

    scene v12rs4 # TPP. Show MC getting into his bed
    with dissolve

    pause 0.75

    scene v12rs5 # TPP. Show MC sleeping
    with dissolve

    pause 0.75

    scene v12rs5a # TPP. Same as v12rs5, MC different sleeping position
    with dissolve

    pause 0.75

    scene black
    with dissolve
    
    pause 2.5

    stop music fadeout 3

    if v11_riley_roomate:
        jump v12_aubrey_wake_up_ri #scene 31a
    else:
        jump v12_aubrey_wake_up #scene 31