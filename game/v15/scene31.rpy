# SCENE 31: Frat bathroom, MC looks at himself in suit, looking good
# Locations: Frat bathroom
# Characters: MC (Outfit: Wedding Suit)
# Time: Morning

label v15s31:
    if False: #making sure it shows on Lint
        scene emily_selfie_31


        pause 0.75

# -Transition from night to morning-

# -MC is wearing his homecoming suit as he walks into the bathroom-
    scene v15s31_1 # TPP. Show MC looking at himself in the mirror as he is wearing the suit, slight smile, mouth closed.
    with dissolve

    u "(Right, let's see how I'm looking.)"

    scene v15s31_2 # FPP. MC looking at the mirror to see himself in the suit, slight smile, mouth closed.
    with dissolve

    u "(Damn, I'm looking fine as hell!)"

    u "(Feels good to suit up for special occasions, ha.)"

    u "(And now I'm getting high school prom flashbacks...)"

    play sound "sounds/swoosh.mp3"
    show screen fantasyOverlay
    
    scene v15s31_3 # TPP. Flashback image of MC and Emily taking a picture for prom. Emily has her back to MC and MC's hands are on Emily's hips, both have big smiles.
    with dissolve

    ""

    play sound "sounds/swoosh.mp3"
    
    scene v15s31_2
    with dissolve
    hide screen fantasyOverlay 
    u "(Back when I was happy with Emily, and I thought relationships were easy. Haha! How wrong I was...)"

    menu:
        "Send Emily a selfie":
            scene v15s31_4 # TPP. Show MC's hand pulling his phone out of his pocket.
            with dissolve

            pause 0.75

            scene v15s31_1a # TPP. Show MC taking a selfie of himself in the suit, slight smile, mouth closed.
            with flash

            pause 0.75

            scene v15s31_5 # TPP. Show MC pressing buttons on his phones, slight smile, mouth closed.
            with dissolve

            pause 0.75

            $ emily.messenger.addImgReply("images/v15/Scene 31/emily_selfie_31.webp", func=None) #Selfie in a suit
            $ emily.messenger.addReply("Getting prom flashbacks.")
            $ emily.messenger.newMessage("OMG! Haha, you actually look the same. Where are you headed?", queue=False)
            $ emily.messenger.addReply("Wedding ceremony for Aubrey's parents.")
            $ emily.messenger.newMessage("Oh, nice! Tell her I said hi! Miss you guys! Have fun! :)", queue=False)
            $ emily.messenger.addReply("Will do. We miss you too :)")

            label v15s31_PhoneContinue:
                if emily.messenger.replies:
                    call screen phone
                if emily.messenger.replies:
                    u "(I should reply to Emily.)"
                    jump v15s31_PhoneContinue

            scene v15s31_4a # TPP. Show MC's hand putting his phone away.
            with dissolve

            pause 0.75

        "Don't contact Emily":
            scene v15s31_2
            with dissolve
                
            u "(Probably not a good idea to freshen those memories...)"

    u "(Alright, time to meet Aubrey.)"

    u "(I wonder what she's wearing?)"

    play sound "sounds/dooropen.mp3"

    scene v15s31_6 # TPP. Show MC leaving the bathroom, slight smile, mouth closed.
    with dissolve

    pause 0.75

    jump v15s32