# SCENE 35: Your Room Sat Afternoon
# Locations: MC Wolves/Apes room
# Characters: MC (Outfit 3)
# Time: Saturday Morning

label v9_room_sat_aft:
    if joinwolves:
        scene v9rsa1 # TPP. Show MC stood in his Wolves room near his bed.
        with fade

        pause 1

        scene v9rsa2 # TPP. Show MC flopped facedown on his bed.
        with dissolve

        u "(How much longer do I have?)"

        scene v9rsa3 # TPP. Show MC now on his back on his bed, looking at his phone (don't show phone screen)
        with dissolve
        
        pause 1

        scene v9rsa3a # TPP. Same camera as v9rsa3, MC puts his phone down and yawns.
        with dissolve

        u "(Just a quick nap)"

        scene v9rsa4 # TPP. Show MC's Wolves room door.
        with dissolve

        play sound "sounds/knock.mp3"

        u "Ugh!"

        jump v9_run_w_imre

    else:
        scene v9rsa5 # TPP. Show MC stood in his Apes room near his bed.
        with fade

        pause 1

        scene v9rsa6 # TPP. Show MC flopped facedown on his bed.
        with dissolve

        u "(How much longer do I have?)"

        scene v9rsa7 # TPP. Show MC now on his back on his bed, looking at his phone (don't show phone screen)
        with dissolve
        
        pause 1

        scene v9rsa7a # TPP. Same camera as v9rsa3, MC puts his phone down and yawns.
        with dissolve

        u "(Just a quick nap)"

        scene v9rsa8 # TPP. Show MC's Apes room door.
        with dissolve

        play sound "sounds/knock.mp3"

        u "Ugh!"

        jump v9_run_w_ryan