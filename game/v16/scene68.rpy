# SCENE 68: Transition Walking back with Penelope
# Locations: School Hallway
# Characters: MC (Outfit: 2), PENELOPE (Outfit: 2)
# Time: Thurdsay Night


label v16s68:
    scene v16s68_1 # TPP. MC (slight smile, mouth is closed) exits the cafeteria doors, and is now in the hallway
    with dissolve
    
    pause 0.75
    
    # 0 = Unselected, 
    # 1 = Wednesday_alone, 
    # 2 = Thrusday_alone, 
    # 4 = Friday_alone, 
    # 0x10 = Wednesday_shared, 
    # 0x20 = Thursday_shared, 
    # 0x40 = Friday_shared
    #
    # -if PenelopeFriend and (MC's partner is on baby duty alone) or MC is on baby duty with partner Thursday 
    if penelope.relationship == Relationship.FRIEND and ( (2 & v16s27_mc_baby_duty_night == 2 and 0x20 & v16s27_mc_baby_duty_night != 0x20) or 0x20 & v16s27_mc_baby_duty_night == 0x20):
        scene v16s68_2 # TPP. MC (slight smile, mouth is closed) continues walking along the hallway alone, the cafetria is no longer in the render
        with dissolve

        pause 0.75

    # -if PenelopeFriend and MC is on baby duty alone Thurssday
    if penelope.relationship == Relationship.FRIEND and 2 & v16s27_mc_baby_duty_night == 2: 

        scene v16s68_2
        with dissolve

        u "*Sighs* (The fun's over. Now it's time to be a responsible father and go collect [v16_baby_name].)"

    # -if PenelopeRS (if date in v14 went well) 
    if penelope.relationship == Relationship.FRIEND: 

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

        # -if PenelopeRS and MC has baby duty with partner Thursday
        if penelope.relationship == Relationship.FRIEND and 0x20 & v16s27_mc_baby_duty_night == 0x20: 

            scene v16s68_3
            with dissolve

            u "Oh, crap!"

            scene v16s68_3b # FPP. Show just Penelope (no expression, mouth open, looking at MC)
            with dissolve

            pe "What is it?"

            scene v16s68_3c # FPP. Show just Penelope (no expression, mouth closed, looking at MC)
            with dissolve
            
            if v16s27_parent_chloe:
                u "I'm on baby duty tonight with Chloe. I need to go collect it while I'm here."

            else: # Nora 
                u "I'm on baby duty tonight with Nora. I need to go collect it while I'm here."

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
            
            pause 0.75

        # -if PenelopeRS and MC has baby duty alone Thrusday 
        if penelope.relationship == Relationship.FRIEND and 2 & v16s27_mc_baby_duty_night == 2:

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

            scene v16s68_2c # TPP. MC and Penelope (both slight smiles, mouths closed, looking down the hallway) walking side by side down the hallway
            with dissolve
            
            pause 0.75

        # -if PenelopeRS and MC's partner is on baby duty alone Thursday
        if penelope.relationship == Relationship.FRIEND and (2 & v16s27_mc_baby_duty_night != 2 and 0x20 & v16s27_mc_baby_duty_night != 0x20):

            scene v16s68_3
            with dissolve
            
            pause 0.75

            if v16s27_parent_chloe:
                u "Lucky for you, Chloe is on baby duty tonight."
            
            else: # Nora 
                u "Lucky for you, Nora is on baby duty tonight."

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

            pause 0.75

    # -Regardless of all that-

    # -if PenelopeRS and MC is not on baby duty with partner on Thursday, transition to Scene 69-
    if penelope.relationship == Relationship.LOYAL and 0x20 & v16s27_mc_baby_duty_night != 0x20: 

        jump v16s69

    # -if MC is on baby duty with partner on Thursday, transition to Scene 47-
    
    elif 0x20 & v16s27_mc_baby_duty_night == 0x20:

        jump v16s47

    # -if PenelopeFriend and MC is on baby duty alone Thursday, transition to Scene 46-
    elif penelope.relationship == Relationship.FRIEND and 2 & v16s27_mc_baby_duty_night == 2:

        jump v16s46

    # -if PenelopeFriend and MC's partner is on baby duty alone, transition to Scene 42-
    elif penelope.relationship == Relationship.FRIEND and (2 & v16s27_mc_baby_duty_night != 2 and 0x20 & v16s27_mc_baby_duty_night != 0x20):

        jump v16s42
