# SCENE 47: MC goes to Nora's Cabin
# Locations: Street to Nora's Cabin.
# Characters: MC (Outfit: 1), NORA (Outfit: 1)
# Time: Afternoon

label v15s47:
    play music "music/v15/Track Scene 47.mp3" fadein 2

    scene v15s47_1 # TPP. MC in the back of the Cab looking out the window seeing the trees and countryside area, Neutral face, mouth closed.
    with dissolve

    u "(There's no doubt Nora's hiding in her dad's cabin.)"

    u "(I just want to make sure she's okay. I hope she's not angry when I show up unannounced.)"

    u "(I could try calling her first...?)"

    scene v15s47_2 # TPP. MC in the back of the Cab looking at his phone, neutral face, mouth closed.
    with dissolve

    menu:
        "Call Nora":
            $ add_point(KCT.BOYFRIEND)
            
            play sound "sounds/ring.mp3"

            scene v15s47_2a # TPP. MC holding the phone to his ear, neutral face, mouth closed
            with dissolve

            no "Hey! This is Nora, and I'm obviously doing something far more important than what you're calling about, so leave a-"

            play sound "sounds/answercall.mp3"

            scene v15s47_2b # TPP. MC holding the phone away from his face and pressing a button to hang up the phone, neutral face, mouth closd.
            with dissolve

            u "(Straight to voicemail. No surprises there.)"

            scene v15s47_2c # TPP. MC putting his phone away, neutral face, mouth closed.
            with dissolve

            pause 0.75

        "Don't call Nora":
            $ add_point(KCT.BRO)
            
            scene v15s47_3 # TPP. MC in the back of the Cab looking out the window new set of scenery, Neutral face, mouth closed.
            with dissolve

            u "(No reason to call. I'm almost there anyway... Plus, I doubt she's gonna answer.)"

    scene v15s47_4 # TPP. Outside shot of the Cab driving down the road.
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v15s48