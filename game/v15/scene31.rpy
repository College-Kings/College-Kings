# SCENE 31: Frat bathroom, MC looks at himself in suit, looking good
# Locations: Frat bathroom
# Characters: MC (Outfit: Wedding Suit)
# Time: Morning


label v15s31:
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

    ### Note for Oscar. Tried to put in the show screen fantasyOverlay for the flashback photo but it was messingup the render table.

    scene v15s31_3 # TPP. Flashback image of MC and Emily taking a picture for prom. Emily has her back to MC and MC's hands are on Emily's hips, both have big smiles.
    with dissolve

    ### Note for Oscar. Hide overlay would be here.

    scene v15s31_2
    with dissolve

    u "(Back when I was happy with Emily, and I thought relationships were easy. Haha! How wrong I was...)"

    menu:
        "Send Emily a Selfie.":
            $ add_point(KCT.BOYFRIEND)
            scene v15s31_4 # TPP. Show MC's hand pulling his phone out of his pocket.
            with dissolve

            pause  

            scene v15s31_1a # TPP. Show MC taking a selfie of himself in the suit, slight smile, mouth closed.
            with flash

            pause 

            scene v15s31_5 # TPP. Show MC pressing buttons on his phones, slight smile, mouth closed.
            with dissolve

            $ emily.messenger.addImgReply("Selfie in a suit")
            $ emily.messenger.addReply("Getting prom flashbacks.")
            $ emily.messenger.newMessage("OMG! Haha, you actually look the same. Where are you headed?")
            $ emily.messenger.addReply("Wedding ceremony for Aubrey's parents.")
            $ emily.messenger.newMessage("Oh, nice! Tell her I said hi! Miss you guys! Have fun! :)")
            $ emily.messenger.addReply("Will do. We miss you too :)")

            scene v15s31_4a # TPP. Show MC's hand putting his phone away.
            with dissolve

        "Don't contact Emily.":
            $ add_point(KCT.BRO)
            scene v15s31_2
            with dissolve
                
            u "(Probably not a good idea to freshen those memories...)"

    u "(Alright, time to meet Aubrey.)"

    u "(I wonder what she's wearing?)"

    play sound "sounds/dooropen.mp3"

    scene v15s31_6 # TPP. Show MC leaving the bathroom, slight smile, mouth closed.
    with dissolve

    jump v15s32 