# SCENE 68: Transition Walking back with Penelope
# Locations: School Hallway
# Characters: MC (Outfit: 2), PENELOPE (Outfit: 2)
# Time: Night


label v16s68:
    ###!!!TRANSCRIBER NOTE!!!### The variables for MC having the "baby" or not have not yet been established

    scene v16s68_1 # TPP. MC (slight smile, mouth is closed) exits the cafeteria doors, and is now in the hallway
    with dissolve

    if penelope.relationship.value <= Relationship.FRIEND.value:    # -if PenelopeFriend and MC's partner is on baby duty alone or MC is on baby duty with partner

        scene v16s68_2 # TPP. MC (slight smile, mouth is closed) continues walking along the hallway alone, the cafetria is no longer in the render
        with dissolve

    if penelope.relationship.value <= Relationship.FRIEND.value:    # -if PenelopeFriend and MC is on baby duty alone

        scene v16s68_2
        with dissolve

        u "*Sighs* (The fun's over. Now it's time to be a responsible father and go collect [baby_name].)"

    if penelope.relationship.value >= Relationship.GIRLFRIEND.value:    # -if PenelopeRS (if date in v14 went well) <---!!!Check to see if this is a separate variable from the relationship value!!!  ###!!!TRANSCRIBER NOTE###!!!

        scene v16s68_2a # TPP. MC (slight smile, mouth is closed, looks back and see's Penelope) and Penelope (slight smile, mouth is open, looking at MC) Penelope is waving at MC
        with dissolve

        pe "Hey, where are you speeding off to?"

        scene v16s68_3 # FPP. Show just Penelope (slight smile, mouth closed, looking at MC)
        with dissolve

        u "*Chuckles* Well... I was going home."

        scene v16s68_3a # FPP. Show just Penelope (slight smile, mouth open, looking at MC)
        with dissolve

        pe "I was thinking you might like to come home with me."

        scene v16s68_3
        with dissolve

        u "But you're Polly's best friend and I'm just a humble student. Are you sure you want to mix with the likes of me?"

        scene v16s68_3a
        with dissolve

        pe "*Laughs* I'll make an exception, just this once."

        if penelope.relationship.value >= Relationship.GIRLFRIEND.value:    # -if PenelopeRS and MC has baby duty with partner tonight

            scene v16s68_3
            with dissolve

            u "Oh, crap!"

            scene v16s68_3b # FPP. Show just Penelope (no expression, mouth open, looking at MC)
            with dissolve

            pe "What is it?"

            scene v16s68_3c # FPP. Show just Penelope (no expression, mouth closed, looking at MC)
            with dissolve

            u "I'm on baby duty tonight with [baby_partner]. I need to go collect it while I'm here."

            scene v16s68_3a
            with dissolve

            pe "Oh, that thing."

            scene v16s68_3
            with dissolve

            u "Yeah, that thing. It's really getting in the way of my life right now!"

            scene v16s68_3a
            with dissolve

            pe "Well, you should have thought about that before deciding to have a baby! Haha."

            scene v16s68_3
            with dissolve

            u "Haha, yeah..."

            scene v16s68_3a
            with dissolve

            pe "There's always next time."

            scene v16s68_3
            with dissolve

            u "Yeah, once we're past these baby nights I'll be much freer."

            scene v16s68_3a
            with dissolve

            pe "Okay, sure. Bye then, [name]."

            scene v16s68_2b # TPP. MC (no expression, mouth closed) continues walking along the hallway away from Penelope, Penelope (dissapointed expression, mouth is closed, looking at MC walk away) standing still watching MC walk away
            with dissolve

        if penelope.relationship.value >= Relationship.GIRLFRIEND.value:    # -if PenelopeRS and MC has baby duty alone tonight

            scene v16s68_3
            with dissolve

            u "There is one small problem, however."

            scene v16s68_3b
            with dissolve

            pe "Oh? What's that?"

            scene v16s68_3c
            with dissolve

            u "I'm on baby duty tonight. I was just about to collect it."

            scene v16s68_3a
            with dissolve

            pe "I don't mind. You can bring it with you."

            scene v16s68_3
            with dissolve

            u "Are you sure? There's going to be lots of crying."

            scene v16s68_3a
            with dissolve

            pe "Aw, bless. I'll try not to upset you."

            scene v16s68_3
            with dissolve

            u "Haha, not me! The baby!"

            scene v16s68_3a
            with dissolve

            pe "*Laughs* Come on. Let's go."

            scene v16s68_2c  # TPP. MC and Penelope (both slight smiles, mouths closed, looking down the hallway) walking side by side down the hallway
            with dissolve

        if penelope.relationship.value >= Relationship.GIRLFRIEND.value:    # -if PenelopeRS and MC's partner is on baby duty alone

            scene v16s68_3
            with dissolve

            u "Lucky for you, [baby_partner] is on baby duty tonight."

            scene v16s68_3a
            with dissolve

            pe "Oh, wow, that's lucky!"

            scene v16s68_3
            with dissolve

            u "Yep, no kids to hold me down tonight!"

            scene v16s68_3a
            with dissolve

            pe "*Laughs* Let's get out here then."

            scene v16s68_2c
            with dissolve

    # -Regardless of all that-

    if penelope.relationship.value >= Relationship.GIRLFRIEND.value and :    # -if PenelopeRS and MC is not on baby duty with partner, transition to Scene 69-

        jump v16s69

    elif penelope.relationship.value >= Relationship.GIRLFRIEND.value and :    # -if MC is on baby duty with partner, transition to Scene 47-

        jump v16s47

    else penelope.relationship.value >= Relationship.GIRLFRIEND.value and :    # -if PenelopeFriend and MC is on baby duty alone, transition to Scene 46-

        jump v16s46

    else:    # -if PenelopeFriend and MC's partner is on baby duty alone, transition to Scene 42-

        jump v16s42
