# SCENE 23: MC shower and Aubrey text
# Locations: Shower, MC's Wolf Room, MC's Ape Room
# Characters: MC (Towel, Outfit: 9)
# Time: Morning

init python:
    def v15s23_reply1():
        aubrey.messenger.newMessage("Perfect ;)")

    def v15s23_reply2():
        aubrey.messenger.newMessage("Hehe, I know you will ;)")

label v15s23:
    # -MC takes a shower-
    scene v15s23_1 # TPP. We see MC neutral expression, mouth closed waist up in the shower (rinsing his hair render as best as possible).
    with dissolve

    pause 0.75

    scene v15s23_2 # TPP. MC, neutral expression mouth closed turns off the shower.
    with dissolve

    pause 0.75

    scene v15s23_3 # TPP. MC, smile, mouth closed, in shower (waste up) thinking to himself.
    with fade

    u "(Well, Halloween was a success... Thankfully I'll never have to wear that costume ever again, haha.)"

    scene v15s23_4 # TPP. MC, neutral expression, mouth closed, wearing a towel standing in the slightly steamy bathroom, positioned in front of a steamed-up mirror.
    with dissolve

    pause 0.75

    scene v15s23_5 # FPP. MC, neutral expression, mouth closed, looks at his reflection in the steamed up mirror. 
    with dissolve

    pause 0.75

    menu:
        "Draw a happy face":
            $ add_point(KCT.BOYFRIEND)
            
            scene v15s23_6 # FPP. MC smiling, mouth closed leans towards the mirror and raises his finger like he's about to draw on the mirror with his finger.
            with dissolve

            pause 0.75

            scene v15s23_5a # FPP. MC, smiling, mouth closed, looks at his reflection in the steamed up mirror that has a happy face hand-drawn in the fog on the mirror.
            with dissolve
            
            u "(Maybe I should take art next semester...) *Laughs*"

        "Draw a dick":
            $ add_point(KCT.TROUBLEMAKER)
            $ add_point(KCT.BRO)
            
            scene v15s23_6
            with dissolve

            pause 0.75

            scene v15s23_5b # FPP. MC, smiling, mouth closed, looks at his reflection in the steamed-up mirror that has a penis hand-drawn in the fog on the mirror.
            with dissolve
    
            u "(Maybe I should take art next semester...) *Laughs*"

    scene v15s23_7 # TPP. MC (back to camera) wearing a towel, opening the bathroom door and exiting through it.
    with fade
    
    pause 0.75

    # Pre load Aubrey Text conversation before branching Ape or Wolf 
    $ aubrey.messenger.newMessage("Hey smelly, come to the Chicks house. I have an extra special surprise for you.", force_send=True)
    if aubrey.relationship.value < Relationship.FWB.value:
        $ aubrey.messenger.addReply("Smelly? I just showered! Anyway, I'll see you soon :)", v15s23_reply1)

    else:
        $ aubrey.messenger.addReply("I just showered actually, so I smell amazing. But I accept your invitation...")
        $ aubrey.messenger.newMessage("Where was my invitation???")
        $ aubrey.messenger.addReply("Uhh... I'll make it up to you...? Lol", v15s23_reply2)

    if joinwolves:
        scene v15s23_8a # TPP. Same as v15s23_8 but MC's WOLF ROOM.
        with dissolve

        pause 0.75

        scene v15s23_9a # TPP. Same as v15s23_9 but MC's WOLF ROOM.
        with dissolve

        pause 0.75

        scene v15s23_10a # TPP. Same as v15s23_10 but MC's WOLF ROOM.
        with dissolve

        pause 0.75

        scene v15s23_11a # TPP. Same as v15s23_11 but MC's WOLF ROOM.
        with dissolve

        pause 0.75

        scene v15s23_12a # TPP. Same as v15s23_12 but MC's WOLF ROOM.
        with dissolve
        
        pause 0.75

        scene v15s23_13a # TPP. Same as v15s23_13 but MC's WOLF ROOM.
        with dissolve

        pause 0.75

        label v15s23_aubrey_text_continue:
            if aubrey.messenger.replies:
                call screen phone
            if aubrey.messenger.replies:
                u "(I should reply to Aubrey.)"
                jump v15s23_aubrey_text_continue

        scene v15s23_14a # TPP. Same as v15s23_14 but MC's WOLF ROOM.
        with dissolve

        u "(I wonder what the surprise is...)"

        scene v15s23_15a # TPP. Same as v15s23_15 but MC's WOLF ROOM.
        with dissolve

        pause 0.75

        scene v15s23_16a # TPP. Same as v15s23_16 but MC's WOLF ROOM.
        with dissolve

        u "(Time to find out!)"

    else:
        scene v15s23_8 # TPP. MC, smiling, mouth closed, wearing a towel, entering his room. [MC's APE ROOM]
        with dissolve

        pause 0.75

        scene v15s23_9 # TPP. MC, smiling, mouth closed, standing naked in front of his bed. His towel is on the bed and he has his pants in his hands. [MC's APE ROOM]
        with dissolve

        pause 0.75

        scene v15s23_10 # TPP. MC, smiling, mouth closed, putting on his pants. [MC's APE ROOM]
        with dissolve

        pause 0.75

        scene v15s23_11 # TPP. MC, smiling, mouht clkosed, with his pants on. [MC's APE ROOM]
        with dissolve

        pause 0.75

        scene v15s23_12 # TPP. Close of up MC's phone on the table or nightstand. [MC's APE ROOM]
        with dissolve

        pause 0.75

        scene v15s23_13 # TPP. MC, neutral expression, mouth closed, wearing pants, holding his phone and looking down at it. [MC's APE ROOM]
        with dissolve

        pause 0.75

        label v15s23_aubrey_text_continue2:
            if aubrey.messenger.replies:
                call screen phone
            if aubrey.messenger.replies:
                u "(I should reply to Aubrey.)"
                jump v15s23_aubrey_text_continue2

        scene v15s23_14 # TPP. MC, smiling, thinking, mouth closed, putting his phone in his back pocket. [MC's APE ROOM]
        with dissolve

        u "(I wonder what the surprise is...)"

        scene v15s23_15 # TPP. MC, smiling, mouth closed, putting his shirt on. [MC's APE ROOM]
        with dissolve

        pause 0.75

        scene v15s23_16 # TPP. MC, opening the door to his room and exiting through it. [MC's APE ROOM]
        with dissolve

        u "(Time to find out!)"
    
    stop music fadeout 3
    
    jump v15s26